Livro l1 = new();

l1.titulo = "Dora Aventureira";
l1.autor = "Osmas Loss";
l1.disponibilidade = true;

Livro l2 = new();

l2.titulo = "Orgulho e preconceito";
l2.autor = "Jane Foster";
l2.disponibilidade = true;

Livro l3 = new();

l3.titulo = "Akinator";
l3.autor = "Neres da Silva";
l3.disponibilidade = false;

Biblioteca b1 = new();

b1.nome = "Livraria of course";
b1.AdicionarLivro(l1);
b1.AdicionarLivro(l2);
b1.AdicionarLivro(l3);

Livro lResult = new Livro();
lResult = b1.BuscarPorTitulo("Akinator");

Console.WriteLine(lResult.autor);