import requests

class TestClient:
    def get_event_data(self, accountId):
        payload = { "accountId": accountId }
        r = requests.get(
            "https://www.nested-object.com/v3/users/me/",
            params=payload
        )

        if r.status_code == 200:
            return r.status_code, "Extract complete"
        else:
            return r.status_code, r.text