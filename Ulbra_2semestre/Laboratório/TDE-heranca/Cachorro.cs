public class Cachorro : Animal
{
    public Cachorro(string nome, int idade) : base(nome, idade, 4)
    {
        
    }

    public override void EmitirSom()
    {
        ExibirNumeroDePatas(); 
        Console.WriteLine("O cachorro late: Au Au!");
    }
}