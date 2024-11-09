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


