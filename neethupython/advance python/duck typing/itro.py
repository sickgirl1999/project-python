#duck typing
class Vscode:
    def compile(self):
        print("compile using vscode")
    def execute(self):
        print("execute using vs code")
    def debug(self):
        print("debug using vs code")
class Pycharm:
    def compile(self):
        print("compile using pycharm")
    def execute(self):
        print("execute by using pycharm")
    def debug(self):
        print("debug by using pycharm")
class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
        ide.debug()
p=Programmer()
ref=Pycharm()
p.coding(ref)




