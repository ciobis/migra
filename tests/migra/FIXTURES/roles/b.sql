create role admin WITH CREATEDB NOINHERIT LOGIN REPLICATION BYPASSRLS CONNECTION LIMIT 10;
create role anonymous;

grant admin to anonymous;