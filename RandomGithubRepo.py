#-----------------------------------------------------------------
# RandomGithubRepo.py
#
# Find a truly random repository from within the githubisphere
# Typical useage includes uncovering and reading really bad repo README files that
# just say things like "My code examples" or "Collection of various scripts"
#
# Copyright (C) 2016, Ryan Davison
# License: MIT
#-----------------------------------------------------------------

import requests, webbrowser
from random import randrange

##def randomNumber:

num = randrange(0, 60000000, 1)

def requestAllRepos(num):
    r= requests.get('https://api.github.com/repositories', params = {'since': num})
    full_name = r.json()[0]['full_name']
    url = "https://github.com/" + full_name
    return url


webbrowser.open(requestAllRepos(num), new = 1)

