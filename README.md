# README.md

# RAG Azure

RAG Azure is a Python package for building **Retrieval-Augmented Generation (RAG) chatbots** powered by **Azure AI Search** and **Azure OpenAI**. This package allows users to integrate document-based retrieval with large language models to provide context-aware responses.

## Features
- Seamless integration with **Azure AI Search** for document retrieval.
- Embedding and querying using **Azure OpenAI**.
- Document loading and parsing from various sources.
- Modular and configurable setup.
- Easy-to-use API for different chatbot applications.

## Installation
To install the package, use:

```sh
pip install git+https://github.com/your-repo/rag-azure.git
```

Alternatively, install from source:

```sh
git clone https://github.com/your-repo/rag-azure.git
cd rag-azure
pip install .
```

## Configuration
RAG Azure requires **Azure API keys** and **configuration parameters**. Define these in a `.env` file in your project root:

```ini
AZURE_OPENAI_API_KEY=your_openai_api_key
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=your_model_deployment_name
AZURE_OPENAI_ENDPOINT=your_openai_endpoint
AZURE_OPENAI_API_VERSION=your_api_version
AZURE_EMBEDDINGS_DEPLOYMENT_NAME=your_embeddings_deployment_name
AZURE_EMBEDDINGS_MODEL_NAME=your_embeddings_model_name
AZURE_EMBEDDINGS_API_KEY=your_embeddings_api_key
AZURE_AI_SEARCH_API_KEY=your_search_api_key
AZURE_AI_SEARCH_ENDPOINT=your_search_endpoint
AZURE_AI_SEARCH_INDEX_NAME=your_search_index_name
AZURE_AI_SEARCH_SERVICE_NAME=your_search_service_name
DOCS_PATHS=/path/to/documents
```

## Usage
### Load the Package
Import the necessary components in your script:

```python
from rag_azure import Config, LLM, RETRIEVER, load_documents, CHAT_RAG_CHAIN
```

### Run a Query
Use the chatbot pipeline to generate responses:

```python
def ask_question(query):
    response = CHAT_RAG_CHAIN.invoke({"input": query})
    return response["answer"]

question = "What is the latest maintenance report?"
answer = ask_question(question)
print(answer)
```

### Load Documents
To index new documents, use:

```python
documents = load_documents()
print(f"Loaded {len(documents)} documents.")
```

## Running Tests
Run unit tests using:

```sh
pytest tests/
```

## Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit changes (`git commit -m "Add new feature"`).
4. Push to your branch (`git push origin feature-branch`).
5. Create a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For inquiries, open an issue or reach out to `your.email@example.com`.
