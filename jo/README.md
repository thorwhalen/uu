# jo

Automatically making flask webservices from python objects

To install:	```pip install jo```

Note: You can find more modern and flexible version of `jo` in these packages: `py2http` and `qh`.


# Examples

## ObjWrapper

A class to wrap a "controller" class for a web service API.
It takes care of LRU caching objects constructed before (so they don't need to be re-constructed for every
API call), and converting request.json and request.args arguments to the types that will be recognized by
the method calls.

```
:param obj_constructor: a function that, given some arguments, constructs an object. It is this object
    that will be wrapped for the webservice
:param obj_constructor_arg_names:
:param convert_arg: (processing) a dict keyed by variable names (str) and valued by a dict containing a
    'type': a function (typically int, float, bool, and list) that will convert the value of the variable
        to make it web service compliant
    'default': A value to assign to the variable if it's missing.
:param The pattern that determines what attributes are allowed to be accessed. Note that patterns must be
    complete patterns (i.e. describing the whole attribute path, not just a subset. For example, if you want
    to have access to this.given.thing you, specifying r"this\.given" won't be enough. You need to specify
    "this\.given.thing" or "this\.given\..*" (the latter giving access to all children of this.given.).
    Allowed formats:
        a re.compiled pattern
        a string (that will be passed on to re.compile()
        a dict with either
            an "exclude", pointing to a list of patterns to exclude
            an "include", pointing to a list of patterns to include
:param to_jdict: (input processing) Function to convert an output to a jsonizable dict
```