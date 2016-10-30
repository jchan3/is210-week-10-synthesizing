#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_01."""


def sum_orders(customers, orders):
    """A function that combines two datasets into a single dictionary keyed by
        customer id.

    Args:
        customers(dictionary): A dictionary of customers keyed by customer_id.
        orders(dictionary): A dictionary of orders keyed by order id.

    Returns:
        dictionary: A dictionary with a key of customer id and the inner keys
        of name, email, orders, and total.

    Examples:

        >>> import data
        >>> sum_orders(data.CUSTOMERS, data.ORDERS)
        {1: {'orders': 3, 'total': 1287, 'name': 'Ekaterin Vorsoisson', 'email':
        'evorsoisson@komarr.net'}, 2: {'orders': 5, 'total': 2778, 'name': 'Cord
        elia Naismith', 'email': 'cordelia@beta.com'}, 3: {'orders': 3, 'total':
        358, 'name': 'Ivan Vorpatril', 'email': 'iv398@barrayar.net'}, 4: {'orde
        rs': 5, 'total': 1207, 'name': 'Aral Vorkosigan', 'email': 'viceroy@serg
        yar.net'}, 5: {'orders': 3, 'total': 451, 'name': 'Eli Quinn', 'email':
        'admiral@dendarii.com'}, 6: {'orders': 3, 'total': 1198, 'name': 'Bel Th
        orne', 'email': 'portmaster@graf.net'}, 7: {'orders': 3, 'total': 1897,
        'name': 'Simon Illyan', 'email': 'impsec@barrayar.net'}, 8: {'orders': 1
        , 'total': 204, 'name': 'Duv Galeni', 'email': 'dg1367@barrayar.net'}, 9
        : {'orders': 2, 'total': 1704, 'name': 'Gregor Vorbarra', 'email': 'imps
        ec@barrayar.net'}}


    """
    newdict = {}

    for value in orders.itervalues():
        temp_id = value.get('customer_id', None)
        if newdict.get(temp_id, None):
            temp_count = newdict[temp_id]['orders'] + 1
            newdict[temp_id]['orders'] = temp_count
            temp_total = newdict[temp_id]['total']
            newdict[temp_id]['total'] = temp_total + value['total']
        else:
            newdict[temp_id] = {}
            newdict[temp_id]['name'] = customers[temp_id]['name']
            newdict[temp_id]['email'] = customers[temp_id]['email']
            newdict[temp_id]['orders'] = 1
            newdict[temp_id]['total'] = value['total']

    return newdict
