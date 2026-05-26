from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI

from crew import build_crew

load_dotenv()

app = FastAPI()


@app.post("/run")
def run_crew():
    result = build_crew().kickoff()
    return {"result": str(result)}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

