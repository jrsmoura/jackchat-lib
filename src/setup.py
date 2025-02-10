from setuptools import setup, find_packages

setup(
    name="rag-azure",
    version="0.1.0",
    description="A package for RAG-based chatbots using Azure AI Search and OpenAI.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "langchain-openai",
        "langchain-community",
        "langchain-core",
        "tiktoken",
        "python-dotenv",
        "azure-search-documents"
    ],
    entry_points={
        "console_scripts": [
            "rag-azure=rag_azure.cli:main"
        ]
    },
)