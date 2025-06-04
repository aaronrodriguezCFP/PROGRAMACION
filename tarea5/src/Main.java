import com.akihabara.market.dao.ProductoDAO;
import com.akihabara.market.dao.DatabaseConnection;
import com.akihabara.market.model.ProductoOtaku;
import com.akihabara.market.view.InterfazConsola;

import java.sql.SQLException;
import java.util.List;

/**
 * Main actúa como Controlador: maneja el flujo de la aplicación,
 * recibe la opción desde la Vista (InterfazConsola), llama al DAO
 * para acceder al modelo y luego devuelve resultados a la Vista.
 */
public class Main {

    public static void main(String[] args) {
        // 1) Verificar la conexión básica (opcional, DatabaseConnection lo indica por consola)
        DatabaseConnection db = new DatabaseConnection();
        if (db.getConexion() == null) {
            System.err.println("No se pudo establecer la conexión. Saliendo.");
            return;
        }

        // 2) Instanciar Vista y DAO
        InterfazConsola vista = new InterfazConsola();
        ProductoDAO dao = new ProductoDAO();

        boolean salir = false;
        while (!salir) {
            int opcion = vista.mostrarMenuYLeerOpcion();
            switch (opcion) {
                case 1:
                    // Añadir producto
                    try {
                        ProductoOtaku nuevo = vista.pedirDatosProducto();
                        dao.agregarProducto(nuevo);
                        vista.mostrarMensaje("→ Producto agregado con ID = " + nuevo.getId());
                    } catch (SQLException e) {
                        vista.mostrarMensaje("ERROR al agregar producto: " + e.getMessage());
                    }
                    break;

                case 2:
                    // Consultar producto por ID
                    try {
                        int idBuscar = vista.pedirId("Ingresa el ID del producto a consultar:");
                        ProductoOtaku encontrado = dao.obtenerProductoPorId(idBuscar);
                        vista.mostrarProducto(encontrado);
                    } catch (SQLException e) {
                        vista.mostrarMensaje("ERROR al consultar producto: " + e.getMessage());
                    }
                    break;

                case 3:
                    // Listar todos los productos
                    try {
                        List<ProductoOtaku> todos = dao.obtenerTodosLosProductos();
                        vista.mostrarListaProductos(todos);
                    } catch (SQLException e) {
                        vista.mostrarMensaje("ERROR al listar productos: " + e.getMessage());
                    }
                    break;

                case 4:
                    // Listar productos por nombre
                    try {
                        String texto = vista.pedirCadena("Ingresa texto para buscar en el nombre:");
                        List<ProductoOtaku> encontrados = dao.buscarProductosPorNombre(texto);
                        vista.mostrarListaProductos(encontrados);
                    } catch (SQLException e) {
                        vista.mostrarMensaje("ERROR al buscar por nombre: " + e.getMessage());
                    }
                    break;

                case 5:
                    // Listar productos por categoría
                    try {
                        String categoria = vista.pedirCadena("Ingresa la categoría a buscar:");
                        List<ProductoOtaku> porCategoria = dao.buscarProductoPorCategoria(categoria);
                        vista.mostrarListaProductos(porCategoria);
                    } catch (SQLException e) {
                        vista.mostrarMensaje("ERROR al buscar por categoría: " + e.getMessage());
                    }
                    break;

                case 6:
                    // Actualizar producto
                    try {
                        int idActualizar = vista.pedirId("Ingresa el ID del producto a actualizar:");
                        // Primero comprobamos que existe
                        ProductoOtaku anterior = dao.obtenerProductoPorId(idActualizar);
                        if (anterior == null) {
                            vista.mostrarMensaje("→ No existe ningún producto con ID = " + idActualizar);
                        } else {
                            vista.mostrarMensaje("→ Datos actuales: " + anterior);
                            vista.mostrarMensaje("→ Ingresa los nuevos datos:");
                            ProductoOtaku modificado = vista.pedirDatosProducto();
                            modificado.setId(idActualizar);
                            boolean ok = dao.actualizarProducto(modificado);
                            if (ok) {
                                vista.mostrarMensaje("→ Producto actualizado correctamente.");
                            } else {
                                vista.mostrarMensaje("→ No se pudo actualizar el producto.");
                            }
                        }
                    } catch (SQLException e) {
                        vista.mostrarMensaje("ERROR al actualizar producto: " + e.getMessage());
                    }
                    break;

                case 7:
                    // Eliminar producto
                    try {
                        int idEliminar = vista.pedirId("Ingresa el ID del producto a eliminar:");
                        boolean borrado = dao.eliminarProducto(idEliminar);
                        if (borrado) {
                            vista.mostrarMensaje("→ Producto eliminado correctamente.");
                        } else {
                            vista.mostrarMensaje("→ No existe producto con ID = " + idEliminar);
                        }
                    } catch (SQLException e) {
                        vista.mostrarMensaje("ERROR al eliminar producto: " + e.getMessage());
                    }
                    break;

                case 8:
                    // Salir
                    salir = true;
                    vista.mostrarMensaje("¡Hasta luego!");
                    break;
            }
        }

        // Al salir del bucle, cerramos la conexión
        try {
            db.cerrarConexion();
        } catch (Exception e) {
            // Si fallara al cerrar, sólo lo ignoramos
        }
    }
}

