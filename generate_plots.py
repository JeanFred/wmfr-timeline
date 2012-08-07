#!python
# -*- coding: UTF-8 -*-

from svg.charts import time_series
import os

def generate_plots():
    """Generate the various plots"""
    yield 'Members', members_Plot()


def members_Plot():
    """Generate the plot of the members
    """
    g = time_series.Plot({})
    g.width = 1000
    g.height = 500
    g.timescale_divisions = '1 years'
    g.key = False
    g.x_label_format = '%Y-%m'
    g.min_y_value = 0
    #g.max_x_value = '2014-01'

    g.show_x_labels = False
    g.show_y_labels = False
    g.show_x_guidelines = False
    g.show_y_guidelines = False
    g.show_data_values = False
    g.show_data_points = False
    g.draw_lines_between_points = True
    g.area_fill = False
    
    data = read_data(os.path.join(os.path.dirname(__file__),
                                  'data', 'members.dat'))
    g.add_data(
        {'data': data,
        'title': 'Members'})
    return g

def read_data(file_path):
    data = []
    with open(file_path) as f:
        for line in f:
            (date, number) = line.rstrip().split(',')
            data.extend([date, int(number)])
    return data

def write_plots():
    """Write the plots on disk
    """
    root = os.path.dirname(__file__)
    for plot_name, plot in generate_plots():
        res = plot.burn()
        with open(os.path.join(root, plot_name + '.svg'), 'w') as f:
            f.write(res)


if __name__ == '__main__':
    write_plots()
