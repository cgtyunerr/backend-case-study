# Backend Developer Case Study: Shared Ledger System

## Architecture

The project architecture is monorepo. The monorepo module hold common class, methods, etc. Other 2 apps use this common things. The main purpose of this architecture is to minimize the duplicate codes and maximize the code reusability.

## Main Problems

- Enum extension: In python, enums are not extendable but in our project we must extend the enums to prevent code duplication and bound generic types. For these two purpose, I use class decorators. The disadvantage of this method is making enums dynamic.
```python
# In monorepo/core/commons/extend_enum_decorator
def extend_enum(inherited_enum):
    """Extend enum decorator."""

    def wrapper(added_enum):
        """Extend enum method."""
        joined = {}
        for item in inherited_enum:
            joined[item.name] = item.value
        for item in added_enum:
            joined[item.name] = item.value
        return enum.Enum(added_enum.__name__, joined)

    return wrapper
```
- Self migration problem: Owing to monorepo architecture, we must separate the migrations because apps must be isolated from each other regarding to migrations. To ensure this isolation, I use 2 alembic folder these are located in apps and add name area to the alembic.ini file to show alembic folders location. Details about migrations is in docs/01_migrations.md.
- Generic is problem: Although genericity increases code reusability, it makes static type checking more difficult. It also makes Pydantic's job more difficult.

## Auxiliary tools and technologies
- pre-commit: Pre-commit was used to maintain code standards and prevent errors like committing directly to the main branch. Also, Linting was secured with pre-commit.
- commitizen: Commitizen was used for version control.
- github workflows: It is used for CI.
- doc tools: They are used for ensuring code documentation and code documentation is secured with pre-commit.
