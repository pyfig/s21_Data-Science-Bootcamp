import logging
from random import randint
import requests
import config

logging.basicConfig(
    filename=config.log_file,
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

class Research:
    def __init__(self, path):
        self.path = path
        logging.info("Initialized Research class with path: %s", path)

    def file_reader(self, has_header=True):
        logging.info("Reading file: %s", self.path)
        try:
            with open(self.path, "r") as file:
                lines = file.readlines()

            start_idx = 1 if has_header else 0
            result = []

            for line in lines[start_idx:]:
                values = line.strip().split(',')
                result.append([int(values[0]), int(values[1])])

            logging.info("Successfully read file with %d lines of data", len(result))
            return result
        except Exception as e:
            logging.error("Error reading file: %s", str(e))
            raise

    class Calculations:
        def __init__(self, data):
            self.data = data
            logging.info("Initialized Calculations with data size: %d", len(data))

        def counts(self):
            logging.info("Calculating counts of heads and tails")
            heads = sum(1 for item in self.data if item[0] == 1)
            tails = len(self.data) - heads
            logging.info("Counts: heads=%d, tails=%d", heads, tails)
            return heads, tails

        def fractions(self):
            logging.info("Calculating fractions of heads and tails")
            heads, tails = self.counts()
            total = heads + tails
            head_fraction = (heads / total) * 100
            tail_fraction = (tails / total) * 100
            logging.info(
                "Fractions: head_fraction=%.2f%%, tail_fraction=%.2f%%",
                head_fraction,
                tail_fraction,
            )
            return head_fraction, tail_fraction

    class Analytics(Calculations):
        def predict_random(self, num_of_steps):
            logging.info("Generating %d random predictions", num_of_steps)
            predictions = [
                [randint(0, 1), 1 - randint(0, 1)] for _ in range(num_of_steps)
            ]
            logging.info("Predictions: %s", predictions)
            return predictions

        def predict_last(self):
            logging.info("Predicting the last observation from data")
            last = self.data[-1]
            logging.info("Last observation: %s", last)
            return last

        def save_file(self, data, file_name, file_extension):
            file_path = f"{file_name}.{file_extension}"
            try:
                with open(file_path, "w") as file:
                    file.write(data)
                logging.info("File saved successfully: %s", file_path)
            except Exception as e:
                logging.error("Error saving file: %s", str(e))
                raise

        def send_telegram_message(self, message):
            logging.info("Sending message to Telegram channel")
            payload = {
                "chat_id": config.token_chat_id,
                "text": message,
            }
            try:
                response = requests.post(config.telegram_webhook_url, json=payload)
                response.raise_for_status()
                logging.info("Message sent successfully: %s", message)
            except Exception as e:
                logging.error("Error sending message to Telegram: %s", str(e))
