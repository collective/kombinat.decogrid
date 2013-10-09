#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os.path
import string
import sys


class Deco(object):

    css_row = "row"
    css_cell = "cell"
    css_width = "width"
    css_position = "position"

    template = string.Template(open(
        os.path.join(os.path.dirname(__file__), 'deco.css'), 'r').read())

    def __init__(self, width, margin, columns, omit, maxlevel=7, tag='div'):
        self.width = width
        self.margin = margin
        self.columns = columns
        self.omit = omit
        self.maxlevel = maxlevel
        self.tag = tag

    @property
    def p_cell(self):
        return 100.0 / self.width * self.cell

    @property
    def p_margin(self):
        return 100.0 / self.width * self.margin

    @property
    def portal_margin(self):
        if self.omit:
            return 0
        return self.margin / 2.0

    @property
    def p_portal_margin(self):
        return 100.0 / self.width * self.portal_margin

    @property
    def cell(self):
        if self.omit:
            margin = (self.columns - 1) * self.margin
        else:
            margin = self.columns * self.margin

        return float(self.width - margin) / self.columns

    @property
    def width_full(self):
        if self.omit:
            return 100

        return 100.0 / self.width * (self.width - self.margin)

    @property
    def position_0(self):
        if self.omit:
            return - 100

        return 100.0 / self.width * (self.width - (self.margin * 0.5))

    def widths(self):
        css = ""
        for i in range(1, self.columns + 1):
            w = 100.0 / self.width * (i * self.cell + (i - 1) * self.margin)
            css += "\n%s.%s-%d { width: %.4f%%; }" % (
                self.tag, self.css_width, i, w)

        return css

    def positions(self):
        css = ""
        for i in range(0, self.columns):
            if self.omit:
                p = -100 + 100.0 / self.width * \
                    i * (self.cell + self.margin)
            else:
                p = -100 + 100.0 / self.width * \
                    (i * self.cell + (i + 0.5) * self.margin)

            css += "\n%s.%s-%d { margin-left: %.4f%%; }" % (
                self.tag, self.css_position, i, p)

        return css

    def conveniences(self):
        css = """\
%s.%s-full { width: %.4f%%; }
""" % (self.tag, self.css_width, self.width_full)

        for i in range(2, min(self.maxlevel, self.columns)):
            pos = ""
            for j in range(1, i):

                if self.omit:
                    cell = float(self.width - (i - 1) * self.margin) / i
                else:
                    cell = float(self.width - self.margin * i) / i

                css += "\n%s.%s-%d\\3a %d { width: %.4f%%; }" % (
                    self.tag, self.css_width, j, i,
                    100.0 / self.width * (j * cell + (j - 1) * self.margin))

                pos += "\n%s.%s-%d\\3a %d { margin-left: %.4f%%; }" % (
                    self.tag, self.css_position, j, i, -100 + (
                        100.0 / self.width * (j * cell + (j + (
                            not self.omit and 0.5 or 0)) * self.margin)))

            css += pos + "\n"

        return css

    def __getitem__(self, key):
        value = getattr(self, key)
        if callable(value):
            return value()

        return value

    def __call__(self):
        if int(self.cell) != self.cell:
            sys.stdout.write("/* WARN: You don't have int pixel values.*/\n\n")

        return self.template.substitute(self)


def generator():
    parser = argparse.ArgumentParser(description="""%(prog)s [options]

%(prog)s generate decogrid columns.css for plone (http://deco.gs) Default \
values are written in brackets.""")

    parser.add_argument('-c', '--columns', dest='columns', default=16,
                        type=int, metavar="COLUMNS",
                        help="how many columns (16)")

    parser.add_argument('-m', '--margin', dest='margin', default=10,
                        type=int, metavar="MARGIN",
                        help="margin in pixels between each cell (10)")

    parser.add_argument('-w', '--width', dest='width', default=960,
                        type=int, metavar="WIDTH",
                        help="portal width in pixels including potentially " +
                             "left and/or right margins (960)")

    parser.add_argument('-l', '--convenience-level', type=int, dest='level',
                        default=7,
                        help="max level of convenience classes to create (7)")

    parser.add_argument('-t', '--tag', type=str, dest='tag', default='div',
                        help="html tag to be used for 'row', 'cell' and "
                             "'convenience' css classes (div)")

    # boolean parameters
    parser.add_argument('-o', '--omit-margin', action='store_true',
                        dest='omit', default=False,
                        help="omit left and right margin around the portal " +
                             "(recommended for nesting grids inside grids)")

    options = parser.parse_args()

    deco = Deco(options.width,
                options.margin,
                options.columns,
                options.omit,
                options.level,
                options.tag)

    sys.stdout.write(deco())


if __name__ == '__main__':
    generator()
