# create postgres db from terminal
=============IN TERMINAL=====================
show psql query editor = sudo -u postgres psql
Create DB = create database online_course;
CREATE USER newuser WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE "online_course" to newuser;
GRANT CREATE ON SCHEMA public TO newuser;
GRANT USAGE ON SCHEMA public TO newuser;
ALTER SCHEMA public OWNER TO newuser;
ALTER SCHEMA public OWNER TO newuser;
ALTER DATABASE online_course OWNER TO newuser;




List All database = \l
Use database = \c online_course
Show All Tables = \d
List of all tables = \dt
Describe Table = \d table_name or \d+ table_name
Quit from query = \q
Help commands = \?

INSERT INTO api_category(name,slug,is_active,created_at,updated_at)values
('Uncategorized','uncategorized',True,now(),now());
select * from api_category limit 1;
truncate table api_category;
truncate table api_category cascade; //related table
truncate table api_posts_post_categories restart identity;//index start from 1
truncate table api_category restart identity cascade;

===================IN PGADMIN===================
SELECT *
FROM information_schema.columns
WHERE table_name = 'api_category';
INSERT INTO api_category(name,slug,is_active,created_at,updated_at)values
('Uncategorized','uncategorized',True,now(),now());
select * from api_category limit 1;
===================UPDATE QUERY=============================
update api_posts set allow_comments = True;
update api_posts set is_sticky = False;
update api_posts set is_on_thesquare = False;
update api_posts set is_on_thesquare = False;
update api_posts set is_draft = False;
update api_posts set pending_for_review = False;
update api_posts set custom_canonical_url = '';
============================================================
ISSUE : Password Authentication Failed
Solution : Change Master password from AWS -> RDS -> Modify Instance


================ GRANT AND REVOKE PERMISSION ===================
SELECT * FROM information_schema. table_privileges LIMIT 5;
SELECT grantee, privilege_type 
FROM information_schema.role_table_grants 
WHERE table_name='api_posts';
REVOKE DELETE ON TABLE api_posts FROM postgres;
GRANT DELETE ON TABLE api_posts TO postgres;
=================================================================
Error: django.core.exceptions.ImproperlyConfigured: Error loading psycopg2 or psycopg module
Solution: pip3 install psycopg2-binary