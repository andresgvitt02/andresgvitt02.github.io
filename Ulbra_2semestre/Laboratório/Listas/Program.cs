//Array
// int [] meuArray = {1, 2, 3, 4, 5};

// for(int i = 0; i < meuArray.Length; i++)
// {
//     Console.WriteLine(meuArray[i]);
// }

using System.Collections;
//List
// List<int> myList = new List<int>();
// myList.Add(20);
// myList.Add(21);
// myList.Add(22);
// myList.Add(23);

// foreach(int elemento in myList)
// {
//     Console.WriteLine(elemento);
// }

//ArrayList
ArrayList arrayList = new ArrayList();
arrayList.Add(100);
arrayList.Add("alo");
foreach(var elemento in arrayList)
{
    Console.WriteLine(elemento);
}