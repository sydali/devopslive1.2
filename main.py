from typing import Union
import uvicorn
 

from fastapi import FastAPI
from decouple import Config

config = Config()
config.read('.env')
int_val = config('VAR')

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
	
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
 uvicorn.run("main:app", host="0.0.0.0", port=8000, reload = False)
