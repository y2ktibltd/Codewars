#!/usr/bin/env python3
def format_duration(seconds):
    if seconds==0:return 'now'
    y=d=h=m=s=0
    res=[]
    y=seconds//31536000
    seconds%=31536000
    d=seconds//86400
    seconds%=86400
    h=seconds//3600
    seconds%=3600
    m=seconds//60
    seconds%=60
    s=seconds
    if s>0:
        num_seconds=f'{s}{" seconds" if s>1 else " second"}'
    else:
        num_seconds=""
    if m>0:
        num_minutes=f'{m}{" minutes" if m>1 else " minute"}'
    else:
        num_minutes=""
    if h>0:
        num_hours=f'{h}{" hours" if h>1 else " hour"}'
    else:
        num_hours=""
    if d>0:
        num_days=f'{d}{" days" if d>1 else " day"}'
    else:
        num_days=""
    if y>0:
        num_years=f'{y}{" years" if y>1 else " year"}'
    else:
        num_years=""
    if len(num_years)>0:
        res.append("".join(f'{num_years if len(num_years)>0 else ""}'))
    if len(num_days)>0:
        res.append("".join(f'{num_days if len(num_days)>0 else ""}'))
    if len(num_hours)>0:
        res.append("".join(f'{num_hours if len(num_hours)>0 else ""}'))
    if len(num_minutes)>0:
        res.append("".join(f'{num_minutes if len(num_minutes)>0 else ""}'))
    if len(num_seconds)>0:
        res.append("".join(f'{num_seconds if len(num_seconds)>0 else ""}'))
#    res=f'{num_years if len(num_years)>0 else ""}'
#    res+=f'{num_days if len(num_days)>0 else ""}'
#    res+=f'{num_hours if len(num_hours)>0 else ""}'
#    res+=f'{num_minutes if len(num_minutes)>0 else ""}'
#    print(res)
#    print(len(res))
    if len(res)>1:
        res[-2]+=" and "
        res[-2]="".join(res[-2:])
        res.pop()
#    print(res)
#    print(len(res))
#        res[-1]+="".join(f'{num_seconds if len(num_seconds)>0 else ""}')
#    if len(res)==0 and len(num_seconds)>0:
#        res.append("".join(f'{num_seconds if len(num_seconds)>0 else ""}'))
#    if len(num_seconds)>0:
#        res.append("".join(f'{num_seconds if len(num_seconds)>0 else ""}'))
#    print(num_years,num_days,num_hours,num_minutes,num_seconds, sep=", ")
#    print(y,d,h,m,s)
    res=", ".join(res)
#    print(res)
    return res

print(format_duration(0)) # 1 second
print(format_duration(1)) # 1 second
print(format_duration(62)) # 1 minute and 2 seconds
print(format_duration(120)) # 2 minutes
print(format_duration(3600)) # 1 hour
print(format_duration(3662)) # 1 hour, 1 minute and 2 seconds
print(format_duration(3234656345662)) # 1 hour, 1 minute and 2 seconds
