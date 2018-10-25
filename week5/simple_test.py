#!/usr/bin/python

users = [
    { 'admin': True, 'active': True, 'name': 'Kevin' },
    { 'admin': True, 'active': False, 'name': 'Elisabeth' },
    { 'admin': False, 'active': True, 'name': 'Josh' },
    { 'admin': False, 'active': False, 'name': 'Kim' },
]

line = 1
for user in users:
    if user['admin'] and user['active']:
       print("%s ACTIVE - (ADMIN) %s" % (line, user['name']))
    elif user['admin']:
       print("%s (ADMIN) %s" % (line, user['name']))
    elif user['active']:
       print("%s ACTIVE - %s" % (line, user['name']))
    else:
       print("%s %s" % (line, user['name']))
    line += 1