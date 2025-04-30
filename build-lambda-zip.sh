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
