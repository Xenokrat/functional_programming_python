# Введение в функциональное программирование на Python. Урок 1

## 1. Пример избавления от промежуточных значений

Имеем скрипт на `python`, в котором проверяется, что все страны из списка `countries`
существуют в базе данных.

```python
def get_country_data() -> str:
    current_time = datetime.utcnow()
    monitoring_date = (datetime.utcnow() - timedelta(days=1)).strftime("%d-%m")
    alert_text = (f"*ALERT*: The database time is: "
                f"_{current_time.strftime('%d.%m %H:%M')}_\n"
                f"One or more countries are missing from database in "
                f"_{monitoring_date}_:\n")
```

Для этого вводится переменная `alert_text`, которая в ходе работы скрипта "обрастает"
дополнительными значениями по мере того, как проверяются данные.

```python
def get_country_data() -> str:
    ...
    for platform in current_country_dict:
        default_country_set = default_country_dict[platform] 
        current_country_set = current_country_dict[platform]

        if default_country_set != current_country_set:
            missing_countries = default_country_set - current_country_set
            alert_text += f"\n*{platform}*:\n"
            alert_text += "\n".join(missing_countries)
            alert_text += "\n----------------------------"
```

Таким образом мы храним промежуточные значения в переменной `alert_text` и
изменяем значение этой переменной по мере работы скрипта.

Как можно было бы избавиться от хранения промежуточных результатов в данном случае?
Можно было бы попробовать разбить все составляющие текста в `alert_text` на
небольшие функции, и затем соединить результат:

```python
def get_base_alert_text() -> str:
    return (
        f"*ALERT*: The database time is: "
        f"_{datetime.utcnow().strftime('%d.%m %H:%M')}_\n"
        f"One or more countries are missing from database in "
        f"_{(datetime.utcnow() - timedelta(days=1)).strftime("%d-%m")}_:\n"
    )

def get_missing_countries_by_platform() -> tuple[str, set[str]]:
    return (
        (platform, default_country_set - current_country_set)
        for default_country_set, current_country_set in zip(
            default_country_dict[platform], current_country_dict[platform]
        )
        for platform in current_country_dict
    )

def get_missing_countries_list() -> str:
    return (
        f"\n*{platform}*:\n----------------------------".join(missing_countries)
        for platform, missing_countries in get_missing_countries_by_platform()
    )

def get_alert_text() -> str:
    return get_base_alert_text() + get_missing_countries_list()
```

Полученное решение выглядит более "функциональным" и не требует хранения промежуточных
результатов.

## 2. Пример системы, где промежуточные состояния вычислений вообще никак не хранятся в явном виде

Если рассматривать решение из примера выше, то можно сказать, что возможно
создать более функциональную архитектуру таким образом, чтобы вместо
хранения промежуточных резльтатов, итоговое значение как бы получалось сразу как
результат вычесления функций (одной большой композиции из функций, как всей программы).

Тогда для программы как в примере выше мы бы заменили все проверки информации в БД на разбивку на множество функций и потом вернули бы сложенный результат их работы.
