# [Obscurity](https://www.hackthebox.eu/home/machines/profile/219)
## IP : 10.10.10.168


> `nmap 10.10.10.168`
* 22/tcp   open   ssh
* 80/tcp   closed http
* 8080/tcp open   http-proxy
* 9000/tcp closed cslistener

Website : http://10.10.10.168:8080/

**Step 1** : 
Message from the [home page](http://10.10.10.168:8080/).
> Message to server devs: the current source code for the web server is in __SuperSecureServer.py__ in the secret development directory`

After some tests the server is fuzzable from the root. Any file or folder can be returned by the browser.

enumeration potential : http://obscurity:8080/FUZZ/SuperSecureServer.py

**Step 2** : Understanding the custom made server

see (*hints/SuperSecureServer.py*)
 > `nmap 10.10.10.168`