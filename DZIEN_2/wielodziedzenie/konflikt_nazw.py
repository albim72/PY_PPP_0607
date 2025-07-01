class A:
    def hello(self):
        print("Hello from A")   
        
class B:
    def hello(self):
        print("Hello from B")   
        
class C(A, B):
    pass
