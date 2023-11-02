class Curso
{
    public string nome;
    public string duracao;
    public string professor;

    public void ShowDetails()
    {
        Console.WriteLine($"Curso: {nome}");
        Console.WriteLine($"Duração: {duracao}");
        Console.WriteLine($"Professor: {professor}");

    }
    public void SetInformation(string nomePar, string duracaoPar, string professorPar)
    {
        nome = nomePar;
        duracao = duracaoPar;
        professor = professorPar;
    }
}
