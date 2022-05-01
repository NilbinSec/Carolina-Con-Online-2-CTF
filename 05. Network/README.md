# Network
A fun exercise in privesc.

# rootMe: User
**Point Value:** 75

**Prompt**
_We found out that a hacker planted a backdoor in one of our systems, can you try to get root access?_

_Hacker created an account as a backdoor into the system
We have info that the username the hacker used was 'hacker', we believe they were using a weak password as well There are 2 flags on this machine, one user flag and one root flag located at their respective home directories_


Flag: **flag{sudo-is-dangerous}**

**Methodology**
Running nmap -A on the host showed a different version of OpenSSH running on port 2222. That seemed like the backdoor mentioned in the description. The hint said that the username was "hacker" and they used an insecure password, so an initial guess of "hacker" worked and we could get in, after exploring a bit there was a text file in the home directory of another user (49sd) that had the flag in it.

# rootMe: root
**Point Value:** 91

**Prompt**
_We found out that a hacker planted a backdoor in one of our systems, can you try to get root access?_

_Hacker created an account as a backdoor into the system
We have info that the username the hacker used was 'hacker', we believe they were using a weak password as well There are 2 flags on this machine, one user flag and one root flag located at their respective home directories_


Flag: **flag{git-is-dangerous}**

**Methodology**
network - rootMe: root is a series of privilege escalations. Starting with the hacker:hacker login we got from rootMe: user, running sudo -l lists the commands that user is allowed to run. It outputs: 

_User hacker may run the following commands on f0c5ac70c94c:
    (49sd) NOPASSWD: /bin/less_

So we can run /bin/less as user 49sd. Running sudo -u 49sd less <any file> brings us into less. Less lets you run commands with !, so typing !/bin/bash drops us into a shell as user 49sd. Running sudo -l again shows us:
  
_User 49sd may run the following commands on f0c5ac70c94c:
    (root) NOPASSWD: /root/addto49sdrepo.sh_
  
This is less helpful, but the contents of that file was posted as a hint in the notifications tab. It unzips anything in the ~/repos/ folder (dangerously overwriting existing files) into a new git repository and makes a commit. I zipped up a post commit hook at .git/hooks/post-commit that ran ls /root > /tmp/out, and from the new output I saw there was a /root/root.txt file. So I changed the git post-commit hook to cat that file, which contained the flag.
The post-hook was a file that looked like this:
  
#!/bin/bash
cat /root/root.txt > /tmp/out
  
