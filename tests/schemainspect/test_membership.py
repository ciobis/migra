from sqlbag import S

from schemainspect import get_inspector

CREATE = """
DROP ROLE IF EXISTS admin;
DROP ROLE IF EXISTS webuser;

CREATE ROLE admin;
CREATE ROLE webuser;
GRANT admin TO webuser;
"""


def test_membership(db):
    # with S(db) as s:
    #     s.execute(CREATE)
        
    with S(db) as s:
        s.execute(CREATE)
        i = get_inspector(s)

        membership_admin_webuser = i.memberships[('admin', 'webuser', False)]
        assert (membership_admin_webuser.create_statement == 'grant admin to webuser  granted by test;')
        assert (membership_admin_webuser.drop_statement == 'revoke admin from webuser;')