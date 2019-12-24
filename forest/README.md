# Forest

## Step 0 - Sniffing ports...

![port_scan_part_1](images/forest_port_scan_1.png)

![port_scan_part_2](images/forest_port_scan_2.png)


![port_scan_part_3](images/forest_port_scan_3.png)

> The port 5985 is bind to a `winrm` service which allow us to connect the machine through a Powershell.

> The port 88 is bind to a Kerberos service (which is an authnetification administrator... [more details](https://blog.varonis.fr/explication-de-lauthentification-kerberos/) and [here](https://docs.microsoft.com/fr-fr/windows-server/security/kerberos/kerberos-authentication-overview) or [here](https://docs.oracle.com/cd/E19120-01/open.solaris/819-3321/intro-25/index.html))

> The ports 135 and 593 are [RPC service](https://fr.wikipedia.org/wiki/Remote_procedure_call)

> The ports 135 and 139 are relared to [NetBios service](https://fr.wikipedia.org/wiki/NetBIOS) which is a network architecture over TCP/IP

> The ports 389 and 3268 are [LDAP services](https://fr.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol)

> The service `kpassword5` (port 464) seems to be a part of [Kerberos to allow user change setting password](https://security.stackexchange.com/questions/205492/what-is-this-service).

> `ncacn_http` seems to be a [RPC http proxy](https://docs.microsoft.com/en-us/windows/win32/midl/ncacn-http).

> The ports 3269 and 636 are unde [tcpd service](http://www.rootr.net/man/man/tcpd/8)