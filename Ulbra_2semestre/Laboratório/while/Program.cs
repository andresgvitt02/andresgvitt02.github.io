// int x = 0;

// while (x<51)
// {
// Console.WriteLine(x);
// x++;
// }

int y = 0;
int soma = 0; 

while (true){
    Console.WriteLine("Digite um número inteiro ou 0 para sair: ");
    y = Convert.ToInt32(Console.ReadLine());
    soma+=y;

    if (y==0)
    break;
}
Console.WriteLine($"{soma+y}");