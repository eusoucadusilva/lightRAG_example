import os
from dotenv import load_dotenv

from llama_index.core import Settings, SimpleDirectoryReader, Document
from llama_index.core.indices.vector_store import VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core.query_engine import RouterQueryEngine
from llama_index.core.tools import QueryEngineTool, ToolMetadata

from graph.knowledge_graph import build_graph, export_graph_as_text

load_dotenv()

def create_rag_pipeline():
    # 📄 Carrega documentos da pasta data/
    docs = SimpleDirectoryReader("data").load_data()

    # 🌐 Cria grafo e converte em texto
    G = build_graph()
    graph_text = export_graph_as_text(G)
    graph_doc = Document(text=graph_text)

    # ⚙️ Configura LLM e embeddings
    Settings.llm = OpenAI(model="gpt-4o")
    Settings.embed_model = OpenAIEmbedding()

    # 🔍 Índices
    vector_index = VectorStoreIndex.from_documents(docs)
    graph_index = VectorStoreIndex.from_documents([graph_doc])  # trata grafo como texto

    # 🛠️ Ferramentas
    vector_tool = QueryEngineTool(
        query_engine=vector_index.as_query_engine(),
        metadata=ToolMetadata(name="text", description="Informações dos documentos originais.")
    )

    graph_tool = QueryEngineTool(
        query_engine=graph_index.as_query_engine(),
        metadata=ToolMetadata(name="graph", description="Relações semânticas do grafo de conhecimento.")
    )

    # 🧠 Engine com roteamento
    router_engine = RouterQueryEngine.from_defaults(
        query_engine_tools=[vector_tool, graph_tool]
    )

    return router_engine
