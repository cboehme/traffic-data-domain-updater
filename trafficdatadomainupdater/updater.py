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

from trafficdatadomainupdater import ecocounterapi, githubapi


def find_domains(max_domain_id):
    domains = []
    for domain_id in range(1, max_domain_id + 1):
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
