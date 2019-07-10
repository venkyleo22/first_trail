__author__ = 'konangiv'

class Foo(object):
    @classmethod
    def class_foo(cls):
        print("class method for the class: %s" %cls)

    def obj_foo(self):
        print("obj method for object: %s" %self)

Foo.class_foo()
print(__name__)
k=Foo()
k.obj_foo()
j=Foo()
j.obj_foo()
#Foo.obj_foo()