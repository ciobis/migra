create extension hstore;

create role postgres;

create schema goodschema;

create table goodschema.t(id uuid, value text);

create table t(id uuid, value text);

CREATE TYPE goodschema.sdfasdfasdf AS ENUM ('not shipped', 'shipped', 'delivered');

create index on goodschema.t(id);

create view goodschema.v as select 1 AS a;

create schema goodschema2;

create table goodschema2.t(id uuid, value text);

CREATE TYPE goodschema2.sdfasdfasdf AS ENUM ('not shipped', 'shipped', 'delivered');

create index on goodschema2.t(id);

create view goodschema2.v as select 1 AS a;

grant select on table t to postgres;
