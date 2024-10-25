from langchain.vectorstores import FAISS
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

# Создание vectorstores и сохранение его
def create_vectorstores(path, models , data : list, saves = True):
    try:
        vectorstore = FAISS.from_texts(
        [
            i.page_content.replace("\n", " ")
            for i in data
        ], 
        embedding=models
        )
        if saves:
            vectorstore.save_local(path)
        return vectorstore
    except:
        return "Error create vectorstores"
    
# Загрузка vectorstores из папки сохранения
def load_vectorstores(patch, model):
    try:
        vectorstore = FAISS.load_local(
        patch, 
        model,
        allow_dangerous_deserialization=True
        )
        return vectorstore
    except:
        return "Error load vectorstores"
    
# Загрузка данных из папки
def load_folder(patch):
    try:
        loader = DirectoryLoader( path=patch, loader_cls=PyPDFLoader)
        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter.from_language(
            language=Language.MARKDOWN, 
            chunk_size=1024, 
            chunk_overlap=128
        )
        split_data = splitter.split_documents(docs)
        return split_data
    except:
        return "Error load folder"

