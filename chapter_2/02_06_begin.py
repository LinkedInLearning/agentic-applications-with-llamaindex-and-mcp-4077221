#!/usr/bin/env python3
import os
import weaviate
from weaviate.agents.query import QueryAgent
from weaviate.agents.classes import QueryAgentCollectionConfig
from weaviate.classes.query import Filter
from weaviate.auth import AuthApiKey
import dotenv

dotenv.load_dotenv(override=True)

# This script assumes you have a Weaviate instance with an "ECommerce" collection

def main():
    """
    Demonstrates advanced patterns for customizing the Weaviate Query Agent.
    """
    with weaviate.connect_to_weaviate_cloud(
        cluster_url=os.getenv("WEAVIATE_URL"),
        auth_credentials=AuthApiKey(os.getenv("WEAVIATE_API_KEY")),
    ) as client:
        print("✓ Connected to Weaviate")

        # TODO: 1. Define the Agent's Persona with a System Prompt
        # Follow the lesson text to create a QueryAgent with a custom system prompt
        # that defines its persona as a "friendly and knowledgeable fashion expert".
        # Then, ask it for a recommendation for a "dress for a summer party".
        print("\n--- Pattern 1: System Prompt ---")
        response = None  # Replace this line
        if response:
            print(f"Agent Persona Response:\n{response.final_answer}\n")


        # TODO: 2. Focus the Agent on the Right Data
        # Follow the lesson text to configure the agent to only use the "name", "price",
        # and "brand" properties from the "ECommerce" collection.
        # Then, ask it to "Recommend something." for someone who likes "vintage clothes".
        print("\n--- Pattern 2: Focusing on the Right Data ---")
        response = None  # Replace this line
        if response:
            print("Focused Agent Response:")
            response.display()


        # TODO: 3. Create a Specialized Agent with Persistent Filters
        # Follow the lesson text to create a specialized "luxury bot" that can only
        # access handbags over $500. Then, test it by asking it to
        # "Find me an affordable t-shirt."
        print("\n--- Pattern 3: Persistent Filters ---")
        response = None  # Replace this line
        if response:
            print("Specialized Luxury Bot Response:")
            response.display()


        # TODO: 4. Improve User Experience with Streaming
        # Follow the lesson text to stream a response from the agent with the
        # fashion expert persona. Ask it to "Recommend some footwear for me."
        print("\n--- Pattern 4: Streaming ---")
        print("Streaming Agent Response:")
        print("Agent: ", end="")
        # Replace the line below with the streaming logic from the lesson
        print("TODO: Implement streaming response.")


if __name__ == "__main__":
    main()
