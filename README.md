# pypack

## An alternative to pip (uses pip but has more features) to install packages.

It stores the package names of the packages that you want to install in a text file called 'requirements.txt', so that if you are migrating to another machine it becomes easier for you to install all the modules that you had previously installed in the older machine.
You just need to carry the 'requirements.txt' file.

**Installing pypack**

Clone the repository from git and install using setup.py.

```
python setup.py install --user
```

OR

Install from pip using:

```
pip install pypack
```


**Installing packages one by one:**
```
pypack install <packagename>
```

**For Example:**
```
pypack install pandas
pypack install idleTime==0.5.0.2
```


**Installing packages from requirement.txt:**
```
pypack install -r requirements.txt
```



**Uninstalling packages one by one:**
```
pypack uninstall <packagename>
```

**For Example:**
```
pypack uninstall pandas
pypack uninstall idleTime==0.5.0.2
```


**Uninstalling packages from requirement.txt:**
```
pypack uninstall -r requirements.txt
```
