create extension citext;

create role postgres;

create schema goodschema;
    
CREATE TYPE goodschema.sdfasdfasdf AS ENUM ('not shipped', 'shipped', 'delivered', 'not delivered');

create table goodschema.t(id uuid, name text, value text);

create view goodschema.v as select 2 as a;

create schema goodschema2;
    
CREATE TYPE goodschema2.sdfasdfasdf AS ENUM ('not shipped', 'shipped', 'delivered', 'not delivered');

create table goodschema2.t(id uuid, name text, value text);

create view goodschema2.v as select 2 as a;
