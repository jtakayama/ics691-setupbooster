CREATE ROLE makahiki;

ALTER ROLE makahiki WITH LOGIN UNENCRYPTED PASSWORD 'makahiki' NOSUPERUSER CREATEDB NOCREATEROLE;

CREATE DATABASE makahiki OWNER makahiki;

REVOKE ALL ON DATABASE makahiki FROM PUBLIC;

GRANT CONNECT ON DATABASE makahiki TO makahiki;

GRANT ALL ON DATABASE makahiki TO makahiki;