drop table jogos;
drop table usuários;

create table jogos (
    id serial primary key,
    nome varchar(50) not null,
    categoria varchar(40) not null,
    console varchar(20) not null
);

create table usuários (
    nome varchar(20) not null,
    nickname varchar(8) primary key,
    senha varchar(100) not null
);

insert into usuários (nome, nickname, senha)
values ('nome', 'nickname', 'senha');

insert into jogos (nome, categoria, console)
values 
    ('tetris', 'puzzle', 'atari'),
    ('god of war', 'hack and slash', 'ps2'),
    ('mortal kombat', 'fighting', 'snes'),
    ('valorant', 'fps', 'pc'),
    ('crash bandicoot', 'platform', 'ps1'),
    ('need for speed', 'racing', 'pc');
	
select * from jogos;

select * from usuários;