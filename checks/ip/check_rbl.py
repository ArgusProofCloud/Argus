#! /usr/bin/env python3

# Import Modules
import sys
import os
import getopt
import socket
import string
if sys.version_info[0] == 3:
    import queue as Queue
else:
    import Queue
import threading
import ipaddress
import timeit

# Python version check
rv = (2, 6)
if rv >= sys.version_info:
    print('{"name": "Blacklist", "message": "ERROR: Requires Python 2.6 or greater"}')
    sys.exit(3)

# List of DNS blacklists
serverlist = []
with open("blocklists.txt") as file:
    serverlist = list(map(str.rstrip, file.readlines()))

####

queue = Queue.Queue()
debug = False
global on_blacklist
on_blacklist = []


class ThreadRBL(threading.Thread):
    """A Blocklist check thread
    """
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Grab hosts from queue
            hostname, root_name = self.queue.get()
            check_host = "%s.%s" % (hostname, root_name)
            start_time = timeit.default_timer()
            try:
                check_addr = socket.gethostbyname(check_host)
            except socket.error:
                check_addr = None
            if check_addr is not None and "127.0.0." in check_addr:
                on_blacklist.append(root_name)

            elapsed = timeit.default_timer() - start_time

            # Signal queue that job is done
            self.queue.task_done()

def main(argv, environ):
    """Main function

    Args:
        argv (list): List of arguments from the command line.
        environ (os.environ): The current environment variables.
    """
    host = argv[1]

    if host:
        try:
            addr = socket.gethostbyname(host)
        except:
            print('{"name": "Blacklist", "message": "ERROR: Host %s not found - maybe try a FQDN?"}'% host)
            sys.exit()

    if sys.version_info[0] >= 3:
        ip = ipaddress.ip_address(addr)
    else:
        ip = ipaddress.ip_address(unicode(addr))
    if ip.version == 6:
        addr_exploded = ip.exploded
        check_name = '.'.join([c for c in addr_exploded if c != ':'])[::-1]
    else:
        addr_parts = addr.split('.')
        addr_parts.reverse()
        check_name = '.'.join(addr_parts)
    # Make host and addr the same thing to simplify output functions below
    host = addr

# ##### Start thread stuff

    # Spawn a pool of threads then pass them the queue
    for i in range(10):
        t = ThreadRBL(queue)
        t.setDaemon(True)
        t.start()

    # Populate the queue
    for blhost in serverlist:
        queue.put((check_name, blhost))

    # Wait for everything in the queue to be processed
    queue.join()

# ##### End thread stuff

# Create output
    if on_blacklist:
        output = '%s on %s blacklist(s): %s' % (
            host, len(on_blacklist), ', '.join(on_blacklist))

        # Status is CRITICAL
        if len(on_blacklist) >= 2:
            print('{"name": "Blacklist", "score": 0, "message": "Domain %s found on more than 2 blacklists."}' % output)

        # Status is WARNING
        elif len(on_blacklist) == 1:
            print('{"name": "Blacklist", "score": 5, "message": "Domain %s found on 1 blacklist."}' % output)

    else:
        # Status is OK and host is not blacklisted
        print('{"name": "Blacklist", "score": 10, "message": "Domain %s not found on known blacklists."}'% host)

if __name__ == "__main__":
    main(sys.argv, os.environ)
