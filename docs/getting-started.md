# Getting started

A historical API, initiated in 2023, offers daily historical event data including events, 652 presidents' details, notable births and deaths, historical curiosities, and holidays. Additionally, it provides four daily historical questions in 18 languages. Material for MkDocs can be installed with [`pip`][pip]

[pip]: #with-pip

## Installing

### with pip <small>recommended</small> { #with-pip data-toc-label="with pip" }

History API is published as a [Python package] and can be installed with
`pip`, ideally by using a [virtual environment]. Open up a terminal and install
History API with:

To install the library, simply run the following command:

```bash
pip install history-api
```

!!! tip

    If you don't have prior experience with Python, we recommend reading
    [Using Python's pip to Manage Your Projects' Dependencies], which is a
    really good introduction on the mechanics of Python package management and
    helps you troubleshoot if you run into errors.

[Python package]: https://pypi.org/project/mkdocs-material/
[virtual environment]: https://realpython.com/what-is-pip/#using-pip-in-a-python-virtual-environment
[Using Python's pip to Manage Your Projects' Dependencies]: https://realpython.com/what-is-pip/

### with git

Material for MkDocs can be directly used from [GitHub] by cloning the
repository into a subfolder of your project root which might be useful if you
want to use the very latest version:

To install the development version, do the following:

```bash
git clone https://github.com/leviobrabo/history-api
```

[GitHub]: https://github.com/leviobrabo/history-api

Next, install the theme and its dependencies with:

```
pip install -e history-api
```
