from fastapi import FastAPI

app = FastAPI(title="TRdev API")

@app.get("/")
def home():
    return {"status": "online", "api": "TRdev API"}

@app.post("/agent/run")
def run_agent(agent: str, action: str, data: dict):
    return {
        "agent": agent,
        "action": action,
        "status": "queued",
        "data": data
    }
