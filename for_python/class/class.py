class parent:
    def funcl1(self):
        print("this is parent")
class child(parent):
    def funcl2(self):
        print("this is child")
ob = child()
ob.funcl1()
ob.funcl2()
ob2 = parent()
ob2.funcl1()
print(help(parent))
