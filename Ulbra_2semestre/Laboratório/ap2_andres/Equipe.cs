public class Equipe
{
    public string NomeEquipe;
    public Jogador[] Jogadores = new Jogador[5];
    private int jogadorCt = 0;

    public Equipe(string nomeEquipe)
    {
        NomeEquipe = nomeEquipe;
    }

    public int PontosTotal()
        {
            int totalPontos = 0;
            foreach (var jogador in Jogadores)
            {
                totalPontos += jogador.Pontos;
            }
            return totalPontos;
        }

    public int QuantidadeJogadoresNaoNulos() // Método  para contar a quantidade de jogadores não nulos na equipe.
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

    public void AdicionarJogador(Jogador jogador) // Método para adicionar um jogador à equipe.
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