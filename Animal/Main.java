package Animal;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Cuidadora cuidadora = new Cuidadora(); //instancia que gestiona los animales
        Scanner sc = new Scanner(System.in);   //scanner para leer datos
        int opcion;

        //menú principal en bucle
        do {
            System.out.println("\n===== MENÚ =====");
            System.out.println("1. Registrar PERRO");
            System.out.println("2. Registrar GATO");
            System.out.println("3. Buscar animal por chip");
            System.out.println("4. Mostrar todos los animales");
            System.out.println("0. Salir");
            System.out.print("Opción: ");
            opcion = sc.nextInt();
            sc.nextLine(); //limpiar el salto de línea del buffer

            switch (opcion) {
                case 1:
                    //REGISTRAR PERRO
                    System.out.print("Introduce número de chip: ");
                    String chipPerro = sc.nextLine();

                    System.out.print("Nombre: ");
                    String nombrePerro = sc.nextLine();

                    System.out.print("Edad: ");
                    int edadPerro = sc.nextInt();
                    sc.nextLine();

                    System.out.print("Raza: ");
                    String razaPerro = sc.nextLine();

                    System.out.print("¿Está adoptado? (true/false): ");
                    boolean adoptadoPerro = sc.nextBoolean();
                    sc.nextLine();

                    System.out.print("Tamaño (pequeño/mediano/grande): ");
                    String tamaño = sc.nextLine();

                    //creamos el objeto Perro y lo registramos
                    Perro nuevoPerro = new Perro(chipPerro, nombrePerro, edadPerro, razaPerro, adoptadoPerro, tamaño);
                    cuidadora.agregarAnimal(nuevoPerro);
                    break;

                case 2:
                    //REGISTRAR GATO
                    System.out.print("Introduce número de chip: ");
                    String chipGato = sc.nextLine();

                    System.out.print("Nombre: ");
                    String nombreGato = sc.nextLine();

                    System.out.print("Edad: ");
                    int edadGato = sc.nextInt();
                    sc.nextLine();

                    System.out.print("Raza: ");
                    String razaGato = sc.nextLine();

                    System.out.print("Está adoptado? (true/false): ");
                    boolean adoptadoGato = sc.nextBoolean();
                    sc.nextLine();

                    System.out.print("Test leucemia positivo? (true/false): ");
                    boolean leucemia = sc.nextBoolean();
                    sc.nextLine();

                    //creamos el objeto Gato y lo registramos
                    Gato nuevoGato = new Gato(chipGato, nombreGato, edadGato, razaGato, adoptadoGato, leucemia);
                    cuidadora.agregarAnimal(nuevoGato);
                    break;

                case 3:
                    //BUSCAR ANIMAL POR CHIP
                    System.out.print("Introduce número de chip a buscar: ");
                    String chipBusqueda = sc.nextLine();
                    cuidadora.buscarPorChip(chipBusqueda);
                    break;

                case 4:
                    //MOSTRAR TODOS LOS ANIMALES
                    cuidadora.mostrarTodos();
                    break;

                case 0:
                    //SALIR DEL PROGRAMA
                    System.out.println("Saliendo del programa.");
                    break;

                default:
                    //OPCIÓN NO VÁLIDA
                    System.out.println("Opción no válida. Inténtalo de nuevo.");
            }

        } while (opcion != 0); //el bucle se repite mientras no se de la opción de salir 

        sc.close(); //cerramos el Scanner
    }
}
