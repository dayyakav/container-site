Containerized local website with a FastAPI backend

# Requirements

- Podman / Docker installed

# Installation

1.  Build container:
    
    ```
    podman build -t my-app .
    ```
    
2.  Run:
    
    ```
    podman run -p 8000:8000 my-app
    ```
