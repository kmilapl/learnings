use carros;

CREATE TABLE marca(
	id INT not null auto_increment,
    nome_marca VARCHAR(255) NOT NULL,
    primary key (id)
);

CREATE TABLE inventario(
	id INT NOT NULL auto_increment,
    modelo VARCHAR(255) NOT NULL,
    transmissao VARCHAR(255) NOT NULL,
    motor VARCHAR(255) NOT NULL,
    tipo_combustivel VARCHAR(255) NOT NULL,
    marcas_id INT NOT NULL,
    primary key (id),
    foreign key(marcas_id) REFERENCES marca(id)
);