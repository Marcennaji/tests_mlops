import logging
import os

LOG_FILE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "../logs/customer_churn.log"
)

os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - [%(module)s] %(message)s",
    handlers=[logging.FileHandler(LOG_FILE_PATH, mode="a"), logging.StreamHandler()],
)

logger = logging.getLogger("ProjectLogger")
