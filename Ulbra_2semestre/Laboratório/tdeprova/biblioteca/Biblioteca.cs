class Biblioteca
{
    public string nome;
    public Livro livro1;
    public Livro livro2;
    public Livro livro3;
    public void AdicionarLivro(Livro livro)
    {
        if(livro1 == null)
        {
            livro1 = livro;
        }
        else if(livro2 == null)
        {
            livro2 = livro;
        }
        else if(livro3 == null)
        {
            livro2 = livro;
        }
        else{
            Console.WriteLine("A biblioteca está cheia.");
        }
    }
    public Livro BuscarPorTitulo(string titulo)
    {
        if(titulo == livro1.titulo)
        {
            return livro1;
        }
        else if(titulo == livro2.titulo)
        {
            return livro2;
        }
        else if(titulo == livro3.titulo)
        {
            return livro3;
        }
        else{
            return null;
        }
    }
}