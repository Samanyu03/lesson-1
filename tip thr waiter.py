def bill (bill_amount,tip_perc):
    total=bill_amount*(1+.01*tip_perc)
    total=round(total,2)
    
    print(f"the new total is {total}")
bill(140,50)