//operadores relacionais 
int x = 10;
int y = 20;

Console.WriteLine(x == y);
Console.WriteLine(x > y);
Console.WriteLine(x < y);
//Console.WriteLine();
//Console.WriteLine;
//Console.WriteLine;

//operadores lópgicos
bool resultado;
bool c1 = true;
bool c2 = false;

//operador and
resultado = c1 && c2;
Console.WriteLine(resultado);

//operador or
resultado = c1 || c2;
Console.WriteLine(resultado);

//operador ternário
// condicao ? valorSeVerdadeiro : valorSeFalso

int numero = 5;
string resultadoTernario = (numero % 2 = 0 ) ? "Par" : "Impar";
Console.WriteLine(resultadoTernario);
