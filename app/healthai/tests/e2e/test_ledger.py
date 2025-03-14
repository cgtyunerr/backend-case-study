"""HealthAI ledger e2e test."""


class TestGetCurrentBalance:
    def test_200(self, health_client):
        result = health_client.get(
            "/ledger/1",
        )
        assert result.status_code == 200
