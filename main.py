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

@app.get("/recipe/list/")
async def RecipeList(sort : str | None = None, pivot : str | None = None):
    if sort == 'asc':
        return {"id_list" : list(range(1,17))}
    elif sort == 'desc':
        return {"id_list" : list(range(1,17)[::-1])}
    else:
        return {"id_list" : list(range(1,17))}

@app.get("/recipeStep/{recipe_id}/{step_num}")
async def RecipeStepById(recipe_id : int, step_num : int):
    return {"step_info" : "this is dummy step info"}