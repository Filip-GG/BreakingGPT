from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

app = FastAPI()
config = 'config.json'

class Query(BaseModel):
    type : str
    query : str
    """
    type - переменная типа запроссв{
        query - запрос в llm (в query запрос)
        restart - рестарт системы 
        start_rog - запуск rog обуения
        folder_list - список файлов для обучения
        load_file - загрузка файла
        delete_file - удаление файла (в query название файла)
        }
    """

query_type = ["query", "restart", "start_rog", "folder_list", "load_file", "delete_file"]

# Получение списка файлов для обучения
@app.post('/folder_list')
async def folder_list(data: Query):
    if data.type == query_type[3]:
        from file_message import dataset_listdir
        return dataset_listdir('dataset')
    return 'Ошибка запросса'

# Удаление файла
@app.post('/del_file')
async def del_file(data: Query):
    if data.type == query_type[5]:
        from file_message import delete_file
        return delete_file('./dataset/'+data.query)
    return 'Ошибка запросса'

# Загрузка файла
@app.post('/uploloadfile')
def upload_file(uploaded_file: UploadFile = File(...)):
    file_location = f"dataset_input/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())
    from file_message import to_all_pdf
    to_all_pdf('dataset_input','./dataset/')
    return f"Файл сохранен '{file_location}'"

# Запрос пользывателя
@app.post('/user')
async def query(data: Query):
    if data.type == query_type[0]:
        from model import query
        out = query(data.query, config)
        return out
    return "У вас не достаточно прав для использывавания."

# Запрос администратора
@app.post('/admin')
async def admin_qery(data: Query):
    if data.type == query_type[0]:
        return query(data)
    
    # переобучение системы
    if data.type == query_type[2]:
        from vectorstores import create_vectorstores, load_folder
        from model import connect_embeddings_model
        from file_message import to_all_pdf

        try:
            ambedding_model = connect_embeddings_model(config)
            #to_all_pdf('dataset_input','./dataset/')
            data = load_folder('./dataset/')
            create_vectorstores(ambedding_model, data)
            return 'Обучние прошло успешно'
        except: 
            return 'Ошибка обучени на rog'
        