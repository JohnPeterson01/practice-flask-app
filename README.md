## Practice Flask App Development

This is a practice project working with Flask, SQLAlchemy and Postgres. 

Initial code comes from: https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/. Inspiration also taken from the microcosm sample service (https://github.com/globality-corp/microcosm-sample-service)

The purpose of this project is also to learn about several design patterns including: 
- factories
- abstract classes
- singletons
- adapters

### Project commands:
Virtual environment
```
python3 -m venv venv
. venv/bin/activate
deactivate
```


Install Packages
```
pip install -e .
```

Run app (from root directory)
```
runserver
```

Redis
```
docker run -d --rm -p 6379:6379 --name flask-redis redis
docker stop flask-redis
```

DB - make sure postgres is running (docker or local)
```python
createuser user-service-user
createdb -O user-service-user user_service
createdb -O user-service-user user_service_test
```

Create all (-D used to drop before creating)
```python
create-all [-D]
```

Drop all tables
```python
drop-all
```

```python - not working
python manage.py db init (only needed if starting project from scratch)
python manage.py db migrate
python manage.py db upgrade
```

Testing
- Make sure redis is up
- Make sure postgres is up

Run tests
- [-s] used to prevent nose from capturing stdout
```
nosetests -s
```

Debugging
- Place the following snippet inside the code block
```python
import pdb; 
pdb.set_trace() 
```

Multi line statement in python debugger (hit Ctrl-D to go back to debugger)
```python
!import code; code.interact(local=vars())
```
