from langchain.vectorstores import FAISS
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

# Создание vectorstores и сохранение его
def create_vectorstores(models , data : list, saves = True, path = 'vectorstores') -> FAISS:
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
        print("Error create vectorstores")
        return "Error create vectorstores"
    
# Загрузка vectorstores из папки сохранения
def load_vectorstores(patch, model) -> FAISS:
    try:
        vectorstore = FAISS.load_local(
        patch, 
        model,
        allow_dangerous_deserialization=True
        )
        return vectorstore
    except:
        print("Error load vectorstores")
        return "Error load vectorstores"

# Сохранение split_data в папку
def save_slit_data(split_data : list):
    save_dict = dict(zip(
        [item.page_content.replace("\n", " ") for item in split_data], 
        [f"Файл: {item.metadata['source']} Страница {item.metadata['page']}" for item in split_data ]
    ))

    import pickle
    with open('text_spliter/data.pkl', 'wb') as f:
        pickle.dump(save_dict, f)
    return True

# Считывание данных из text_spliter
def load_data_dict() -> dict:
    import pickle
    with open('text_spliter/data.pkl', 'rb') as f:
        loaded_dict = pickle.load(f)
    return loaded_dict

# Загрузка данных из папки
def load_folder(patch = './dataset/'):
    try:
        loader = DirectoryLoader( path=patch, loader_cls=PyPDFLoader)
        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter.from_language(
            language=Language.MARKDOWN, 
            chunk_size=1024, 
            chunk_overlap=128
        )
        split_data = splitter.split_documents(docs)
        save_slit_data(split_data)
        return split_data
    except:
        print("Error load folder")
        return "Error load folder"
