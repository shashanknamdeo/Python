# incorrect
def getLastThrusdayOfTheMonth():
    """
    """
    from dateutil.relativedelta import relativedelta, TH
    today_date = datetime.today()
    current_month = today_date.month
    # 
    for i in range(1, 6):
        t = today_date + relativedelta(weekday=TH(i))
        if t.month != current_month:
            # since t is exceeded we need last one which we can get by subtracting -2 since it is already a Thursday.
            t = t + relativedelta(weekday=TH(-2))
            break
    return t.strftime('%d-%b-%Y')

# correct code
def getLastThrusdayOfTheMonth():
    """
    """
    from datetime import datetime
    from dateutil.relativedelta import relativedelta, TH
    today_date = datetime.today()
    current_month = today_date.month
    # 
    for i in range(1, 6):
        t = today_date + relativedelta(weekday=TH(i))
        if t.month != current_month:
            # since t is exceeded we need last one which we can get by subtracting -2 since it is already a Thursday.
            t = t + relativedelta(weekday=TH(-2))
            break
    return t.strftime('%d-%b-%Y')