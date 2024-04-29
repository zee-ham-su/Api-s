from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class FoodEnum(str, Enum):
    fruit = 'fruit'
    vegetable ='vegetable'
    dairy = 'dairy'


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


@app.get('/users/me')
async def get_current_user():
    return {'user_id': 'this is the current user'}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}



@app.get('/foods/{food_name}')
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.fruit:
        return {"food_name": food_name, "message": "This is a fruit"}
    if food_name == FoodEnum.vegetable:
        return {"food_name": food_name, "message": "This is a vegetable"}
    
    return {"food_name": food_name, "message": "This is a dairy"}
