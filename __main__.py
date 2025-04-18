import logging

from app import logger

log = logging.getLogger(__name__)


def main() -> None:
    logger.setup()
    log.info("App starting..")


if __name__ == "__main__":
    main()
