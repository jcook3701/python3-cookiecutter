# Python3 Cookiecutter

__Author:__ Jared Cook  
__Version:__ 0.1.0  

## Overview
Python3 cookiecutter template project + Github docs template generation + Sphinx docs template generation.  

__Note:__ Unless you are using a newer version of cookiecutter >= 2, ```--no-input``` is necessary for template generation without error.  

1. Pull Project with cookiecutter command:  
``` shell
$ cookiecutter git@github.com:jcook3701/python3-cookiecutter.git \
	--no-input \
	project_name="test-project"  
```

## Development

1. Pull code from development branch while testing updates.  

``` shell
$ cookiecutter git@github.com:jcook3701/python3-cookiecutter.git \
	 --checkout develop \
	  --no-input \
	  project_name="test-project"
```
replace ```test-project``` or any of the other variables with real context configuration variables:  

### Future Ideas:  
1. [Organizing cookiecutters in directories](https://cookiecutter.readthedocs.io/en/latest/advanced/directories.html#organizing-cookiecutters-in-directories)  
   * Add freecad paths for freecad projects.  
   * etc.  
2. Create python repository to make it easy to swap nested vars but might eventually use newer version of cookiecutter from pypi.  
3. Update configuration file to include or disclude the Dockerfile (Only needed for webapps)
4. Create seperate repo to utilze cookiecutter 1.7 with custom json config inorder to update pyproject.toml variables in 'config' variable.  


### Authors Notes:  
1. This code currently works with cookiecutter 1.7 from Ubuntu's apt repositories.  

### TODO's
1. [Poetry](https://python-poetry.org/docs/managing-dependencies/#group-include-poetry) library to manage python dependencies. 
2. 