# pypack

## An alternative to pip (uses pip but has more features) to install packages.

It stores the package names of the packages that you want to install in a text file called 'requirements.txt', so that if you are migrating to another machine it becomes easier for you to install all the modules that you had previously installed in the older machine.
You just need to carry the 'requirements.txt' file.

**Installing packages one by one:**
```
pypack <packagename>
```

**For Example:**
```
pypack pandas
pypack idleTime==0.5.0.2
```


**Installing packages from requirement.txt:**
```
pypack -r requirements.txt
```
