
callbacks = []

def at(**kwargs):
    def decorator(func):
        a = {}
        a['time'] = kwargs.get('time')
        a['method'] = func
        callbacks.append(a)
        print("at callback {} is registered".format(a))
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

print('now calling callbacks')
for c in callbacks:
    print c
    c['method'](f, 'lino')  # be careful! I put f, instead of self


