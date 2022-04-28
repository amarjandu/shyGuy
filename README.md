# shyGuy

## About
This project aims to modify video streams by covering up the faces that it 
finds. The goal is to get some type of data feed that can be imported into OBS.

## Prerequisites
Create a virtualenv folder to `${project_root}/.venv`.

Run:
```bash
    make cvenv
```

Install python dependencies
Run:
```bash
# make sure the venv is active... 👀
pip install -r requirements.txt
```


### Getting interface files

_**Optional**_

This initalizes [python-type-subs](https://github.com/microsoft/python-type-stubs) as
a submodule, and copies the `cv2/__init__.pyi` file into the pip package 
installation location.

Run:
```bash
git submodule init 
git submodule update
make link_interfaces
```



```
⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣤⣤⣀⣠⣴⣶⣶⣦⠀⠀
⠀⠀⠀⠀⠀⠘⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⣰⣿⡆⠀⠀⣀⡀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⡿⠀⠀
⠀⣿⣿⡇⠀⣸⣿⣿⣆⠀⠀⠀⠀⣿⣿⣿⣿⡟⠁⠀⠀
⠀⣿⡿⠀⠀⢿⣿⣿⣿⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀
⠀⠈⠀⠀⠀⠘⣿⣿⡟⠀⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀
⢰⡀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣤⠀⠀
⠈⠁⡀⠀⢷⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣷⠀
⠀⢀⣿⣦⣀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⡆
⠀⢿⣿⣿⣿⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢟⠀
⢤⣀⣀⣀⣨⣽⣿⡿⠿⠿⠿⣿⣿⣿⠿⠿⠿⣿⣿⡇⠀
⠀⠈⠉⠉⠉⠉⠁⠀⡀⠀⠀⠀⠀⠀⠀⣀⣴⣿⡿⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠶⠶⠶⠶⠿⠟⠋⠁⠀⠀⠀
I'm a shy guy, I like to hide from time to time.
```