"""
Module responsible for document retrieval using Azure AI Search.
"""
from langchain_community.retrievers import AzureAISearchRetriever
from langchain_community.vectorstores.azuresearch import AzureSearch

from .config import Config
from .models import EMBEDDINGS

embedding_function = EMBEDDINGS.embed_query

vector_store = AzureSearch(
    azure_search_endpoint=Config.AZURE_AI_SEARCH_ENDPOINT,
    azure_search_key=Config.AZURE_AI_SEARCH_API_KEY,
    index_name=Config.AZURE_AI_SEARCH_INDEX_NAME,
    embedding_function=EMBEDDINGS.embed_query,
    additional_search_client_options={"retry_total": 3},
)

RETRIEVER = AzureAISearchRetriever(
    api_key=Config.AZURE_AI_SEARCH_API_KEY,
    service_name=Config.AZURE_AI_SEARCH_SERVICE_NAME,
    content_key="content",
    top_k=5,
    index_name=Config.AZURE_AI_SEARCH_INDEX_NAME
)
