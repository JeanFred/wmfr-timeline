#!python
# -*- coding: UTF-8 -*-

#from svg.charts import time_series
import os
import datetime
from date2coord import timedelta_to_coord


def read_data(file_path):
    """Read data from the given file.
    Data is expected in a comma separated value fomat like"""
    data = []
    with open(file_path) as f:
        for line in f:
            (datestr, number) = line.rstrip().split(',')
            date = datetime.datetime.strptime(datestr, '%Y-%m').date()
            yield (date, int(number))


def create_plots():
    """Create the plots on disk"""
    root = os.path.dirname(__file__)
    data = read_data(os.path.join(root, 'data', 'members.dat'))
    print data_to_svg(data)


def data_to_svg(data):
    """Convert some time data to a SVF line"""
    first = data.next()
    factor = 10
    start = '<path d="M%s %s ' % (timedelta_to_coord(first[0]), factor * first[1])
    end = '"  class="members"/>'
    content = " ".join(["L%s %s" % (timedelta_to_coord(x[0]), factor * x[1]) for x in data])
    return start + content + end


if __name__ == '__main__':
    create_plots()
