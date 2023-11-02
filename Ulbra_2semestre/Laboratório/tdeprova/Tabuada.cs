class Tabuada
{
    public int numeroBase;
    public void imprimirTabuada()
    {
        for(int i = 1; i <= 10; i++)
        {
            Console.WriteLine($"{numeroBase} x {i} = {numeroBase * i}");
        }   
    }
}
