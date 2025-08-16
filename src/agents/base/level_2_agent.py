from agno.agent import Agent
from agno.embedder.ollama import OllamaEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.models.ollama import Ollama
from agno.storage.sqlite import SqliteStorage
from agno.vectordb.lancedb import LanceDb, SearchType

# Load Agno documentation in a knowledge base
knowledge = UrlKnowledge(
    urls=["https://docs.agno.com/introduction.md"],
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="agno_docs",
        search_type=SearchType.hybrid,
        # Use local Ollama for embeddings
        embedder=OllamaEmbedder(
            id="nomic-embed-text",
            host="http://ollama:11434",
            dimensions=768,
        ),
    ),
)

# Store agent sessions in a SQLite database
storage = SqliteStorage(table_name="agent_sessions", db_file="tmp/agent.db")

agent = Agent(
    name="Agno Assist",
    model=Ollama(
        id="llama3.2:3b",
        provider="Ollama",
        host="http://ollama:11434",
    ),
    instructions=[
        "Use ONLY your knowledge for answering the question.",
        "Answer the question in one sentence.",
        "If you don't know the answer, say 'I don't have that information'.",
    ],
    knowledge=knowledge,
    storage=storage,
    add_datetime_to_instructions=True,
    # Add the chat history to the messages
    add_history_to_messages=True,
    # Number of history runs
    num_history_runs=3,
    markdown=True,
)

if __name__ == "__main__":
    # Load the knowledge base, comment out after first run
    # Set recreate to True to recreate the knowledge base if needed
    # agent.knowledge.load(recreate=True)
    agent.print_response("What was my last question?", stream=True)
