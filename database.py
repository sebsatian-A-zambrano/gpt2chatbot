import sqlite3

def crear_base_datos():
    conn = sqlite3.connect('ventas_placas_video.db')
    cursor = conn.cursor()
    
    # Crear tablas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        ClienteID INTEGER PRIMARY KEY,
        Nombre TEXT NOT NULL,
        Apellido TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Productos (
        ProductoID INTEGER PRIMARY KEY,
        Nombre TEXT NOT NULL,
        Marca TEXT NOT NULL,
        Modelo TEXT NOT NULL,
        Precio REAL NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ventas (
        VentaID INTEGER PRIMARY KEY,
        ClienteID INTEGER,
        ProductoID INTEGER,
        Cantidad INTEGER NOT NULL,
        FechaVenta TEXT NOT NULL,
        FOREIGN KEY (ClienteID) REFERENCES Clientes (ClienteID),
        FOREIGN KEY (ProductoID) REFERENCES Productos (ProductoID)
    )
    ''')

    # Insertar datos de ejemplo en Clientes
    clientes = [
        ('Juan', 'Pérez'),
        ('María', 'Gómez'),
        ('Carlos', 'López'),
        ('Ana', 'Martínez'),
        ('Luis', 'Rodríguez'),
        ('Sofía', 'Hernández'),
        ('Miguel', 'Fernández'),
        ('Lucía', 'García')
    ]
    cursor.executemany("INSERT INTO Clientes (Nombre, Apellido) VALUES (?, ?)", clientes)

    # Insertar datos de ejemplo en Productos
    productos = [
        ('GeForce RTX 3090', 'NVIDIA', 'RTX 3090', 1499.99),
        ('Radeon RX 6900 XT', 'AMD', 'RX 6900 XT', 999.99),
        ('GeForce RTX 3080', 'NVIDIA', 'RTX 3080', 699.99),
        ('Radeon RX 6800 XT', 'AMD', 'RX 6800 XT', 649.99),
        ('GeForce RTX 3070', 'NVIDIA', 'RTX 3070', 499.99),
        ('Radeon RX 6700 XT', 'AMD', 'RX 6700 XT', 479.99)
    ]
    cursor.executemany("INSERT INTO Productos (Nombre, Marca, Modelo, Precio) VALUES (?, ?, ?, ?)", productos)

    # Insertar datos de ejemplo en Ventas
    ventas = [
        (1, 1, 1, '2023-01-15'),
        (2, 2, 2, '2023-02-20'),
        (3, 3, 1, '2023-03-10'),
        (4, 4, 3, '2023-04-05'),
        (5, 5, 2, '2023-05-12'),
        (6, 6, 1, '2023-06-18'),
        (7, 2, 4, '2023-07-22'),
        (8, 1, 5, '2023-08-30')
    ]
    cursor.executemany("INSERT INTO Ventas (ClienteID, ProductoID, Cantidad, FechaVenta) VALUES (?, ?, ?, ?)", ventas)
    
    conn.commit()
    conn.close()