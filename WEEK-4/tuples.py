# Tuple is data type you can write with ()
# tuple has order
# index to acces the items
# unchangable(unmutable)

print(())
print(type(()))
t = tuple()
print(t)
print(type(t))

years = (2012, 2012, 2015, 2016, 2016, 2016,2019, 2019, 2019, 2020, 2021, 2022)
print(years[0])
print(years[1])
print(years[-1])


print(2023 in years)
start_year  = 2010
for year in years:
    print(f'how many items {year}', years.count(year), years.index(year))
    print(year - start_year)


tp1 = (1,2, 3)
tp2 = (4, 5, 6)
print(tp1 + tp2)

nordic_countries = ('Finland','Sweden','Norway','Denmark', 'Iceland')
scandinavian_countries = nordic_countries[1:]
print(scandinavian_countries)
print(nordic_countries[1:4])
print(list(nordic_countries))

