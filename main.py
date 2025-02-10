from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from plt_settings import plt_show
import config
import re



def plus_between_words() -> str:
    string = input("Введите профессию для анализа: ")
    config.text_for_plt = string
    return string.replace(" ", "+")

def get_stats():

    text = plus_between_words()
    
    city_string = input("Введите город: ")
    config.city_string_for_plt = city_string
    
    if city_string == "Россия":
        city_number = 113
    elif city_string in ["Санкт-петербург", "Санкт-Петербург", "Спб", "СПБ"]:
        city_number = 2
    elif city_string == "Казань":
        city_number = 88
    elif city_string == "Екатеринбург":
        city_number = 3
    elif city_string == "Самара":
        city_number = 78
    
    URL = f"https://kazan.hh.ru/search/vacancy?text={text}&salary=&ored_clusters=true&enable_snippets=true&area={city_number}&page=1"
    print(f"\nВаша ссылка: {URL}")
    ua = UserAgent()
    
    # Открываем браузер с помощью Selenium
    try:
        options = Options()
        options.add_argument(f"user-agent={ua.random}")
        options.add_argument("start-maximized")
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get(URL)
        time.sleep(3)
        html = driver.page_source
        driver.quit()
    except:
        print("Ошибка открытия браузера")
        driver.quit()
    
    soup = BeautifulSoup(html, "html.parser")
    
    # Парсим все div с классом "magritte-content___-hu36_4-0-30"
    try:
        exp_label = soup.find_all("div" , class_="magritte-content___-hu36_4-0-30")
        list_of_words = []
        for num in exp_label:
            list_of_words.append(num.text.replace("\xa0", " ").replace("\u202f", ""))
        print(f"\nЛист всех спарсеных div: {list_of_words}")
        print(f"\nКоличество div: {len(exp_label)}")

        # Нужно из листа всех div отсортировать -> ['Нет опыта24', 'От 1 года до 3 лет241', 'От 3 до 6 лет716', 'Более 6 лет162']
        order = {
            "Нет опыта": 0,
            "От 1 года до 3 лет": 1,
            "От 3 до 6 лет": 2,
            "Более 6 лет": 3
        }

        def sort_key(item):
            for key in order:
                if key in item:
                    return order[key]
            return 999

        sorted_exp = sorted(list_of_words, key=sort_key)
        sorted_exp_list = sorted_exp[0:4]
        print(f"\nОтсортированный список: {sorted_exp_list}")
        
        # После отделим числа от строк, получим два списка
        strings = []
        numbers = []
        for exp in sorted_exp_list:
            num_match = re.search(r'\d+$', exp)
            if num_match:
                num = num_match.group()
                text = exp[:num_match.start()].strip()
        
                strings.append(text)
                numbers.append(num)
        
        print(f"\nСтроки: {strings}")
        config.numbers_int = [int(i) for i in numbers]
        config.strings_for_plt = strings
        print(f"\nЧисла: {config.numbers_int}")
        
    #AttributeError: 'NoneType' object has no attribute 'text'
    except:
        print(f"\nОшибка, проверьте введенное значение")

if __name__ == "__main__":
    get_stats()
    plt_show()