import time
import schedule

from app.crons.mixes import Mixes
from app.utils.threading import background


@background
def start_cron_jobs():
    """
    This is the function that triggers the cron jobs.
    """
    Mixes().run()
    
    # schedule.run_pending()