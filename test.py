# exp_label_elements = [exp_label[30].text.replace("\u202f", ""), exp_label[31].text.replace("\u202f", ""), exp_label[32].text.replace("\u202f", ""), exp_label[33].text.replace("\u202f", "")]
# exp_label_int = [int(i) for i in exp_label_elements]

# try:
#     exp_label = soup.find_all("div" , class_="magritte-text___pbpft_3-0-26 magritte-text_style-secondary___1IU11_3-0-26 magritte-text_typography-label-2-regular___ia7GB_3-0-26")
#     exp_dict = {
#         "Нет опыта" : int(exp_label[31].text.replace("\u202f", "")),
#         "От 1 года до 3 лет" : int(exp_label[30].text.replace("\u202f", "")),
#         "От 3 до 6 лет" : int(exp_label[32].text.replace("\u202f", "")),
#         "Более 6 лет" : int(exp_label[33].text.replace("\u202f", ""))
#     }
#     print(exp_dict)
# except:
#     print("Ошибка, проверьте введенное значение")

# exp_label_elements = [exp_label[30].text.replace("\u202f", ""), exp_label[31].text.replace("\u202f", ""), exp_label[32].text.replace("\u202f", ""), exp_label[33].text.replace("\u202f", "")]

# def plt_show():
#     x = ['Нет опыта', 'От 1 года до 3 лет', 'От 3 до 6 лет', 'Более 6 лет']

#     plt.bar(x, config.exp_label_int, label=f"{config.text_for_plt}") #Параметр label позволяет задать название величины для легенды
#     plt.xlabel('Года')
#     plt.ylabel('Кол-во ваканский')
#     plt.title('Пример столбчатой диаграммы')
#     plt.legend()
#     plt.show()

# exp_label = soup.find("div" , class_="magritte-content___-hu36_4-0-30").find("div" , "magritte-text___pbpft_3-0-26 magritte-text_style-secondary___1IU11_3-0-26 magritte-text_typography-label-2-regular___ia7GB_3-0-26")
# print(exp_label) # 12 Golang берет первую

# from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
# import time
# import datetime
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from plt_settings import plt_show
# import config
# import re



# def plus_between_words() -> str:
#     string = input("Введите профессию для анализа: ")
#     config.text_for_plt = string
#     return string.replace(" ", "+")

# def get_stats():

#     text = plus_between_words()
    
#     URL = f"https://kazan.hh.ru/search/vacancy?text={text}&salary=&ored_clusters=true&enable_snippets=true&area=113&page=1"
#     ua = UserAgent()
    
#     try:
#         options = Options()
#         options.add_argument(f"user-agent={ua.random}")
#         options.add_argument("start-maximized") # На весь экран
#         options.add_argument("--headless")  # Скрыть окно браузера
#         driver = webdriver.Chrome(options=options)
#         driver.get(URL)
#         time.sleep(3)
#         html = driver.page_source
#         driver.quit()
#     except:
#         print("Ошибка открытия браузера")
#         driver.quit()
    
#     soup = BeautifulSoup(html, "html.parser")

#     try:
#         exp_label = soup.find_all("div" , class_="magritte-content___-hu36_4-0-30")
#         list_of_words = []
#         for num in exp_label:
#             list_of_words.append(num.text.replace("\xa0", " "))
    
#         print(list_of_words[33:37])
        
#         exp_list = list_of_words[33:37]
#         strings = []
#         numbers = []
#         for exp in exp_list:
#             num_match = re.search(r'\d+$', exp)  # Ищем число в конце строки
#             if num_match:
#                 num = num_match.group()  # Получаем найденное число
#                 text = exp[:num_match.start()].strip()  # Обрезаем строку до числа
        
#                 strings.append(text)
#                 numbers.append(num)

#         print("Строки:", strings)
#         numbers_int = [int(i) for i in numbers]
#         print("Числа:", numbers_int)
        
        
            
#     #AttributeError: 'NoneType' object has no attribute 'text'
#     except:
#         print(f"Ошибка, проверьте введенное значение")

# if __name__ == "__main__":
#     get_stats()
#     # plt_show()


# list_1 = ['От 4 часов в день12', 'Неполный день10', 'Разовое задание8', 'По выходным', 'По вечерам', 'Не имеет значения', 'от 50 000 ₽227', 'от 155 000 ₽185', 'от 260 000 ₽133', 'от 365 000 ₽81', 'от 470 000 ₽37', 'от 575 000 ₽13', 'Своя зарплата', 'Указан доход227', 'Россия1142', 'Москва775', 'Санкт-Петербург163', 'Новосибирская область21', 'Республика Татарстан19', 'Программист, разработчик738', 'DevOps-инженер105', 'Руководитель группы разработки90', 'Тестировщик47', 'Другое22', 'Информационные технологии, системная интеграция, интернет871', 'Розничная торговля145', 'Услуги для бизнеса132', 'Услуги для населения96', 'СМИ, маркетинг, реклама, BTL, PR, дизайн, продюсирование94', 'Не требуется или не указано1090', 'Высшее52', 'Среднее профессиональное2', 'Не имеет значения', 'От 3 до 6 лет715', 'От 1 года до 3 лет241', 'Более 6 лет162', 'Нет опыта24', 'Полная занятость1124', 'Частичная занятость10', 'Проектная работа8', 'Волонтерство', 'Оформление по ГПХ или по совместительству56', 'Стажировка9', 'Удаленная работа566', 'Полный день557', 'Гибкий график15', 'Сменный график4', 'Вахтовый метод', 'Без вакансий от кадровых агентств1060', 'От аккредитованных ИТ-компаний520', 'С адресом455', 'Доступные людям с инвалидностью40', 'Меньше 10 откликов23', 'В названии вакансии', 'В названии компании', 'В описании вакансии']

# list_2 = ['Неполный день422', 'От 4 часов в день344', 'Разовое задание50', 'По выходным45', 'По вечерам10', 'Не имеет значения', 'от 100 000 ₽1900', 'от 200 000 ₽1020', 'от 300 000 ₽503', 'от 400 000 ₽193', 'от 500 000 ₽93', 'Своя зарплата', 'Указан доход2552', 'Россия10044', 'Москва6109', 'Санкт-Петербург1364', 'Новосибирская область271', 'Свердловская область240', 'Программист, разработчик2705', 'DevOps-инженер816', 'Тестировщик736', 'BI-аналитик, аналитик данных628', 'Аналитик531', 'Информационные технологии, системная интеграция, интернет5481', 'Финансовый сектор1523', 'Услуги для бизнеса591', 'Розничная торговля519', 'СМИ, маркетинг, реклама, BTL, PR, дизайн, продюсирование497', 'Не требуется или не указано7596', 'Высшее2443', 'Среднее профессиональное120', 'Не имеет значения', 'От 3 до 6 лет4662', 'От 1 года до 3 лет4017', 'Нет опыта757', 'Более 6 лет608', 'Полная занятость9572', 'Частичная занятость422', 'Проектная работа50', 'Волонтерство', 'Оформление по ГПХ или по совместительству569', 'Стажировка169', 'Полный день6541', 'Удаленная работа3271', 'Гибкий график190', 'Сменный график39', 'Вахтовый метод3', 'Без вакансий от кадровых агентств9586', 'С адресом5041', 'От аккредитованных ИТ-компаний3322', 'Меньше 10 откликов854', 'Доступные людям с инвалидностью494', 'В названии вакансии', 'В названии компании', 'В описании вакансии']

# print(len(list_1))
# print(len(list_2))
# print(list_1 == list_2)