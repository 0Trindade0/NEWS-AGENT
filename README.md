NEWS-AGENT: Intelligent Autonomous News Curator
NEWS-AGENT is a Python-based autonomous agent designed to automate the entire content curation lifecycle: discovery, extraction, AI-powered summarization, and organized publication to Notion.

It is built specifically for users who need to stay updated on complex global topics (e.g., "US-Iran Conflict") without the noise of ads, trackers, or paywalls found on traditional news portals.

🚀 Key Features
Automated Discovery: Monitors Google News via RSS feeds to find the most recent and relevant articles.

Advanced Link Resolution: Implements specialized decoding to bypass complex Google News redirection layers.

Deep Content Extraction: Captures full text, metadata, and top images using newspaper4k.

AI-Powered Summarization: Generates high-level executive summaries in Portuguese/English using the Gemini 2.0 Flash SDK.

Notion Integration: Automatically publishes structured reports to a Notion database, creating a personal "News Blog."

🏗️ Architecture
The project strictly follows the Hexagonal Architecture (Ports & Adapters) pattern. This ensures that the core business logic is completely decoupled from external tools, APIs, and frameworks.

Domain: Core data models (NewsArticle).

Application (Ports): Interfaces defining the contracts for searching, fetching, summarizing, and notifying.

Infrastructure (Adapters): Concrete implementations for Google News, Gemini AI, and the Notion API.

Directory Structure
Plaintext
news_agent/
├── src/
│   ├── domain/                # Data models
│   ├── application/           # Use cases and Ports (Interfaces)
│   │   └── ports/
│   ├── infrastructure/        # Adapters (Technical implementations)
│   │   ├── ai/                # Gemini SDK integration
│   │   ├── scrapers/          # Google Search & Newspaper4k logic
│   │   └── notify/            # Notion API client
│   └── main.py                # Entry point (Composition Root)
├── .env                       # API Keys (git-ignored)
└── requirements.txt           # Project dependencies
🛠️ Tech Stack
Python 3.12+

Google GenAI SDK: Large Language Model (LLM) processing.

Newspaper4k: Advanced web scraping and article parsing.

Notion-Client: Official SDK for Notion workspace integration.

Googlenewsdecoder: Specialized logic for resolving encoded URLs.

⚙️ Installation & Setup
Clone the repository:

Bash
git clone https://github.com/your-username/news-agent.git
cd news_agent
Set up the virtual environment:

Bash
python -m venv .venv
# Activate on Windows:
.\.venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Environment Variables:
Create a .env file in the root directory:

Snippet de código
NOTION_TOKEN=secret_your_token_here
NOTION_DATABASE_ID=your_database_id_here
GEMINI_API_KEY=your_google_ai_studio_key_here
📈 Usage
Run the agent via the main entry point:

Bash
python main.py
The agent will search for the topic defined in main.py, process the findings through the Gemini AI, and publish the results to your Notion workspace in real-time.
