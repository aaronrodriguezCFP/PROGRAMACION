package Animal;

import java.util.HashMap;

public class Cuidadora {

    //HashMap para almacenar los animales con su número de chip 
    private HashMap<String, Animal> animales;

    public Cuidadora() {
        animales = new HashMap<>(); //inicia la estructura de datos
    }

    //dar de alta animales
    public boolean agregarAnimal(Animal animal) {
        String chip = animal.getChip();
        if (animales.containsKey(chip)) {
            System.out.println("Ya existe un animal con el chip: " + chip);
            return false;
        }
        animales.put(chip, animal); //almacena el animal en la estructura HashMap
        System.out.println("Animal registrado con chip: " + chip);
        return true;
    }

    //buscar un animal por chip
    public void buscarPorChip(String chip) {
        if (animales.containsKey(chip)) {
            Animal animal = animales.get(chip); //obtiene el animal por chip
            animal.mostrar();  //ejecuta mostrar() de Perro o Gato
        } else {
            System.out.println("No se encontró ningún animal con el chip: " + chip);
        }
    }

    // mostrar todos los animales registrados
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
}
