"""Calendar Router."""

from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (
    ExtraParams,
    ProviderChoices,
    StandardParams,
)
from openbb_core.app.query import Query
from openbb_core.app.router import Router

router = Router(prefix="/calendar")

# pylint: disable=unused-argument


@router.command(
    model="CalendarIpo",
    examples=[
        "# Get all IPOs available.",
        "obb.equity.calendar.ipo()",
        "# Get IPOs for specific dates.",
        "obb.equity.calendar.ipo(start_date='2024-02-01', end_date='2024-02-07')",
    ],
)
async def ipo(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get historical and upcoming initial public offerings (IPOs)."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="CalendarDividend",
    examples=[
        "# Get dividend calendar for specific dates.",
        "obb.equity.calendar.dividend(start_date='2024-02-01', end_date='2024-02-07')",
    ],
)
async def dividend(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get historical and upcoming dividend payments. Includes dividend amount, ex-dividend and payment dates."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="CalendarSplits",
    examples=[
        "# Get stock splits calendar for specific dates.",
        "obb.equity.calendar.splits(start_date='2024-02-01', end_date='2024-02-07')",
    ],
)
async def splits(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get historical and upcoming stock split operations."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="CalendarEarnings",
    examples=[
        "# Get earnings calendar for specific dates.",
        "obb.equity.calendar.earnings(start_date='2024-02-01', end_date='2024-02-07')",
    ],
)
async def earnings(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get historical and upcoming company earnings releases. Includes earnings per share (EPS) and revenue data."""
    return await OBBject.from_query(Query(**locals()))
