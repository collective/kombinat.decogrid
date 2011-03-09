#!/usr/bin/env python
# -*- coding: utf-8 -*-
import optparse
import os

cell = 0.1
while int(cell) != cell:
    width = int(raw_input("Portal width [960]: ") or 960)
    padding = int(raw_input("Global margin between columns [10]: ") or 10)
    columns = int(raw_input("Columns [16]: ") or 16)
    lrm = (raw_input("Use left/right margin [Y/n]: ").lower() or 'y') == 'y'

    if lrm:
        # when using a left/right margin it would be
        # n-1 * padding + 2 * 0.5 * padding = n * padding
        cell = float(width - columns * padding) / columns
    else:
        cell = float(width - (columns - 1) * padding) / columns

    if int(cell) != cell:
        print "\n\nWARNING: You won't get valid cell width pixel entries."
        if (raw_input("Go on, don't ask me! [y/N]: ").lower() or 'n') == 'y':
            break

css = """

/* The %d-column Deco Grid System for fixed width of %dpx:
 * Cells are %dpx (%.2f%%), margin will be %dpx (%.2f%%).
 * Portal left/right margin is %dpx (%.2f%%).
 */

div.row {
  float: left;
  width: 100%%;
  display: block;
  position: relative;
}
div.cell {
  position: relative;
  float: left;
  left: 100%%;
}

/* Width classes. */ """ % (columns, width,
                            cell, 100.0 / width * cell,
                            padding, 100.0 / width * padding,
                            lrm and padding / 2.0 or 0,
                            lrm and 100.0 / width * (padding / 2.0) or 0)

# width
for i in range(1, columns + 1):
    css += "\ndiv.width-%d { width: %.4f%%; }" % (
        i, 100.0 / width * (i * cell + (i - 1) * padding))

# positioning
css += """

/* Positioning classes, these are subtracting from a rightmost position, which
is why they seem the wrong way around */"""
for i in range(0, columns):
    css += "\ndiv.position-%d { margin-left: -%.4f%%; }" % (
        i, 100 - (100.0 / width * (lrm and (i * cell + (i + 0.5) * padding) \
                                       or (i * (cell + padding)))))

# convenience classes
css += """
/* End of the core Deco Grid System */

/* Convenience classes. Not strictly necessary. */
div.width-full { width: %.4f%% }
div.position-0 { margin-left: -%.4f%% }
""" % (100.0 / width * (width - (lrm and padding or 0)),
       100.0 / width * (width - (lrm and padding * 0.5 or 0)))

for i in range(2, min(7, columns)):
    pos = ""
    for j in range(1, i):

        # calculate new cell width
        cell = float(width - (i - (not lrm and 1 or 0)) * padding) / i

        css += "\ndiv.width-%d\\3a %d { width: %.4f%% }" % (
            j, i, 100.0 / width * \
                          (j * cell + (j - 1) * padding))

        pos += "\ndiv.position-%d\\3a %d { margin-left: -%.4f%% }" % (
            j, i, 100 - (100.0 / width * \
                         (j * cell + (j + (lrm and 0.5 or 0)) * padding)))

    css += pos + "\n"

print css


def generator():
    parser = optparse.OptionParser(usage="""%prog [options]

%prog generate decogrid columns.css for plone (http://deco.gs).""")

    parser.add_option('-w', '--width', action='store_true',
                      dest='width', default=960, type="int",
                      help="portal width in pixels incl. potentially margins")

    parser.add_option('-m', '--margin', action='store_true',
                      dest='margin', default=10, type="int",
                      help="Margins between cells.")

    parser.add_option('-c', '--columns', action='store_true',
                      dest='columns', default=16, type="int",
                      help="Columns.")

    parser.add_option('-o', '--omit-margin', action='store_true',
                      dest='omit', default=False, type="bool",
                      help="Omit left and right margin around portal " + \
                           "(recommended for nesting grids inside grids).")

    (options, args) = parser.parse_args()

    if len(args) != 0:
        parser.print_help()
        return

if __name__ == '__main__':
    generator()
