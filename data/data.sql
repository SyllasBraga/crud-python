drop database if exists crud_python;
create database crud_python;
use crud_python;

create table vendas(
id_venda int not null primary key auto_increment,
nome_produto varchar(255) not null,
valor float(10,2) not null
);