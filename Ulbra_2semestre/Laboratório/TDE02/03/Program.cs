class Program
{
    static void Main()
    {
        string nome = "Paulo";
        int idade = 17;
        double nota = 7.5;

        string saidaConcatenacao = "Aluno " + nome + " tem " + idade + " anos e nota " + nota + ".";

        string saidaInterpolacao = $"Aluno {nome} tem {idade} anos e nota {nota}.";

        Console.WriteLine(saidaConcatenacao);
        Console.WriteLine(saidaInterpolacao);
    }
}
