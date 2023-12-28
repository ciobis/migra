create role anonymous with NOSUPERUSER NOCREATEDB INHERIT NOLOGIN NOREPLICATION NOBYPASSRLS connection limit -1 password NULL ;

drop role webuser;