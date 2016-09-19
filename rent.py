#!/usr/bin/env python
"""
Charge my roommates rent.

I pay 1266.67
Total is 10750
I need to cash out 9483.33
"""

import venmo

ME = 1266.67
CHARGES = {
    '@nicholas-lippis': 1600,
    '@dylan-harris-3': 1600,
    '@robert-garbanati': 1700,
    '@zmorris': 1500,
    '@traplord': 1325,
    '@ben-hunter-3': 1125,
    '@Claire-Redemer': 633.33,
}
TOTAL = 10750


def main():
    assert ME + sum(CHARGES.values()) == TOTAL
    for user, amount in CHARGES.iteritems():
        venmo.payment.charge(user, amount, 'rent')


if __name__ == '__main__':
    main()
