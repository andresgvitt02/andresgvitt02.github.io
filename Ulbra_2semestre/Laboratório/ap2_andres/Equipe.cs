public class Equipe
{
    public string NomeEquipe;
    public Jogador[] Jogadores = new Jogador[5];
    public int jogadorCt = 0;

    public Equipe(string nomeEquipe)
    {
        NomeEquipe = nomeEquipe;
    }

    // Método  para contar os pontos de cada equipe \\
    public int PontosTotal()
        {
            int totalPontos = 0;
            foreach (var jogador in Jogadores)
            {
                totalPontos += jogador.Pontos;
            }
            return totalPontos;
        }

    // Método  para contar a quantidade de jogadores não nulos na equipe \\
    public int QuantidadeJogadoresNaoNulos() 
    {
        int quantidadeNaoNulos = 0;
        for (int i = 0; i < jogadorCt; i++)
        {
            if (Jogadores[i] != null)
            {
                quantidadeNaoNulos++;
            }
        }
        return quantidadeNaoNulos;
    }

    // Método para adicionar um jogador à equipe.
    public void AdicionarJogador(Jogador jogador) 
{
    if (jogadorCt < 5)
    {
        Jogadores[jogadorCt] = jogador;
        jogadorCt++;
        Console.WriteLine($"Jogador {jogador.Nome} adicionado à equipe {NomeEquipe}.");
    }
    else
    {
        Console.WriteLine("A equipe já possui 5 jogadores. Não é possível adicionar mais.");
    }
}
}