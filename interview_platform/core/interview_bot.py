from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain, create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain 
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import json
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain.vectorstores.utils import filter_complex_metadata
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from sentence_transformers import SentenceTransformer
from transformers import AutoModel, AutoTokenizer
import torch
from openai import OpenAI   
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import create_retrieval_chain
import datasets

# 直接讀入hugging face文件的情況
#class Document:
#    def __init__(self, content, metadata=None):
#        self.page_content = content
#        self.metadata = metadata if metadata is not None else {}

class InterviewBot:
    # def __init__(self, content="", chat_history=None):
    def __init__(self, chat_history=None):
        
        # cmd: ollama run llama3:8b
        # cmd: ollama pull llama3:8b
        self.embeddings = OllamaEmbeddings(model='llama3:8b')
        self.llm = ChatOpenAI(model = 'llama3:8b', base_url = 'http://localhost:11434/v1', api_key='ollama')
        # ----------------------------------------------------------------------
        # run too long
        # use hugging face data to do the 
        #self.page_content = content
        #ds_sft = datasets.load_dataset('TigerResearch/tigerbot-kaggle-leetcodesolutions-en-2k')
        #ds = ds_sft['train']
        #questions = [row['instruction'] + " " + row['input'] for row in ds]
        #answers = [row['output'] for row in ds]
        # 加入 metadata，可以是空字典或者具体信息
        #documents = [Document(question + " " + answer, {'source': 'LeetCode Solution'}) for question, answer in zip(questions, answers)]
        # 正确地将整个 documents 列表传递给 FAISS.from_documents
        #self.vector_store = FAISS.from_documents(documents, self.embeddings)
        # ----------------------------------------------------------------------

        self.vector_store = FAISS.from_texts(['鄧不利多是霍格華滋的校長'], self.embeddings)
        self.retriever = self.vector_store.as_retriever()

        
        prompt = ChatPromptTemplate.from_messages([
            # 答案基於事先輸入的資料
            ('system', 'Answer the user\'s questions based on the below context:\n\n{context}'),
            MessagesPlaceholder(variable_name='chat_history'),
            ('user', '{input}'),
        ])
        # document_chain負責找外部資料
        self.document_chain = create_stuff_documents_chain(self.llm, prompt)

        prompt = ChatPromptTemplate.from_messages([
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
            ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation"),
        ])

        # 生成回應
        # retriever_chain 負責找對話紀錄
        self.retriever_chain = create_history_aware_retriever(self.llm, self.retriever, prompt)
        # 建立可以檢索對話跟外部輸入資料的 chain
        self.retrieval_chain = create_retrieval_chain(self.retriever_chain, self.document_chain)

        # 保存對話紀錄
        # Initialize chat_history
        # self.chat_history = chat_history if chat_history is not None else [] # chat history
        self.chat_history = []
    
    def build_contextual_prompt(self):
        recent_messages = self.chat_history[-5: ] if self.chat_history is not None else []
        context = " ".join([f"{msg['role']}: {msg['content']}" for msg in recent_messages])
        return context


    def get_response(self, user_input):
        self.chat_history.append({'role': 'user', 'content': user_input})
        contextual_prompt = self.build_contextual_prompt()

        response = self.retrieval_chain.invoke({
            'input': user_input,
            'context': contextual_prompt,
            'chat_history': self.chat_history
        })

        self.chat_history.append({'role': 'system', 'content': response['answer']})
        return response['answer']

        #return prompt

