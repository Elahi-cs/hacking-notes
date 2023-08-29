Proper Operating System preparation is required before conducting any penetration test.

We should organizer our structure according to penetration testing stages and the targets' OS

Create an Firefox account for pentesting purposes only where we save all bookmarks. Assume it'll be seen by a third party at some point.

Three problems with passwords:
1. Complexity
2. Re-usage
3. Remembering

Password managers solve all three problems

Containers:

Isolated group of processes running on a single host that corresponds to a complete application.

Vagrant: Create configure and manage VMs in a host as if they were Docker containers in an OS.

Recommended tools to install on a fresh Linux (ParrotOS) : 
See tools.list
```sudo apt install $(cat tools.list | tr "\n" " ") -y```

Recommended tools to install on a fresh Windows: 
Chocolatey Python VSCode Git WSL2 OpenSSH OpenVPN Windows Terminal Netcat NMap Wireshark Burp Suite HeidiSQL SysInternals Putty Golang Neo4J OpenJDK

Use the following script for timestamps in bash prompts (useful for logging):
```echo 'export PS1="-[\[$(tput sgr0)\]\[\033[38;5;10m\]\d\[$(tput sgr0)\]-\[$(tput sgr0)\]\[\033[38;5;10m\]\t\[$(tput sgr0)\]]-[\[$(tput sgr0)\]\[\033[38;5;214m\]\u\[$(tput sgr0)\]@\[$(tput sgr0)\]\[\033[38;5;196m\]\h\[$(tput sgr0)\]]-\n-[\[$(tput sgr0)\]\[\033[38;5;33m\]\w\[$(tput sgr0)\]]\\$ \[$(tput sgr0)\]"' >> .bashrc```
