# servicearea-api
API to manage Polygon of Service Area

### Clone
```
$ git clone git@gitlab.com:ilhamije/referral-system.git
$ cd referral-system
```

<br >
## Preparing the SuperUser / Admin Account. 
<br>
### create superuser. 
On Terminal 1
```
./manage.py createsuperuser  
Email address: admin@domain.com  
Name: Admin  
Password: very-secured-pswd  
```

### Run on psql.  
Database  
```
CREATE USER prosa_user WITH PASSWORD 'prosa_pass';
CREATE DATABASE prosa_db;
GRANT ALL PRIVILEGES ON DATABASE prosa_db to prosa_user;
ALTER USER prosa_user CREATEDB;
```

Admin Account  
```
UPDATE authentication_customuser
SET is_staff = 1
WHERE email = 'admin@domain.com';
```


### Run Docker

```
$ docker-compose build && docker-compose up -d
```

### Check running docker image (optional)

```
$ docker-compose ps -a
```

### Shutting down docker image (optional)

```
$ docker-compose down
```

