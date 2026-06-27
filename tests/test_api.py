import pytest

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



@pytest.mark.parametrize("payload", [
    {},
    {"wrong": "study"},
    {"action": ""},
    {"action": None}
])
def test_post_invalid_action(payload, client):
    response = client.post("/action", json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
