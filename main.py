import os
import django

# Set the default settings module for the Django environment

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foodtruck.settings")
# Initialize Django

django.setup()

from fastapi import FastAPI
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from food_truck_finder.controller import food_truck_router


# Create a new FastAPI instance
app = FastAPI()

# Include the food truck router with a prefix of "/api"
app.include_router(food_truck_router, prefix="/api")

# Mount the static files directory to serve static files (e.g., CSS, JS) at the "/static" URL path
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the index.html at the root URL
@app.get("/", response_class=HTMLResponse)
async def serve_index():
    with open(os.path.join("static", "index.html")) as f:
        return HTMLResponse(content=f.read(), status_code=200)
