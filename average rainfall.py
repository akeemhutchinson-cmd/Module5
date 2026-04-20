years = int(input ("How many years: "))
months = 12
total_rainfall = 0

for year in range(years):
    for month in range(months):
        m = float(input("inches of rain: "))
        total_rainfall += m
cumaverage = total_rainfall / (years * months)

print ("Total months: ", months * years)
print ("total inches of rainfall: ",total_rainfall)
print (f"Average rainfall was {cumaverage} inches of rain over a {months * years} period")

