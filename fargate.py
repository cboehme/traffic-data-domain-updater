import os

from trafficdatadomainupdater import githubapi
from trafficdatadomainupdater.updater import update_domain_list

githubapi.authorize(os.environ["GITHUB_TOKEN"])
update_domain_list(os.environ["GIST_ID"], int(os.environ["MAX_DOMAIN_ID"]))
