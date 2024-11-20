from registrar_cliente import registrar_cliente
from ver_clientes import ver_clientes
from buscar_cliente_por_email import buscar_cliente_por_email
from realizar_compra import realizar_compra
from seguimiento_pedido import seguimiento_pedido

def main():
    while True:
        print("\nGestión de Pedidos")
        print("1. Registrar cliente")
        print("2. Ver clientes")
        print("3. Buscar cliente por email")
        print("4. Realizar compra")
        print("5. Seguimiento de pedido")
        print("6. Salir")    

        opcion = input("Selecciona una opción:")
        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            ver_clientes()
        elif opcion == '3':
            buscar_cliente_por_email()
        elif opcion == '4':
            realizar_compra()
        elif opcion == '5':
            seguimiento_pedido()
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

main()