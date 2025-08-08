# extractor.py

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
import os

# ---- 1. Setup ----
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# ---- 2. Load PDF ----
loader = PyPDFLoader("Remote Work Policy – 2025.pdf")
pages = loader.load()

# ---- 3. Chunk text ----
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(pages)

# ---- 4. Run QA chain ----
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
chain = load_qa_chain(llm, chain_type="stuff")

query = "Summarize the key points from this document."
response = chain.run(input_documents=docs, question=query)

# ---- 5. Output ----
print("📄 Summary:\n")
print(response)
