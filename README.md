## Book of OpenStack: Barachiel  ##

A simple script for mass virtual machine management in the cloud based on [OpenStack](https://www.openstack.org/) software.
It gives you the possibility of issuing the same console commands on multiple servers performing the same role. For example: www, daemon, database etc.
The role must be included in the prefix name with an ordinal number. Authentication is possible through a login and password or SSH key.

```
(openstack)darkstar:agresor$ barachiel classic -h
usage: barachiel classic [-h] [-F FILE] [-p PROJECT] -i ID [-r min max]
                         [-c COMMAND] [-u local remote] [-s] [-f] [-P]

optional arguments:
  -h, --help            show this help message and exit
  -F FILE, --file FILE  Name of .cloudrc file.
  -p PROJECT, --project PROJECT
                        OpenStack project ID.
  -i ID, --id ID        VM instance name.
  -r min max, --range min max
                        Minimal & maximal instance range to use.
  -c COMMAND, --command COMMAND
                        Command to run (default: uptime).
  -u local remote, --upload local remote
                        Upload one or more files/dirs to a remote host.
  -s, --sudo            Run command with sudo.
  -f, --failok          Its OK if command will fail.
  -P, --parallel        Run commands in parallel mode.

(openstack)darkstar:agresor$ barachiel classic -i apache-www -c 'uptime'
Enter username: agresor
Enter password:

Detected machines:

VM name: apache-www1 :: status: ACTIVE
VM name: apache-www2 :: status: ACTIVE

Continue with these machines? [yes/no]: yes
[10.10.1.1] Executing task 'command'
Hostname: apache-www1.web-servers.first-zone-01.lan
[10.10.1.1] run: date
[10.10.1.1] out: Thu Mar 10 21:11:02 CET 2016
[10.10.1.1] out:

||| Done.

[10.10.1.2] Executing task 'command'
Hostname: apache-www2.web-servers.first-zone-02.lan
[10.10.1.2] run: date
[10.10.1.2] out: Thu Mar 10 21:11:04 CET 2016
[10.10.1.2] out:

||| Done.
```
