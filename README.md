[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](http://ayanbag.github.io)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](http://ayanbag.github.io)

# SwitchCaseDev


``SwitchCaseDev`` is a command in python command which is similar to switch-case in java and python.
It is also a implementation of a simple Switch-Case in Python.

### Installation:
```
pip install SwitchCaseDev
```

## Module Interface:

**1. switch()**:

Basic Syntax:

```
switch(case_list,default_value)
```

where,
- case_list = a dictionary item , it contains the dictionary of all the case in which switch will be applied
- default_value = it is the default value which will excute if any of the given case is not applied.


**2. case()**:

Basic Syntax:

``
case(value)
``
where, value = the case the need to be applied.


### Demo:

```
import Switch_Case
exg=Switch_Case.switch(case_list={"a":2,"b":4},default_value=0)
print(exg.case("a"))
```

Output:
2
