import matplotlib.pyplot as plt
import config



def plt_show():
    x = config.numbers_int
    y = config.strings_for_plt
    
    plt.figure(figsize=(8, 5))
    bars = plt.bar(y, x, label=f"{config.text_for_plt}")
    
    for bar, value in zip(bars, x):
        plt.text(bar.get_x() + bar.get_width() / 2, value, str(value), ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    plt.xlabel('Опыт')
    plt.ylabel('Кол-во ваканский')
    plt.title(f'Анализ ваканский, {config.city_string_for_plt}')
    plt.legend()
    plt.show()

