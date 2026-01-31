# {{ site.title }}

[![License](https://img.shields.io/github/license/{{ site.github_username }}{{ site.baseurl }})](LICENSE.md)

**Author:** {{ site.author }}  
**Version:** {{ site.version }}  

## Overview
{{ site.description }}  

**Utilizes:**  
The **{{ site.title }}** depends on the following repositories for its documentation and sub-features.  

* [cookiecutter-cookiecutter](https://github.com/jcook3701/cookiecutter-cookiecutter) is the the parent repository for {{ site.title }}.  Updates from ```cookiecutter_project_upgrader``` are pulled from this repository.
* [Github docs](https://github.com/jcook3701/github-docs-cookiecutter) cookiecutter template generation for Github Pages (Jekyll).
* [Sphinx docs](https://github.com/jcook3701/sphinx-cookiecutter) cookiecutter template generation for Python Sphinx Documentation.
* [Nutri-Matic](https://github.com/jcook3701/nutri-matic) cookiecutter utilities for streamlining development and utilization of Cookiecutter templates.

**Maintains:**  
The **{{ site.title }}** is used to maintain the build and ci/cd structure for the following projects.  

* **[Nutri-Matic](https://github.com/jcook3701/nutri-matic) cookiecutter utilities for streamlining development and utilization of Cookiecutter templates.

***

🛠️ **CI/CD Check List:**

* ![dependency-check](https://github.com/jcook3701/python3-cookiecutter/actions/workflows/dependency-check.yml/badge.svg)
* ![format-check](https://github.com/jcook3701/python3-cookiecutter/actions/workflows/format-check.yml/badge.svg)
* ![lint-check](https://github.com/jcook3701/python3-cookiecutter/actions/workflows/lint-check.yml/badge.svg)
* ![security-audit](https://github.com/jcook3701/python3-cookiecutter/actions/workflows/security-audit.yml/badge.svg)
* ![spellcheck](https://github.com/jcook3701/python3-cookiecutter/actions/workflows/spellcheck.yml/badge.svg)
* ![tests](https://github.com/jcook3701/python3-cookiecutter/actions/workflows/tests.yml/badge.svg)
* ![typecheck](https://github.com/jcook3701/python3-cookiecutter/actions/workflows/typecheck.yml/badge.svg)

***

**Note:** Unless you are using a newer version of cookiecutter >= 2, ```--no-input``` is necessary for template generation without error.  

## Usage Examples

**Example:** Pull from main branch.  
**Note:** [Nutri-Matic](https://github.com/jcook3701/nutri-matic) is needed in active python environment.  

1. Pull Project with cookiecutter command:  

``` shell
$ cookiecutter git@github.com:jcook3701/python3-cookiecutter.git \
	--no-input \
	project_name="test-project"  
```

**Example:** Pull from develop branch.  

1. Pull code from development branch while testing updates.  

``` shell
$ cookiecutter git@github.com:jcook3701/python3-cookiecutter.git \
	  --checkout develop \
	  --no-input \
	  project_name="test-project"
```
replace ```test-project``` or any of the other variables with real context configuration variables:  

**Note:** replace ```test-project``` or any of the other variables with real context configuration variables.  

***

## 🌱 Getting Started

* [Requirements]({{ site.github_io_url }}/manual/setup-guide/requirements)
* [Installation guide]({{ site.github_io_url }}/manual/introduction/installation-guide)  

## 📚 Documentation

The {{ site.title }} documentation is available at [docs]({{ site.github_io_url }}).  

## 🤝 Contributing

If you're interested in contributing to the {{ site.title }} project:  
* Start by reading the [contributing guide]({{ site.github_io_url }}/manual/developer-resources/contribute).  
* Learn how to setup your local environment, in our [developer guide]({{ site.github_io_url }}/manual/contribute/developer-guide).  
* Look through our [style guide]({{ site.github_io_url }}/manual/contribute/style-guides/index).  

***

## 🍹 Authors Notes

1. This code currently works with cookiecutter (V2.6) from Ubuntu's apt repositories.

## ⚖️ License

{{ site.copyright }}  

This project is licensed under the **{{ site.license }} License**.  
See the [LICENSE]({{ site.repo_blob }}/LICENSE.md) file for the full license text.  

SPDX-License-Identifier: {{ site.license }}

***

### Future Ideas:  

1. [Organizing cookiecutters in directories](https://cookiecutter.readthedocs.io/en/latest/advanced/directories.html#organizing-cookiecutters-in-directories)  
   * Add freecad paths for freecad projects.  
   * etc.  
2. Create python repository to make it easy to swap nested vars but might eventually use newer version of cookiecutter from pypi.  
3. Update configuration file to include or disclude the Dockerfile (Only needed for a webapp)
4. Create separate repo to utilize cookiecutter 1.7 with custom json config in order to update pyproject.toml variables in 'config' variable.  

### Authors Notes:  

1. This code currently works with cookiecutter 1.7 from Ubuntu's apt repositories.  
