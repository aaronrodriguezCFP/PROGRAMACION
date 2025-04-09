package Animal;

public abstract class Animal {
    protected String chip;
    protected String nombre;
    protected int edad;
    protected String raza;
    protected boolean adoptado;

    public Animal(String chip, String nombre, int edad, String raza, boolean adoptado) {
        this.chip = chip;
        this.nombre = nombre;
        this.edad = edad;
        this.raza = raza;
        this.adoptado = adoptado;
    }

    public String getChip() {
        return chip;
    }

    //añadido para gestionar adopciones
    public boolean isAdoptado() {
        return adoptado;
    }

    public void setAdoptado(boolean adoptado) {
        this.adoptado = adoptado;
    }

    public abstract void mostrar();
}
