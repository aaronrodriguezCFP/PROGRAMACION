package app;

import dao.PeliculaDAO;
import modelo.Pelicula;

import java.util.Scanner;

public class Menu {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\n1 - Ver películas");
            System.out.println("2 - Salir");
            System.out.print("Elige una opción: ");
            opcion = sc.nextInt();

            switch (opcion) {
                case 1 -> {
                    for (Pelicula p : PeliculaDAO.obtenerPeliculas()) {
                        System.out.printf("%-5s %-30s %-20s %-10d %-10s %-15s%n",
                                p.getId(), p.getTitulo(), p.getDirector(), p.getDuracion(),
                                p.getClasificacion(), p.getGenero());
                    }
                }
                case 2 -> System.out.println("Hasta luego.");
                default -> System.out.println("Opción no válida.");
            }
        } while (opcion != 2);

        sc.close();
    }
}
