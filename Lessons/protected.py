class BaseClass:
    def __init__(self):
        self._protected_value = 'Protected'
        self.__private_variable = 'Private'
    def _protected_method(self):
        print('Protected method')

    def __private_method(self):
        print('Private method')

    def public(self):
        self.__private_method
base = BaseClass()

# print(base._protected_value)
# base._protected_method
# base.public()
print(base.__private_variable)