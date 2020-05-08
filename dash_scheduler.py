import schedule
import time
import logging


class DashScheduler:
    def __init__(self, dashes, render_function, context):
        self.dashes = dashes
        self.render_function = render_function
        self.context = context

    def run(self):
        logging.info("Running all dashes.")

        for dash in self.dashes:
            dash.drawContent()

        self.render_function(self.context)

        logging.info("Cycle completed")

    def start(self):
        logging.info("Scheduling jobs started.")
        self.run()
        schedule.every().minute.do(self.run)

        while True:
            schedule.run_pending()

