from rag.pipeline import run_query

if __name__ == "__main__":
    print("Local RAG + Langfuse Pipeline Running\n")

    while True:
        query = input("Enter your question (or 'exit'): ")

        if query.lower() == "exit":
            break

        answer = run_query(query)

        print("\nAnswer:")
        print(answer)
        print("\n" + "="*50 + "\n")