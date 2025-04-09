package Animal;

//representa una adopción realizada en la protectora.
public class Adopcion {
    private Animal animal;
    private String nombrePersona;
    private String dni;

    public Adopcion(Animal animal, String nombrePersona, String dni) {
        this.animal = animal;
        this.nombrePersona = nombrePersona;
        this.dni = dni;
    }

    public Animal getAnimal() {
        return animal;
    }

    public String getNombrePersona() {
        return nombrePersona;
    }

    public String getDni() {
        return dni;
    }

    public void mostrarAdopcion() {
        System.out.println("Animal adoptado:");
        animal.mostrar();
        System.out.println("Adoptado por: " + nombrePersona + ", DNI: " + dni);
    }
}