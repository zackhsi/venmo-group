#!/usr/bin/env python
"""
Charge my roommates rent.

I pay 1247.61
Total is 10750
I need to cash out 9502.39
"""

import venmo

ME = 1247.61
CHARGES = {
    '@nicholas-lippis': 1571.43,
    '@dylan-harris-3': 1771.43,
    '@robert-garbanati': 1671.43,
    '@zmorris': 1471.43,
    '@traplord': 1296.43,
    '@ben-hunter-3': 1096.43,
    '@Claire-Redemer': 623.81,
}
TOTAL = 10750
TOLERANCE = 0.01


def main():
    total_charged = ME + sum(CHARGES.values())
    if abs(TOTAL - total_charged) > TOLERANCE:
        print('Rent {} does not equal total {}'
              .format(
                  ME + sum(CHARGES.values()),
                  TOTAL,
              ))
        return
    for user, amount in CHARGES.iteritems():
        venmo.payment.charge(user, amount, 'rent')


if __name__ == '__main__':
    main()
