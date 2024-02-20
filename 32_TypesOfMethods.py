# There are three types of methods in python 1) Instance Method, ClassMethod, StaticMethod
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

obj1 = MyClass()
print(obj1.method())
print(obj1.classmethod())
print(obj1.staticmethod())
    
"""
    The instance method takes one parameter, self, which points to an instance of MyClass
    when the method is called. 
    (but of course instance methods can accept more than just one parameter).
    Can modify both class state and object state.
    """

"""
    Class methods take a cls parameter that points to the class—and
    not the object instance—when the method is called.
    Can Only modify Class state.
    """

"""
    This type of method takes neither a self nor a cls parameter 
    (but of course it's free to accept an arbitrary number of other parameters).
    Neither modify object state nor class state. 
"""
    