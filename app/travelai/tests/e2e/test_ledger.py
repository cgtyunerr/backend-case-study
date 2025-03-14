"""Ledger e2e test module."""


class TestGetCurrentBalance:
    def test_200(self, travel_client):
        result = travel_client.get(
            "/ledger/1",
        )
        assert result.status_code == 200
