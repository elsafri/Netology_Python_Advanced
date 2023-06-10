import requests
import bs4
from fake_headers import Headers
from pprint import pprint
test = []
keywords = ['Flask','Django']
raw_title_list = []
results_list = []
headers = Headers(browser='firefox', os='win').generate()
base_url = 'https://spb.hh.ru'
url = base_url + '/search/vacancy?text=python&area=1&area=2'

python_page_html = requests.get(url, headers=headers).text
python_page_html_soup = bs4.BeautifulSoup(python_page_html,'lxml')
div_main_info_tag = python_page_html_soup.find('main', class_='vacancy-serp-content')

a_tag = div_main_info_tag.find_all('a', class_='serp-item__title')
for results in a_tag:
    title = results.text
    title_split = title.split()
    for ti_sp in title_split:
        for i in range(len(keywords)):
            if keywords[i] in ti_sp:
                results_list.append(title)
                i += 1

span_tag = div_main_info_tag.find_all('span', class_='bloko-header-section-3')
for info in span_tag:
    salary = info.text
    salary_split = salary.split()
    for money in salary:
        if 'USD' in money:
            raw_title_list.append(salary)
        else:
            test.append(salary)






if __name__ == '__main__':
  print(test)


