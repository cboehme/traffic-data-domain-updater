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

rm -f traffic-data-domain-updater.zip

(
  cd venv/lib/python3.13/site-packages &&
  zip -r ../../../../traffic-data-domain-updater.zip . -x "*/__pycache__/*"
)

(
  cd venv/lib64/python3.13/site-packages &&
  zip -r ../../../../traffic-data-domain-updater.zip . -x "*/__pycache__/*"
)

zip -r traffic-data-domain-updater.zip trafficdatadomainupdater -x "*/__pycache__/*"
zip traffic-data-domain-updater.zip lambda_function.py
