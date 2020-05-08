import schedule
import time
import logging


class DashScheduler:
    def __init__(self, dashes, render_function, context, seconds_in_advance):
        self.dashes = dashes
        self.render_function = render_function
        self.context = context
        self.seconds_in_advance = seconds_in_advance

    def run(self):
        logging.info("Running all dashes.")

        for dash in self.dashes:
            dash.drawContent()

        self.render_function(self.context)

        logging.info("Cycle completed")

    def start(self):
        logging.info("Scheduling jobs started.")
        self.run()
        scheduled_seconds_in_minute = 60 - self.seconds_in_advance
        formatted_scheduled_seconds_in_minute = ":00" if scheduled_seconds_in_minute == 60 \
                                                else ":{}".format(scheduled_seconds_in_minute)

        schedule.every().minute.at(formatted_scheduled_seconds_in_minute).do(self.run)

        while True:
            schedule.run_pending()
            time.sleep(5)

