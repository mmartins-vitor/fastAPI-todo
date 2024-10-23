from fastapi import APIRouter

todo_router = APIRouter(prefix="/api", tags=["Todo"])

@todo_router.get("/")
def all_todos():
    return "Not Implemented"

@todo_router.post("/")
def todo_post():
    return "Not Implemented"

@todo_router.put("/{key}")
def update_put(key:int):
    return "Not Implemented"

@todo_router.delete("/{key}")
def delete_todo(key:int):
    return "Not Implemented"