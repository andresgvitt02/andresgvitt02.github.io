CREATE TABLE Categorias
{
    Codigo int Not Null Primary Key,
    Nome varchar(100)
};

CREATE TABLE Produtos
{
    Codigo int Not Null Primary Key,
    Descricao varchar(100),
    Data_Cadastro Date,
    Valor_Unitario float,
    Cod_Cat int Not Null,
    Constraint Categoria_tem_Produtos
        Foreign Key (Cod_Cat) references Categorias(Codigo)
};

CREATE TABLE Fornecedores
{
    Codigo int Not Null Primary Key,
    Nome varchar(100)
}

CREATE TABLE Pedidos
{
    Quantidade int Not Null Primary Key,
    Valor_Unitario float,
    Date Date,
    Cod_fornec int Not Null,
    Prod_Quant int Not Null
    Constraint Fornecedores_Pede_Produtos
        Foreign Key (Cod_Fornec) references Fornecedores(Codigo)
    Constraint Produtos_tem_Fornecedores
        Foreign Key (Prod_Cod)references Produtos(Codigo)
}