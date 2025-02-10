"""
Module defining LLM and embeddings configuration.
"""
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from .config import Config
import tiktoken

LLM = AzureChatOpenAI(
    azure_deployment=Config.AZURE_OPENAI_MODEL_DEPLOYMENT_NAME,
    azure_endpoint=Config.AZURE_OPENAI_ENDPOINT,
    api_version=Config.AZURE_OPENAI_API_VERSION,
    api_key=Config.AZURE_OPENAI_API_KEY,
    temperature=0
)

EMBEDDINGS = AzureOpenAIEmbeddings(
    azure_deployment=Config.AZURE_EMBEDDINGS_DEPLOYMENT_NAME,
    azure_endpoint=Config.AZURE_OPENAI_ENDPOINT,
    model=Config.AZURE_EMBEDDINGS_MODEL_NAME,
    api_key=Config.AZURE_EMBEDDINGS_API_KEY,
    chunk_size=64
)

ENCODING = tiktoken.get_encoding("gpt2")
