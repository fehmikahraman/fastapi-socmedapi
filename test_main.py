from fastapi.testclient import TestClient

from socmedapi.main import app

client= TestClient(app)

def test_create_post ():
    body="this is a test post body"
    response = client.post("/post", json={"body": body})
    
    assert response.status_code == 201

def test_get_all_posts():
    response = client.get("/post")
    assert response.status_code==200

def test_create_comment_for_post ():
    body="this is a test post body"
    post_id=1
    response = client.post("/comment", json={"body": body, "post_id": post_id})
    
    assert response.status_code == 201
