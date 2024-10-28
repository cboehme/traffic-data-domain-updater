import json

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


def update_gist(domains):
    url = "https://api.github.com/gists/5034712e9e86452d9197998b2837fc76"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer ",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    patch_body = {
        "files": {
            "domains.json": {
                "content": json.dumps(domains, sort_keys=True, indent=2),
            }
        }
    }
    try:
        response = requests.patch(url, headers=headers, json=patch_body)
        response.raise_for_status()
        print(response.status_code)
    except Exception as e:
        print(f"An error occurred: {e}")
