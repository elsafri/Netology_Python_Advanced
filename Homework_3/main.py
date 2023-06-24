import requests
from fake_headers import Headers
import bs4
import json

result_list = []


def get_headers():
    return Headers(browser='firefox', os='win').generate()


url = 'https://spb.hh.ru/search/vacancy'
params = {
    'area': (1, 2),
    'text': 'python django flask',
    'page': 0
}
try:
    while True:
        hh_html = requests.get(url=url, params=params, headers=get_headers()).text
        hh_soup = bs4.BeautifulSoup(hh_html, 'lxml')
        print(f'Собираем вакансии со страницы {params["page"]}')
        params['page'] += 1
        tag_content = hh_soup.find('div', id='a11y-main-content')
        div_item_tags = tag_content.find_all('div', class_='serp-item')

        for div_item_tag in div_item_tags:
            vacancy = div_item_tag.find('h3')
            link = vacancy.find('a').get('href')
            try:
                salary = div_item_tag.find('span', class_='bloko-header-section-3').text.replace('\u202f', '')
            except:
                salary = 'Зарплата не указана'
            company = div_item_tag.find('a', class_='bloko-link bloko-link_kind-tertiary').text.replace('\xa0', '')
            city = div_item_tag.find('div', class_='vacancy-serp-item__info').contents[1].contents[0]
            result_list.append(
                  {
                      "вакансия": vacancy.text,
                      "ссылка": link,
                      "компания": company,
                      "зарплата": salary,
                      "город": city
                  }

            )
except:
    pass

if __name__ == '__main__':
    with open('vacancies.json', 'w', encoding='utf-8') as f:
        json.dump(result_list, f, ensure_ascii=False, indent=5)

