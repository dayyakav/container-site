Containerized local website with a FastAPI backend

# Requirements

- [Podman](https://podman.io/) / [Docker](https://www.docker.com/) installed

# Installation

1.  Build container:
    
    ```
    podman build -t my-app .
    ```
    
2.  Run:
    
    ```
    podman run -p 8000:8000 my-app
    ```
