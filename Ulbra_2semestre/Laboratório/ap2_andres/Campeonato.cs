public class Campeonato
{
    public string NomeCampeonato;
    public Equipe[] EquipesParticipantes = new Equipe[10]; // Suporta até 10 equipes \\
    private int equipeCount = 0; // Inicia o número de jogadores da equipe em 0 \\

    public Campeonato(string nomeCampeonato)
    {
        NomeCampeonato = nomeCampeonato;
    }

    // Adicionar equipes e a quantidade limitada de jogadores nelas \\
    public void AdicionarEquipe(Equipe equipe) 
    {
        if (equipeCount < 10)
        {
            EquipesParticipantes[equipeCount] = equipe;
            equipeCount++; // Incremento \\
        }
        else
        {
            Console.WriteLine("O campeonato já atingiu o limite de equipes participantes.");
        }
    }

    // Iniciar a partida \\
    public void IniciarPartida(Equipe e1, Equipe e2)
    {
        if (e1 != null && e2 != null)
        {
            int jogadoresNaoNulosEquipe1 = e1.QuantidadeJogadoresNaoNulos();
            int jogadoresNaoNulosEquipe2 = e2.QuantidadeJogadoresNaoNulos();

            if (jogadoresNaoNulosEquipe1 == 5 && jogadoresNaoNulosEquipe2 == 5)
            {
               

                Console.WriteLine($"Inicia a partida entre {e1.NomeEquipe} e {e2.NomeEquipe}.");

                
                Console.WriteLine("\n");

                // Foreach para verificar se a variável (jogador) de cada equipe não é nula \\
                foreach (var jogador in e1.Jogadores) 
                {
                    if (jogador != null)
                    {
                        jogador.Jogar();
                    }
                }

                foreach (var jogador in e2.Jogadores)
                {
                    if (jogador != null)   
                    {
                        jogador.Jogar();
                    }
                }
              
            }
            else
            {
                Console.WriteLine("As duas equipes devem ter 5 jogadores!");
            }
        }
        else
        {
            Console.WriteLine("Uma das equipes não está completa, não é possível iniciar a partida!");
        }
    }

    // Exibir a tabela de classificação do campeonato \\
    public void Classificacao() 
    {   
        // Loop para para percorrer cada equipe \\
        for (int i = 0; i < equipeCount; i++)
        {
            // Método para verificar a pontuação de cada equipe. 
            // e assim determinar a classificação em ordem decrescente
            for (int j = i + 1; j < equipeCount; j++)
            {
                if (EquipesParticipantes[j].PontosTotal() > EquipesParticipantes[i].PontosTotal())
                {
                    Equipe temp = EquipesParticipantes[i];
                    EquipesParticipantes[i] = EquipesParticipantes[j];
                    EquipesParticipantes[j] = temp;
                }
            }
        }

        Console.WriteLine("Classificação:");
        
        for (int i = 0; i < equipeCount; i++)
        {
            Console.WriteLine($"{i + 1}. {EquipesParticipantes[i].NomeEquipe} - Pontos: {EquipesParticipantes[i].PontosTotal()}");
        }
    }
}