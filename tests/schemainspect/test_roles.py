from sqlbag import S

from schemainspect import get_inspector

CREATE = """
DROP ROLE IF EXISTS admin;
DROP ROLE IF EXISTS webuser;

CREATE ROLE admin WITH CREATEDB NOINHERIT LOGIN REPLICATION BYPASSRLS CONNECTION LIMIT 10;
CREATE ROLE webuser;
"""


def test_roles(db):
    with S(db) as s:
        s.execute(CREATE)
        i = get_inspector(s)

        admin_role = i.roles['admin']
        assert (admin_role.drop_statement == 'drop role admin;')
        assert (admin_role.create_statement == 'create role admin with NOSUPERUSER CREATEDB NOINHERIT LOGIN REPLICATION BYPASSRLS connection limit 10 password NULL ;')
        assert (admin_role.update_statement == 'alter role admin with NOSUPERUSER CREATEDB NOINHERIT LOGIN REPLICATION BYPASSRLS connection limit 10 password NULL ;')
        webuser_role = i.roles['webuser']
        assert (webuser_role.drop_statement == 'drop role webuser;')
        assert (webuser_role.create_statement == 'create role webuser with NOSUPERUSER NOCREATEDB INHERIT NOLOGIN NOREPLICATION NOBYPASSRLS connection limit -1 password NULL ;')
        assert (webuser_role.update_statement == 'alter role webuser with NOSUPERUSER NOCREATEDB INHERIT NOLOGIN NOREPLICATION NOBYPASSRLS connection limit -1 password NULL ;')