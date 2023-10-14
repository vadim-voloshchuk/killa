import requests
import bs4


# url = 'http://pogoda-service.ru/archive_gsod.php'
url = 'http://pogoda-service.ru/ajax_dwh_gsod.php?country=RS'

file = open('russian_stations.txt','wt')

res = requests.get(url)
full_lst = res.content.decode('utf-8').split(';')
full_lst.pop()
for each in full_lst:
    st = each.index('(')+1
    en = each.rindex(')')
    one = each[st:en]
    print(one)
    ls = one.split(',')
    print(ls)
    station = ls[0].lstrip("'").rstrip("'")
    station_id = ls[1].lstrip("'").rstrip("'")
    print(station, station_id)
    file.write(f'{station}\t{station_id}\n')
    print('Успешно записано!')

file.close()
