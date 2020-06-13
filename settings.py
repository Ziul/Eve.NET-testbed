# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2014 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import os
import domain

# Sensible settings are retrieved from environment variables when available in
# the hosting environment (Heroku), or set to default values for local testing.
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = int(os.environ.get('MONGO_PORT', 27017))
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'testbed')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'testbed')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'evenet-testbed')

# $PORT is defined if we are hosted on Heroku
if os.environ.get('PORT') is None:
    DEBUG = True

# Allow full range of CRUD operations on resources and items
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE', 'PUT']

# Enable 'User Restricted Resource Access' (see
# http://python-eve.org/authentication.html#user-restricted.) This will allow
# accounts to only edit/retrieve data created by themselves.
# AUTH_USERNAME_FIELD = domain.account_key

# Disable HATEOAS
HATEOAS = False

# We want the whole document back with POST/PATCH/PUT responses.
BANDWIDTH_SAVER = False

# Turn soft deletes on
SOFT_DELETE = True

# Enable schema route
SCHEMA_ENDPOINT = 'schema'

# Set the API domain
DOMAIN = domain.DOMAIN
