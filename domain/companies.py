# -*- coding: utf-8 -*-
"""
    'companies' resource and schema settings.

    :copyright: (c) 2014 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from common import required_string

_schema = {
    # company id ('id')
    'name': required_string,
    'password': {'type': 'string', 'nullable': True},
    'state_or_province': {'type': 'string', 'nullable': True},
}

definition = {
    'url': 'companies',
    'item_title': 'company',
    # 'additional_lookup': company_lookup,
    'schema': _schema,
}
