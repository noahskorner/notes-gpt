import os
import chromadb
import uuid
import sys

if __name__ == "__main__":
    directory = sys.argv[1]

    # Initialize the chromadb collection
    chroma_client = chromadb.HttpClient()
    chroma_client.delete_collection(name="notes")
    collection = chroma_client.create_collection(name="notes")

    # Embed the documents
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                with open(os.path.join(root, file), 'r', encoding='utf-8') as document:
                    content = document.read()
                    content_with_path = f"{relative_path}\n{content}"
                    collection.add(documents=[content_with_path], ids=str(uuid.uuid4()))


    print("Successfully embedded documents into the chroma database.")

