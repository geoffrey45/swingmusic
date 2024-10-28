import schedule


from abc import ABC, abstractmethod


class CronJob(ABC):
    """
    A cron job that will be run on a regular interval.
    """

    def __init__(self, name: str, hours: int):
        self.name = name
        self.hours = hours

        schedule.every(self.hours).seconds.do(self.run)

    @abstractmethod
    def run(self):
        """
        The function that will be called by the cron job.
        """
        ...