package dao;

import conexion.ConexionDB;
import modelo.Pelicula;

import java.sql.*;
import java.util.ArrayList;

public class PeliculaDAO {

    public static ArrayList<Pelicula> obtenerPeliculas() {
        ArrayList<Pelicula> lista = new ArrayList<>();

        String sql = """
            SELECT p.id_pelicula, p.titulo, p.director, p.duracion, p.clasificacion, g.nombre AS genero
            FROM pelicula p JOIN genero g ON p.id_genero = g.id_genero
        """;

        try (Connection con = ConexionDB.conectar();
             Statement stmt = con.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                Pelicula p = new Pelicula(
                    rs.getString("id_pelicula"),
                    rs.getString("titulo"),
                    rs.getString("director"),
                    rs.getInt("duracion"),
                    rs.getString("clasificacion"),
                    rs.getString("genero")
                );
                lista.add(p);
            }

        } catch (SQLException e) {
            System.out.println("error al obtener películas:");
            e.printStackTrace();
        }

        return lista;
    }
}
