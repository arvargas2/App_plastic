import os
# ------------- variables ---------------------
op_menu = ""          # Selección menú principal
op_producto = ""      # Selección menú productos
nombre_producto = ""  # Nombre del producto
cantidad = 0          # cantidad a comprar
op_tipo_cliente = ""  # Selección General/Socio
tipo_cliente = ""     # General/Socio
valor_producto = 0    # valor unitario
en_efectivo = "N"     # S/N-> paga o NO en efectivo
subtotal = 0          # Precio X Cantidad
monto_descuento = 0     # monto del dscto aplicado
total_pagar = 0       # Monto total a pagar
mensaje = ""          # Mensaje en el ticket

# ----------- Código Principal ----------------
while True:
    mensaje="" #---> limpiar variable
    
    os.system("cls")
    op_menu = str(input('''
    ============ APP PLASTIC ===============                      
    1. Venta de productos
    2. Ver estadísticas
    3. Salir
    \n Elija opción:  '''))

    if op_menu == "1":
        
        os.system("cls")
        print("\n ---- VENTA DE PRODUCTOS ----")
        op_producto = str(input('''
        Producto \t\t  Valor General \t Valor Socio
        1.- Tazón \t\t $ 800 \t\t $ 500
        2.- Llavero \t\t $ 500 \t\t $ 300
        3.- Polera estampada \t $ 5.000 \t $ 3.000
        \n Elija opción:     '''))

        if op_producto == "1":
            nombre_producto = "Tazón"
            op_tipo_cliente = str(input('''
            Seleccione el tipo de cliente:                                              
            (1)General \t (2)Socio   '''))

            if op_tipo_cliente == "1":
                tipo_cliente = "General"
                valor_producto = 800
            if op_tipo_cliente == "2":
                tipo_cliente = "Socio"
                valor_producto = 500

        if op_producto == "2":
            nombre_producto = "Llavero"
            op_tipo_cliente = str(input('''
            Seleccione el tipo de cliente:                                              
            (1)General \t (2)Socio   '''))

            if op_tipo_cliente == "1":
                tipo_cliente = "General"
                valor_producto = 500
            if op_tipo_cliente == "2":
                tipo_cliente = "Socio"
                valor_producto = 300

        if op_producto == "3":
            nombre_producto = "Polera estampada"
            op_tipo_cliente = str(input('''
            Seleccione el tipo de cliente:                                              
            (1)General \t (2)Socio   '''))

            if op_tipo_cliente == "1":
                tipo_cliente = "General"
                valor_producto = 5000
            if op_tipo_cliente == "2":
                tipo_cliente = "Socio"
                valor_producto = 3000

        cantidad = int(input(f'''
        Esta comprando {nombre_producto}
        a un valor ${valor_producto} c/u

        Ingrese la cantidad: '''))

        while not cantidad > 0:
            print("Error, mínimo 1 producto")
            cantidad = int(input(f'''
            Esta comprando {nombre_producto}
            a un valor ${valor_producto} c/u

            Ingrese la cantidad: '''))

        subtotal = valor_producto*cantidad

        en_efectivo = str(input(f'''
        Subtotal ${subtotal}

        Si paga en efectivo 20% dscto

        ¿Paga en efectivo?  S/N  ''')).strip().upper()

        if en_efectivo == "S":
            monto_descuento = subtotal*0.20            
            mensaje = f"Descuento pago efectivo 20% ${monto_descuento}"

        total_pagar = subtotal-monto_descuento
        #--- ticket ----
        os.system("cls")
        print(f''''
        ------- TICKET COMPRA -----
        Producto: {nombre_producto}
        Cantidad de entradas: {cantidad}	
        Tipo cliente: {tipo_cliente} Subtotal ${subtotal}
        {mensaje}
        Total pagar $ {total_pagar}  ''')
        
        os.system("pause")
