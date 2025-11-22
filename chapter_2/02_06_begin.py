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
        fashion_expert_prompt = """
        You are a friendly and knowledgeable fashion expert specializing in vintage clothing.
        When asked for recommendations, provide a brief, enthusiastic description for each item,
        highlighting its vintage appeal. Your tone should be helpful and stylish.
        """

        qa_with_persona = None # Replace this code

        response = None  # Replace this code
        print(f"Agent Persona Response:\n{response.final_answer}\n")


        # TODO: 2. Focus the Agent on the Right Data
        # Follow the lesson text to configure the agent to only use the "name", "price",
        # and "brand" properties from the "ECommerce" collection.
        # Then, ask it to "Recommend something." for someone who likes "vintage clothes".
        print("\n--- Pattern 2: Focusing on the Right Data ---")
        response = None  # Replace this code
        if response:
            print("Focused Agent Response:")
            response.display()


        # TODO: 3. Create a Specialized Agent with Persistent Filters
        # Follow the lesson text to create a specialized "luxury bot" that can only
        # access handbags over $500.
        print("\n--- Pattern 3: Persistent Filters ---")
        luxury_bot = None # Replace this code

        response = luxury_bot.ask("Find me an affordable t-shirt.")
        print("Specialized Luxury Bot Response:")
        response.display()


        # TODO: 4. Improve User Experience with Streaming
        # Follow the lesson text to stream a response from the agent with the
        # fashion expert persona. Ask it to "Recommend some footwear for me."
        print("\n--- Pattern 4: Streaming ---")
        response_generator = None # Replace this code

        print("Streaming Agent Response:")
        print("Agent: ", end="")
        for chunk in response_generator:
            if chunk.text:
                print(chunk.text, end="", flush=True)
        print("\n")


if __name__ == "__main__":
    main()
