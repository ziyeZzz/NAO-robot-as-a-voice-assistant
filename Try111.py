Ddate = "2016 March 26"
array = Ddate.split();
year = array[0]
month = array[1]
date = array[2]
print year
print month
print date
print array
i = 0
mon = ["January","February","March","April","May","June","July","August","September","October","November","December"];
for m in mon:
    if(month == mon[i]):
        month = i+1
        if(month<10):
            month = "0"+str(month)
    i = i+1
print month
day = date +"."+month+"."+year
print day
    
