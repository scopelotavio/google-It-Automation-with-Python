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