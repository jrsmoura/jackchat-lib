"""
Question-answering pipeline using RAG.
"""
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from .retriever import RETRIEVER
from .models import LLM

def format_docs(docs):
    """
    Formats retrieved documents for the language model input.
    
    Args:
        docs (list): List of document chunks.
    
    Returns:
        str: Formatted document content.
    """
    return "\n\n".join(doc.page_content for doc in docs)

system_prompt = (
    "You are an assistant for question-answering tasks using retrieved documents.\n\n"
    "Context:\n\n{context}"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

rag_chain = (RunnablePassthrough.assign(context=lambda x: format_docs(x["context"])) | prompt | LLM | StrOutputParser())

CHAT_RAG_CHAIN = RunnableParallel({"context": RETRIEVER, "input": lambda x: x["input"]}).assign(answer=rag_chain)
