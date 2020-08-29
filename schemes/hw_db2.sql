create table if not exists Genre(
	id serial primary key,
	name varchar(40) unique
);

create table if not exists Band(
	id serial primary key,
	name varchar(80) not null,
	description varchar(280),
	country varchar(40),
	genre_id integer references Genre(id)
);

create table if not exists Album(
	id serial primary key,
	name varchar(80) not null,
	band_id integer references Band(id),
	year date not null
);


create table if not exists Track(
	id serial primary key,
	album_id integer references Album(id),
	position_in_album integer not null,
	time time without time zone,
	name varchar(80) not null
);

