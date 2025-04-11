# Cenário de Aplicação: Sistema RAG para Empresa de Cursos de Inteligência Emocional (Ex: Febracis)

## 🧠 Cenário

**Empresa**: Febracis  
**Objetivo**: Oferecer cursos de inteligência emocional e coaching para profissionais, empreendedores e pessoas que buscam se desenvolver pessoal e profissionalmente.

---

## 💡 Como o Código Pode Ser Útil

### 📄 Documentos de Conhecimento

A Febracis possui diversos documentos sobre seus cursos, metodologias, depoimentos de clientes, artigos sobre inteligência emocional e mais.

O objetivo é carregar esses documentos no sistema e criar um **grafo de conhecimento** que relacione as informações entre si, como:

- `Cursos` → `Conteúdo abordado` → `Benefícios`
- `Depoimentos` → `Transformação`
- `Facilitadores` → `Especialização`

---

### 📌 Exemplo de Dados

```
Curso CIS → Formação em Inteligência Emocional  
Método CIS → Coaching e PNL para alta performance  
Facilitadores → Profissionais especializados em desenvolvimento humano  
Transformação → Aumento da performance e equilíbrio emocional  
```

---

### 🧭 Grafo de Conhecimento

O grafo construído a partir do código pode ser uma representação semântica de como os cursos, métodos, facilitadores e transformações estão conectados.

---

### 🧠 Consulta ao Sistema (RAG)

Com o pipeline RAG (Retriever-Augmented Generation), o cliente pode fazer perguntas e o sistema utilizará tanto o grafo de conhecimento quanto os documentos para gerar uma resposta contextualizada.

#### Exemplo de perguntas que o cliente pode fazer:

- "Quais cursos a Febracis oferece para líderes?"
- "Qual é a metodologia do curso CIS?"
- "Como a inteligência emocional pode melhorar minha performance profissional?"

---

## 🛠️ Implementação no Código

### 📁 Arquivo `data/arquivo.txt` (Dados sobre a empresa):

```
Febracis → Empresa de cursos de inteligência emocional.  
Método CIS → Curso focado em coaching e inteligência emocional.  
Facilitadores → Profissionais qualificados em coaching e PNL.  
Benefícios → Aumento de performance e equilíbrio emocional.  
```

---

### 📊 Grafo de Conhecimento (`knowledge_graph.py`):

```python
def build_graph():
    G = nx.Graph()
    G.add_edge("Febracis", "empresa de cursos de inteligência emocional")
    G.add_edge("Método CIS", "coaching e inteligência emocional")
    G.add_edge("Facilitadores", "coaching e PNL")
    G.add_edge("Benefícios", "aumento de performance")
    return G
```

---

### 🤖 Consulta do Sistema (`main.py`):

Quando você rodar o código com o pipeline RAG, o sistema será capaz de responder às perguntas de forma inteligente, utilizando o grafo de conhecimento e os documentos armazenados no diretório `data/`.

#### Exemplo de consulta:

```python
question = "Quais cursos a Febracis oferece para líderes?"
response = engine.query(question)
print("\nResposta:", response)
```

#### Resultado esperado:

```
A Febracis oferece o curso Método CIS, que é focado em coaching e inteligência emocional para líderes e profissionais de alta performance.
```

---

## 🚀 Expansão para Outros Recursos

- **Depoimentos de Alunos**: Pode ser criado um grafo adicional com depoimentos e suas respectivas transformações.
- **Novos Cursos**: Basta adicionar novos arquivos de dados ou atualizar os existentes.

---

## 📋 Passos para Implementar o Cenário

1. **Carregar os Dados de Cursos e Transformações**
   - Criar arquivos de texto em `data/` com detalhes sobre os cursos, facilitadores e benefícios.

2. **Construir o Grafo de Conhecimento**
   - Usar a função `build_graph()` para relacionar os conceitos de maneira semântica.

3. **Configurar o RAG Pipeline**
   - Utilizar o `rag_pipeline.py` para configurar o pipeline RAG.
   - Adicionar os dados no formato correto usando `SimpleDirectoryReader`.

4. **Consulta do Usuário**
   - Testar o sistema com perguntas sobre cursos, benefícios e transformações.

---

## ❓ Exemplo de Perguntas Possíveis

- "Qual é o conteúdo abordado no Método CIS?"
- "O que é coaching e como ele pode ajudar na minha vida profissional?"
- "Quem são os facilitadores do curso CIS?"
- "Como a inteligência emocional pode melhorar a minha produtividade no trabalho?"

