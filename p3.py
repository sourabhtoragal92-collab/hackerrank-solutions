import sys

def timeConversion(s):
    period = s[-2:]
    hour = int(s[:2])
    rest = s[2:-2]
    
    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
            
    return f"{hour:02d}{rest}"

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    if s:
        print(timeConversion(s))