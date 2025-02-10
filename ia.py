def extraer_producto(pregunta):
    productos = {
        "geforce rtx 3090": "GeForce RTX 3090",
        "radeon rx 6900 xt": "Radeon RX 6900 XT",
        "geforce rtx 3080": "GeForce RTX 3080",
        "radeon rx 6800 xt": "Radeon RX 6800 XT",
        "geforce rtx 3070": "GeForce RTX 3070",
        "radeon rx 6700 xt": "Radeon RX 6700 XT"
    }
    for producto_clave in productos:
        if producto_clave in pregunta:
            return productos[producto_clave]
    return None

def extraer_marca(pregunta):
    marcas = {
        "nvidia": "NVIDIA",
        "amd": "AMD"
    }
    for marca_clave in marcas:
        if marca_clave in pregunta:
            return marcas[marca_clave]
    return None

def extraer_cliente(pregunta):
    clientes = {
        ("juan", "pérez"): ("Juan", "Pérez"),
        ("maría", "gómez"): ("María", "Gómez"),
        ("carlos", "lópez"): ("Carlos", "López"),
        ("ana", "martínez"): ("Ana", "Martínez"),
        ("luis", "rodríguez"): ("Luis", "Rodríguez"),
        ("sofía", "hernández"): ("Sofía", "Hernández"),
        ("miguel", "fernández"): ("Miguel", "Fernández"),
        ("lucía", "garcía"): ("Lucía", "García")
    }
    for cliente_clave in clientes:
        if cliente_clave[0] in pregunta and cliente_clave[1] in pregunta:
            return clientes[cliente_clave]
    return None

def interpretar_pregunta(pregunta):
    pregunta = pregunta.lower()

    if "cuánto cuesta" in pregunta:
        producto = extraer_producto(pregunta)
        if producto:
            return '''
                SELECT Precio FROM Productos
                WHERE Nombre LIKE ?
            ''', (f"%{producto}%",)
        else:
            return "No se pudo identificar el producto.", None

    if "qué productos" in pregunta:
        marca = extraer_marca(pregunta)
        if marca:
            return '''
                SELECT Nombre, Modelo FROM Productos
                WHERE Marca LIKE ?
            ''', (f"%{marca}%",)
        else:
            return "No se pudo identificar la marca.", None

    if "cuántas unidades" in pregunta and "se vendieron" in pregunta:
        producto = extraer_producto(pregunta)
        if producto:
            return '''
                SELECT SUM(Cantidad) FROM Ventas
                JOIN Productos ON Ventas.ProductoID = Productos.ProductoID
                WHERE Productos.Nombre LIKE ?
            ''', (f"%{producto}%",)
        else:
            return "No se pudo identificar el producto.", None

    if "cuándo compró" in pregunta:
        cliente = extraer_cliente(pregunta)
        producto = extraer_producto(pregunta)
        if cliente and producto:
            nombre, apellido = cliente
            return '''
                SELECT FechaVenta FROM Ventas
                JOIN Clientes ON Ventas.ClienteID = Clientes.ClienteID
                JOIN Productos ON Ventas.ProductoID = Productos.ProductoID
                WHERE Clientes.Nombre LIKE ? AND Clientes.Apellido LIKE ?
                AND Productos.Nombre LIKE ?
            ''', (f"%{nombre}%", f"%{apellido}%", f"%{producto}%")
        else:
            return "No se pudo identificar el cliente o el producto.", None

    if "quiénes son mis clientes" in pregunta or "cuáles son mis clientes" in pregunta:
        return '''
            SELECT Nombre, Apellido FROM Clientes
        ''', None

    if "qué productos tengo" in pregunta:
        return '''
            SELECT Nombre, Marca, Modelo, Precio FROM Productos
        ''', None

    if "qué ventas tengo" in pregunta:
        return '''
            SELECT Ventas.VentaID, Clientes.Nombre, Clientes.Apellido, Productos.Nombre, Ventas.Cantidad, Ventas.FechaVenta
            FROM Ventas
            JOIN Clientes ON Ventas.ClienteID = Clientes.ClienteID
            JOIN Productos ON Ventas.ProductoID = Productos.ProductoID
        ''', None

    return "No se pudo interpretar la pregunta.", None