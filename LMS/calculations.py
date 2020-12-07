from datetime import date,datetime


def emi_cal(principal_amt,int_rate,duration):
    r=int_rate/12/100
    c=duration*12
    emi= principal_amt*r*(((1+r)**c)/((1+r)**c-1))
    return round(emi)


def balance_remain(date_of_borrowing,emi,paid,yr):
    d=str(date.today()-date_of_borrowing)
    p=d.split()
    to_int=int(p[0])
    de=to_int/30/12
    str_deminusyr=str(round(de-yr))
    if de > yr: 
        return "Overdue by "+ str_deminusyr +" years."
    else:
        bal=str(round(((yr-de)*emi*12)-paid))
        return "Pending payment of Rs."+ bal 




