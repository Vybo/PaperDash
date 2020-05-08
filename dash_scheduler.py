import schedule
import time
import logging


class DashScheduler:
    def __init__(self, dashes, render_function):
        self.dashes = dashes
        self.render_function = render_function

    def start(self):
        logging.info("Scheduling jobs started.")
        self.run()
        while True:
            schedule.run_pending()
            time.sleep(1)

    def run(self):
        logging.info("Running all dashes.")

        for dash in self.dashes:
            dash.drawContent()

        self.render_function()

        schedule.every().minute.do(self, self.run(self))

