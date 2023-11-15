public class Gato : Animal
{

    public Gato(string nome, int idade) : base(nome, idade, 4)
    {
        
    }

    public override void EmitirSom()
    {
        ExibirNumeroDePatas(); 
        Console.WriteLine("O gato mia: Miau!");
    }
}