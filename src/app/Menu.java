package app;

import conexion.ConexionDB;

import java.sql.*;
import java.util.Scanner;

public class Menu {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\n--- MENÚ DEL CINE ---");
            System.out.println("1 - ver películas");
            System.out.println("2 - añadir película");
            System.out.println("3 - eliminar película");
            System.out.println("4 - modificar película");
            System.out.println("5 - salir");
            System.out.print("elige una opción: ");
            opcion = sc.nextInt();
            sc.nextLine();
            switch (opcion) {
                case 1 -> verPeliculas();
                case 2 -> añadirPelicula(sc);
                case 3 -> eliminarPelicula(sc);
                case 4 -> modificarPelicula(sc);
                case 5 -> System.out.println("hasta luego.");
                default -> System.out.println("opción no válida.");
            }

        } while (opcion != 5);

        sc.close();
    }

    //opción1
    public static void verPeliculas() {
        try {
            Connection con = ConexionDB.conectar();
            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery(
                "SELECT p.id_pelicula, p.titulo, p.director, p.duracion, p.clasificacion, g.nombre AS genero " +
                "FROM pelicula p JOIN genero g ON p.id_genero = g.id_genero");

            System.out.printf("%-5s %-30s %-20s %-10s %-10s %-15s%n", 
                "ID", "Título", "Director", "Duración", "Clasif.", "Género");
            System.out.println("-------------------------------------------------------------------------");

            while (rs.next()) {
                System.out.printf("%-5s %-30s %-20s %-10d %-10s %-15s%n",
                    rs.getString("id_pelicula"),
                    rs.getString("titulo"),
                    rs.getString("director"),
                    rs.getInt("duracion"),
                    rs.getString("clasificacion"),
                    rs.getString("genero"));
            }

            con.close();
        } catch (SQLException e) {
            System.out.println("error al mostrar películas");
            e.printStackTrace();
        }
    }

    // opción2
    public static void añadirPelicula(Scanner sc) {
        try {
            Connection con = ConexionDB.conectar();
            System.out.print("ID de la película: ");
            String id = sc.nextLine();

            //ver si ya existe
            PreparedStatement check = con.prepareStatement("SELECT * FROM pelicula WHERE id_pelicula = ?");
            check.setString(1, id);
            ResultSet rs = check.executeQuery();

            if (rs.next()) {
                System.out.println("ya existe una película con ese ID.");
            } else {
                System.out.print("Título: ");
                String titulo = sc.nextLine();
                System.out.print("Director: ");
                String director = sc.nextLine();
                System.out.print("Duración (minutos): ");
                int duracion = sc.nextInt(); sc.nextLine();
                System.out.print("Clasificación: ");
                String clasificacion = sc.nextLine();
                System.out.print("ID del género (ejemplo: ACC): ");
                String idGenero = sc.nextLine();

                //insertar peli
                PreparedStatement insert = con.prepareStatement("INSERT INTO pelicula VALUES (?, ?, ?, ?, ?, ?)");
                insert.setString(1, id);
                insert.setString(2, titulo);
                insert.setString(3, director);
                insert.setInt(4, duracion);
                insert.setString(5, clasificacion);
                insert.setString(6, idGenero);

                int filas = insert.executeUpdate();
                if (filas > 0) {
                    System.out.println("película añadida correctamente.");
                }
            }

            con.close();
        } catch (SQLException e) {
            System.out.println("error al añadir película");
            e.printStackTrace();
        }
    }

    //opcioón3
    public static void eliminarPelicula(Scanner sc) {
        try {
            Connection con = ConexionDB.conectar();
            System.out.print("ID de la película a eliminar: ");
            String id = sc.nextLine();

            PreparedStatement ps = con.prepareStatement("DELETE FROM pelicula WHERE id_pelicula = ?");
            ps.setString(1, id);

            int filas = ps.executeUpdate();
            if (filas > 0) {
                System.out.println("película eliminada.");
            } else {
                System.out.println("no existe ninguna película con ese ID.");
            }

            con.close();
        } catch (SQLException e) {
            System.out.println("error al eliminar película");
            e.printStackTrace();
        }
    }

    //opción4
    public static void modificarPelicula(Scanner sc) {
        try {
            Connection con = ConexionDB.conectar();
            System.out.print("ID de la película a modificar: ");
            String id = sc.nextLine();

            //ver si ya existe 
            PreparedStatement check = con.prepareStatement("SELECT * FROM pelicula WHERE id_pelicula = ?");
            check.setString(1, id);
            ResultSet rs = check.executeQuery();

            if (!rs.next()) {
                System.out.println("no existe ninguna película con ese ID.");
                return;
            }

            System.out.print("nuevo título: ");
            String nuevoTitulo = sc.nextLine();
            System.out.print("nueva clasificación: ");
            String nuevaClasificacion = sc.nextLine();

            PreparedStatement update = con.prepareStatement(
                "UPDATE pelicula SET titulo = ?, clasificacion = ? WHERE id_pelicula = ?");
            update.setString(1, nuevoTitulo);
            update.setString(2, nuevaClasificacion);
            update.setString(3, id);

            int filas = update.executeUpdate();
            if (filas > 0) {
                System.out.println("película modificada.");
            }

            con.close();
        } catch (SQLException e) {
            System.out.println("error al modificar película");
            e.printStackTrace();
        }
    }
}

