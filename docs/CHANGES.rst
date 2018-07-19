Changelog
=========

0.4 (unreleased)
----------------

- Added more strings classifiers items for the metadata package
  [macagua]

- Fixed warning: no files found matching '*.txt' from MANIFEST.in file
  [macagua]

- Fix packaging error, ``CHANGES.rst`` was missing in eggs.
  [saily]


0.3 (2013-10-09)
----------------

- Switch from ``optparse`` to ``argparse``, so we need >= Python 2.7 now.
  [saily]

- Add more configurable parser, allow non-div tags, allow to strip tags by
  passing ``""`` as argument for ``-t``.
  [saily]

- Allow users to limit convenience classes by using ``--level`` parameter.
  default is still ``min(columns, 7)``.
  [saily]


0.2 - 2012-07-09
----------------

- fixed css lineendings
- removed double "position-0" declaration
  [petschki]

0.1.1 - 2011-05-26
------------------

- updated install documentation [petschki]

0.1 - 2011-04-07
----------------

- Idea and initial release
  [saily]
