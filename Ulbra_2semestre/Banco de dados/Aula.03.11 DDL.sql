CREATE TABLE Clientes
(
    Id int Not Null Primary key,
    Nome char(100)

);

CREATE TABLE Enderecos
(
    Id int Not Null Primary Key,
    Logradouro varchar (100),
    Numero int,
    Bairro varchar (50),
    Cidade varchar(20),
    Estado char(2),
    Clientes_Id int Not Null,
    Constraint Clientes_tem_Enderecos
    Foreign Key (Clientes_Id) references Clientes(Id)
);

--Adicionar coluna em uma tabela
ALTER TABLE Enderecos add column Email varchar(30);

--Apagar coluna de uma tabela
ALTER TABLE Enderecos drop column email;

--Dropando(apagando) a chave estrangeira(FK)
ALTER TABLE Enderecos drop
    Constraint Clientes_tem_Enderecos;

--Adicionando uma chave estrangeira
ALTER TABLE Enderecos 
    add Constraint Novo 
        Foreign Key(Clientes_Id)references Clientes(Id);

--Inserindo tuplas
Insert into Clientes
    (Id, Nome)
    values(100, 'Mari');

Insert into Clientes
    (Id, Nome)
    values(200, 'Andres');

Insert into Clientes
    (Id, Nome)
    values(300, 'João');

Insert Into Enderecos
    (Id, Logradouro, Bairro, Cidade, Estado, Clientes_Id)
    values(200, 'Rua Das violetas, 5051', 'Bom Jesus', 'Arroio do sal', 'RS', 200)

Insert Into Enderecos
    (Id, Logradouro, Bairro, Cidade, Estado, Clientes_Id)
    values (100, 'Rua das tirivas, 36', 'Vila São João', 'Torres', 'RS', 100)

Update Enderecos set Numero = '5051' 

