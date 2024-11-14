from ecocounterdomainupdater import githubapi
from ecocounterdomainupdater.fetcher import update_domain_list


def lambda_handler(event, context):
    githubapi.authorize("TOKEN")
    update_domain_list("33d03f2de5add333c0217106cca35478", 10_001)
