#!/usr/bin/python3
import json
import requests
import socket
import sys

#source link db: https://www.networkinghowtos.com/howto/common-database-server-port-numbers/
#source link ad: https://docs.microsoft.com/nl-NL/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements#4
#source link ad:https://isc.sans.edu/diary/Cyber+Security+Awareness+Month+-+Day+27+-+Active+Directory+Ports/7468


key="4VdRQ9pNJvTsJNw4dF2VMQz3VczqbV0a"
results=[]
def main(type:str,domain:str):
    """_summary_

    Args:
        type (str): type of request
        domain (str): Domain to check
    """
    try:
        if type=="domain":
            host_name = domain
            host_ip = socket.gethostbyname(host_name)
        elif type=="ip":
            host_ip = domain
        response = requests.get("https://api.shodan.io/shodan/host/"+host_ip+"?key="+key)
        try:
            responsedr=json.loads(response.text)
            keyval="tags"
            responselist=responsedr[keyval]
            dbfound=False

            for i in responselist:
                if i == "database":
                    dbfound=True
                    results.append(
                        {"name":"database",
                        "score":0,
                        "message":"database found",
                        "description":"Shodan found a database"})
            if not dbfound:
                results.append(
                        {"name":"database",
                        "score":10,
                        "message":"database is not found",
                        "description":"Shodan didn't found a database."})
        except:
            results.append({})

        try:

            datums=[entry['timestamp'] for entry in responsedr['data']]
            datum=datums[0]
            yy=datum[0:4]
            mm=datum[5:7]
            dd=datum[8:10]
            hh=datum[11:13]
            min=datum[14:16]
            sec=datum[17:19]
            datum=yy+"-"+mm+"-"+dd+" "+hh+":"+min+":"+sec

            portlist=[entry['port'] for entry in responsedr['data']]
            dbports=[5432,1433,1434,3306,3050,5432,3351,1583]
            adports=[9389,389,636,88,445]
            redis=[6379,26379]
            badports=dbports+adports+redis
            foundbadports=[]
            for port in portlist:
                for dport in badports:
                    if port==dport:
                        foundbadports.append(port)
            countp=len(foundbadports)
            score=10-countp*2
            if score<0:
                score=0
            results.append(
                 {"name":"badports",
                 "score":score,
                 "message":"bad ports",
                 "description":"Shodan has found "+str(countp)+ " bad ports. Datum:"+str(datum)})

        except:
            results.append({})

        try:
            vulns=responsedr['vulns']
            countcve=len(vulns)
            score=10-countcve*2

            if score<0:
                score=0
            results.append(
                {"name":"Vulnabilities",
                "score":score,
                "message":"CVEs",
                "description":"Shodan has found "+str(countcve)+ " CVEs."})
        except:
            results.append(
                {"name":"Vulnabilities",
                "score":10,
                "message":"CVEs",
                "description":"Shodan did not found any CVEs."})

    except:
        results.append({})

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])
