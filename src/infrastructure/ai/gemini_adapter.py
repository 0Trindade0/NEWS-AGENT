from google import genai
from google.api_core import exceptions # Para capturar erros específicos de cota
from src.application.ports.summarizer_port import SummarizerPort

class GeminiAdapter(SummarizerPort):
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)
        self.model_name = "gemini-1.5-flash" # Modelo mais leve e com cota maior

    def summarize(self, text: str, topic: str) -> str:
        print(f"[*] Gerando resumo inteligente com Gemini SDK...")

        prompt_sistema = (
            f"Você é um analista especializado em {topic}. "
            "Crie um resumo executivo direto e em português."
        )

        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=f"Resuma focando em '{topic}':\n\n{text[:12000]}",
                config={"system_instruction": prompt_sistema}
            )
            return response.text if response.text else "Resumo vazio."

        except Exception as e:
            if "429" in str(e):
                print("[!] Cota da API Gemini atingida. Usando texto original fatiado.")
            elif "400" in str(e):
                print("[!] Erro de API Key. Verifique se a chave no .env é válida.")
            else:
                print(f"[!] Erro inesperado na IA: {e}")
            
            return text[:1000] + " (Resumo indisponível - erro de cota/chave)"