import requests
from datetime import datetime
from bs4 import BeautifulSoup


class RussianWeatherArchive():
    def __init__(self):
        self.__station_ids = {}
        with open('russian_stations.txt', 'rt') as file:
            all_file_lst = file.readlines()
            for each in all_file_lst:
                lst = each.split('\t')
                self.__station_ids[lst[0]] = lst[1].rstrip('\n')

    @property
    def staton_ids(self):
        return self.__station_ids
    
    def __get_value_from_td_tag(string_with_value:str):
        type(string_with_value)
        res = string_with_value[string_with_value.index('>')+1:string_with_value.rindex('<')]
        return res

    def get_weather_arhive(self, station_name:str, end_time:str = None):
        if end_time is None:
            end_time = datetime.now().strftime('%d.%m.%Y')

        left_part_date = end_time[:end_time.rindex('.')]
        start_time = f'{left_part_date}.{int(end_time.split(".")[2])-2}'
        station_id = self.__station_ids[station_name]
        url = f'http://pogoda-service.ru/archive_gsod_res.php?country=RS&station={station_id}&datepicker_beg={start_time}&datepicker_end={end_time}&bsubmit=Посмотреть'

        text_res = requests.get(url).content.decode('utf-8')

        soup = BeautifulSoup(text_res, 'html.parser')
        td_tag = soup.find_all('td')
        td_lst = [str(each) for each in td_tag]

        table_lst = []
        for each_string_index in range(int(len(td_lst)/8)):
            
            one_string_dict = {"date": RussianWeatherArchive.__get_value_from_td_tag(td_lst[each_string_index]),
                               "max temp": RussianWeatherArchive.__get_value_from_td_tag(td_lst[each_string_index+1]),
                               "min temp": RussianWeatherArchive.__get_value_from_td_tag(td_lst[each_string_index+2]),
                               "average temp": RussianWeatherArchive.__get_value_from_td_tag(td_lst[each_string_index+3]),
                               "pressure": RussianWeatherArchive.__get_value_from_td_tag(td_lst[each_string_index+4]),
                               "wind speed": RussianWeatherArchive.__get_value_from_td_tag(td_lst[each_string_index+5]),
                               "precipitation": RussianWeatherArchive.__get_value_from_td_tag(td_lst[each_string_index+6]),
                               "effective temp": RussianWeatherArchive.__get_value_from_td_tag(td_lst[each_string_index+7])}
            
            print(each_string_index)
            
            table_lst.append(one_string_dict)
        return table_lst
    

if __name__ == '__main__':
    archive = RussianWeatherArchive()
    
    res = archive.get_weather_arhive('Таганрог')
    print(res)

# http://pogoda-service.ru/archive_gsod_res.php?country=RS&station=347200&datepicker_beg=01.01.2021&datepicker_end=31.12.2022&bsubmit=%D0%9F%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80%D0%B5%D1%82%D1%8C