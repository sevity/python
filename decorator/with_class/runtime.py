# runtime type
# in this type of decorator.. the decorator(param_wrap function) will be called every time decorated method is called.
def add_tag(tag_name):
    print '111'  # come here while file loading

    def func_wrap(func):  # method name here
        print '222'  # also come here while file loading

        def param_wrap(self, name):  # method param here
            print '333'  # come here after f.show() is called !!!
            return "<{0}><{1}><{0}>".format(tag_name, func(self, name))
        return param_wrap
    return func_wrap


class Foo(object):
    @add_tag('div')
    def get_name(self, name):
        print '444'
        return name

    @add_tag('p')
    def get_title(self, name):
        print '444'
        return name


f = Foo()
# the decorator(param_wrap function) will be called by below lines
print f.get_name('lino')
print f.get_title('sevity')
