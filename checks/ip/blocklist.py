import sys
import json
import queue
import random
import threading
import dns.resolver

jobQueue = queue.Queue()
blocked = []

def main(domain: str):
    results = []
    ips = enqueue(domain)

    for i in range(100):
        threading.Thread(target=checkThread, daemon=True).start()

    jobQueue.join()

    if len(blocked) > 0:
        blockedIps = {}
        for ip, blocklist in blocked:

            ips.remove(ip)

            if ip not in blockedIps:
                blockedIps[ip] = []
                blockedIps[ip].append(blocklist)
            else:
                blockedIps[ip].append(blocklist)

        for ip in blockedIps:
            results.append({
                "name": "Blocklists",
                "score": 0,
                "message": f"{ip} is found on a blocklist.",
                "value": blockedIps[ip]
            })


    for ip in ips:
        results.append({
            "name": "Blocklists",
            "score": 10,
            "message": f"{ip} is not found on a blocklist.",
            "value": ip
        })

    print(json.dumps(results))

def readBlocklists() -> list:
    with open("./blocklists.txt") as file:
        blocklists =  list(map(str.strip, file.readlines()))
        random.shuffle(blocklists)
        return blocklists

def checkThread():
    global jobQueue
    while not jobQueue.empty():
        ip, blocklist = jobQueue.get()

        try:
            result = dns.resolver.resolve("%s.%s" % (ip, blocklist))
            for ipVal in result:
                if "127.0.0." in ipVal.to_text():
                    blocked.append((ip, blocklist))
                    return
        except:
            pass
        finally:
            jobQueue.task_done()

def enqueue(domain: str):
    ips = []
    blocklists = readBlocklists()
    try:
        result = dns.resolver.resolve(domain)
        for ipVal in result:
            ips.append(ipVal.to_text())
            for blocklist in blocklists:
                jobQueue.put((ipVal.to_text(), blocklist))
        return ips
    except:
        print("{}")
        sys.exit(0)

if __name__ == "__main__":
    main(sys.argv[1])
