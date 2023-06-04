import logging

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to The AI Among Us api."}


@app.get("/health_check", status_code=status.HTTP_200_OK)
def health_check():
    return {"message": "ok"}
