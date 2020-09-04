create table if not exists Genre(
	id serial primary key,
	name varchar(40) unique
);

create table if not exists Band(
	id serial primary key,
	name varchar(80) not null,
	description varchar(280),
	country varchar(40)
);

create table if not exists GenreBand(
	genre_id integer references Genre(id),
	band_id integer references Band(id),
	constraint pkgb primary key (genre_id, band_id)
);

create table if not exists Album(
	id serial primary key,
	name varchar(80) not null,
	year date not null
);

create table if not exists BandAlbum(
	band_id integer references Band(id),
	album_id integer references Album(id),
	constraint pkba primary key (band_id, album_id)
);

create table if not exists Track(
	id serial primary key,
	album_id integer references Album(id),
	position_in_album integer not null,
	time integer not null,
	name varchar(80) not null
);

create table if not exists Collection(
	id serial primary key,
	name varchar(80) not null,
	year date not null
);

create table if not exists CollectionTrack(
	collection_id integer references Collection(id),
	track_id integer references Track(id),
	constraint pkct primary key (collection_id, track_id)
);

