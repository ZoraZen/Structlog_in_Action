"""strategies.py: This module setup strategies.

This module shows how logger work within strategy.
"""
import asyncio
import inspect

import structlog


class StrategyA:
    def __init__(self, run_id):
        self.run_id = run_id
        self.log = structlog.get_logger(__name__).bind(
            run_id=self.run_id,
            strategy_name=self.__class__.__name__,
        )

    async def execute(self):
        self.log.info("Executing strategy A...")
        await asyncio.sleep(2)
        self.log.info("Strategy A execution finished.")


class StrategyB:
    def __init__(self, run_id):
        self.run_id = run_id
        self.log = structlog.get_logger(__name__).bind(
            run_id=self.run_id,
            strategy_name=self.__class__.__name__,
        )

    async def execute(self):
        self.log.info(
            "Executing strategy B...", function_name=inspect.currentframe().f_code.co_name
        )
        await asyncio.sleep(3)
        self.log.info(
            "Strategy B execution finished.", function_name=inspect.currentframe().f_code.co_name
        )


class StrategyC:
    ERROR_MESSAGE = "Something went wrong in StrategyC"

    def __init__(self, run_id):
        self.run_id = run_id
        self.log = structlog.get_logger(__name__).bind(
            run_id=self.run_id,
            strategy_name=self.__class__.__name__,
        )

    async def execute(self):
        try:
            self.log.info("Executing strategy C...")
            await asyncio.sleep(1)
            raise RuntimeError(self.ERROR_MESSAGE)
            self.log.info("Strategy C execution finished.")  # This line will never be reached
        except Exception as e:
            self.log.exception("An error occurred during strategyC execution", exception=str(e))


if __name__ == "__main__":
    from logger_config import configure_logger
    import uuid

    configure_logger()

    run_id = str(uuid.uuid4())

    strategy_a = StrategyA(run_id)
    asyncio.run(strategy_a.execute())
