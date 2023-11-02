// Exercício 1: Soma de Números de 1 a 10
//   int soma = 0;

// for (int i = 1; i <= 10; i++)
// {
//     soma += i;
//     Console.WriteLine(soma);
// }
// return 0;

// Exercício 2: Contagem Regressiva com while
//  int contador = 10;
// while (contador >= 0) {
//         Console.WriteLine(contador);
//         contador--;
//     }
// return 0;

// Exercício 3: Pular Números Ímpares
// for (int i = 1; i <= 20; i++)
//         {
//             if (i % 2 != 0)
//             {
//                 continue;
//             }
//             Console.WriteLine(i);
//         }

// Exercício 4: Sair Quando o Quadrado For Maior que 50
// int numero = 1;
// while (true)
//         {
//             int quadrado = numero * numero;

//             if (quadrado > 50)
//             {
//                 Console.WriteLine("O primeiro quadrado maior que 50 é: " + quadrado);
//                 break;
//             }

//             numero++;
//         }

// Exercício 5: Tabuada de um Número Usando for
//  Console.Write("Digite um número inteiro: ");
//         int numero = Convert.ToInt32(Console.ReadLine());

//         Console.WriteLine($"Tabuada do {numero}:");

//         for (int i = 1; i <= 10; i++)
//         {
//             int resultado = numero * i;
//             Console.WriteLine($"{numero} x {i} = {resultado}");
//         }

//  Exercício 6: Soma com Loop do-while
//  int soma = 0;
//  int numero;

//  do
//  {
//      Console.Write("Digite um número inteiro ou 0 para encerrar: ");
//      numero = Convert.ToInt32(Console.ReadLine());

//     soma += numero;
// }
// while (numero != 0);

// Console.WriteLine($"A soma total é: {soma}");

//  Exercício 7: Encontrar o Primeiro Múltiplo de 3 e 7
//  for (int i = 1; i <= 100; i++)
//         {
//             if (i % 3 == 0 && i % 7 == 0)
//             {
//                  Console.WriteLine($"O primeiro número múltiplo de 3 e 7 é: {i}");
//                  break;
//              }
//         }

// Exercício 8: Fatorial de um Número
// Console.Write("Digite um número inteiro positivo: ");
//         int numero = Convert.ToInt32(Console.ReadLine());

//         if (numero < 0)
//         {
//             Console.WriteLine("Por favor, insira um número positivo.");
//         }
//         else
//         {
//             long fatorial = 1; 

//             for (int i = 1; i <= numero; i++)
//             {
//                 fatorial *= i;
//             }

//             Console.WriteLine($"O fatorial de {numero} é: {fatorial}");
//         }

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
        Console.WriteLine("Média: " + status);

        //Perguntar pára continuar 
        Console.WriteLine("\nDeseja realizar um novo relatório? (s/n)");
        continuar = Console.ReadLine()?.ToLower();
    }while (continuar == "s");

Console.WriteLine("Obrigado por usar o gerador de relatório");