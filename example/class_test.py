# coding=utf-8
"""
    create by pymu
    on 2020/12/30
    at 17:35
"""


class Parent:
    a = 1

    def say(self, name):
        print(2)

    def do(self):
        self.say("22")


class Son(Parent):

    def say(self, name):
        print(1)


if __name__ == '__main__':
    parent = Parent()
    son = Son()
    for i in son.__dir__():
        setattr(parent, i, getattr(son, i))
    print(parent.do())
