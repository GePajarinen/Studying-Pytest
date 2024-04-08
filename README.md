# Class pytest
Course from Coursera   
[![Python app test with GA](https://github.com/GePajarinen/class-pytest/actions/workflows/main.yml/badge.svg)](https://github.com/GePajarinen/class-pytest/actions/workflows/main.yml)

> Testing is a mandatory component of DevOps.
-------------------------------------------
Creating virtual enviroment:

```
which virtualenv
virtaulenv --help
virtualenv ~/.venv # to hide the venv into a invisible foldar
source ~/.venv/bin/activate # to activitae the venv
```

To configure the bash to have a venv for everynew tab:
```
vim ~/.bashrc
```
Add to the file:
```
# Source Virtualenv:
source ~/.venv/bin/activate 
```

To falitate the life, we can create a file with the most used commands:
Create the file:
```
touch Makefile
```
And add the commands.

Create a requirements file:
```
touch requirements.txt   
```
```pytest```   
```pytest-cov``` -> it convers the percentage of what was tested   
```pylint``` -> it captures the bad coding and syntax errors   
```black``` -> to auto format the file   
```ipython``` -> turns the venv into a Notebook type (~ Jupiter) just type ipython to activate it and exit(). Good to prototype the unit test.     
```nbval```-> to test Notebooks.ipynb

To test only one module:
```
python -m pytest -vv folder/file.py::module_name
```






