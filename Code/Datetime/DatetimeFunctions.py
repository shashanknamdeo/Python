"""
%a         Abbreviated weekday name                                        Sun, Mon
%A         Full weekday name                                               Sunday, Monday
%w         Weekday as decimal number                                       0…6
%d         Day of the month as a zero-padded decimal                       01, 02
%-d        day of the month as decimal number                              1, 2..
%b         Abbreviated month name                                          Jan, Feb
%m         month as a zero padded decimal number                           01, 02
%-m        month as a decimal number                                       1, 2
%B         Full month name                                                 January, February
%y         year without century as a zero padded decimal number            99, 00 
%-y        year without century as a decimal number                        0, 99
%Y         year with century as a decimal number                           2000, 1999
%H         hour(24 hour clock) as a zero padded decimal number             01, 23
%-H        hour(24 hour clock) as a decimal number                         1, 23
%I         hour(12 hour clock) as a zero padded decimal number             01, 12
%-I        hour(12 hour clock) as a decimal number                         1, 12
%p         locale’s AM or PM                                               AM, PM
%M         Minute as a zero padded decimal number                          01, 59
%-M        Minute as a decimal number                                      1, 59
%S         Second as a zero padded decimal number                          01, 59
%-S        Second as a decimal number                                      1, 59
%f         microsecond as a decimal number, zero padded on the left side   000000, 999999
%z         UTC offset in the form +HHMM or -HHMM    
%Z         Time zone name   
%j         day of the year as a zero padded decimal number                 001, 365
%-j        day of the year as a decimal number                             1, 365
%U         Week number of the year (Sunday being the first)                0, 6
%W         Week number of the year                                         00, 53
%c         locale’s appropriate date and time representation               Mon Sep 30 07:06:05 2013
%x         locale’s appropriate date representation                        11/30/98
%X         locale’s appropriate time representation                        10:03:43
%%         A literal ‘%’ character                                         %
"""

datetime.strptime(i, 'data_fornat')
# example  datetime.strptime('2023-01-03T15:25:00', "%Y-%m-%dT%H:%M:%S") -> datetime.datetime(2023, 1, 3, 15, 25)

formatted = datetime.now().strftime('data_fornat')
# example   datetime.now().strftime("%Y%m%d_%H%M") -> '20230103_1525'


# timedelta
# Syntax : datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) 
date_after_two_day = datetime.now() + timedelta(days = 2)

# replace
Date.replace()
# Syntax : datetime.replace(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) 
# Date = date(2010, 2, 12) -> 2010-02-12
# Date.replace(month=5) -> 2010-05-12