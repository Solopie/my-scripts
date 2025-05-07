# Exploit Scripts

TODO: Automate the population of this README file. At the moment it is manual.

| Script | Tags | Description | Context |
| --- | --- | --- | --- |
| [python/command_injection_via_ssrf.py](command_injection_via_ssrf.py) | requests,threading,beautifulsoup | External web application vulnerable to SSRF. Can reach internal application on port 80 via SSRF and exploit a command injection with GET requests. | [HTB UpDown](https://app.hackthebox.com/machines/493) |
| [python/timebased_upload_filename.py](timebased_upload_filename.py) | requests,threading,hashlib,parsedate_to_datetime | PHP web application with upload function that uploads files even if the file extension is not allowed. Filename of uploaded file is replaced with MD5 hash generated from `filename+epoch time`. File upload requires CAPTCHA so must be done manually. | [HTB Help](https://app.hackthebox.com/machines/Help) |


