"""strategies.py: This module setup strategies.

This module shows how logger work within strategy.
"""
import asyncio
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
        self.log.info("Executing strategy B...")
        await asyncio.sleep(3)
        self.log.info("Strategy B execution finished.")


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
            self.log.exception("An error occurred during strategy execution", exception=str(e))
