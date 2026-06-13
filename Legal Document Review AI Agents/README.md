# Legal Documents Review AI Agent 

A sophisticated Retrieval-Augmented Generation (RAG) system designed to navigate the complex landscape of European Union AI regulations. By leveraging advanced language models and vector search, this tool provides precise, context-aware insights into legal documentation, starting with the EU AI Act.

## Overview

This project demonstrates how RAG architectures can efficiently process vast legal datasets to provide accurate, intelligent responses. It utilizes the latest advancements in LLMs to interpret nuanced legal terminology.

### Technology Stack

* **Core LLM:** OpenAI ChatGPT 4.0
* **Vector Database:** ChromaDB
* **Embeddings:** OpenAI Embeddings
* **Orchestration:** LangChain

## Features

* **Context-Aware Analysis:** Processes large-scale legal documents as context.
* **Semantic Search:** Fast and accurate retrieval of relevant legal clauses.
* **Intelligent Reasoning:** Utilizes LLM capabilities to synthesize and explain complex legal requirements.
* **Extensible:** Easily adaptable to other regulatory frameworks and legal papers.

---

## Installation

### Prerequisites

* Python 3.10+
* An active [OpenAI API Key](https://platform.openai.com/)

### Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/legal-ai-navigator.git
    cd legal-ai-navigator
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables:**
    Set your OpenAI API key in your terminal session:
    ```bash
    export OPENAI_API_KEY='your_key_value_here'
    ```
    *(For Windows users, use `set OPENAI_API_KEY=your_key_value_here`)*

4.  **Run the Application:**
    Navigate to the `app/` folder and launch the Streamlit interface:
    ```bash
    cd app
    streamlit run app.py
    ```

---

## Contributing

We welcome contributions to improve the Legal AI Navigator! Whether it's adding support for new legal frameworks, enhancing the retrieval mechanism, or improving the UI, please follow these steps:

1.  Fork the repository.
2.  Create a feature branch (`git checkout -b feature/amazing-feature`).
3.  Commit your changes.
4.  Push to the branch.
5.  Open a Pull Request.

---

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or suggestions, please open an issue or reach out to the project maintainers.
