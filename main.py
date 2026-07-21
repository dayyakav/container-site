from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from utils import get_uptime, get_hostname, get_python_version

app = FastAPI()

@app.get("/", response_class=FileResponse)
def read_index():
    return "index.html"

@app.get("/styles.css", response_class=FileResponse)
def read_index():
    return "styles.css"

@app.get("/info")
def read_info():

    uptime = get_uptime()
    hostname = get_hostname()
    python_version = get_python_version()

    return {
        "status": [
        {"os_uptime": uptime}, {"hostname": hostname}, {"python_version": python_version}
    ]}
