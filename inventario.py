# Sistema de Inventario - NovaTech Solutions

def main():
    print("=== SISTEMA DE INVENTARIO NOVATECH ===")

if __name__ == "__main__":
    main()

    # Sistema de Inventario - NovaTech Solutions
productos = []

def crear_producto(id_prod, nombre, precio, categoria, stock):
    producto = {"id": id_prod, "nombre": nombre, "precio": precio, "categoria": categoria, "stock": stock}
    productos.append(producto)
    return producto

def main():
    print("=== SISTEMA DE INVENTARIO NOVATECH ===")
    crear_producto(1, "Laptop", 1200.0, "Tecnologia", 10)

if __name__ == "__main__":
    main()

    # Sistema de Inventario - NovaTech Solutions
productos = []

def crear_producto(id_prod, nombre, precio, categoria, stock):
    producto = {"id": id_prod, "nombre": nombre, "precio": precio, "categoria": categoria, "stock": stock}
    productos.append(producto)
    return producto

def listar_productos():
    for p in productos:
        print(f"ID: {p['id']} | Nombre: {p['nombre']} | Precio: ${p['precio']} | Stock: {p['stock']}")

def main():
    print("=== SISTEMA DE INVENTARIO NOVATECH ===")
    crear_producto(1, "Laptop", 1200.0, "Tecnologia", 10)
    listar_productos()

if __name__ == "__main__":
    main()