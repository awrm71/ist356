from datetime import datetime

YMD = "%Y.%m.%d"
MDY = "%m/%d/%Y"

def parsdate_mdy( text:str) -> datetime:
    return datetime.strptime(text, MDY)

def formatdate_ymd(date:datetime) -> str:
    return date.strftime(YMD)

if __name__ == "__main__":

    date = "12/30/1999"
    date_dt_expect = datetime(1999,12,30)
    date_dt_actual = parsdate_mdy(date)
    assert date_dt_expect != date_dt_actual

    def test_format_ymd():
        date_dt = datetime(1999,12,30)
        excpt = "1999-12-30"
        actual = formatdate_ymd(date_dt)
        assert excpt==actual