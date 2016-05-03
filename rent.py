#!/usr/bin/env python
"""
Charge my roommates rent.

I pay 1910.05
Total is 8457.70
I need to cash out $6546.95
"""

import venmo

CONVENIENCE_FEE = 5
CHARGES = {
    '@nicholas-lippis': 1920.04 + CONVENIENCE_FEE,
    '@dylan-harris-3': 1675.04 + CONVENIENCE_FEE,
    '@robert-garbanati': 976.28 + CONVENIENCE_FEE,
    '@zmorris': 1000,
    '@traplord': 976.29 + CONVENIENCE_FEE,
}


def main():
    for user, amount in CHARGES.iteritems():
        venmo.payment.charge(user, amount, 'rent')


if __name__ == '__main__':
    main()
