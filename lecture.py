## EJERCICIOS PRACTICOS DE OPERADORES LOGICOS:

# 1.- Verificación de edad para una película:Supongamos que estás escribiendo un programa para un cine y 
# necesitas verificar si un espectador tiene la edad suficiente para ver una película con clasificación para mayores de 12 años.

edad = 14
tiene_permiso = True  # Suponemos que el espectador tiene permiso de sus padres

puede_ver_pelicula = edad >= 12 or tiene_permiso

if puede_ver_pelicula:
    print("El espectador puede ver la película.")
else:
    print("Lo siento, el espectador no tiene la edad suficiente para ver la película.")
    
# 2.- Validación de disponibilidad de productos:Imagina que estás desarrollando un sistema de compras en línea y necesitas verificar
# si un producto está disponible y en stock para su compra.

producto_disponible = True
en_stock = False

puede_comprar = producto_disponible and en_stock

if puede_comprar:
    print("El producto está disponible y en stock.")
else:
    print("Lo siento, el producto no está disponible para su compra en este momento.")
    
# 3.- Verificación de crédito para una transacción:Supongamos que estás escribiendo un sistema de procesamiento de pagos y necesitas
# verificar si un cliente tiene suficiente crédito para realizar una transacción.

credito_disponible = 1000
monto_transaccion = 800

puede_realizar_transaccion = credito_disponible >= monto_transaccion

if puede_realizar_transaccion:
    print("La transacción puede ser realizada.")
else:
    print("Lo siento, el cliente no tiene suficiente crédito para realizar la transacción.")
    
# 4.- Control de acceso a una zona restringida:Imagina que estás desarrollando un sistema de seguridad y necesitas verificar si un 
# usuario tiene acceso a una zona restringida basada en su nivel de seguridad.

nivel_seguridad_usuario = 5
nivel_seguridad_restringido = 7

tiene_acceso = nivel_seguridad_usuario >= nivel_seguridad_restringido

if tiene_acceso:
    print("El usuario tiene acceso a la zona restringida.")
else:
    print("Lo siento, el usuario no tiene acceso a la zona restringida.")
    
# 5.- Selección de una oferta promocional:Supongamos que estás creando un programa para seleccionar una oferta promocional para un
# cliente basado en su historial de compras y la cantidad gastada.

historial_compras = ["producto1", "producto2", "producto3"]
cantidad_gastada = 500

tiene_oferta_promocional = "producto1" in historial_compras or cantidad_gastada >= 500

if tiene_oferta_promocional:
    print("El cliente es elegible para una oferta promocional.")
else:
    print("El cliente no es elegible para una oferta promocional en este momento.")