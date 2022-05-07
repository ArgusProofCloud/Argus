import webtech
import nvdlib
import sys


wt = webtech.WebTech(options={'json': True})

used_tech = wt.start_from_url('https://' + sys.argv[1], timeout=1)
used_tech = used_tech.get('tech')

res = []
for i in used_tech:
    if i.get('version') is not None:
        res.append(i.get('name') + " " + i.get('version'))

res = '\n'.join(res)

for i in res.split('\n'):
    cve = []
    r = nvdlib.searchCVE(keyword = i)
    for eachCVE in r:
        cve.append("Id: " + eachCVE.id)
        cve.append("Score: " + str(eachCVE.v3score))
        cve.append("Severity: " +eachCVE.v3severity)

if len(r) > 0:
    print(f'{{"name": "cve", "score": 0, "message": {cve} "description": "cve"}}')
else:
    print(f'{{"name": "cve", "score": 10, "message": "No CVE found", "description": "cve"}}')