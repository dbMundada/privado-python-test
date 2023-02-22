import requests
import os, Path

def test():
    endpoint = "https://" + str(Path("hooks.slack.com/services", os.getenv("SLACK_WEBHOOK")))
    headers = {"Content-Type": "application/json"}
    requests.post(endpoint, headers=headers, json=payload)