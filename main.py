from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from recipeName import recipe

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/recipe/{recipe_id}")
async def RecipeById(recipe_id : int):
    
    return {"name" : recipe[recipe_id]}