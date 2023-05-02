drop database if exists crud_python;
create database crud_python;
use crud_python;

create table vendas(
id_venda int not null primary key auto_increment,
nome_produto varchar(255) not null,
valor float(10,2) not null,
cliente_id int not null
);

create table cliente(
id_cliente int not null primary key auto_increment,
nome_cliente varchar(255) not null,
login varchar(255) unique not null
);

alter table vendas
add foreign key fk_cliente_venda(cliente_id) references cliente(id_cliente);

insert into cliente values (default, "José", "josé@gmail.com");
insert into vendas values (default, "Sabão", 10.62, 1);