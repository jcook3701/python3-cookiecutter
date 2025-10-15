# Python3 Cookiecutter

__Author:__ Jared Cook  
__Version:__ 0.1.0  

## Overview
Python3 cookiecutter template project + Github docs template generation.  

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

### Authors Notes:  
1. This code currently works with cookiecutter from Ubuntu's repository.  
