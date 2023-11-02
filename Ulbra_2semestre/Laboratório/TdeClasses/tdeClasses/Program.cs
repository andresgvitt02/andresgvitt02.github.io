// Exercício 1: Classe Pessoa
// Crie uma classe Pessoa com os atributos nome, idade e cidadeNatal. Inicialize um objeto desta
// classe e exiba seus atributos no console.

Pessoa pessoa = new Pessoa();
pessoa.nome = "Andres";
pessoa.idade = 20;
pessoa.cidadeNatal = "Capão da Canoa";
Console.WriteLine($"{pessoa.nome}");
Console.WriteLine($"{pessoa.idade} anos");
Console.WriteLine($"{pessoa.cidadeNatal}");
class Pessoa{
    public string nome;
    public int idade;
    public string cidadeNatal;
}