Nothing special, just some example

## What it does

Single HTML page with a link to the '/info' API endpoint. What else?

## Screenshots

<img src="screenshot.png" alt="screenshot.png" width="633" height="435">

## Requirements

- [Podman](https://podman.io/) / [Docker](https://www.docker.com/) installed

## Installation

1.  Clone this repo:
    
    ```
    git clone https://github.com/dayyakav/container-site.git
    ```
    
2.  Build container:
    
    ```
    podman build -t my-app .
    ```
    
3.  Run:
    
    ```
    podman run -p 8000:8000 my-app
    ```
    
4.  Go to http://127.0.0.1:8000
