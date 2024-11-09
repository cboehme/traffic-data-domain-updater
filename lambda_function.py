from ecocounterdomainupdater.fetcher import update_domain_list


def lambda_handler(event, context):
    update_domain_list()
