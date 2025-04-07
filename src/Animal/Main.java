package Animal;

public class Main {
    public static void main(String[] args) {
        Cuidadora cuidadora = new Cuidadora();

        Perro perro1 = new Perro("001", "Max", 4, "Labrador", false, "grande");
        Gato gato1 = new Gato("002", "Luna", 2, "Persa", true, true);
        Perro perro2 = new Perro("003", "Rocky", 3, "Beagle", false, "mediano");
        Gato gato2 = new Gato("004", "Mishi", 1, "Siamés", false, false);

        //animal con chip duplicado
        Perro perroDuplicado = new Perro("001", "Toby", 5, "Golden", true, "grande");

        //alta
        cuidadora.agregarAnimal(perro1);
        cuidadora.agregarAnimal(gato1);
        cuidadora.agregarAnimal(perro2);
        cuidadora.agregarAnimal(gato2);
        cuidadora.agregarAnimal(perroDuplicado); //debería salir una advertencia
        System.out.println("\nLista de animales registrados:");
        cuidadora.mostrarTodos();
    }
}
