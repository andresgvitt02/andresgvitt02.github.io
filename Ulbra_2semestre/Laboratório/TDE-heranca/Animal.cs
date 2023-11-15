
public class Animal
{
    public string Nome { get; set; }
    public int Idade { get; set; }

    protected int NumeroDePatas { get; set; }

    public Animal(string nome, int idade, int numeroDePatas)
    {
        Nome = nome;
        Idade = idade;
        NumeroDePatas = numeroDePatas;
    }

    public virtual void EmitirSom()
    {
        Console.WriteLine("O animal emite um som genérico.");
    }

    protected void ExibirNumeroDePatas()
    {
        Console.WriteLine($"Número de patas: {NumeroDePatas}");
    }
}