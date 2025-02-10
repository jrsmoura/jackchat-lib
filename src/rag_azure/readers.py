"""
Module for document loading and preprocessing.
"""
from langchain_community.document_loaders import PyMuPDFLoader
from .config import Config

def load_documents():
    """
    Loads and splits documents from configured paths.
   
    Returns:
        list: A list of processed document chunks.
    """
    docs_list = []
    for doc in Config.DOCS_PATHS:
        loader = PyMuPDFLoader(doc)
        temp = loader.load_and_split()
        docs_list += temp
    return docs_list
