package Animal;

import java.util.HashMap;

//clase que gestiona los animales y adopciones en la protectora.
public class Cuidadora {

    //almacenar los animales con su número de chip
    private HashMap<String, Animal> animales;

    //almacenar las adopciones realizadas
    private HashMap<String, Adopcion> adopciones;

    public Cuidadora() {
        animales = new HashMap<>();   //almacenar animales
        adopciones = new HashMap<>(); //almacenar adopciones
    }

    //dar de alta animales
    public boolean agregarAnimal(Animal animal) {
        String chip = animal.getChip();
        if (animales.containsKey(chip)) {
            System.out.println("Ya existe un animal con el chip: " + chip);
            return false;
        }
        animales.put(chip, animal); 
        System.out.println("Animal registrado con chip: " + chip);
        return true;
    }

    //buscar animal por chip
    public void buscarPorChip(String chip) {
        if (animales.containsKey(chip)) {
            Animal animal = animales.get(chip); //obtiene el animal por chip
            animal.mostrar(); //mostrar() de Perro o Gato
        } else {
            System.out.println("No se encontró ningún animal con el chip: " + chip);
        }
    }

    //mostrar animales registrados
    public void mostrarTodos() {
        if (animales.isEmpty()) {
            System.out.println("No hay animales registrados.");
        } else {
            System.out.println("Animales registrados en la protectora:");
            for (Animal animal : animales.values()) {
                animal.mostrar();
            }
        }
    }

    //adopción de un animal si no está adoptado
    public void realizarAdopcion(String chip, String nombrePersona, String dni) {
        if (!animales.containsKey(chip)) {
            System.out.println("No existe ningún animal con el chip: " + chip);
            return;
        }

        Animal animal = animales.get(chip);
        if (animal.isAdoptado()) {
            System.out.println("El animal ya ha sido adoptado.");
            return;
        }

        Adopcion adopcion = new Adopcion(animal, nombrePersona, dni);
        adopciones.put(chip, adopcion);
        animal.setAdoptado(true); //marcar animal como adoptado

        System.out.println("Adopción registrada correctamente.");
    }

    //dar de baja un animal y su adopción si existe 
    public void darDeBaja(String chip) {
        if (!animales.containsKey(chip)) {
            System.out.println("No existe ningún animal con el chip: " + chip);
            return;
        }

        //eliminar adopción si existe
        if (adopciones.containsKey(chip)) {
            adopciones.remove(chip);
            System.out.println("Se ha eliminado la adopción asociada.");
        }

        animales.remove(chip);
        System.out.println("Animal con chip " + chip + " dado de baja correctamente.");
    }

    //mostrar estadísticas de gatos 
    public void mostrarEstadisticasGatos() {
        int totalGatos = 0;
        int gatosConLeucemia = 0;

        for (Animal animal : animales.values()) {
            if (animal instanceof Gato) {
                totalGatos++;
                Gato gato = (Gato) animal;
                if (gato.isTestLeucemia()) {
                    gatosConLeucemia++;
                }
            }
        }

        System.out.println("Estadísticas de gatos:");
        System.out.println("Total de gatos: " + totalGatos);
        System.out.println("Con test de leucemia positivo: " + gatosConLeucemia);
    }
}
