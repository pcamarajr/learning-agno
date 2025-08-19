from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.ollama import Ollama

# Initialize memory for user preferences
memory = Memory(
    model=Ollama(
        id="llama3.2:3b",
        provider="Ollama",
        host="http://ollama:11434",
    ),
    db=SqliteMemoryDb(
        table_name="user_memories",
        db_file="tmp/agent.db"
    ),
    delete_memories=True,
    clear_memories=True,
)

agent = Agent(
    model=Ollama(
        id="llama3.2:3b",
        provider="Ollama",
        host="http://ollama:11434",
    ),
    # Add instructions to tell the agent how to behave
    instructions=[
        "You are a helpful AI assistant with memory capabilities.",
        "Answer user questions directly and conversationally.",
        "Use the information you learn about users to provide personalized "
        "responses.",
        "When users ask questions, provide helpful and informative answers.",
        "Be friendly and engaging in your responses.",
    ],
    memory=memory,
    enable_agentic_memory=True,
    # Add chat history to messages for context
    add_history_to_messages=True,
    # Number of history runs to include
    num_history_runs=3,
    markdown=True,
)

if __name__ == "__main__":
    # Define a user ID for memory retrieval
    user_id = "test_user@example.com"

    agent.print_response(
        "Hello my name is Eva.",
        stream=True,
        user_id=user_id
    )

    agent.print_response(
        "I'm curious about the meaning of my name.",
        stream=True,
        user_id=user_id
    )

    agent.print_response(
        "Who was the first person named like me?",
        stream=True,
        user_id=user_id
    )
