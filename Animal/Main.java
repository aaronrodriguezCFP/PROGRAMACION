package Animal;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Cuidadora cuidadora = new Cuidadora();
        Scanner sc = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\n===== MENÚ =====");
            System.out.println("1. dar de alta animal");
            System.out.println("2. listar animales");
            System.out.println("3. buscar animal por chip");
            System.out.println("4. realizar adopción");
            System.out.println("5. dar de baja animal");
            System.out.println("6. mostrar estadísticas de gatos");
            System.out.println("7. salir");
            System.out.print("opción: ");
            opcion = sc.nextInt();
            sc.nextLine(); 

            switch (opcion) {
                case 1:
                    //alta de animal (perro o gato)
                    System.out.print("¿Qué tipo de animal quieres registrar? (perro/gato): ");
                    String tipo = sc.nextLine().toLowerCase();

                    System.out.print("Número de chip: ");
                    String chip = sc.nextLine();

                    System.out.print("Nombre: ");
                    String nombre = sc.nextLine();

                    System.out.print("Edad: ");
                    int edad = sc.nextInt();
                    sc.nextLine();

                    System.out.print("Raza: ");
                    String raza = sc.nextLine();

                    System.out.print("¿Está adoptado? (true/false): ");
                    boolean adoptado = sc.nextBoolean();
                    sc.nextLine();

                    if (tipo.equals("perro")) {
                        System.out.print("Tamaño (pequeño/mediano/grande): ");
                        String tamaño = sc.nextLine();
                        Perro nuevoPerro = new Perro(chip, nombre, edad, raza, adoptado, tamaño);
                        cuidadora.agregarAnimal(nuevoPerro);
                    } else if (tipo.equals("gato")) {
                        System.out.print("¿Test de leucemia positivo? (true/false): ");
                        boolean leucemia = sc.nextBoolean();
                        sc.nextLine();
                        Gato nuevoGato = new Gato(chip, nombre, edad, raza, adoptado, leucemia);
                        cuidadora.agregarAnimal(nuevoGato);
                    } else {
                        System.out.println("Tipo de animal no válido.");
                    }
                    break;

                case 2:
                    cuidadora.mostrarTodos();
                    break;

                case 3:
                    System.out.print("Introduce el chip del animal a buscar: ");
                    String chipBuscar = sc.nextLine();
                    cuidadora.buscarPorChip(chipBuscar);
                    break;

                case 4:
                    System.out.print("Introduce el chip del animal a adoptar: ");
                    String chipAdopcion = sc.nextLine();

                    System.out.print("Nombre de la persona adoptante: ");
                    String nombrePersona = sc.nextLine();

                    System.out.print("DNI del adopt1ante: ");
                    String dni = sc.nextLine();

                    cuidadora.realizarAdopcion(chipAdopcion, nombrePersona, dni);
                    break;

                case 5:
                    System.out.print("Introduce el chip del animal a dar de baja: ");
                    String chipBaja = sc.nextLine();
                    cuidadora.darDeBaja(chipBaja);
                    break;

                case 6:
                    cuidadora.mostrarEstadisticasGatos();
                    break;

                case 7:
                    System.out.println("Saliendo del programa...");
                    break;

                default:
                    System.out.println("Opción no válida. Intenta de nuevo.");
            }

        } while (opcion != 7);

        sc.close();
    }
}
