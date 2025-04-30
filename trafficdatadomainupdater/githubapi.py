# Traffic Data Domain Updater - Updates the list of counter site domains
# Copyright (C) 2025  Christoph Böhne
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import json
import re

import requests

_access_token = None


def authorize(token: str):
    global _access_token
    _access_token = token


def _get_headers():
    return {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {_access_token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }


def get_gist(gist_id: str):
    url = f"https://api.github.com/gists/{gist_id}"
    try:
        response = requests.get(url, headers=_get_headers())
        response.raise_for_status()
        gist = response.json()
        return json.loads(gist["files"]["domains.json"]["content"])
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def update_gist(gist_id: str, domains):
    url = f"https://api.github.com/gists/{gist_id}"
    patch_body = {
        "files": {
            "domains.json": {
                "content": re.sub(" {2}},\\w*\n {2}\\{", "}, {", json.dumps(domains, sort_keys=True, indent=2, ensure_ascii=False), flags=re.MULTILINE),
            }
        }
    }
    try:
        response = requests.patch(url, headers=_get_headers(), json=patch_body)
        response.raise_for_status()
    except Exception as e:
        print(f"An error occurred: {e}")
