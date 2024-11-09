from ecocounterdomainupdater import ecocounterapi, githubapi


def find_domains(max_domain_id):
    domains = []
    for domain_id in range(1, max_domain_id):
        print("Trying domain id %d" % domain_id)
        sites = ecocounterapi.fetch_sites_in_domain(domain_id)
        if len(sites) > 0:
            domains.append({
                "id": domain_id,
                "name": sites[0]["nomOrganisme"],
            })
    return domains


def update_domain_list():
    domains = find_domains(10_001)
    old_domains = githubapi.get_gist()
    if domains != old_domains:
       githubapi.update_gist(domains)


if __name__ == "__main__":
    update_domain_list()
