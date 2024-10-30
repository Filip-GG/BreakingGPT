from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()
config = 'config.json'

class Query(BaseModel):
    type : str
    query : str
    """
    type - переменная типа запроссв{
        query - запрос в llm
        restart - рестарт системы
        start_rog - запуск rog обуения
        load_file - загрузка файла
        delete_file - удаление файла
        }
    """

query_type = ["query", "restart", "start_rog", "load_file", "delete_file"]

# Запрос
@app.post('/')
async def query(data: Query):
    if data.type == query_type[0]:
        from model import query
        out = query(data.query, config)
        return out
    return "У вас не достаточно прав для использывавания."

@app.post('/admin')
async def admin_qery(data: Query):
    if data.type == query_type[0]:
        return query(data)
    