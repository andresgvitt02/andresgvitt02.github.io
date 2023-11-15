-- Comentário 

/* Insere um
comentário longo */

/* Clientes (Id int primary key, Nome char(100));
Enderecos (Id int primary key, Logradouro varchar (100), Numero int, Bairro varchar(50), Cidade varchar(20),
Estado char(2) Clientes_Id int references Clientes (Id));
*/

-- CREATE TABLE Clientes 
-- (
--      Id int Not Null Primary key,
--     Nome char(100)
-- );

-- CREATE TABLE Enderecos
-- (
--     Id int Not Null Primary Key,
--      Logradouro varchar (100),
--     Numero int, 
--     Bairro varchar (50),
--      Cidade varchar(20),
--      Estado char(2),
--      Clientes_Id int Not Null,
--      Constraint Clientes_tem_Enderecos
--          Foreign Key (Clientes_Id) references Clientes(Id)
-- )
*\


/* continuação TDE */

CREATE TABLE Professor (
    Id INT NOT NULL PRIMARY KEY,
    Nome VARCHAR(50),
    Especializacao VARCHAR(50),
    Idade INT
);


CREATE TABLE Leciona (
    Id_Leciona INT PRIMARY KEY,
    Id_Prof INT,
    Id_Disc INT,
    FOREIGN KEY (Id_Prof) REFERENCES Professor(Id_Prof),
    FOREIGN KEY (Id_Disc) REFERENCES Disciplina(Id_Disc)
);

CREATE TABLE Disciplina (
    Id_Disc INT PRIMARY KEY,
    Disciplina VARCHAR(50),
    Carga_Horaria INT
);


CREATE TABLE Utiliza (
    Id_Utiliza INT PRIMARY KEY,
    Id_Disc INT,
    Id_Software INT,
    FOREIGN KEY (Id_Disc) REFERENCES Disciplina(Id_Disc),
    FOREIGN KEY (Id_Software) REFERENCES Software(Id_Software)
);

CREATE TABLE Software (
    Id INT PRIMARY KEY,
    Nome VARCHAR(100),
    Tipo VARCHAR(50)
);