# Tests

## Tests

In the project, e2e, integration and unit tests are made by using pytest. conftest.py(pytest configuration) is added main directory.

## test-setup Script

- The main purpose of this script is to maintain CI.
```yml
      - name: Create test environment
        run: |
          scripts/test-setup.sh
```
- workflow install test setup by using this script. Also, it is practical while testing. At this stage of project, database is just controlled by monorepo. That's why the test setup is only in the monorepo. However, if another app control the database, test setup must be added in this app and setup and teardown file must be added in the setup folder. Also, necessary script commands must be added in test-setup.sh.


## Conftest
```python
@pytest.fixture(scope="function")
async def session() -> AsyncGenerator[AsyncSession, None]:
    database_session_manager: DatabaseSessionManager = DatabaseSessionManager(
        str(settings.DB.db_url)
    )
    async with database_session_manager.get_session() as session:
        yield session
```
- This fixture ensure multiple functions and classes will be tested in series.

```python
@pytest.fixture(scope="session")
def health_client():
    with TestClient(<app_name>_api) as client:
        yield client
```
- This fixture create client for our e2e tests. In our we case we need 2 client because we have 2 apps.
