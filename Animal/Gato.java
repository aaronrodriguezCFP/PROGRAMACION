package Animal;

public class Gato extends Animal {
    private boolean testLeucemia;

    public Gato(String chip, String nombre, int edad, String raza, boolean adoptado, boolean testLeucemia) {
        super(chip, nombre, edad, raza, adoptado);
        this.testLeucemia = testLeucemia;
    }

    public boolean isTestLeucemia() { //añadido
        return testLeucemia;
    }

    public void mostrar() {
        System.out.println("GATO - Chip: " + chip + ", Nombre: " + nombre + ", Edad: " + edad +
                           ", Raza: " + raza + ", Adoptado: " + adoptado + ", Test Leucemia: " + testLeucemia);
    }
}
