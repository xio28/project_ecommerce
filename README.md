<div align="center">
    <h1>Kangaroo</h1>
    <h6>Proyecto E-commerce</h6>
</div>
<hr>

**Kangaroo** es un comercio de distribución de productos para animales basado en el modelo de e-commerce *(comercio online)*. Para el correcto funcionamiento del comercio se ha decidido implementar un sistema de información que almacene los siguientes datos:

* El propio **e-commerce** deberá guardar:
    * NIF
    * Nombre del comercio (Kangaroo)
    * Dirección (diccionario)
    * Productos en venta (diccionario)

* Datos del **cliente** que se registra en la plataforma:
    * Nombre de usuario
    * Contraseña
    * Email
    * Nombre y apellidos
    * DNI
    * Direccion (diccionario)
    * Teléfono de contacto
    * Mascotas (diccionario)
    * Métodos de pago guardados (diccionario)
    * Si el cliente ha sido recomendado


* Datos de el **proveedor** que suministra el producto:
    * NIF
    * Nombre / Empresa
    * Dirección (diccionario)
    * Contacto

* Información del **producto** de venta:
    * Proveedor
    * Stock
    * Precio de venta
    * Categoria
    * Reseñas

* Información del **pedido**:
    * ID (autoincrementado)
    * Pedido (diccionario con los datos del propio pedido)

* Generar un nuevo **método de pago**:
    * Codigo de transaccion
    * Datos del cliente
    * Importe_total

    * Tipo de pago:
        * Bizum
        * Paypal
        * Tarjeta:
            * Número tarjeta
            * Nombre
            * Fecha de caducidad
            * CVV

<hr>
<h6 align="center">IES ANA LUISA BENITEZ - DAW 2021-2022 (ETS / PRO)</h6>
