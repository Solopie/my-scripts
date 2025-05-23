# My Scripts

Contains a variety of scripts that I make for exploitation or enumeration when hacking.

TODO: Automate the population of this README file. At the moment it is manual.

<table>
  <thead>
    <tr>
      <th>Script</th>
      <th style="width: 10%">Tags</th>
      <th style="width: 70%;">Description</th>
      <th style="width: 10%">Context</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="python/command_injection_via_ssrf.py">command_injection_via_ssrf.py</a></td>
      <td>requests, threading, beautifulsoup</td>
      <td>
        External web application vulnerable to SSRF. Can reach internal application on port 80 via SSRF and exploit a command injection with GET requests.
      </td>
      <td><a href="https://app.hackthebox.com/machines/493">HTB UpDown</a></td>
    </tr>
    <tr>
      <td><a href="python/timebased_upload_filename.py">timebased_upload_filename.py</a></td>
      <td>requests, threading, hashlib, parsedate_to_datetime</td>
      <td>
        PHP web application with upload function that uploads files even if the file extension is not allowed. Filename of uploaded file is replaced with MD5 hash generated from <code>filename+epoch time</code>. File upload requires CAPTCHA so must be done manually.
      </td>
      <td><a href="https://app.hackthebox.com/machines/Help">HTB Help</a></td>
    </tr>
    <tr>
      <td><a href="python/parse_pcap_list_ips_in_arp.py">parse_pcap_list_ips_in_arp.py</a></td>
      <td>pcap,scapy,ipaddress</td>
      <td>
        Ran wireshark on a host in a Active Directory environment and passively listened to network traffic. Listening for ARP broadcasts is a method of passively identifying active host IPs on the network.
      </td>
      <td>HTB Academy Enumeration Exercise</td>
    </tr>
    <tr>
      <td><a href="python/parse_pcap_list_hostnames_nbns.py">parse_pcap_list_hostnames_nbns.py</a></td>
      <td>pcap,scapy</td>
      <td>
        Ran wireshark on a host in a Active Directory environment and passively listened to network traffic. Listening for NBNS (NetBIOS Name Service) broadcasts is a method of passively identifying active hostnames on the network.
      </td>
      <td>HTB Academy Enumeration Exercise</td>
    </tr>
    <tr>
      <td><a href="python/ssrf_internal_port_fuzzing.py">ssrf_internal_port_fuzzing.py</a></td>
      <td>requests, multiprocessing, tqdm</td>
      <td>
        Web application vulnerable to SSRF. Fuzzing for internally open ports.
      </td>
      <td><a href="https://app.hackthebox.com/machines/493">HTB UpDown</a></td>
    </tr>
  </tbody>
</table>

