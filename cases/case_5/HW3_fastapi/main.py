from fastapi import FastAPI

app = FastAPI()

#Define Endpoints:
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}


#Implement Business Logic Layer:
def get_item(item_id: int, query_param: str = None):
    # Business logic to retrieve item information
    return {"item_id": item_id, "query_param": query_param, "description": "Item details"}

def perform_some_task(data: dict):
    # Business logic to perform a specific task
    return {"result": "Task completed successfully"}

#Integrate Business Logic with Endpoints:

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    item_info = get_item(item_id, query_param)
    return item_info

@app.post("/perform_task")
def perform_task(data: dict):
    result = perform_some_task(data)
    return result


