#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.rst")
        remove_file("docs/authors.rst")

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join("{{ cookiecutter.project_slug }}", "cli.py")
        remove_file(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    print(
        "Project created! Remember to add a PYPI_TOKEN or TESTPYPI_TOKEN secret to your github repository."
    )
    print(
        "Also remember to switch to using the real PyPi index in .github/workflows/deploy.yml by using PYPI_TOKEN, as the TestPyPi has been used for now."
    )
