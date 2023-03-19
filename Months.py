long_months = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
short_months = ['april', 'june', 'september', 'november']

month = input("Enter a month: ").lower()

if month == "february":
    print('{0} has 28 or 29 days.'.format(month))
elif month in long_months:
    print('{0} has 31 days.'.format(month))
elif month in short_months:
    print('{0} has 30 days.'.format(month))
else:
     print(f'{month} is not a valid month. These are the months I know: {", ".join(long_months)}, { ", ".join(short_months) } and february.' )
