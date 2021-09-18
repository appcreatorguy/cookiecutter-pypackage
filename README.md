# Cookiecutter PyPackage

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a Python package.

- GitHub repo: <https://github.com/appcreatorguy/cookiecutter-pythonpackage/>
- Free software: BSD license

## Features

- Testing setup with `unittest` and `python setup.py test` or `pytest`
- [GitHub Actions](https://github.com/features/actions): Ready for Travis Continuous Integration testing
- [Tox](http://testrun.org/tox/) testing: Setup to easily test for Python 3.6, 3.7, 3.8
- [Sphinx](http://sphinx-doc.org/) docs: Documentation ready for generation with, for example, [Read the Docs](https://readthedocs.io/)
- [bump2version](https://github.com/c4urself/bump2version): Pre-configured version bumping with a single command
- Auto-release to [PyPI](https://pypi.python.org/pypi) when you push a new tag to master (optional)
- Command line interface using Click (optional)

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```bash
pip install -U cookiecutter
```

Generate a Python package project:

```bash
cookiecutter https://github.com/appcreatorguy/cookiecutter-pythonpackage.git
```

Then:

- Create a repo and put it there.
- Install the dev requirements into a virtualenv. (`pip install -r requirements_dev.txt`)
- [Register](https://packaging.python.org/tutorials/packaging-projects/uploading-the-distribution-archives) your project with PyPI.
- Add a secret to your github repository named PYPI\_TOKEN (or TESTPYPI\_TOKEN) to enable PyPi deployment.
- Add the repo to your [Read the Docs](https://readthedocs.io/) account + turn on the Read the Docs service hook.
- Release your package by pushing a new tag to master.
- Add a `requirements.txt` file that specifies the packages you will need for your project and their versions. For more info see the [pip docs for requirements files](https://pip.pypa.io/en/stable/user_guide/#requirements-files).
- Enable [Dependabot](https://github.com/features/security) security updates and Vulnerability Alerts.

### Fork This / Create Your Own

If you have differences in your preferred setup, I encourage you to fork this to create your own version. Or create your own; it doesn't strictly have to be a fork.

- It's up to you whether or not to rename your fork/own version. Do whatever you think sounds good.

### Or Submit a Pull Request

I also accept pull requests on this, if they're small, atomic, and if they make my own packaging experience better.
