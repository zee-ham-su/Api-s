from fastapi import FastAPI

app = FastAPI()



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
async def get_items():
    return {"message": 'hello from the get items method'}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}