package modelo;

public class Pelicula {
    private String id, titulo, director, clasificacion, genero;
    private int duracion;

    public Pelicula(String id, String titulo, String director, int duracion, String clasificacion, String genero) {
        this.id = id;
        this.titulo = titulo;
        this.director = director;
        this.duracion = duracion;
        this.clasificacion = clasificacion;
        this.genero = genero;
    }

    public String getId() { return id; }
    public String getTitulo() { return titulo; }
    public String getDirector() { return director; }
    public int getDuracion() { return duracion; }
    public String getClasificacion() { return clasificacion; }
    public String getGenero() { return genero; }
}
