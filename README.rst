======================
Cookiecutter PyPackage
======================
Cookiecutter_ template for a Python package.

* GitHub repo: https://github.com/audreyfeldroy/cookiecutter-pypackage/
* Free software: BSD license

Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``pytest``
* `GitHub Actions`_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 3.6, 3.7, 3.8
* Sphinx_ docs: Documentation ready for generation with, for example, `Read the Docs`_
* bump2version_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click (optional)

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/audreyfeldroy/cookiecutter-pypackage.git

Then:

* Create a repo and put it there.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Register_ your project with PyPI.
* Add a secret to your github repository named PYPI_TOKEN (or TESTPYPI_TOKEN) to enable PyPi deployment.
* Add the repo to your `Read the Docs`_ account + turn on the Read the Docs service hook.
* Release your package by pushing a new tag to master.
* Add a ``requirements.txt`` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.
* Enable Dependabot_ security updates and Vulnerability Alerts.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.


.. _Github Actions: https://github.com/features/actions
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _Read the Docs: https://readthedocs.io/
.. _Dependabot: https://github.com/features/security
.. _bump2version: https://github.com/c4urself/bump2version
.. _PyPi: https://pypi.python.org/pypi
