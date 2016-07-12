#!/usr/bin/env python
"""
Charge my roommates rent.

I pay 1900
Total is 10750
I need to cash out 8850
"""

import venmo

CHARGES = {
    '@nicholas-lippis': 1600,
    '@dylan-harris-3': 1600,
    '@robert-garbanati': 1700,
    '@zmorris': 1500,
    '@traplord': 1325,
    '@ben-hunter-3': 1125,
}


def main():
    total_charged = 1900 + sum(CHARGES.values())
    error_message = ('{} != 10750, need {} more'
                     .format(total_charged, 10750 - total_charged))
    assert total_charged == 10750, error_message
    for user, amount in CHARGES.iteritems():
        venmo.payment.charge(user, amount, 'rent')


if __name__ == '__main__':
    main()
