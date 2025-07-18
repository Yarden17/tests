.. image:: https://odoo-community.org/readme-banner-image
   :target: https://odoo-community.org/get-involved?utm_source=readme
   :alt: Odoo Community Association

==========================
Project Task Add Very High
==========================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:af956a92880cd7badcce70e98b18582b37a36b7bb4743f6213eac99df669d51a
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Production%2FStable-green.png
    :target: https://odoo-community.org/page/development-status
    :alt: Production/Stable
.. |badge2| image:: https://img.shields.io/badge/license-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fproject-lightgray.png?logo=github
    :target: https://github.com/OCA/project/tree/18.0/project_task_add_very_high
    :alt: OCA/project
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/project-18-0/project-18-0-project_task_add_very_high
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/project&target_branch=18.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module extends the field priority in project tasks, adding two new
levels of priority. The two new levels of priority are: High and Very
High.

On a task form, the priority widget is displayed with three stars
instead of one:

|image1|

On a Kanban view, the priority widget is displayed as well with three
stars instead of one:

|image2|

Without having this module installed, on the form it would look like as
that:

|image3|

and on Kanban:

|image4|

In case this module is uninstalled, all the tasks that were previously
set as High or Very High priority will be converted to Normal priority.

.. |image1| image:: https://raw.githubusercontent.com/OCA/project/12.0/project_task_add_very_high/static/description/image.png
.. |image2| image:: https://raw.githubusercontent.com/OCA/project/12.0/project_task_add_very_high/static/description/image2.png
.. |image3| image:: https://raw.githubusercontent.com/OCA/project/12.0/project_task_add_very_high/static/description/image_a.png
.. |image4| image:: https://raw.githubusercontent.com/OCA/project/12.0/project_task_add_very_high/static/description/image2_a.png

**Table of contents**

.. contents::
   :local:

Usage
=====

To use this module, you need to:

1. Open a task or create a new one
2. On the priority widget, three stars are displayed (instead of one)
3. Click on the second star: the priority of this task is now set to
   High
4. Click on the third star: the priority of this task is now set to Very
   High

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/project/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/project/issues/new?body=module:%20project_task_add_very_high%0Aversion:%2018.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* Onestein

Contributors
------------

- Andrea Stirpe <a.stirpe@onestein.nl>
- Yves Goldberg (Ygol InternetWork) yves@ygol.com
- ``Heliconia Solutions Pvt. Ltd. <https://www.heliconia.io>``\ \_

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-astirpe| image:: https://github.com/astirpe.png?size=40px
    :target: https://github.com/astirpe
    :alt: astirpe

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-astirpe| 

This module is part of the `OCA/project <https://github.com/OCA/project/tree/18.0/project_task_add_very_high>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
