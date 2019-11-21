class bank:
    def interest(self):
        return 0
class localbank(bank):
    def interest(self):
        return 10.5
ob = localbank()
print(ob.interest())
