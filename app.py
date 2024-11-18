from dotenv import load_dotenv
from fastapi import FastAPI

from routers import manual_router, resume_router

load_dotenv()

app = FastAPI()

app.include_router(resume_router.router)
app.include_router(manual_router.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("__main__:app", port=5000, host="0.0.0.0", reload=True)
