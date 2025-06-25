class TimeZone:
    time=0 
    standard=""
def accept():
    time = int(input("Enter the time in 24-hour format (HHMM): "))
    standard = input("Enter the time zone (" \
    " PDT - PACIFIC TIME" \
    " MDT - MOUNTAIN TIME" \
    " CDT - CENTRAL TIME" \
    " EDT - EASTERN TIME" \
    " BRA - BRASIL" \
    " UTC - UNIVERSAL TIME" \
    " BST - BRITSIH STANDARD TIME" \
    " CEST - GERMANY" \
    " MSK - RUSSIAN FEDERATION" \
    " UAE - UNITED ARAB EMIRATES" \
    " IST - INDIAN STANDARD TIME" \
    " SNGP - SINGAPORE" \
    " CSTB - CHINA STANDARD TIME (BEIJING)" \
    " CSTC - CHINA STANDARD TIME (CHINA)" \
    " JST - JAPAN" \
    " AEST - AUSTRALIA" \
    " NZST - NEW ZEALAND): ").upper()
    return time, standard

def toUTC(time, standard):
    guide = {"PDT": -7, "MDT": -6, "CDT": -5, "EDT": -4, "BRA": -3, "UTC": 0, "BST": 1, "CEST": 2, "MSK": 3, "UAE": 4, "IST": 5.3, "SNGP": 8, "CSTB": 8, "CSTC": 8, "JST": 9, "AEST": 10, "NZST": 12}
    if standard in guide:
        offset = guide[standard]
        utc_time = int((time + (offset * 100 * (-1))))
        return utc_time

def toIST(time, standard):
    utc_time = toUTC(time, standard)
    newTime = (utc_time + (5.3 * 100))
    if(abs(newTime%100) >= 60):
            newTime += 40
    return newTime

def formatTime(time):
    n=len(str(time))
    if n < 4:
        time = "0" * (4 - n) + str(time)
    return str(time)

Time = TimeZone()
Time.time, Time.standard = accept()
utc_time = toUTC(Time.time, Time.standard)
if(utc_time>2400):
    utc_time -= 2400
    print("UTC Time is next day")
elif(utc_time<0):
    utc_time += 2400
    print("UTC Time is previous day")
ist_time = int(toIST(Time.time, Time.standard))
if(ist_time>2400):
    ist_time -= 2400
    print("IST Time is next day")
elif(ist_time<0):
    ist_time += 2400
    print("IST Time is previous day")

print(f"Time in {Time.standard} is {formatTime(Time.time)}, which is {formatTime(utc_time)} in UTC and {formatTime(ist_time)} in IST.")