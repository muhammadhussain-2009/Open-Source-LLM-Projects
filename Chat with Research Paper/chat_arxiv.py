import streamlit as st
import arxiv
from agno.agent import Agent
from agno.models.ollama import Ollama

# Set up the Streamlit app
st.title("Chat with Research Papers 🔎🤖")
st.caption("This app allows you to chat with arXiv research papers using a local Ollama model.")

# Create an instance of the Assistant
assistant = Agent(
    model=Ollama(id="gemma3:1b"),
)


def search_arxiv(query: str, max_results: int = 3):
    search = arxiv.Search(query=query, max_results=max_results)
    client = arxiv.Client()
    return list(client.results(search))

# Get the search query from the user
query = st.text_input("Enter the Search Query", type="default")

if query:
    papers = search_arxiv(query)
    if not papers:
        st.write("No papers found for that query.")
    else:
        prompt = "I found the following arXiv papers:\n"
        for idx, paper in enumerate(papers, start=1):
            prompt += f"\n{idx}. {paper.title}\n"
            prompt += f"Authors: {', '.join(str(a) for a in paper.authors)}\n"
            prompt += f"Summary: {paper.summary}\n"
            prompt += f"URL: {paper.entry_id}\n"
        prompt += "\nUsing these paper summaries, answer the user's query in a helpful way."

        response = assistant.run(prompt, stream=False)
        st.write(response.content)