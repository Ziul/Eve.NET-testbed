# -*- coding: utf-8 -*-
"""
    this package exposes the API domain and commonly used settings.

    :copyright: (c) 2013 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import countries
import companies
import accounts
from common import account, account_key  # noqa (will raise W0611 on pyflakes)

DOMAIN = {
    'countries': countries.definition,
    'companies': companies.definition,
    'accounts': accounts.definition,
}
