import json
from localEmbeddings import LocalEmbeddings
from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from vectorstores import load_vectorstores

# Подключение к лодели embeddings
def connect_embeddings_model(config) -> LocalEmbeddings:
    try:
        with open(config, 'r') as config_file: 
            config = json.load(config_file)
    except:
        print('Error open config')
        return 'Error open config'
    try: 
        model_embeddings = LocalEmbeddings(
            model=config['model_embeddings'],
            linck=config['base_url_embeddings']
        )
        return model_embeddings
    except:
        print('Error connect embeddings model')
        return 'Error connect embeddings model'
    
# Функция подключения к модели
def connect_model(config) -> OpenAI:
    try:
        with open(config, 'r') as config_file: 
            config = json.load(config_file)
    except:
        print('Error open config')
        return 'Error open config'
    try:
        model = OpenAI(
            base_url=config['base_url_gtp'],
            model=config['model_gpt'],
            api_key='non'
        )
        return model
    except:
        print('Error connect model')
        return 'Error connect model'

# Ответ на запрос
def query(text, config):
    model = connect_model(config)
    embeddings_model = connect_embeddings_model(config)


    vectorstore = load_vectorstores('vectorstores', embeddings_model)
    retriever = vectorstore.as_retriever()

    vect = retriever.invoke(text)
    temple = ChatPromptTemplate([
        ("system", 'Дай ответ в 3-7 предложений на вопрос. Зная следующую информацию: {vect}'),
        ("user", '{text}')
    ])
    out = model.invoke(
        temple.invoke({
            'vect':vect,
            'text':text
        })
    )
    return out