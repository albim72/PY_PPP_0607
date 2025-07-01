class Base:
    def __init__(self):
        print("Base init!")

class Left(Base):
    def __init__(self):
        print("Left init!")
        super().__init__()


class Right(Base):
    def __init__(self):
        print("Right init!")
        
class Child(Left, Right):
    def __init__(self):
        print("Child init!")
        Left.__init__(self)
        Right.__init__(self)
