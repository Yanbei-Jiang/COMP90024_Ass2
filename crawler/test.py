import schedule
from datetime import datetime

def test():
    print("wowwowowowowowo")

schedule.every().day.at("05:11").do(test)

while(True):
    schedule.run_pending()


