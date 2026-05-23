# Module 01 - Introduction to Git and GitHub
# Module 02 - Using Git Locally
# Module 03 - Working with Remotes



## Review: Basic interaction with GitHub
This reading contains the code used in the instructional videos from Basic interaction with GitHub. 

### Introduction
This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written, allow you to practice running it, and can be used as a reference to refer back to. 

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

#### GIT CLONE
```bash
git clone https://github.com/redquinoa/health-checks.git
```

Code output: 
```bash
Cloning into 'health-checks'...
Username for 'https://github.com': redquinoa
Password for 'https://redquinoa@github.com': 
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
```

#### GIT HEALTH-CHECKS / LS
```bash
cd health-checks/
ls -l
```

Code output: 
```bash
total 4
-rw-rw-r-- 1 user user 62 Jan  6 14:06 README.md
```

#### GIT COMMIT
```bash
atom README.md
# health-checks
Scripts that check the health of my computers
This repo will be populated with lots of fancy checks. 
```

```bash
git commit -a -m "Add one more line to README.md"
```

Code output:
```bash
[master 807cb50] Add one more line to README.md
1 file changed, 2 insertions(+)
```

#### GIT PUSH
```bash
git push
```

Code output: 
```bash
Username for 'https://github.com': redquinoa
Password for 'https://redquinoa@github.com': 
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 347 bytes | 347.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/redquinoa/health-checks.git
   3d9f86c..807cb50  master -> master
```

#### GIT CONFIG / PULL
```bash
git config --global credential.helper cache
```
```bash
git pull
```

Code output: 
```bash
Username for 'https://github.com': redquinoa
Password for 'https://redquinoa@github.com': 
Already up to date.
```

```bash
git pull
```

Code output: 
```bash
Already up to date.
```





