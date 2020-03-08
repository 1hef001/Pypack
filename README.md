# packpy

## An alternative to pip (uses pip but has more features) to install packages.

It stores the package names of the packages that you want to install in a text file called 'requirements.txt', so that if you are migrating to another machine it becomes easier for you to install all the modules that you had previously installed in the older machine.
You just need to carry the 'requirements.txt' file.

**Installing packpy**

Clone the repository from git and install using setup.py.

```
python setup.py install --user
```

OR

Install from pip using:

```
pip install packpy
```


**Installing packages one by one:**
```
packpy install <packagename>
```

**For Example:**
```
packpy install pandas
packpy install idleTime==0.5.0.2
```


**Installing packages from requirement.txt:**
```
packpy install -r requirements.txt
```



**Uninstalling packages one by one:**
```
packpy uninstall <packagename>
```

**For Example:**
```
packpy uninstall pandas
packpy uninstall idleTime==0.5.0.2
```


**Uninstalling packages from requirement.txt:**
```
packpy uninstall -r requirements.txt
```
