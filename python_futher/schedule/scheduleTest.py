import time
import schedule
import datetime

# schedule 阻塞

def job():
    print('Job1:每隔10秒执行一次的任务，每次执行2秒')
    print('Job1-startTime:%s' %(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    time.sleep(2)
    print('Job1-endTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print('------------------------------------------------------------------------')

if __name__ == '__main__':
    schedule.every(10).seconds.do(job)
    # schedule.every().second.do(job)
    # schedule.every(10).minutes.do(job)
    # schedule.every().minute.do(job)
    # schedule.every(10).hours.do(job)
    # schedule.every().hour.do(job)
    # schedule.every(10).days.do(job)
    # schedule.every().day.do(job)
    # schedule.every(10).weeks.do(job)
    # schedule.every().week.do(job)
    # schedule.every().monday.do(job)
    # schedule.every().tuesday.do(job)
    # schedule.every().wednesday.do(job)
    # schedule.every().thursday.do(job)
    # schedule.every().friday.do(job)
    # schedule.every().saturday.do(job)
    # schedule.every().sunday.do(job)
    while True:
        schedule.run_pending()