from sqlbag import S

from schemainspect import get_inspector

CREATE = """
DROP ROLE IF EXISTS admin;
DROP ROLE IF EXISTS webuser;

CREATE ROLE admin;
CREATE ROLE webuser;

GRANT webuser to admin;
"""


def test_memberships(db):
    with S(db) as s:
        s.execute(CREATE)
        i = get_inspector(s)

        webuser_to_admin = i.memberships[('webuser', 'admin', False)]
        assert (webuser_to_admin.drop_statement == 'revoke webuser from admin;')
        assert (webuser_to_admin.create_statement == 'grant webuser to admin  granted by test;')

        assert i.indexes == i.indexes