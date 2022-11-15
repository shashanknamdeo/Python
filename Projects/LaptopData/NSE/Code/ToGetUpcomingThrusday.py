# If I run code on 29th, I need 29th as Thursday, but If I run the code after 29, I need 6th October as next Thursday
# 23 se lekar 29 tak, haar din 29 hi chahiye
def toGetUpcomingThrusday():
    from datetime import datetime
    from dateutil.relativedelta import relativedelta, TH
    today_day=datetime.today()
    upcoming_thrusday=today_day+relativedelta(weekday=TH)
    return upcoming_thrusday.strftime('%d-%b-%Y')

