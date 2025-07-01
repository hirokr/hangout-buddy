# hangout_buddy/main.py

from fastapi import FastAPI
from core.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.PROJECT_NAME)

# Middleware (CORS, future rate limiting, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Healthcheck
@app.get("/")
def read_root():
    return {"msg": "Hangout Buddy API is running"}

# Router registration
# from api.v1.endpoints import auth, users

# app.include_router(auth.router, prefix=f"{settings.API_PREFIX}/auth", tags=["Auth"])
# app.include_router(users.router, prefix=f"{settings.API_PREFIX}/users", tags=["Users"])
