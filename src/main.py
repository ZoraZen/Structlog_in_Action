import asyncio
import uuid
import structlog
from logger_config import configure_logger
from strategies import StrategyA
from strategies import StrategyB
from strategies import StrategyC


async def main():
    configure_logger()

    log = structlog.get_logger(__name__)

    run_id = str(uuid.uuid4())
    log = structlog.get_logger(__name__).bind(run_id=run_id)

    strategy_a = StrategyA(run_id)
    strategy_b = StrategyB(run_id)
    strategy_c = StrategyC(run_id)

    try:
        await asyncio.gather(
            strategy_a.execute(),
            strategy_b.execute(),
            strategy_c.execute(),
        )
    except Exception as e:
        log.exception("An error occurred during strategy execution", exception=str(e))
    log.info("Application finished.")


if __name__ == "__main__":
    asyncio.run(main())
