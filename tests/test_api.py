def test_get_state(client):
    response = client.get("/state")
    assert response.status_code == 200
    data = response.get_json()
    assert "energy" in data
    assert "coffee" in data
    assert "knowledge" in data

def test_post_reset(client):
    response = client.post("/reset")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Game reset"
    assert "state" in data

def test_study_action(client):
    response = client.post("/action", json={"action": "study"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["action"] == "study"
    assert "state" in data

def test_post_wrong_action(client):
    response = client.post("/action", json={"wrong": "study"})
    assert response.status_code == 400
    data = response.get_json()
    assert data["error"] == "action is required"