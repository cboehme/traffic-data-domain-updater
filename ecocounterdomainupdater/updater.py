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


def update_domain_list(gist_id, max_domain_id):
    domains = find_domains(max_domain_id)
    old_domains = githubapi.get_gist(gist_id)
    if domains != old_domains:
       githubapi.update_gist(gist_id, domains)


if __name__ == "__main__":
    githubapi.authorize("TOKEN")
    update_domain_list("33d03f2de5add333c0217106cca35478", 10_001)
