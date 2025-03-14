"""Manuel setup module."""

import asyncio

from add_data import AddData


async def setup():
    await AddData.add_ledger_entry_health_ai()
    await AddData.add_ledger_entry_travel_ai()


if __name__ == "__main__":
    asyncio.run(setup())
