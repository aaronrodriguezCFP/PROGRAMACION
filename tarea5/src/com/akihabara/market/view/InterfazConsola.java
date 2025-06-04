package com.akihabara.market.view;

import com.akihabara.market.model.ProductoOtaku;

import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

/**
 * InterfazConsola se encarga de TODA la interacción con el usuario
 * (mostrar menús, leer opciones, pedir datos de productos, mostrar listas, etc.).
 * Nunca debe contener lógica de negocio ni acceso directo a la base de datos.
 */
public class InterfazConsola {

    private Scanner scanner;

    public InterfazConsola() {
        scanner = new Scanner(System.in);
    }

    /**
     * Muestra el menú principal y retorna la opción elegida por el usuario.
     * Continúa solicitando hasta que se ingrese un número válido entre 1 y 8.
     */
    public int mostrarMenuYLeerOpcion() {
        int opcion = -1;
        do {
            System.out.println("\n===== AKIHABARA MARKET =====");
            System.out.println("1) Añadir producto");
            System.out.println("2) Consultar producto por ID");
            System.out.println("3) Listar todos los productos");
            System.out.println("4) Listar productos por nombre");
            System.out.println("5) Listar productos por categoría");
            System.out.println("6) Actualizar producto");
            System.out.println("7) Eliminar producto");
            System.out.println("8) Salir");
            System.out.print("Selecciona una opción (1-8): ");
            try {
                opcion = Integer.parseInt(scanner.nextLine().trim());
                if (opcion < 1 || opcion > 8) {
                    System.out.println("→ Opción inválida. Debe ser un número entre 1 y 8.");
                    opcion = -1;
                }
            } catch (NumberFormatException e) {
                System.out.println("→ Entrada inválida. Ingresa un número entre 1 y 8.");
            }
        } while (opcion == -1);
        return opcion;
    }

    /**
     * Pide al usuario los datos necesarios para crear o actualizar un producto.
     * No pide ID, puesto que en INSERT no existe, y en UPDATE se asume que ya se conoce.
     * @return ProductoOtaku con nombre, categoría, precio y stock (id = 0 provisional).
     */
    public ProductoOtaku pedirDatosProducto() {
        ProductoOtaku p = new ProductoOtaku();
        System.out.print("Nombre: ");
        p.setNombre(scanner.nextLine().trim());

        System.out.print("Categoría: ");
        p.setCategoria(scanner.nextLine().trim());

        // Leer precio
        while (true) {
            System.out.print("Precio: ");
            String entradaPrecio = scanner.nextLine().trim();
            try {
                double precio = Double.parseDouble(entradaPrecio);
                if (precio < 0) {
                    System.out.println("→ El precio no puede ser negativo.");
                    continue;
                }
                p.setPrecio(precio);
                break;
            } catch (NumberFormatException e) {
                System.out.println("→ Entrada inválida. Ingresa un número decimal válido para el precio.");
            }
        }

        // Leer stock
        while (true) {
            System.out.print("Stock: ");
            String entradaStock = scanner.nextLine().trim();
            try {
                int stock = Integer.parseInt(entradaStock);
                if (stock < 0) {
                    System.out.println("→ El stock no puede ser negativo.");
                    continue;
                }
                p.setStock(stock);
                break;
            } catch (NumberFormatException e) {
                System.out.println("→ Entrada inválida. Ingresa un número entero válido para el stock.");
            }
        }

        return p;
    }

    /**
     * Pide al usuario un ID de producto y lo retorna. Valida que sea un entero positivo.
     * @param mensaje Texto a mostrar como indicación (por ejemplo: "Ingresa el ID:").
     * @return int ID válido (> 0).
     */
    public int pedirId(String mensaje) {
        int id = -1;
        do {
            System.out.print(mensaje + " ");
            try {
                id = Integer.parseInt(scanner.nextLine().trim());
                if (id <= 0) {
                    System.out.println("→ El ID debe ser un número entero positivo.");
                    id = -1;
                }
            } catch (NumberFormatException e) {
                System.out.println("→ Entrada inválida. Debes ingresar un número entero.");
            }
        } while (id == -1);
        return id;
    }

    /**
     * Pide al usuario una cadena de texto (por ejemplo, nombre parcial o categoría).
     * @param mensaje Texto a mostrar como indicación.
     * @return String ingresado (sin espacios al inicio o final).
     */
    public String pedirCadena(String mensaje) {
        System.out.print(mensaje + " ");
        return scanner.nextLine().trim();
    }

    /**
     * Muestra la información de un producto. Si es null, informa que no existe.
     * @param p ProductoOtaku a mostrar.
     */
    public void mostrarProducto(ProductoOtaku p) {
        if (p == null) {
            System.out.println("→ Producto no encontrado.");
        } else {
            System.out.println(p);
        }
    }

    /**
     * Muestra una lista de productos. Si está vacía, informa que no hay resultados.
     * @param lista Lista de ProductoOtaku.
     */
    public void mostrarListaProductos(List<ProductoOtaku> lista) {
        if (lista == null || lista.isEmpty()) {
            System.out.println("→ No se encontraron productos.");
        } else {
            System.out.println("\n--- Resultados ---");
            for (ProductoOtaku p : lista) {
                System.out.println(p);
            }
        }
    }

    /**
     * Muestra un mensaje genérico en consola.
     * @param texto Texto a imprimir.
     */
    public void mostrarMensaje(String texto) {
        System.out.println(texto);
    }
}
