import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from __init__ import setup_rag_system, retrieve_answer  # Fix the import
if __name__ == "__main__":
    setup_rag_system()  # Initialize FAISS and store embeddings
    query = "What is this document about?"
    
    print(f"\nProcessing query: {query}")
    response = retrieve_answer(query)

    print("\n🔍 Top Search Results:\n")
    for result in response:
        print(f"📄 Filename: {result['filename']}")
        print(f"📌 Chunk: {result['chunk'][:300]}...")  # Show first 300 chars only
        print(f"🔢 Distance: {round(result['distance'], 3)}\n")
