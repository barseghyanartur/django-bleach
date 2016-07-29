Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: none

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.4.1
-----

* Add BleachCharField and BleachTextField model fields.

0.4
---

* Add BleachCharField and BleachTextField model fields.

0.3.0
-----

* The `BleachField` model field now does its own sanitisation,
  and does *not* specify a default form field or widget.
  Developers are expected to provide their own widget as needed.

0.2.1
-----

* Make the package python3 compatible.

0.2.0
-----

* Add `bleach_linkify` template filter from whitehat2k13

0.1.3
-----

* Add missing `templatetags` package, by using `find_packages()`
* Correct templatetag name: bleach.py -> bleach_tags.py

0.1.2
-----

* Fix south migration bug

0.1.1
-----

* add south_triple_field for south integration
* clean up files to meet pep8 compliance

0.1.0
-----

Initial release
