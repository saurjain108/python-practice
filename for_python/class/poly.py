class human:
    def hello(self, name="rony"):
        if name is not "rony":
            print("hello " + name)
        else:
            print("no one is available")
ob = human()
ob.hello("raunak")
ob.hello()
