class LowerAttrMetaclass(type):
    def __new__(
            lowerattr_metaclass,
            future_class_name,
            future_class_parents,
            future_class_attr):
        # do some custom stuff here
        lowercase_attr = {}

        # change future_class_attr to lowercase_attr
        for name, val in future_class_attr.items():
            if not name.startswith("__"):
                lowercase_attr[name.lower()] = val
            else:
                lowercase_attr[name] = val
        return type(future_class_name, future_class_parents, lowercase_attr)


class A(metaclass=LowerAttrMetaclass):
    C = 10

    def ABC(self):
        return 3


uno = A()
print(uno.abc())
print(uno.ABC())
