# servicearea-api
API to manage Polygon of Service Area

### create superuser
./manage.py createsuperuser
Email address: admin@domain.com
Name: Admin
Phone number: 123123
Language: EN
Currency: USD
Password: very-secured-pswd
Password (again): very-secured-pswd


### run on psql

CREATE USER prosa_user WITH PASSWORD 'prosa_pass';
CREATE DATABASE prosa_db;
GRANT ALL PRIVILEGES ON DATABASE prosa_db to prosa_user;
ALTER USER prosa_user CREATEDB;

UPDATE authentication_customuser
SET is_staff = 1
WHERE email = 'admin@domain.com';