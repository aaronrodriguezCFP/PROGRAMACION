package com.akihabara.market.dao;

import com.akihabara.market.model.ProductoOtaku;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

/**
 * Versión simplificada de ProductoDAO, con métodos CRUD y búsquedas.
 * Utiliza try‐with‐resources para cerrar automáticamente Statement y ResultSet.
 */
public class ProductoDAO {

    private Connection conexion;

    public ProductoDAO() {
        // Obtener la conexión (se asume que DatabaseConnection ya está correctamente implementada)
        this.conexion = new DatabaseConnection().getConexion();
    }

    /**
     * Inserta un nuevo producto en la base de datos.
     * @param producto Objeto ProductoOtaku sin id. Tras la inserción, se actualiza producto.id.
     * @throws SQLException si ocurre un error en la operación.
     */
    public void agregarProducto(ProductoOtaku producto) throws SQLException {
        String sql = "INSERT INTO producto (nombre, categoria, precio, stock) VALUES (?, ?, ?, ?)";
        try (PreparedStatement ps = conexion.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {
            ps.setString(1, producto.getNombre());
            ps.setString(2, producto.getCategoria());
            ps.setDouble(3, producto.getPrecio());
            ps.setInt(4, producto.getStock());
            ps.executeUpdate();

            try (ResultSet rs = ps.getGeneratedKeys()) {
                if (rs.next()) {
                    producto.setId(rs.getInt(1));
                }
            }
        }
    }

    /**
     * Obtiene un producto a partir de su ID.
     * @param id Identificador del producto.
     * @return ProductoOtaku si existe, o null si no se encuentra.
     * @throws SQLException si ocurre un error en la operación.
     */
    public ProductoOtaku obtenerProductoPorId(int id) throws SQLException {
        String sql = "SELECT * FROM producto WHERE id = ?";
        try (PreparedStatement ps = conexion.prepareStatement(sql)) {
            ps.setInt(1, id);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    return new ProductoOtaku(
                        rs.getInt("id"),
                        rs.getString("nombre"),
                        rs.getString("categoria"),
                        rs.getDouble("precio"),
                        rs.getInt("stock")
                    );
                }
            }
        }
        return null;
    }

    /**
     * Recupera todos los productos de la tabla.
     * @return Lista (posiblemente vacía) de todos los productos.
     * @throws SQLException si ocurre un error en la operación.
     */
    public List<ProductoOtaku> obtenerTodosLosProductos() throws SQLException {
        String sql = "SELECT * FROM producto";
        List<ProductoOtaku> lista = new ArrayList<>();

        try (PreparedStatement ps = conexion.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                lista.add(new ProductoOtaku(
                    rs.getInt("id"),
                    rs.getString("nombre"),
                    rs.getString("categoria"),
                    rs.getDouble("precio"),
                    rs.getInt("stock")
                ));
            }
        }

        return lista;
    }

    /**
     * Actualiza un producto existente.
     * @param producto ProductoOtaku con id y nuevos valores.
     * @return true si se modificó al menos una fila, false en caso contrario.
     * @throws SQLException si ocurre un error en la operación.
     */
    public boolean actualizarProducto(ProductoOtaku producto) throws SQLException {
        String sql = "UPDATE producto SET nombre = ?, categoria = ?, precio = ?, stock = ? WHERE id = ?";
        try (PreparedStatement ps = conexion.prepareStatement(sql)) {
            ps.setString(1, producto.getNombre());
            ps.setString(2, producto.getCategoria());
            ps.setDouble(3, producto.getPrecio());
            ps.setInt(4, producto.getStock());
            ps.setInt(5, producto.getId());
            return ps.executeUpdate() > 0;
        }
    }

    /**
     * Elimina un producto por su ID.
     * @param id Identificador del producto a borrar.
     * @return true si se eliminó al menos una fila, false en caso contrario.
     * @throws SQLException si ocurre un error en la operación.
     */
    public boolean eliminarProducto(int id) throws SQLException {
        String sql = "DELETE FROM producto WHERE id = ?";
        try (PreparedStatement ps = conexion.prepareStatement(sql)) {
            ps.setInt(1, id);
            return ps.executeUpdate() > 0;
        }
    }

    /**
     * Busca productos cuyo nombre contenga la cadena indicada (LIKE %nombre%).
     * @param nombre Subcadena a buscar.
     * @return Lista de coincidencias (vacía si no hay ninguna).
     * @throws SQLException si ocurre un error en la operación.
     */
    public List<ProductoOtaku> buscarProductosPorNombre(String nombre) throws SQLException {
        String sql = "SELECT * FROM producto WHERE nombre LIKE ?";
        List<ProductoOtaku> lista = new ArrayList<>();

        try (PreparedStatement ps = conexion.prepareStatement(sql)) {
            ps.setString(1, "%" + nombre + "%");
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    lista.add(new ProductoOtaku(
                        rs.getInt("id"),
                        rs.getString("nombre"),
                        rs.getString("categoria"),
                        rs.getDouble("precio"),
                        rs.getInt("stock")
                    ));
                }
            }
        }

        return lista;
    }

    /**
     * Busca productos que pertenezcan exactamente a la categoría indicada.
     * @param categoria Categoría a buscar (ej.: "Figura", "Manga", etc.).
     * @return Lista de productos en esa categoría (vacía si no hay coincidencias).
     * @throws SQLException si ocurre un error en la operación.
     */
    public List<ProductoOtaku> buscarProductoPorCategoria(String categoria) throws SQLException {
        String sql = "SELECT * FROM producto WHERE categoria = ?";
        List<ProductoOtaku> lista = new ArrayList<>();

        try (PreparedStatement ps = conexion.prepareStatement(sql)) {
            ps.setString(1, categoria);
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    lista.add(new ProductoOtaku(
                        rs.getInt("id"),
                        rs.getString("nombre"),
                        rs.getString("categoria"),
                        rs.getDouble("precio"),
                        rs.getInt("stock")
                    ));
                }
            }
        }

        return lista;
    }
}
