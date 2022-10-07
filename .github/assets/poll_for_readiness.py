import time

from urllib import request
import sys

NUM_ATTEMPTS = 20
WAIT_TIME = 15

def poll():
    status_api = sys.argv[1]
    for i in range(NUM_ATTEMPTS):
        print(f"Waiting for API to start (attempt {i+1} of {NUM_ATTEMPTS})")
        try:
            if request.urlopen(status_api).code == 200:
                print(f"{status_api} online after {(i * WAIT_TIME)} seconds")
                return
        except:
            time.sleep(WAIT_TIME)

    print(f"Failed to start {status_api} after {NUM_ATTEMPTS * WAIT_TIME} seconds")
    exit(1)

poll()