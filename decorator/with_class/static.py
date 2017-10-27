# callback registration type(preface way)
# in this type of decorator.. the decorator function is called only when file loading time. not method call time.

def at(**kwargs):
    def decorator(func):
        # below line is called when file loading. not method call time
        print("at decorator with param {} is called!".format(kwargs))
        return func
    return decorator

class Foo(object):
    @at(time='15:00')
    def on_train(self, name):
        print('on_train with {} is called!'.format(name))

    @at(time='17:00')
    def on_test(self, name):
        print('on_test with {} is called!'.format(name))

f = Foo()

# the decorator codes will not be called by below lines
f.on_train('lino')
f.on_test('lino')
