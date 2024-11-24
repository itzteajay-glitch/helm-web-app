from fastapi import FastAPI, HTTPException
from utils.helm import get_charts, get_chart_values, generate_helmrelease

app = FastAPI()

@app.get("/charts")
async def list_charts(repo_url: str):
    try:
        charts = get_charts(repo_url)
        return {"charts": charts}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/chart/{name}/values")
async def chart_values(repo_url: str, chart_name: str, version: str):
    try:
        values = get_chart_values(repo_url, chart_name, version)
        return {"values": values}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate")
async def generate_release(chart: dict):
    try:
        release_yaml = generate_helmrelease(chart)
        return {"yaml": release_yaml}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
