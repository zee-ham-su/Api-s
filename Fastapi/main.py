from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/", description="This is the root path")
async def get_root():
    return {"message": "Hello World"}

@app.post('/')
async def post_root():
    return {"message": 'hello from the post method'}

@app.put('/')
async def put_root():
    return {"message": 'hello from the put method'}

@app.get("/items")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def get_item(item_id: bool):
    return {"item_id": item_id}

@app.get('/users/me')
async def read_users_me():
    return {'user_id': 'the current user'}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
