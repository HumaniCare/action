import asyncio

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(subscribe_schedule())
    yield
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Redis task cancelled")


app = FastAPI(lifespan = lifespan)

auth_scheme = HTTPBearer()