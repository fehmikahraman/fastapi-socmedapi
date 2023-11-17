# fastapi-socmedapi
This repo aims to demonstrate the implementation of some core features of FastAPI.

### Installation
> git clone https://github.com/fehmikahraman/fastapi-socmedapi.git <br>
> cd socmedapi <br>
> pip install -r requirements.txt <br>
> pip install -r requirements-dev.txt <br>

### Run
> uvicorn socmedapi.main:app --reload

### Check it

You can check the interactive API document. Open your browser at http://127.0.0.1:8000/docs  <br>
You can check the API paths and parameters.


### Docker

> cd socmedapi <br>
> docker compose up

## Endpoints (Docker)

 (POST) it needs a request body to create a social media post.
> http://localhost:4444/post

(GET) it shows all posts (default max 100).
> http://localhost:4444/posts

(POST) it creates a comment for a post. it requires a request body with a comment and post id. 
> http://localhost:4444/comment

(GET) it gets a post with all comments.
> http://localhost:4444/post/{post_id}

(GET) it gets just the comments on a post.
>http://localhost:4444/post/{post_id}/comment  

## Run tests

> docker exec socmedapi-web-1 pytest -v
