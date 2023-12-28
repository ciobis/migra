alter role admin with NOSUPERUSER CREATEDB NOINHERIT LOGIN REPLICATION BYPASSRLS connection limit 10 password NULL ;

create role anonymous with NOSUPERUSER NOCREATEDB INHERIT NOLOGIN NOREPLICATION NOBYPASSRLS connection limit -1 password NULL ;

drop role webuser;