#!/usr/bin/env python2

import subprocess, sys, operator

domain = "example.com"

allUsers = subprocess.Popen(["getent passwd"], stdout=subprocess.PIPE, shell=True) 
(outUser, errGroup) = allUsers.communicate()

allGroup = subprocess.Popen(["getent group"], stdout=subprocess.PIPE, shell=True) 
(outGroup, errGroup) = allGroup.communicate()

users = {}
usernames = []
groups = {}
groupnames = []

Filter = ["sync", "guest", "nobody", "sshd", "sm_cb01120b539244b7b", "sm_a831d1c051744f3aa", "read-only domain controllers", "samba", "lp", "sudo", "lpadmin", "adm", "admins", "dip", "plugdev", "cdrom", "sambashare", "organization management", "exchange windows permissions", "utmp", "schema admins", "view-only organization management", "tty", "mail", "ircd", "ntp", "proxy", "news", "winbindd_priv", "disk", "staff", "tape", "mail", "bin", "fax", "kmem", "enterprise read-only domain controllers", "ssh", "shadow", "delegated setup", "daemon", "list", "receipient management", "domain controllers", "read only domain controllers", "syslog", "crontab", "video", "um management", "public folder management", "denied rodc password replication group", "irc", "ntp", "group policy creator owners", "news", "proxy", "src", "netdev", "libuuid", "games", "backup", "ssl-cert", "cert publishers", "records management", "operator", "gnats", "landscape", "server management", "enterprise admins", "system", "ump", "exchange trusted subsystem", "domain users", "domain guests", "whoopsie", "dialout", "ras and ias servers", "cdrom", "exchange servers", "utempter", "munin", "voice", "root", "nagios", "exchangelegacyinterop", "logcheck", "uucp", "floppy", "users", "exchange all hosted organizations", "sys", "postdrop", "man", "dnsupdateproxy", "audio", "nogroup", "postfix", "discovery management", "www-data", "allowed rodc password replication group", "sasl", "help desk", "domain computers", "recipient management", "dnsadmins"]


for line in outUser.split("\n"):
    if len(line.split(":")) == 7:
        username = line.split(":")[0]
        if username not in Filter:
            usernames.append(username)
            users[username] = {"fullname": line.split(":")[4], "email": username + "@" + domain, "function":"", "telephone":"", "groups":[]}

for line in outGroup.split("\n"):
    if len(line.split(":")) == 4:
        groupname = line.split(":")[0]
        members = line.split(":")[3].split(",")
        if groupname and groupname not in Filter:
            groupnames.append(groupname)
            groups[groupname] = {"members":members}


for user in users:
    for group in groups:
        if group and group not in Filter:
            if user in groups[group]['members']:
                if user:
                    users[user]['groups'].append(group)
usernames.sort()
groupnames.sort()

print("# Users")

for user in usernames:
    print(("Name: %s") % users[user]['fullname'])
    print(("Email: %s") % users[user]['email'] )
    sys.stdout.write(("Groups:"))
    for group in users[user]['groups']:
        sys.stdout.write(("%s, ") % group)
    print("\n\n")

print("# Groups")
for group in groupnames:
    print(("Group: %s") % group)
    sys.stdout.write(("Members: "))
    for user in groups[group]["members"]:
        sys.stdout.write(("%s, ") % user)
    print("\n\n")

print("# Statistics")
print(("Number of Users: %i") % len(usernames))
print(("Number of Groups: %i") % len(groupnames))
