#test_strategies.py: This module is for test.
import pytest
from strategies import StrategyA
from strategies import StrategyB
from strategies import StrategyC


@pytest.fixture()
def run_id():
    return "test_run"


@pytest.mark.asyncio()
async def test_strategyA(capsys, run_id):
    strategy_a = StrategyA(run_id)
    await strategy_a.execute()

    captured = capsys.readouterr()
    assert "Executing strategy A..." in captured.out
    assert "Strategy A execution finished." in captured.out


@pytest.mark.asyncio()
async def test_strategyB(capsys, run_id):
    strategy_b = StrategyB(run_id)
    await strategy_b.execute()

    captured = capsys.readouterr()
    assert "Executing strategy B..." in captured.out
    assert "Strategy B execution finished." in captured.out


@pytest.mark.asyncio()
async def test_strategyC(capsys, run_id):
    strategy_c = StrategyC(run_id)
    await strategy_c.execute()

    captured = capsys.readouterr()
    assert "Executing strategy C..." in captured.out
    assert "An error occurred during strategyC execution" in captured.out
    assert StrategyC.ERROR_MESSAGE in captured.out
