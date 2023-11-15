class Program
{
    static void Main()
    {
        List<Animal> listaAnimais = new List<Animal>();

        listaAnimais.Add(new Cachorro("Chico", 9));
        listaAnimais.Add(new Gato("Joaquim", 4));
        listaAnimais.Add(new Gato("Mimi", 7));
        listaAnimais.Add(new Cachorro("Thor", 3));

        foreach (Animal animal in listaAnimais)
        {
            Console.WriteLine($"Nome: {animal.Nome}, Idade: {animal.Idade}");
            animal.EmitirSom(); 
            Console.WriteLine();
        }
    }
}