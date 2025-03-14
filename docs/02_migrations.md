# Migrations

## Architecture

A database schema is created for each app because if all the apps use app schema, version tables are conflict. In production, it is not important because each app is deployed to production independently.

## Create Migration

- For healthAI:
```bash
alembic -c alembic.ini --name alembic_healthai revision --autogenerate -m "your message"
```
- For TravelAI:
```bash
alembic -c alembic.ini --name alembic_travelai revision --autogenerate -m "your message"
```
## Migrate Database

- For healthAI:
```bash
poetry run alembic -c alembic.ini --name alembic_healthai upgrade head
```

- For travelAI:
```bash
poetry run alembic -c alembic.ini --name alembic_travelai upgrade head
```

## App Addition

If an app is added the project:

- Alembic folder must be create in the new app folder.
- This folders location must be showed with namespace in alembic.ini.
- The new schema is generated in env.py file.
- Method in below must be added in env.py and add this method to context configuration 'include_object=include_object' to protect other schemas after the first migrations.

```python
def include_object(object, name, type_, reflected, compare_to):
    if type_ == "table":
        return object.schema in ["schema_name"]
    return True
```
