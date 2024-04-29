from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


@app.get("/", description="This is the root path")
async def get_root():
    return {"message": "Hello World"}

@app.post('/')
async def post_root():
    return {"message": 'hello from the post method'}

@app.put('/')
async def put_root():
    return {"message": 'hello from the put method'}

@app.get("/users")
async def read_items():
    return {"message": "list items from the read method"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

@app.get('/users/me')
async def get_current_user():
    return {'user_id': 'this is the current user'}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
