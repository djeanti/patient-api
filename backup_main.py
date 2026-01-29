from enum import IntEnum 
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

api = FastAPI()

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class TodoBase(BaseModel):
    todo_name: str = Field(..., min_lenght=3, max_lenght=512, description='Name of the todo')
    todo_description: str = Field(..., description='Description of the todo')
    priority: Priority = Field(default=Priority.LOW, description='Priority of the todo')

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    todo_id: int = Field(..., description='Unique identifier of the todo') 

class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(None, min_lenght=3, max_lenght=512, description='Name of the todo')
    todo_description: Optional[str] = Field(None, description='Description of the todo')
    priority: Optional[Priority] = Field(None, description='Priority of the todo')



all_todos = [
    Todo(todo_id = 1, todo_name = 'Sports', todo_description = 'Do 5 pushups', priority=Priority.HIGH),
    Todo(todo_id = 2, todo_name = 'Read', todo_description = 'Read 5 pages', priority=Priority.MEDIUM),
    Todo(todo_id = 3, todo_name = 'Shop', todo_description = 'Go buy groceries', priority=Priority.LOW),
    Todo(todo_id = 4, todo_name = 'Study', todo_description = 'Study FastAPI until 14h00 PM', priority=Priority.MEDIUM),
    Todo(todo_id = 5, todo_name = 'Medidate', todo_description = 'Medidate 10 minutes after waking up everyday', priority=Priority.HIGH)
]


"""
# endpoint
@api.get('/') # '/' specifies where is the endpoint
def index():
    return {'message': 'hellow world'}

@api.get('/calculation') # '/' specifies where is the endpoint
def index(): # cpu method that uses cpu (so no need to turn it asynchronous)
    pass
    return {'message': 'hellow world'}
"""

@api.get('/todos/{todo_id}', response_model=Todo) # equivalent to URL: localhost:9999/todos/2
def get_todo(todo_id):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
    raise HTTPException(404, detail='Todo not found')

# URL: localhost:9999/todos?first_n=3 -> query parameter is used
@api.get('/todos', response_model=List[Todo])
def get_todo(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos

@api.post('/todos', response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = len(all_todos)+1
    new_dict =  Todo(todo_id = new_todo_id, todo_name=todo.todo_name, todo_description=todo.todo_description, priority=todo.priority)
    all_todos.append(new_dict)   
    return new_dict

@api.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return todo
    raise HTTPException(404, detail='Todo not found')

@api.delete('/todos/{todo_id}', response_model=Todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
    raise HTTPException(404, detail='Todo not found')
