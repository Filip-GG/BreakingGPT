from langchain.embeddings.base import Embeddings
import requests
import time

class LocalEmbeddings(Embeddings):
    def __init__(self,linck,model, sleep_interval=1):
        self.model = model
        self.linck = linck
        self.sleep_interval = sleep_interval

    def embed_document(self, text):
        j = {
            "model": self.model,
            "input": text
        }

        res = requests.post(
            self.linck,
            json = j
        )
        vec = res.json()['data'][0]['embedding']
        
        return vec

    def embed_documents(self, texts, chunk_size = 0):
        res = []
        for x in texts:
            res.append(self.embed_document(x))
            time.sleep(self.sleep_interval)
        return res

    def embed_query(self, text):
        j = {
            "model": self.model,
            "input": text
        }

        res = requests.post(
            self.linck,
            json = j,

        )
        vec = res.json()['data'][0]['embedding']
        
        return vec