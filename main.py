from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from recipeName import recipes

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https?://(localhost|127\.0\.0\.1)(:\d+)?",
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/recipe/{recipe_id}")
async def RecipeById(recipe_id : int):
    return {"name" : next((r["name"] for r in recipes if r["id"] == recipe_id), None)}

@app.get("/recipe/list/")
async def RecipeList(sort : str | None = None, order : str | None = None):
    if sort == 'name':
        return list({r["id"]: r["name"] for r in sorted(recipes, key=lambda x: x["name"], reverse=(order=='desc'))})
    elif sort == 'abv':
        return list({r["id"]: r["name"] for r in sorted(recipes, key=lambda x: x["alcohol"], reverse=(order=='desc'))})
    elif sort == 'latest':
        return list({r["id"]: r["name"] for r in sorted(recipes, key=lambda x: x["created_at"], reverse=True)})
    elif sort == 'popular':
        return list({r["id"]: r["name"] for r in sorted(recipes, key=lambda x: x["popularity"], reverse=True)})
    else:
        return list({r["id"]: r["name"] for r in sorted(recipes, key=lambda x: x["name"])})

@app.get("/recipeStep/{recipe_id}/{step_num}")
async def RecipeStepById(recipe_id : int, step_num : int):
    return {"step_info" : "this is dummy step info"}