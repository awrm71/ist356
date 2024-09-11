from datetime import datetime

YMD = "%Y.%m.%d"
MDY = "%m/%d/%Y"

def parsdate_mdy( text:str) -> datetime:
    return datetime.strptime(text, MDY)

def formatdate_ymd(date:datetime) -> str:
    return date.strftime(YMD)

date = "12/30/1999"
date_dt = parsdate_mdy(date)
date_str = formatdate_ymd(date_dt)
print(date_str)

