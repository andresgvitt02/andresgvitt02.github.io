string continuar;
do{
        Console.WriteLine("Digite o nome do estudante: ");
        string nome = Console.ReadLine();
        Console.WriteLine("Digite a primeira nota: ");
        double nota1 = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Digite a segunda nota: ");
        double nota2 = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Digite a terceira nota: ");
        double nota3 = Convert.ToDouble(Console.ReadLine());

        //cálculo da média 
        double media = (nota1 + nota2 + nota3)/3;

        string status;
        if(media >= 7)
        {
            status = "Aprovado!";
        }
        else
        {
            status = "Reprovado!";
        }

        //Gerar relatório
        Console.WriteLine("Nome: " + nome);
        Console.WriteLine($"Notas: {nota1}, {nota2}, {nota3}");
        Console.WriteLine("Média: " + media);
        Console.WriteLine("Status: " + status);

        //Perguntar pára continuar 
        Console.WriteLine("\nDeseja realizar um novo relatório? (s/n)");
        continuar = Console.ReadLine()?.ToLower();
    }
    while (continuar == "s");

Console.WriteLine("Obrigado por usar o gerador de relatório");
