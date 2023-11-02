Produto p1 = new Produto();
p1.nome = "Chocolate";
p1.quantidade = 10;
p1.validade = DateTime.Today;

Produto p2 = new Produto();
p2.nome = "Água";
p1.quantidade = 3;
p2.validade = DateTime.Today;

Mercado mercado = new Mercado();
mercado.nome = "PoupeMais";
mercado.endereco = "av. central 223";
mercado.produto1 = p1;
mercado.produto2 = p2;
Console.WriteLine($"{mercado.nome}");
Console.WriteLine($"{mercado.endereco}");
Console.WriteLine($"{mercado.produto1.nome}");
Console.WriteLine($"{mercado.produto2.nome}");
class Produto{
    public string nome;
    public int quantidade;
    public DateTime validade;
}

class Mercado{
    public string nome;
    public string endereco;
    public Produto produto1;
    public Produto produto2;
}
