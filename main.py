from fastapi import FastAPI
from fastapi.responses import FileResponse
from utils import get_uptime, get_hostname, get_python_version, get_platform, get_python_path, get_server_time

app = FastAPI()

@app.get("/", response_class=FileResponse)
def read_index():
    return "index.html"

@app.get("/styles.css", response_class=FileResponse)
def read_styles():
    return "styles.css"

@app.get("/info")
def read_info():

    uptime = get_uptime()
    hostname = get_hostname()
    python_version = get_python_version()
    platform = get_platform()
    python_path = get_python_path()
    server_time = get_server_time()

    return {
        "status": [
        {"platform": platform},
        {"os_uptime": uptime},
        {"hostname": hostname},
        {"python_version": python_version},
        {"python_path": python_path},
        {"server_time": server_time}
    ]}
