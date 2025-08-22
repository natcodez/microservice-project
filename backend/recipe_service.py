import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_FILE = "recipes.db"

# Initialize database
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        ingredients TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

init_db()


# ---------------- API Routes ---------------- #

@app.get("/recipes")
def get_recipes():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, ingredients FROM recipes")
    rows = cursor.fetchall()
    conn.close()

    recipes = []
    for row in rows:
        recipes.append({
            "id": row[0],
            "name": row[1],
            "ingredients": row[2].split(",")
        })
    return recipes


@app.post("/recipes")
def add_recipe(name: str, ingredients: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO recipes (name, ingredients) VALUES (?, ?)", (name, ingredients))
    conn.commit()
    conn.close()
    return {"message": "Recipe added successfully"}


@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
    conn.commit()
    conn.close()
    return {"message": f"Recipe {recipe_id} deleted successfully"}

