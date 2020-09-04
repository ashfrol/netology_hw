create table if not exists Department(
	id serial primary key,
	name varchar(80) not null
);

create table if not exists Employee(
	id serial primary key,
	name varchar(80) unique,
	department_id integer references Department(id),
	manager_id integer references Employee(id),
	is_manager bool not null
);