# def rag_query(question):
#     docs = ["ULEAM offers AI courses.", "AI research includes robotics and IoT."]
#     # retrieve relevant doc
#     context = [doc for doc in docs if "IoT" in doc]
#     # generate answer
#     return f"Answer based on retrieved data: {context[0]}"

# print(rag_query("What AI research does ULEAM have?"))



# class AgenticRAG:
#     def __init__(self, knowledge_base):
#         self.kb = knowledge_base
#         self.memory = []
    
#     def think(self, question):
#         print(f"🤔 Step 1: Analyzing question: '{question}'")
#         if "AI" in question:
#             keywords = ["AI", "research"]
#         else:
#             keywords = question.split()
#         return keywords

#     def retrieve(self, keywords):
#         print(f"🔍 Step 2: Searching with keywords {keywords}")
#         results = [doc for doc in self.kb if any(k in doc for k in keywords)]
#         self.memory.extend(results)
#         return results

#     def reason(self):
#         print("🧩 Step 3: Combining and verifying information...")
#         return "ULEAM focuses on AI research areas such as robotics, IoT, and machine learning."

#     def run(self, question):
#         keywords = self.think(question)
#         results = self.retrieve(keywords)
#         answer = self.reason()
#         return answer

# # Example use
# docs = ["ULEAM offers AI courses.",
#         "AI research includes robotics and IoT.",
#         "Students develop ML projects in collaboration with industry."]
# agent = AgenticRAG(docs)
# print(agent.run("What AI research does ULEAM have?"))







# Simple RAG workflow with LangChain
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

# Create retriever
db = Chroma(persist_directory="docs_db", embedding_function=OpenAIEmbeddings())
retriever = db.as_retriever()

# Create QA chain
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    retriever=retriever
)

qa.run("What is electromechanical engineering?")
