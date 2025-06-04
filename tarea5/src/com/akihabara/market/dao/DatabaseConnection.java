package com.akihabara.market.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnection {

    // 1. Variables constantes para datos de conexión
    private static final String DB_URL = "jdbc:mysql://localhost:3306/akihabara_db?useSSL=false&serverTimezone=UTC";
    private static final String USER = "userAkihabara";
    private static final String PASSWORD = "Akihabara2025!";

    // 2. Propiedad de conexión
    private Connection conexion;

    /**
     * 3. Constructor
     * Carga el driver de MySQL y establece la conexión con la base de datos.
     * Muestra mensajes en consola informando del estado y captura posibles excepciones.
     */
    public DatabaseConnection() {
        try {
            // Cargar el driver de MySQL en memoria
            Class.forName("com.mysql.cj.jdbc.Driver");
            System.out.println("Se ha cargado en memoria el driver de MySQL.");

            // Establecer la conexión utilizando los datos definidos en las constantes
            conexion = DriverManager.getConnection(DB_URL, USER, PASSWORD);
            System.out.println("Se ha establecido con éxito la conexión a la base de datos.");

        } catch (ClassNotFoundException e) {
            // Ocurre si el driver de MySQL no está en el classpath
            System.err.println("ERROR: No se encontró el driver de MySQL. " +
                               "Revisa que tengas el conector JDBC en el classpath.");
            System.err.println("Detalle de error: " + e.getMessage());
        } catch (SQLException e) {
            // Ocurre si hay problemas al conectar con la base de datos (credenciales, URL, etc.)
            System.err.println("ERROR: No se pudo conectar a la base de datos. " +
                               "Revisa la URL, usuario y contraseña.");
            System.err.println("SQLState: " + e.getSQLState());
            System.err.println("Error code: " + e.getErrorCode());
            System.err.println("Detalle de error: " + e.getMessage());
        }
    }

    /**
     * 4. getConexion()
     * Retorna la instancia de Connection que corresponde a la conexión abierta.
     * @return Connection (puede ser null si ocurrió un error al conectar)
     */
    public Connection getConexion() {
        return conexion;
    }

    /**
     * 4. cerrarConexion()
     * Cierra la conexión si está activa y muestra un mensaje de resultado.
     */
    public void cerrarConexion() {
        if (conexion != null) {
            try {
                if (!conexion.isClosed()) {
                    conexion.close();
                    System.out.println("Se ha cerrado la conexión con la base de datos.");
                }
            } catch (SQLException e) {
                System.err.println("ERROR: No se pudo cerrar la conexión con la base de datos.");
                System.err.println("SQLState: " + e.getSQLState());
                System.err.println("Error code: " + e.getErrorCode());
                System.err.println("Detalle de error: " + e.getMessage());
            }
        } else {
            System.out.println("La conexión ya era null o no estaba activa.");
        }
    }
}
