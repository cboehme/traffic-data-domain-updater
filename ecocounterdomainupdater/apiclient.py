import json
import re

import requests

# Faking headers is only for "obscurity":
HEADERS = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
}


def fetch_sites_in_domain(domain_id: int):
    """
    Retrieves a list of all available counter sites in the given domain.
    """
    url = f"https://www.eco-visio.net/api/aladdin/1.0.0/pbl/publicwebpageplus/{domain_id}?withNull=true"
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 404:
            return []
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def get_gist():
    url = "https://api.github.com/gists/33d03f2de5add333c0217106cca35478"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer ",
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
        "Authorization": "Bearer ",
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
