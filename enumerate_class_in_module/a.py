import my_module
import inspect

for name, obj in inspect.getmembers(my_module):
    if inspect.isclass(obj):
        print name, obj
