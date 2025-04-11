from rag_pipeline import create_rag_pipeline

engine = create_rag_pipeline()

question = "Quais cursos a Febracis oferece para líderes?"
response = engine.query(question)

print("\nResposta:")
print(response)
