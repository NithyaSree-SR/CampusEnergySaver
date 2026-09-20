<<<<<<< HEAD
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os


def get_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings


def create_vector_database():

    folder_path = "knowledge"
    documents = []

    for filename in os.listdir(folder_path):

        if filename.endswith(".txt"):

            file_path = os.path.join(folder_path, filename)

            loader = TextLoader(file_path)

            documents.extend(loader.load())

    print("Files loaded:", len(documents))

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(documents)

    print("Chunks created:", len(chunks))

    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    print("Vector database created successfully!")

    return vectorstore


def load_vector_database():

    embeddings = get_embeddings()

    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    print("Existing vector database loaded!")

    return vectorstore


def get_vector_database():

    if os.path.exists("chroma_db"):

        return load_vector_database()

    else:

        return create_vector_database()


if __name__ == "__main__":

    vectorstore = get_vector_database()

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    query = "How can I save energy when an air conditioner is running in a classroom?"

    results = retriever.invoke(query)

    print("\nRelevant information:")

    for doc in results:

        print("\n---")
=======
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os


def get_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings


def create_vector_database():

    folder_path = "knowledge"
    documents = []

    for filename in os.listdir(folder_path):

        if filename.endswith(".txt"):

            file_path = os.path.join(folder_path, filename)

            loader = TextLoader(file_path)

            documents.extend(loader.load())

    print("Files loaded:", len(documents))

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(documents)

    print("Chunks created:", len(chunks))

    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    print("Vector database created successfully!")

    return vectorstore


def load_vector_database():

    embeddings = get_embeddings()

    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    print("Existing vector database loaded!")

    return vectorstore


def get_vector_database():

    if os.path.exists("chroma_db"):

        return load_vector_database()

    else:

        return create_vector_database()


if __name__ == "__main__":

    vectorstore = get_vector_database()

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    query = "How can I save energy when an air conditioner is running in a classroom?"

    results = retriever.invoke(query)

    print("\nRelevant information:")

    for doc in results:

        print("\n---")
>>>>>>> a11ca4af62bd57625a554b4b60f23b3f9379e30b
        print(doc.page_content)