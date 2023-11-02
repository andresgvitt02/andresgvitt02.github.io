// int i = 11;

// do
// {
//     Console.WriteLine(i);
//     i++;
// }while(i<10);

// int numSecreto = 8;

// int palpite;

 // do
 // {
 //     Console.WriteLine("Digite um número: ");
 //     palpite = Convert.ToInt32(Console.ReadLine());
 // } while(palpite != numSecreto);
 // Console.WriteLine("Você acertou!");

 Console.WriteLine("Digite um número: ");
 int n = 0;
 int soma = 0;
 do{
    Console.WriteLine("Digite um número 0: ");
    n=Convert.ToInt32(Console.ReadLine());
    soma+=n;

 }while(n!=0);
 Console.WriteLine($"(soma)");


