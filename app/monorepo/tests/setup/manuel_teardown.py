"""Manuel teardown."""

import asyncio

from remove_data import RemoveData


async def teardown():
    await RemoveData.remove_ledger_entry_travel_ai()
    await RemoveData.remove_ledger_entry_health_ai()


if __name__ == "__main__":
    asyncio.run(teardown())
