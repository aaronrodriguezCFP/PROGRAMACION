import com.akihabara.market.dao.ProductoDAO;
import com.akihabara.market.dao.DatabaseConnection;
import com.akihabara.market.model.ProductoOtaku;

import java.sql.SQLException;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // 1) Comprueba que la conexión de DatabaseConnection existe
        if (new DatabaseConnection().getConexion() == null) {
            System.err.println("No hay conexión válida. Saliendo.");
            return;
        }

        // 2) Crea una instancia de ProductoDAO
        ProductoDAO dao = new ProductoDAO();

        try {
            // ---- Prueba agregarProducto ----
            ProductoOtaku nuevo = new ProductoOtaku(0, "Figura Luffy Gear 5", "Figura", 69.90, 5);
            dao.agregarProducto(nuevo);
            System.out.println("Insertado ID = " + nuevo.getId());

            // ---- Prueba obtenerProductoPorId ----
            ProductoOtaku p = dao.obtenerProductoPorId(nuevo.getId());
            System.out.println("Obtenido por ID: " + p);

            // ---- Prueba obtenerTodosLosProductos ----
            List<ProductoOtaku> todos = dao.obtenerTodosLosProductos();
            System.out.println("Todos los productos:");
            for (ProductoOtaku prod : todos) {
                System.out.println("  " + prod);
            }

            // ---- Prueba actualizarProducto ----
            p.setPrecio(74.99);
            p.setStock(3);
            boolean modif = dao.actualizarProducto(p);
            System.out.println("Actualización exitosa? " + modif);
            System.out.println("Después de UPDATE: " + dao.obtenerProductoPorId(p.getId()));

            // ---- Prueba buscarProductosPorNombre ----
            List<ProductoOtaku> buscados = dao.buscarProductosPorNombre("Luffy");
            System.out.println("Buscar por nombre 'Luffy':");
            for (ProductoOtaku prod : buscados) {
                System.out.println("  " + prod);
            }

            // ---- Prueba buscarProductoPorCategoria ----
            List<ProductoOtaku> porCat = dao.buscarProductoPorCategoria("Figura");
            System.out.println("Buscar por categoría 'Figura':");
            for (ProductoOtaku prod : porCat) {
                System.out.println("  " + prod);
            }

            // ---- Prueba eliminarProducto ----
            boolean borrado = dao.eliminarProducto(nuevo.getId());
            System.out.println("Eliminación exitosa? " + borrado);
            System.out.println("Después de DELETE, obtengo (null): " +
                               dao.obtenerProductoPorId(nuevo.getId()));

        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // Cierra la conexión global al final (puedes cerrar también dentro del DAO si lo prefieres)
            new DatabaseConnection().cerrarConexion();
        }
    }
}
