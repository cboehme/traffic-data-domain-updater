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

FROM python:3.13-slim
LABEL authors="christoph"

WORKDIR /usr/src/app

COPY dist/traffic-data-domain-updater-1.0.0.tar.gz dist/

RUN pip install --root-user-action=ignore --no-cache-dir dist/traffic-data-domain-updater-1.0.0.tar.gz

COPY fargate.py ./

CMD ["python", "./fargate.py"]
