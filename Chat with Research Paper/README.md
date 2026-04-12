# Chat with Research Papers

A small Streamlit app that lets you search arXiv and chat with short summaries of research papers using a locally hosted Ollama model. This project demonstrates how to combine the arXiv Python client, a local LLM via Ollama, and a lightweight web UI to explore and interact with research paper summaries.

## Contents
- Chat with Research Papers (Streamlit UI)
- arXiv search integration (arxiv)
- Local LLM inference via Ollama (agno + ollama client)
- Optional PDF handling (pypdf listed in dependencies)

## Features
- Search arXiv by query and retrieve paper metadata (title, authors, summary, URL).
- Aggregate found paper summaries into a prompt and send it to a local Ollama model via an Agent wrapper.
- Lightweight Streamlit UI for interactive usage.

## Requirements
- Python >= 3.11
- Local Ollama runtime (ollama daemon) with a model available (the app references `gemma3:1b` by default)
- Network access to arXiv for searching
- Optional: PDF reading support (pypdf) for future expansions

Python dependencies (defined in pyproject.toml):
- agno (Agent wrapper)
- arxiv
- ollama
- openai (present as a dependency for possible future usage)
- pypdf
- streamlit

## Quickstart / Initialization

1. Clone the repository:
```bash
git clone https://github.com/muhammadhussain-2009/Open-Source-LLM-Projects.git
cd "Open-Source-LLM-Projects/Chat with Research Paper"
```

2. Create and activate a virtual environment (example using venv):
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

3. Install the project dependencies:
- If you want to install from pyproject.toml:
```bash
pip install --upgrade pip
pip install .
```
- Or install directly from the dependency list (recommended for development):
```bash
pip install -r requirements.txt  # if you create this file
# OR install the main deps manually:
pip install agno arxiv ollama openai pypdf streamlit
```

4. Install and start Ollama locally, and ensure the desired model is available:
- Install Ollama following its official instructions for your OS.
- Start the Ollama daemon (typical command; follow official docs):
```bash
ollama start
```
- Pull or load the model referenced in the app (example):
```bash
ollama pull gemma3:1b
# or otherwise ensure a model named "gemma3:1b" is available locally
```
Note: If you prefer a different local model, update `Chat with Research Paper/chat_arxiv.py` to reference the desired model id.

5. Run the Streamlit app:
```bash
streamlit run "Chat with Research Paper/chat_arxiv.py"
```
Then open the displayed URL (usually http://localhost:8501).

## Configuration
- Model ID: The app creates an Agent with `Ollama(id="gemma3:1b")`. Change the id to any other model available in your Ollama instance if needed.
- Search results: By default the app fetches up to 3 arXiv results per query. Change `max_results` in `search_arxiv` to fetch more or fewer items.
- PDF ingestion: The pyproject includes pypdf. To enable PDF ingestion in future versions, add UI controls to upload/select a PDF, extract text with pypdf, and feed it into the agent pipeline.

## How it works (brief)
1. User enters a query in the Streamlit UI.
2. The app runs an arXiv search and collects metadata (title, authors, summary, URL).
3. The app constructs a prompt summarizing the returned papers and sends it to the Agent (backed by a local Ollama model).
4. The Agent returns the generated response and the UI displays it.

## Development
- Follow standard Git workflow: fork, branch, make changes, open a pull request.
- Keep commit messages concise and descriptive.
- Keep logic modular (e.g., separate arXiv retrieval, prompting, and UI code) to make testing and extension easier.
- Add automated tests for parsing and prompt-building logic when expanding functionality.

## Contribution Guidelines
Thank you for considering contributing! Suggested process:
1. Fork the repository and create a new branch for your change.
2. Make small, focused commits with clear messages.
3. If adding a feature, update or add documentation and, where applicable, tests.
4. Run the app locally and ensure your changes work end-to-end.
5. Open a pull request describing the change, rationale, and testing performed.

Code style:
- Follow PEP 8 for Python code.
- Use type hints where possible.
- Document public functions with docstrings.

Areas where contributions are welcome:
- PDF ingestion and document chunking
- Embeddings + vector store integration (FAISS, Chroma, etc.) for semantic search
- Persistent caching of arXiv search results
- Dockerfile or containerized deployment
- CI configuration and linting/tests

## Troubleshooting & Support

Common issues and fixes:

- "Model not found" or Ollama connection errors
  - Ensure Ollama is installed and the daemon is running (`ollama start`).
  - Verify the model id (e.g., `gemma3:1b`) is available: `ollama ls` or `ollama pull <model>`.
  - If using a different model, update the `Ollama(id="...")` call.

- Streamlit won't start / port conflict
  - If port 8501 is in use, run: `streamlit run "Chat with Research Paper/chat_arxiv.py" --server.port 8502`
  - Ensure your virtual environment is activated and dependencies installed.

- arXiv search returns no results or rate-limited responses
  - Try a broader query or reduce frequency of requests.
  - The `arxiv` package does not require API keys but is subject to arXiv's usage policies.

- Dependency/version issues
  - Use Python 3.11+ as declared in pyproject.toml.
  - Recreate virtualenv and reinstall dependencies:
    ```bash
    rm -rf .venv
    python -m venv .venv
    source .venv/bin/activate
    pip install -e .
    ```
- Agent/agno exceptions
  - Confirm configuration of the Agent and wrapped model client (Ollama).
  - Inspect exception traces and share them in issues for help. When opening an issue, include:
    - OS and Python version
    - Exact error traceback
    - Steps to reproduce

If you need help, open an issue in the repository with detailed reproduction steps and logs.

## Future Prospects / Roadmap
Potential next steps to improve the project:
- PDF ingestion and multi-document conversation (pypdf + text chunking)
- Add embeddings & a vector store (FAISS/Chroma) for retrieval-augmented generation (RAG)
- Support additional local/backed models and a model selection UI
- Implement streaming responses from the LLM for a more interactive experience
- Add unit/integration tests and CI (GitHub Actions)
- Containerize the app (Docker) and provide a docker-compose that runs the Streamlit app and any required services
- Add user session/history and export chat as markdown
- Add authentication and optional private dataset ingestion

## Security & Privacy
- The app sends arXiv metadata and generated prompts to a local model (no upstream by default if using Ollama locally). If you integrate remote inference providers (OpenAI or others), be mindful of data sent to remote services.
- Do not expose the local Ollama daemon to untrusted networks without appropriate protections.

## Suggested Project Maintenance
- Add a LICENSE (e.g., MIT) to clarify usage and contributions.
- Add a requirements.txt or a poetry/installer config for reproducible installs.
- Add an example `.env` or documentation for configuration variables.

## License
This repository currently does not include a license file. Consider adding one (for example, MIT) to make reuse and contributions clear.
---
