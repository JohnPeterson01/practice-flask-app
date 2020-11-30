## Practice Flask App Development

This is a practice project working with Flask, SQLAlchemy and Postgres. 

Initial code comes from: https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/.

The purpose of this project is also to learn about several design patterns including: 
- factories
- abstract classes
- singletons
- adapters

### Project commands:
Activate virtual environment
```
python -m venv venv
source venv/bin/activate
```

Deactivate
```
deactivate
```

Install Requirements
```
pip install requirements.txt
```

Run app
```
python main.py
```

Redis
```
docker run -d --rm -p 6379:6379 --name flask-redis redis
docker stop flask-redis
```

DB
```
python manage.py db init (only needed if starting project from scratch)
python manage.py db migrate
python manage.py db upgrade
```

