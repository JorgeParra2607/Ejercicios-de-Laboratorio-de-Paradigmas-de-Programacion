class SaldoEfectivoInsuficiente(Exception):
    pass

class SaldoCuentaInsuficiente(Exception):
    pass

class CajeroAutomatico:
    def __init__(self, efectivo_total=100000):
        self.efectivo_total = efectivo_total
        self.cuentas = {
            'user1': {'saldo': 5000, 'pin': '1234'},
            'user2': {'saldo': 10000, 'pin': '5678'},
        }

    def autenticar(self, usuario, pin):
        if usuario in self.cuentas and self.cuentas[usuario]['pin'] == pin:
            self.usuario_actual = usuario
            return True
        else:
            return False

    def mostrar_saldo(self):
        return self.cuentas[self.usuario_actual]['saldo']

    def deposito(self, monto, cuenta_destino=None):
        if cuenta_destino is None:
            cuenta_destino = self.usuario_actual
        if cuenta_destino in self.cuentas:
            self.cuentas[cuenta_destino]['saldo'] += monto
        else:
            print("La cuenta destino no existe.")

    def transferencia(self, monto, cuenta_destino):
        if self.cuentas[self.usuario_actual]['saldo'] < monto:
            raise SaldoCuentaInsuficiente("Saldo insuficiente en la cuenta para realizar la transferencia.")
        if cuenta_destino in self.cuentas:
            self.cuentas[self.usuario_actual]['saldo'] -= monto
            self.cuentas[cuenta_destino]['saldo'] += monto
        else:
            print("La cuenta destino no existe.")

    def retiro(self, monto):
        if self.cuentas[self.usuario_actual]['saldo'] < monto:
            raise SaldoCuentaInsuficiente("Saldo insuficiente en la cuenta para realizar el retiro.")
        if self.efectivo_total < monto:
            raise SaldoEfectivoInsuficiente("Saldo insuficiente en el cajero para realizar el retiro.")
        self.cuentas[self.usuario_actual]['saldo'] -= monto
        self.efectivo_total -= monto

def menu_cajero():
    cajero = CajeroAutomatico()
    
    usuario = input("Ingrese su usuario: ")
    pin = input("Ingrese su PIN: ")

    if cajero.autenticar(usuario, pin):
        while True:
            print("\n--- Menú del Cajero ---")
            print("1. Mostrar saldo")
            print("2. Depósito en cuenta propia")
            print("3. Depósito en otras cuentas")
            print("4. Transferencia a otras cuentas")
            print("5. Retiro de efectivo")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                print(f"\nSaldo actual: ${cajero.mostrar_saldo()}")
            elif opcion == '2':
                monto = float(input("\nIngrese el monto a depositar: "))
                cajero.deposito(monto)
                print("Depósito realizado con éxito.")
            elif opcion == '3':
                monto = float(input("\nIngrese el monto a depositar: "))
                cuenta_destino = input("Ingrese la cuenta destino: ")
                cajero.deposito(monto, cuenta_destino)
                print("Depósito realizado con éxito.")
            elif opcion == '4':
                monto = float(input("\nIngrese el monto a transferir: "))
                cuenta_destino = input("Ingrese la cuenta destino: ")
                try:
                    cajero.transferencia(monto, cuenta_destino)
                    print("Transferencia realizada con éxito.")
                except SaldoCuentaInsuficiente as e:
                    print(e)
            elif opcion == '5':
                monto = float(input("\nIngrese el monto a retirar: "))
                try:
                    cajero.retiro(monto)
                    print("Retiro realizado con éxito.")
                except (SaldoCuentaInsuficiente, SaldoEfectivoInsuficiente) as e:
                    print(e)
            elif opcion == '6':
                print("\nGracias por usar el cajero automático. ¡Hasta luego!")
                break
            else:
                print("\nOpción no válida. Por favor, intente de nuevo.")
    else:
        print("Autenticación fallida. Usuario o PIN incorrecto.")

if __name__ == "__main__":
    menu_cajero()
