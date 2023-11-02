class Program
{
        static void Main(string[] args)
        {
            // Criar o campeonato \\
            Campeonato campeonato = new Campeonato("Brasileirão");
            
            // Crias as equipes \\
            Equipe equipe1 = new Equipe("Grêmio");
            Equipe equipe2 = new Equipe("Internacional");

            Console.WriteLine("\n");

            // Criar os jogadores \\
            Jogador jogador1 = new Jogador("Jogador 1", "Luan");
            Jogador jogador2 = new Jogador("Jogador 2", "Douglas");
            Jogador jogador3 = new Jogador("Jogador 3", "Suárez");
            Jogador jogador4 = new Jogador("Jogador 4", "Renato");
            Jogador jogador5 = new Jogador("Jogador 5", "Paulo");

            Jogador jogador6 = new Jogador("Jogador 6", "Andres");
            Jogador jogador7 = new Jogador("Jogador 7", "Thor");
            Jogador jogador8 = new Jogador("Jogador 8", "Chico");
            Jogador jogador9 = new Jogador("Jogador 9", "Ederson");
            Jogador jogador10 = new Jogador("Jogador 10", "Cristiano");

            // Adicionar os jogadores as suas equipes \\
            equipe1.AdicionarJogador(jogador1);
            equipe1.AdicionarJogador(jogador2);
            equipe1.AdicionarJogador(jogador3);
            equipe1.AdicionarJogador(jogador4);
            equipe1.AdicionarJogador(jogador5);

            Console.WriteLine("\n");

            equipe2.AdicionarJogador(jogador6);
            equipe2.AdicionarJogador(jogador7);
            equipe2.AdicionarJogador(jogador8);
            equipe2.AdicionarJogador(jogador9);
            equipe2.AdicionarJogador(jogador10);

            campeonato.AdicionarEquipe(equipe1);
            campeonato.AdicionarEquipe(equipe2);

            Console.WriteLine("\n");
            
            // Iniciar a partida e mostrar a tabela de classificação \\
            campeonato.IniciarPartida(equipe1, equipe2);

            Console.WriteLine("\n");

            campeonato.Classificacao();
        }
    }

