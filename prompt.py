import chromadb
import ollama

if __name__ == "__main__":
    print(">>> ", end='')
    prompt = input()

    # Initialize the chromadb collection
    chroma_client = chromadb.HttpClient()
    collection = chroma_client.get_collection(name="notes")
    query_result = collection.query(
        query_texts=[prompt],
        n_results=15
    )
    documents = "\n".join(query_result['documents'][0])

    # Prompt the LLM
    messages = [
        {
            'role': 'system',
            'content':
                f"""
                You are an expert on my notes.
                Your task is to thoroughly analyze and reference my notes, then provide a comprehensive and accurate response to the users prompt.
                Please ensure the answer is detailed, relevant to the notes, and directly addresses the question.
                """
        },
        {
            'role': 'user',
            'content': documents
        },
        {
            'role': 'user',
            'content': prompt,
        },
    ]

    while True:
        stream = ollama.chat(model='llama3.2', messages=messages, stream=True)
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
        print("\n>>> ", end='')
        messages.append({
            'role': 'user',
            'content': input()
        })