import threading
import time
import schedule

class Scheduler(threading.Thread):
    def __init__(self):
        super().__init__()
        self.__stop_running = threading.Event()
    

    """
    Schedule a task to repeat at the same time daily
    """

    def scheduleDaily(self, hour, min, job):
        schedule.clear()
        schedule.every().day.at(f'{hour:02d}:{min:02d}').do(job)
    

    def run(self):
        self.__stop_running.clear()
        while not self.__stop_running.is_set():
            schedule.run_pending()
            time.sleep(1)

    def stop(self):
        self.__stop_running.set()


if __name__ == '__main__':
    import emails
    email = emails.Email()

    scheduler = Scheduler()
    scheduler.start()

    hour = time.localtime().tm_hour
    min = time.localtime().tm_min + 1
    print(f'Scheduling test email for {hour:02d}:{min:02d}')
    scheduler.scheduleDaily(hour, min, email.sendEmail)

    time.sleep(60)
    scheduler.stop()