package conexion;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConexionDB {

    public static Connection conectar() {
        try {
            Connection miConexion = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/cine", "root", "curso");

            System.out.println("conexión establecida correctamente.");
            return miConexion;

        } catch (SQLException e) {
            System.out.println("la base de datos no conecta.");
            e.printStackTrace();
            return null;
        }
    }
}
