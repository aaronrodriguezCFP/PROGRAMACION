import com.akihabara.market.model.ProductoOtaku;

/**
 * Clase temporal para probar que ProductoOtaku funciona correctamente.
 * Luego se eliminará o se moverá cuando ya no sea necesario.
 */
public class Main {
    public static void main(String[] args) {
        // Crear un objeto de prueba usando el constructor completo
        ProductoOtaku producto = new ProductoOtaku(
            1,
            "Figura de Anya Forger",
            "Figura",
            59.95,
            8
        );

        // Mostrar en consola usando toString()
        System.out.println(producto);
    }
}
