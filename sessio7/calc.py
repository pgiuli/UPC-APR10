class Operacion:
    def __init__(self, num1, num2, op):
        self.num1 = num1
        self.num2 = num2
        self.op = op
        res = None

    def set_res(self, res):
        self.res = res
    
    def mostrar_resultado(self):
        print(f"{self.num1}{self.op}{self.num2}={self.res}")


class Suma(Operacion):
    def __init__(self, num1, num2, op):
        Operacion.__init__(self, num1,num2, op)
        self.set_res(num1 + num2)

class Resta(Operacion):
    def __init__(self, num1, num2, op):
        Operacion.__init__(self, num1,num2, op)
        self.set_res(num1 - num2)

class Mult(Operacion):
    def __init__(self, num1, num2, op):
        Operacion.__init__(self, num1,num2, op)
        self.set_res(num1 * num2)

class Div(Operacion):
    def __init__(self, num1, num2, op):
        Operacion.__init__(self, num1,num2, op)
        self.set_res(num1 / num2)