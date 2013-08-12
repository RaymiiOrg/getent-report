# GetEnt Reporter

This is a user reporting script. It looks at the UNIX users and groups, and creates a list of which users there are, which groups they are in and which groups there are and which users are in those groups.

I'm using it to report the users on an Active Directory bound node, setup [as described here](https://raymii.org/s/tutorials/SAMBA_Share_with_Active_Directory_Login_on_Ubuntu_12.04.html). 

It supports filtering out unwanted users/groups, and it comes preloaded with a lot of filters.

# Requirements

- Python 2.7

# Example

    $ ./getent-report

    # Users
    Name: Administrator
    Email: administrator@digidentity.eu
    Groups:domain admins, everyone,


    Name: Jane Doe
    Email: jdoe@digidentity.eu
    Groups:everyone,

    # Groups
    Group: marketing
    Members: jdoe, dradcliff, jrowling

    Group: hr
    Members: jtolkien, fbaggins, kjaneway

    # Statistics
    Number of Users: 15
    Number of Groups: 4


