rm -f eco-counter-domain-updater.zip

(
  cd venv/lib/python3.12/site-packages &&
  zip -r ../../../../eco-counter-domain-updater.zip . -x "*/__pycache__/*"
)

(
  cd venv/lib64/python3.12/site-packages &&
  zip -r ../../../../eco-counter-domain-updater.zip . -x "*/__pycache__/*"
)

zip -r eco-counter-domain-updater.zip ecocounterdomainupdater -x "*/__pycache__/*"
