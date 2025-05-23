from datetime import datetime

# 16개의 실제 칵테일 데이터를 생성
recipes = [
    {
        "id": 1,
        "name": "Martini",
        "alcohol": 30,
        "created_at": datetime(2023, 12, 1),
        "popularity": 120,
        "ingredients": ["gin", "dry vermouth", "olive"],
        "difficulty": 2
    },
    {
        "id": 2,
        "name": "Mojito",
        "alcohol": 14,
        "created_at": datetime(2024, 1, 10),
        "popularity": 240,
        "ingredients": ["white rum", "mint", "lime", "sugar", "soda water"],
        "difficulty": 1
    },
    {
        "id": 3,
        "name": "Margarita",
        "alcohol": 25,
        "created_at": datetime(2024, 3, 5),
        "popularity": 180,
        "ingredients": ["tequila", "triple sec", "lime juice", "salt"],
        "difficulty": 2
    },
    {
        "id": 4,
        "name": "Tequila Shot",
        "alcohol": 40,
        "created_at": datetime(2024, 4, 1),
        "popularity": 90,
        "ingredients": ["tequila", "salt", "lime"],
        "difficulty": 1
    },
    {
        "id": 5,
        "name": "Cosmopolitan",
        "alcohol": 27,
        "created_at": datetime(2024, 2, 15),
        "popularity": 160,
        "ingredients": ["vodka", "triple sec", "cranberry juice", "lime juice"],
        "difficulty": 2
    },
    {
        "id": 6,
        "name": "Old Fashioned",
        "alcohol": 32,
        "created_at": datetime(2024, 1, 5),
        "popularity": 200,
        "ingredients": ["bourbon", "bitters", "sugar", "orange peel"],
        "difficulty": 3
    },
    {
        "id": 7,
        "name": "Mai Tai",
        "alcohol": 28,
        "created_at": datetime(2023, 11, 20),
        "popularity": 110,
        "ingredients": ["light rum", "dark rum", "lime juice", "orange curaçao", "orgeat syrup"],
        "difficulty": 3
    },
    {
        "id": 8,
        "name": "Nigasakki",
        "alcohol": 22,
        "created_at": datetime(2024, 3, 20),
        "popularity": 75,
        "ingredients": ["soju", "beer", "cola"],
        "difficulty": 1
    },
    {
        "id": 9,
        "name": "Blue Mojito",
        "alcohol": 16,
        "created_at": datetime(2024, 3, 8),
        "popularity": 130,
        "ingredients": ["white rum", "mint", "lime", "blue curaçao", "sugar", "soda water"],
        "difficulty": 2
    },
    {
        "id": 10,
        "name": "Bloody Mary",
        "alcohol": 10,
        "created_at": datetime(2023, 10, 18),
        "popularity": 150,
        "ingredients": ["vodka", "tomato juice", "lemon juice", "tabasco", "celery"],
        "difficulty": 3
    },
    {
        "id": 11,
        "name": "Manhattan",
        "alcohol": 33,
        "created_at": datetime(2024, 2, 1),
        "popularity": 170,
        "ingredients": ["rye whiskey", "sweet vermouth", "bitters", "cherry"],
        "difficulty": 3
    },
    {
        "id": 12,
        "name": "Champagne Cocktail",
        "alcohol": 20,
        "created_at": datetime(2024, 1, 20),
        "popularity": 100,
        "ingredients": ["champagne", "bitters", "sugar cube", "lemon peel"],
        "difficulty": 2
    },
    {
        "id": 13,
        "name": "Sex on the Beach",
        "alcohol": 18,
        "created_at": datetime(2024, 3, 25),
        "popularity": 210,
        "ingredients": ["vodka", "peach schnapps", "cranberry juice", "orange juice"],
        "difficulty": 1
    },
    {
        "id": 14,
        "name": "Apple Martini",
        "alcohol": 24,
        "created_at": datetime(2024, 2, 20),
        "popularity": 140,
        "ingredients": ["vodka", "apple schnapps", "lemon juice"],
        "difficulty": 2
    },
    {
        "id": 15,
        "name": "Tom Collins",
        "alcohol": 17,
        "created_at": datetime(2023, 9, 28),
        "popularity": 95,
        "ingredients": ["gin", "lemon juice", "sugar", "soda water"],
        "difficulty": 2
    },
    {
        "id": 16,
        "name": "Espresso Martini",
        "alcohol": 21,
        "created_at": datetime(2024, 3, 30),
        "popularity": 185,
        "ingredients": ["vodka", "coffee liqueur", "espresso", "sugar syrup"],
        "difficulty": 3
    }
]