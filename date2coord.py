#!/usr/bin/python

"""Convert a date to SVG abcissa."""

import datetime
import argparse


ORIGIN_DATE = datetime.date(2005, 01, 01)
ORIGIN_OFFSET = 600
YEAR_STEP = 3600
MONTH_STEP = 300
PSEUDO_DAY = YEAR_STEP / float(365) / 12


def mkdate(datestring):
    """Return a date parsed from the ISO notation YYYY-MM-DD."""
    return datetime.datetime.strptime(datestring, '%Y-%m-%d').date()


def timedelta_to_coord(date):
    """Return the abscissa corresponding to the given date."""
    #days_delta = (date - ORIGIN_DATE).days
    years = date.year - ORIGIN_DATE.year
    months = date.month - 1
    days = date.day - 1
    return int(years * YEAR_STEP +
               months * MONTH_STEP +
               days * PSEUDO_DAY +
               ORIGIN_OFFSET)


def main():
    """Main method."""
    parser = argparse.ArgumentParser(description='Converting a date to the coordinate system.')
    parser.add_argument('date', type=mkdate,
                        help='the date to convert in ISO format')
    args = parser.parse_args()
    print timedelta_to_coord(args.date)


if __name__ == "__main__":
    main()
