import com.akihabara.market.dao.DatabaseConnection;

import java.sql.Connection;

/**
 * Clase Main temporal para probar que DatabaseConnection establece correctamente la conexión.
 * Una vez verificado, este código puede eliminarse o comentarse.
 */
public class Main {

    public static void main(String[] args) {
        DatabaseConnection dbConn = new DatabaseConnection();

        // Obtener la conexión y verificar que no sea null
        Connection conexion = dbConn.getConexion();

        if (conexion != null) {
            System.out.println("¡Conexión válida! Podemos ejecutar consultas.");
        } else {
            System.err.println("La conexión es null. Algo falló al intentar conectarse.");
        }

        // Finalmente, cerramos la conexión (buenas prácticas)
        dbConn.cerrarConexion();
    }
}
