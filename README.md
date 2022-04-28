# shyGuy

## About
This project aims to modify video streams by covering up the faces that it 
finds. The goal is to get some type of data feed that can be imported into OBS.

## Prerequisites
Create a virtualenv at `${project_root}/.venv`.

Run:
```bash
#I have a hard option that you should have commands that can
# do this in your ~/.bash_profile, down the line you'll need
# to nuke dependencies... it's useful
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

This initializes [python-type-subs](https://github.com/microsoft/python-type-stubs) as
a submodule, and symlinks the `cv2/__init__.pyi` file into the cv2 module within the virtualenv.

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