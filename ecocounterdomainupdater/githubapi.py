import json
import re

import requests


def get_gist():
    url = "https://api.github.com/gists/33d03f2de5add333c0217106cca35478"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer TOKEN",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        gist = response.json()
        return json.loads(gist["files"]["domains.json"]["content"])
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def update_gist(domains):
    url = "https://api.github.com/gists/33d03f2de5add333c0217106cca35478"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer TOKEN",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    patch_body = {
        "files": {
            "domains.json": {
                "content": re.sub(" {2}},\\w*\n {2}\\{", "}, {", json.dumps(domains, sort_keys=True, indent=2, ensure_ascii=False), flags=re.MULTILINE),
            }
        }
    }
    try:
        response = requests.patch(url, headers=headers, json=patch_body)
        response.raise_for_status()
    except Exception as e:
        print(f"An error occurred: {e}")
