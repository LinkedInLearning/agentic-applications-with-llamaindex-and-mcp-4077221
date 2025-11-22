#!/usr/bin/env python3
import os
import weaviate
from weaviate.agents.query import QueryAgent
from weaviate.agents.classes import ChatMessage
from weaviate.auth import AuthApiKey
import dotenv

dotenv.load_dotenv(override=True)

# Connect to Weaviate Cloud
with weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WEAVIATE_URL"),
    auth_credentials=AuthApiKey(os.getenv("WEAVIATE_API_KEY")),
) as client:
    qa = QueryAgent(
        client=client,
        collections=["ECommerce"]
    )
    print("✓ Query Agent initialized")

    # Search mode - retrieval only
    print("\n--- Search results ---")
    search_response = qa.search(
        "Find me some vintage shoes under $70",
        limit=3
    )

    # Display results
    for obj in search_response.search_results.objects:
        print(f"Name: {obj.properties['name']}")
        print(f"Price: ${obj.properties['price']:.2f}")

    # Ask mode - retrieval + answer generation
    print("\n--- Ask results ---")
    response = qa.ask(
        "I'm looking for a dress for a summer party. What can you recommend?"
    )
    print(response.final_answer)


    # Handling Conversations
    print("\n--- Conversation ---")

    # Initial question
    initial_question = "Recommend some footwear for me."
    initial_response = qa.ask(initial_question)
    print(f"User: {initial_question}")
    print(f"Agent: {initial_response.final_answer}")


    # Build conversation history for the follow-up
    follow_up_question = "Which of those are under $80?"
    conversation = [
        ChatMessage(role="user", content=initial_question),
        ChatMessage(role="assistant", content=initial_response.final_answer),
        ChatMessage(role="user", content=follow_up_question)
    ]

    # The agent understands "those" refers to the footwear from the previous turn
    follow_up = qa.ask(conversation)
    print(f"\nUser: {follow_up_question}")
    print(f"Agent: {follow_up.final_answer}")
