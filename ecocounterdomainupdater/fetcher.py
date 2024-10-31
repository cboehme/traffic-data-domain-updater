import json

from ecocounterdomainupdater import apiclient


def find_domains(max_domain_id):
    domains = []
    for domain_id in range(1, max_domain_id):
        print("Trying domain id %d" % domain_id)
        sites = apiclient.fetch_sites_in_domain(domain_id)
        if len(sites) > 0:
            domains.append({
                "id": domain_id,
                "name": sites[0]["nomOrganisme"],
            })
    return domains


def main():
    domains = find_domains(10_001)
    old_domains = apiclient.get_gist()
    if domains != old_domains:
       apiclient.update_gist(domains)


if __name__ == "__main__":
    main()
