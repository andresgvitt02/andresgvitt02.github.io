string nome = "Paulo";
Console.WriteLine(nome);

int idade = 17;
Console.WriteLine(idade);

double nota = 7.5;
Console.WriteLine(nota);

string saidaConcatenacao = "Aluno " + nome + " tem " + idade + " anos e nota " + nota + ".";

string saidaInterpolacao = $"Aluno {nome} tem {idade} anos e nota {nota}.";

//Console.WriteLine(saidaConcatenacao);\\
//Console.WriteLine(saidaInterpolacao);\\

Console.WriteLine("Saída usando concatenação:");
Console.WriteLine(saidaConcatenacao);

Console.WriteLine("\nSaída usando interpolação:");
Console.WriteLine(saidaInterpolacao);