## Study guide: Basic Interaction with GitHub
There are various remote repository hosting sites:
- [GitHub](http://github.com/)
- [BitBucket](https://bitbucket.org/product)
- [Gitlab](https://gitlab.com/)


Follow the workflow at https://github.com/join to set up a free account, username, and password. After that, [these steps](https://help.github.com/articles/create-a-repo/) will help you create a brand new repository on GitHub.

Some useful commands for getting started:

| Command | Explanation & Link |
|---|---|
| git clone<br>URL | [Git clone is used to clone a remote repository into a local workspace](https://git-scm.com/docs/git-clone) ↗ |
| git push | [Git push is used to push commits from your local repo to a remote repo](https://git-scm.com/docs/git-push) ↗ |
| git pull | [Git pull is used to fetch the newest updates from a remote repository](https://git-scm.com/docs/git-pull) ↗ |

This can be useful for keeping your local workspace up to date.
- https://help.github.com/en/articles/caching-your-github-password-in-git
- https://help.github.com/en/articles/generating-an-ssh-key





## Review: Working with remotes
This reading contains the code used in the instructional videos from Working with remotes

### Introduction
This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written and can be used as a reference as you work through the course.

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.


### GIT REMOTE -V
```bash
git remote -v
```

#### Code output: 
```bash
origin  https://github.com/redquinoa/health-checks.git (fetch)
origin  https://github.com/redquinoa/health-checks.git (push)
```


### GIT REMOVE SHOW ORIGIN
```bash
git remote show origin
```

#### Code output: 
```bash
Username for 'https://github.com': redquinoa
Password for 'https://redquinoa@github.com': 
* remote origin
  Fetch URL: https://github.com/redquinoa/health-checks.git
  Push  URL: https://github.com/redquinoa/health-checks.git
  HEAD branch: master
  Remote branch:
    master tracked
  Local branch configured for 'git pull':
    master merges with remote master
  Local ref configured for 'git push':
    master pushes to master (up to date)
```


### GIT BRANCH -R
```bash
git branch -r
```

#### Code output:
```bash
  origin/HEAD -> origin/master
  origin/master
```

### GIT STATUS
```bash
git status
```

#### Code output: 
```bash
On branch master
Your branch is up to date with 'origin/master'.
nothing to commit, working tree clean
```





## Review: Fetching new changes
This reading contains the code used in the instructional videos from Fetching New Changes

### Introduction
This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written and can be used as a reference as you work through the course. You can follow along in the reading as the instructor discusses the code or review the code after watching the video.


### GIT REMOTE SHOW ORIGIN

```bash
git remote show origin
```
#### Code output: 
```bash
* remote origin
  Fetch URL: https://github.com/redquinoa/health-checks.git
  Push  URL: https://github.com/redquinoa/health-checks.git
  HEAD branch: master
  Remote branch:
    master tracked
  Local branch configured for 'git pull':
    master merges with remote master
  Local ref configured for 'git push':
    master pushes to master (local out of date)
```


### GIT FETCH
```bash
git fetch
```
#### Code output:
```bash
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 4 (delta 0), pack-reused 0
Unpacking objects: 100% (4/4), done.
From https://github.com/redquinoa/health-checks
   807cb50..b62dc2e  master     -> origin/master
```


### GIT LOG
```bash
git log origin/master
```
#### Code output:
```bash
commit b62dc2eacfa820cd9a762adab9213305d1c8d344 (origin/master, origin/HEAD)
Author: Blue Kale <bluekale@example.com>
Date:   Mon Jan 6 14:32:45 2020 -0800
    Add initial files for the checks
commit 807cb5037ccac5512ba583e782c35f4e114f8599 (HEAD -> master)
Author: My name <me@example.com>
Date:   Mon Jan 6 14:09:41 2020 -800
    Add one more line to README.md
commit 3d9f86c50b8651d41adabdaebd04530f4694efb5
Author: Red Quinoa <55592533+redquinoa@users.noreply.github.com>
Date:   Sat Sep 21 14:04:15 2019 -0700
    Initial commit
```


### GIT STATUS
```bash
git status
```
#### Code output: 
```bash
On branch master
Your branch is behind 'origin/master' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)
nothing to commit, working tree clean
```


### GIT MERGE
```bash
git merge origin/master
```
#### Code output: 
```bash
Updating 807cb50..b62dc2e
Fast-forward
 all_checks.py | 18 ++++++++++++++++++
 disk_usage.py | 24 ++++++++++++++++++++++++
 2 files changed, 42 insertions(+)
 create mode 100755 all_checks.py
 create mode 100644 disk_usage.py
```


### GIT LOG
```bash
git log
```
#### Code output:
```bash
commit 1e0a1dfccf01183bfca7e30fb25f115889f95022 (HEAD -> master, origin/master, origin/HEAD)
commit b62dc2eacfa820cd9a762adab9213305d1c8d344 (HEAD -> master, origin/master, origin/HEAD)
Author: Blue Kale <bluekale@example.com>
Date:   Mon Jan 6 14:32:45 2020 -0800
    Add initial files for the checks
commit 807cb5037ccac5512ba583e782c35f4e114f8599 (HEAD -> master)
Author: My name <me@example.com>
Date:   Mon Jan 6 14:09:41 2020 -800
    Add one more line to README.md
commit 3d9f86c50b8651d41adabdaebd04530f4694efb5
Author: Red Quinoa <55592533+redquinoa@users.noreply.github.com>
Date:   Sat Sep 21 14:04:15 2019 -0700
```





## Review: Updating the local repository
This reading contains the code used in the instructional videos from Updating the Local Repository

### Introduction
This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written and can be used as a reference as you work through the course.

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.

### GIT PULL
```bash
git pull
```
#### Code output: 
```bash
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (5/5), done.
Unpacking objects: 100% (6/6), done.
remote: Total 6 (delta 1), reused 6 (delta 1), pack-reused 0
From https://github.com/redquinoa/health-checks
   807cb50..b62dc2e  master       -> origin/master
 * [new branch]      experimental -> origin/experimental
Updating 807cb50..b62dc2e
Fast-forward
 all_checks.py | 15 +++++++++++++++
 1 file changed, 15 insertions(+)
```

### GIT LOG
```bash
git -log -p -1
```
#### Code output: 
```bash
commit 922d65950b5325109525a24b71d8df8a46412d04 (HEAD -> master, origin/master, origin/HEAD)
Author: Blue Kale <bluekale@example.com>
Date:   Mon Jan 6 14:42:44 2020 -0800
    Add disk full check to all_checks.py
diff --git a/all_checks.py b/all_checks.py
index fdc4476..e46cdae 100755
--- a/all_checks.py
+++ b/all_checks.py
@@ -1,16 +1,31 @@
 #!/usr/bin/env python3
 import os
+import shutil
 import sys
(...)
def(check_reboot): 
	""" Returns True if the computer has a pending reboot."""
	Return os.path.exists(“/run/reboot-required”)
+def check_disk_full(disk, mmin_absolute, min_percent):
+	"""Returns True if there isn’t enough disk space, False otherwise."""
+	du = shutil.disk_usage(disk)
+	# Calculate the percentage of free space
+	percent_free = 100 * du.free / du.total
+	# Calculate how many free gigabytes
```

### GIT REMOTE SHOW ORIGIN
```bash
git remote show origin
```
#### Code output: 
```bash
* remote origin
  Fetch URL: https://github.com/redquinoa/health-checks.git
  Push  URL: https://github.com/redquinoa/health-checks.git
  HEAD branch: master
  Remote branches:
    experimental tracked
    master       tracked
  Local branch configured for 'git pull':
    master merges with remote master
  Local ref configured for 'git push':
    master pushes to master (up to date)
```

### GIT CHECKOUT EXPERIMENTAL
```bash
git checkout experimental 
```
#### Code output: 
```bash
Branch 'experimental' set up to track remote branch 'experimental' from 'origin'.
Switched to a new branch 'experimental'
```





## Study guide: Git Remotes
You’ve learned about what a remote is, working with remotes, fetching new changes, and updating the local repository. Use this study guide as an easy reference of Git commands for working with remotes. This study guide gives a brief explanation of these useful commands along with a link to the Git documentation for each command. Keeping study guides like this one easily accessible can help you code more efficiently.


| Command | Explanation & Links |
|---|---|
| git remote | [$ git remote](https://git-scm.com/docs/git-remote) ↗ allows you to manage the set of repositories or “remotes” whose branches you track. |
| git remote -v | [$ git remote -v](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt--v) ↗ is similar to $ git remote, but adding the -v shows more information such as the remote URL. |
| git remote show \<name> | [$ git remote show \<name>](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emshowem) ↗ shows some information about a single remote repo. |
| git remote update | [$ git remote update](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emupdateem) ↗ fetches updates for remotes or remote groups. |
| git fetch | [$ git fetch](https://git-scm.com/docs/git-fetch) ↗ can download objects and refs from a single repo, a single URL, or from several repositories at once. |
| git branch -r | [$ git branch -r](https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--r) ↗ lists remote branches and can be combined with other branch arguments to manage remote branches. |

Keep this table handy while you are getting comfortable using Git remotes. Now, it’s time to put your newfound knowledge of Git remotes to use!





## What is secure shell?
Secure Shell (SSH) is a robust protocol for connecting to servers remotely. In the realm of remote server access, security is going to be more and more important to keep your information safe. Secure Shell is primarily used for logging in to Linux servers, Unix servers, and certain networking equipment such as routers. 

### Alternatives to SSH
SSH provides a shield against prying eyes, but how does it compare to its alternatives?  

Telnet is one popular alternative. Telnet exposes your typed commands, including passwords, to anyone on the network equipped with the right tools. 

Although Transport Layer Security (TLS) encrypts data within web browsers, SSH secures data in interactive terminal sessions or file transfers. This encryption ensures that sensitive information remains confidential during communication. 

Another alternative is virtual private networks (VPNs). VPNs also offer encryption but grant access to entire networks after connection. SSH adheres to the principle of least privilege, restricting users to specific hosts, enhancing security. 

Another option might be remote-control software like VNC or GoToMyPC. They focus on graphical user interfaces and desktop experiences, which may not align with most Linux servers that operate sans desktop environments.

### Operation
SSH operates through two key components: the SSH server and the SSH client. The SSH server, residing on the target server, establishes secure network connections, undergoes mutual authentication, and initiates encrypted login sessions or file transfers. 

Conversely, the SSH client establishes a connection to the SSH server, ensuring a secure interaction. The client makes requests, such as “log me in” or “copy this file.”

### SSH keys
In the SSH protocol, an access credential is known as an SSH key. It serves a similar purpose as usernames and passwords, although system administrators and power users typically use the keys to automate procedures and achieve single sign-on.

Displaying the fingerprint of an SSH key is a useful way to verify that you're using the correct key and that the remote server's key hasn't been tampered with. To display the fingerprint of an SSH key, you can use the ssh-keygen command-line tool. 

### Key takeaways
**SSH prioritizes security in remote server access:** Secure Shell (SSH) is a robust and trusted protocol for securely connecting to servers remotely. It finds widespread use in accessing Linux servers, Unix servers, and specific networking equipment, serving as a shield against unauthorized access and data breaches. 

**Comparing SSH with alternatives:** When you compare SSH to alternatives like Telnet, its security superiority becomes clear. Telnet exposes commands, including passwords, to potential threats, whereas SSH's encryption guarantees confidentiality during interactive terminal sessions and file transfers. Unlike virtual private networks (VPNs) that offer network-wide access, SSH adheres to the principle of least privilege, ensuring users are restricted for enhanced security.

**SSH's operational mechanics and key role:** SSH functions through two core components: the SSH server and the SSH client. The SSH server establishes secure connections, authenticates parties involved, and initiates encrypted sessions. Conversely, the SSH client establishes secure interactions with the server and enables actions like secure login or file copying.

Just like a password, the security of your SSH key is critical. Never share your SSH private key with anyone or put SSH keys into your application code. With someone having access to your information, they can gain unauthorized access by logging in and pretending to be you.





## The SSH protocol
When discussing computer networks, the word “shell” refers to a program that provides an interface for accessing another operating system. With all the effort you put into keeping your own machine secure, you certainly want security when it’s connected to another machine. The Secure Shell network protocol, usually shorthanded to “SSH,” allows secure access to a computer over an unsecured network. 

### What is a protocol? 
A protocol is a set of rules for how two things should communicate with each other. You may have heard the phrase “military protocol,” which refers to the strict guidelines that govern communications between members of the armed forces in all situations. 

In the case of computer protocols, these are usually published as open standards so that any given protocol can be implemented in various products. Having these protocols readily available to everyone means that any machine or network that implements a given protocol should be able to communicate seamlessly with anything else that supports the same protocol. 

For a deeper dive into Secure Shell, see [SSH protocol](https://www.ssh.com/academy/ssh/protocol). 


### The SSH protocol
So how does SSH secure the network? It works on the principle of public-key encryption. The client and the server each generate a strong encryption key for any data that is passed between them. Then, that key gets split in half, with the client retaining one portion and the server keeping the other. It’s a complex version of a simple idea, really; it’s not hard to imagine two people making up an encryption code and then tearing it in half for extra secrecy. 

In SSH, the keys are split between a public key, the public half of the server’s encryption key, and the private key, which is stored only on the server. This way, a user’s machine can encrypt a message using the public key, but only the connected server can decode it because only the server’s private key will successfully decrypt the message. This way, if someone did intercept the network traffic, they still couldn’t read it because they don’t have the server’s private key. Using SSH, your keystrokes and the server’s responses are completely secure. 

For more on these keys, see [Public – private key pairs & how they work](https://www.preveil.com/blog/public-and-private-key/#:~:text=In%20public%20key%20cryptography%2C%20every,using%20their%20matching%20private%20key) and [A Deep Dive on End-to-End Encryption](https://ssd.eff.org/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work). 


### Using the SSH protocol
The SSH protocol is commonly used for logging in to servers remotely. While it is primarily used for logging in to Linux and Unix servers, it is also used to encrypt file transfers and to log in to some network equipment, like routers. 

Of course, your private key should never be transmitted to anyone else or shared anywhere. Most SSH clients will not connect if your private key is not protected from other users. Because your private key is unique to you, it can serve as both authentication and encryption, so the server doesn’t need to ask you for a password.

Besides providing a secure login shell on a remote server, SSH can be used for a number of other functions, including:

- Transferring files between client and server with SCP (Secure Copy Protocol) or SFTP (Secure File Transfer Protocol); for more about these types of file transfers, see the 
[Difference between SFTP and SCP](https://www.tutorialspoint.com/difference-between-sftp-and-scp).

- Forwarding network ports from server to client, or “tunneling”; for more on port forwarding, see [How to Use SSH Port Forwarding](https://phoenixnap.com/kb/ssh-port-forwarding).

- Relaying your login to yet another server behind a firewall, sometimes referred to as a “jump box” or “bastion host”; for more on this relaying method, see [How to Set Up an SSH Jump Server](https://goteleport.com/blog/ssh-jump-server/).

- Running graphical user interface (GUI) applications on a server but displaying them on a local client; for more on this, see [Use X forwarding on a personal computer](https://kb.iu.edu/d/bdnt).  





## Configuring SSH
Computer ports are software-based points where a network connection begins and ends. When using Secure Shell (SSH), the client connects to the server on port 22. After the connection is made, the server sends its public key to the client. Then the client and server negotiate a set of encryption rules, called an encryption algorithm, that both machines can support. When the two machines are in agreement on the encryption algorithm, the server starts a login shell for the user. 

![A diagram shows an SSH client connecting to an SSH server. Information is exchanged until a secure connection is es][img030301]

### Configuring an SSH client
SSH configuration instructions will be different depending on your operating system and the implementation of SSH. On the other hand, instructions for a client to generate its SSH key and connect to a server are more general. Let’s look at how to set up the command-line OpenSSH client and connect to a remote host for the first time. 

#### Generating your key pair
First, you will need to generate your public/private key pair. The first time you connect to a given server using SSH, the server will store a copy of its public key on your machine. This needs to be done only once, as the same key pair can be used to connect to any number of remote hosts.

Open a terminal and enter the command: 
`ssh-keygen -t rsa -b 2048`

OpenSSH will ask where to save the generated keys. Note that it will create a hidden directory called .ssh in your home directory. You can accept the defaults here. 

SSH will also ask you for a passphrase to protect your key. Many people choose not to use a passphrase because if you enter a passphrase here, you will be required to enter it every time your key is used. If you are on a machine that is not secure, however, someone who gains access to that computer will also have access to every system that uses that key. 

If you add a passphrase to your SSH key for added security, you can save the passphrase to an SSH agent, which is a program that manages SSH keys. For more about working with SSH key passphrases, see [Adding your SSH key to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)
. 

After you have set your passphrase or declined the option, OpenSSH will then generate a random public/private key pair and save it. Depending on your hardware, this may take several seconds to complete. OpenSSH will then return a message that your key has been saved and display the fingerprint and a “randomart image” of your new key. Here is an example:

```bash
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/tradel/.ssh/id_rsa): 
Created directory '/Users/tradel/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /Users/tradel/.ssh/id_rsa
Your public key has been saved in /Users/tradel/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:0P4GpCFXlVoZPoQ8ULdqq9L0p2KTYlMwtOLXIwSxfO8 tradel@Todds-MacBook-Pro.local
The key's randomart image is:
+---[RSA 2048]----+
|  ..  .+oo=+     |
| ....  o+++.     |
|  ooo.+ o++      |
|  ..=+ *.. .     |
| . o +o S        |
|  . o.=. +       |
|   . =E+. o      |
|    = *....      |
|   . =.o.o       |
+----[SHA256]-----+
```

### Connecting for the first time
Now that you have a key pair, you can connect to a host. The most basic form of the command to connect is: 

`ssh <username>@<hostname>`

When you connect to a server for the first time, SSH will print out the fingerprint of the remote server’s key and confirm that you really want to connect. The request will look like this:

```bash
The authenticity of host 'my-host (192.168.1.10)' can't be established.
ED25519 key fingerprint is SHA256:KyE8fOzengv6CRTe1EXaeO7dtIF9JKM0VAcKf6sA0RM.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'my-host' (ED25519) to the list of known hosts.
```

You may be asked to enter the password for the account on the remote host. After you do this, a copy of your public key will be stored on the host, and you will not have to enter your password again. Your own copy of your key is sufficient to authenticate your connection. 


### Configuring an SSH server
As we said earlier, SSH server configuration will vary based on your operating system and implementation of SSH. The SSH server component, called a “daemon,” is often installed by default on Linux and Unix. On Linux, the server configuration file is usually at `/etc/ssh/sshd_config` and rarely needs to be changed. 

If you try to connect to a host and see an error like “ssh: connection refused”, consult your operating system documentation for how to install and enable the SSH daemon. 

For use cases like increased security or managing user connections, see [How To Tune your SSH Daemon Configuration on a Linux VPS](https://www.digitalocean.com/community/tutorials/how-to-tune-your-ssh-daemon-configuration-on-a-linux-vps).

Later versions of MacOS also have a command-line SSH client already installed. For a free implementation of SSH for Windows, Mac, and Unix, see [PuTTY: a free SSH and Telnet client](https://www.chiark.greenend.org.uk/~sgtatham/putty/). 


### Pro Tips 
You can use the same private/public key pair across all the machines you control. So if you have two laptops and a tablet, you could copy your key pair to all of them. This can save you a few steps when logging in from other devices.

Once SSH is set up, if the public key sent by the server ever changes, SSH will warn you that something malicious may have happened to the server. You will receive an alert message that states the “Remote host identification has changed” or similar. You should contact your systems administrator if you see this message. Although it’s possible that the server has simply updated its key, it’s also possible that someone is eavesdropping on communications between you and an application in order to steal information. 


Optional features like port forwarding are often disabled by default because they open up potential security holes if they are misused. You may need these optional features to be enabled for something like forwarding network ports from a remote host to your local machine; for instance, if you want to access a service on the host (or the host's network) that is blocked by a firewall. If you need these optional features enabled, turn them on in the sshd_config file.





## API Keys
An Application Programming Interface (API) key is an authentication token that allows you to call an API. An application passes an API key to the API, which is then called to identify the person, programmer, or program trying to access a website. It is frequently accompanied by a set of access rights that are specific to the API the key is linked to. In this reading, you will delve into API keys, their role, their function in authentication and authorization, and how they are used. 

The API key is usually randomly generated by the application and must be sent on every API call. It serves as a distinctive identifier and offers a secure token for authentication.

### Authentication and authorization
API keys may be used for both authentication, making sure you’re who you say you are, and authorization, deciding which APIs you are allowed to call.

When you are authenticating with API keys, you are ensuring that malicious users or applications can’t call an API and make unauthorized or authorized changes. With project authentication (application or site authentication), API keys help identify the project or application that makes the call. If you are using API keys for user authentication, the identity of the user is being verified. 

When you are authorizing with API keys, you are also ensuring that you have the correct API call. Authorization will also check that the API key being used in the project is available.

### How they are used
When using `APIs`, the usage depends on the specific `API`. With most APIs, you are required to send the API key with every request. It can be sent in one of several ways:

1. As an HTTP parameter in the request URL. Example: `GET https://myapp.com/api/users/list?apikey=12345678`

2. As an HTTP header sent with the request. Example: `GET https://myapp.com/api/users/listX-API-Key: 12345678`

3. (Rarely) Posted to a specific authorization endpoint, which returns another token or a cookie to be sent with subsequent requests. Example: `POST https://myapp.com/api/auth{ “token”: “12345678” }`

One last tip, do not hardcode API keys into your application code, especially if it will be posted in a public repository like Github. If you have hardcoded your API keys into your application code, anyone who wants to can make API calls with your authorization! 

Unfortunately, it happens every day. For this reason, many applications are moving away from API keys and toward OAuth, which requires the user to manually authorize an application before using it. With being extra cautious, you can make sure this does not happen to you. 


### Key takeaways
- **API keys facilitate secure interactions:** The API key serves as a crucial authentication token that not only permits API calls, but also plays a vital role in regulating access privileges and defining permissible actions. It's an essential tool in ensuring secure and controlled communication within digital ecosystems.

- **Authentication and authorization:** API keys serve a dual purpose: authentication and authorization. Authentication verifies the identity of users or applications making API calls, preventing unauthorized access or changes. Authorization, on the other hand, ensures that users have the appropriate rights to call specific APIs, promoting controlled usage and adherence to access policies. 

- **Effective API key usage:** When using APIs, the API key can be included as an `HTTP` parameter in the URL or an HTTP header. Ensuring that API keys aren't hardcoded in application code is important in order to prevent unauthorized access. Many applications are transitioning from API keys to more secure methods where manual user authorization enhances security measures and minimizes risks associated with API misuse.





## When to use API Keys
Managing access and safeguarding resources is where API keys come into play. An API may require API keys for part or all of its methods. In this reading, we delve into the concept of API keys, exploring their pivotal role in not only securing and controlling access, but also in gathering insights to some processes API keys should not be used for. 

There are a few reasons why you might want to use API keys.

### What you can use API keys for
Some of the ways you might use API keys include: 
- To block anonymous traffic - Can help to protect your API from abuse and to ensure that only authorized users are able to access it.
- To control the number of calls made to your API - Can help to prevent your API from being overloaded and to ensure that it is available to all authorized users.
- To identify usage patterns - Can be used to improve your API and to make sure that it is meeting the needs of your users.
- To filter logs by API key - Can help you to troubleshoot problems with your API and to identify which users are using your API the most.

### What you cannot use API keys for
You can’t use API keys for: 
- Identifying individual users - API keys do not identify individual users; they identify entire projects.
- Secure authorization - They should be used only to identify and control access to an API.
- Identifying the creators of a project - Service Infrastructure doesn't provide a method to directly look up projects from API keys.

### Key Takeaways
- You use API keys for blocking anonymous traffic, controlling the number of calls made to your API, identifying usage patterns, and to filter logs by API keys. 

- You can’t use API keys for identifying individual users, securing authorization, and identifying the creators of a project. 

API keys serve as the link between the potential of APIs and the demand for restricted usage. As developers continue to harness the power of APIs to weave intricate software ecosystems, a nuanced understanding of API keys' capabilities and boundaries becomes the cornerstone of ensuring secure, efficient, and insightful API management.





## Public vs. private keys
In a rapidly evolving world of technology, it is more critical than ever to establish security policies throughout an organization that safeguard valuable information and data assets. Asymmetric cryptography relies on public and private keys as its core building blocks to maintain data security and confidentiality in the face of dangers. However, to enable organizations to make wise decisions that will protect online interactions and information, it is important that we understand when public and private keys are used and how to do so effectively.


### What is a public key?
A **public key** is frequently employed to establish secure communication through data encryption or to validate the authenticity of a digital signature. Safety is ensured because the public key comes from a trusted certificate authority, which gives digital certificates verifying the owner’s identity and key. Public keys are created through an asymmetric algorithm that conducts several operations on a pair of connected keys before being transmitted over the internet.


### What is a private key?
A private key is a secret and secure key that must be kept confidential and protected. Its role involves decryption and the creation of digital signatures, assuring the data's integrity and authenticity. It is the counterpart of the public key and is shared to decrypt encoded information. Any data encrypted using the private key can be decrypted using the corresponding public key.

### How do public and private keys work together?
Public and private keys work together to ensure secure communication, data encryption, digital signatures, and key exchanges take place safely across various communication channels. This process encompasses:
1. Key generation: A public and private key is generated for both the sender and receiver.
2. Key exchange: The public keys are exchanged between sender and receiver.
3. Encryption: The sender encrypts their data using the recipient's public key.
4. Transmitting encrypted data: The encrypted data is transmitted to the recipient.
5. Decryption: The recipient decrypts the message using their exclusive private key.

### Key takeaway
In summary, although public and private keys are distinct, they work together to create a powerful and flexible foundation for achieving data security, confidentiality, integrity, and authentication in a wide range of digital settings.



# Module 02 - Using Git Locally









# Module 03 - Working with Remotes









# Module 04 - Managing Data and Processes









# Module 05 - Testing in Python









# Module 06 - Bash Scripting









# Module 07 - Final Project









# Public

[img010101]: /back-end-development/public/img010101_path_selected.png
[img010102]: /back-end-development/public/img010102_initial_screen.png
[img010103]: /back-end-development/public/img010103_mac_install_app.png
[img010104]: /back-end-development/public/img010104_extensions_icon.png
[img010105]: /back-end-development/public/img010105_python_extension.png
[img010106]: /back-end-development/public/img010106_Screenshot-2022-06-23-at-16.58.30.png
[img010107]: /back-end-development/public/img010107_Screenshot-2022-06-23-at-17.04.00.png
[img010108]: /back-end-development/public/img010108_Screenshot-2022-06-23-at-17.12.24.png

[img020101]: /back-end-development/public/img020101_For-Loop-Program.png
[img020102]: /back-end-development/public/img020102_BED_C2M1L3_item07-img02.png
[img020201]: /back-end-development/public/img020201_item04-img01.png

[img030301]: /google-It-Automation-with-Python/public/img030301.png