
class operacion():
    def __init__(self, fecha, monto, concepto, tipo):
        super().__init__()
        self.fecha = fecha
        self.monto = monto
        self.concepto = concepto
        self.tipo = tipo

ingreso = operacion("21/05/2023", 500, "Venta carro", "ingreso")

print(ingreso.fecha)