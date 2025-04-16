from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP
from pyautogui import moveTo, dragTo, screenshot
from win32api import mouse_event, SetCursorPos
from keyboard import is_pressed, write, wait
from selenium.webdriver.common.by import By
from random import randint, uniform, choice
from selenium import webdriver
from time import sleep

"""
nok_exchange_rate = 11.7632
usd_exchange_rate = 1.079

driver = webdriver.Edge()
driver.get('https://neal.fun/sun-vs-moon')
driver.maximize_window()


def calc_hysa_yearly(years, yearly_rate, investment_per_year):
    fraction = yearly_rate / 100
    invs_after_rate = [investment_per_year + investment_per_year * fraction]

    for i in range(years - 1):
        invs_after_rate.append(invs_after_rate[-1] + invs_after_rate[-1] * fraction)

    print(f'{round(invs_after_rate[-1] - investment_per_year, 2):,}')
    return round(invs_after_rate[-1] - investment_per_year, 2)

def calc_hysa(years, yearly_rate, investment):
    fraction = yearly_rate / 100
    invs_after_rate = [investment + investment * fraction]

    for i in range(years - 1):
        invs_after_rate.append(invs_after_rate[-1] + invs_after_rate[-1] * fraction)
    
    print(f'Raw: {round(invs_after_rate[-1] - investment, 2):,}')
    print(f'W/ Investment: {round(invs_after_rate[-1], 2):,}')
    return round(invs_after_rate[-1] - investment, 2)

def sandp_500(upfront_investment, monthly_investment, years):
    yearly_rate = 0.109
    monthly_rate = yearly_rate / 12
    months = years * 12
    yearly_investment = monthly_investment * 12
    total = upfront_investment

    for i in range(months):
        total += monthly_investment
        total *= (1 + monthly_rate)
    
    print(f'With Investing: {round(total, 2):,}')
    print(f'Without Investing: {round(yearly_investment * years, 2):,}')
    print(f'Difference: {round(total - yearly_investment * years, 2):,}')
    return round(total, 2)

def calc_gov_bonds_10_yrs(years, investment):
    ten_yr_rate = 0.03638
    ten_yr_return = investment * ten_yr_rate

    print(f'{round(ten_yr_return, 2):,}')
    return round(ten_yr_return, 2)

def calc_etfs(years, investment):
    rate = 0.22

    print(f'{round(investment * rate * years, 2):,}')
    return round(investment * rate * years, 2)   

def find_monthly_salary(hourly_pay, daily_hr):
    daily_earn = hourly_pay * daily_hr
    monthly_salary = daily_earn * 10

    print(f'{round(monthly_salary, 2):,}€')
    print(f'${round(monthly_salary * usd_exchange_rate, 2):,}')
    print(f'{round(monthly_salary * nok_exchange_rate):,} kr')

def eur_to_nok(euro):
    print(f'{round(euro * nok_exchange_rate, 2):,}')
    return round(euro * nok_exchange_rate, 2)

def nok_to_eur(nok):
    print(f'{round(nok / nok_exchange_rate, 2):,}')
    return round(nok / nok_exchange_rate, 2)

def eur_to_usd(euro):
    print(f'{round(euro * usd_exchange_rate, 2):,}')
    return round(euro * usd_exchange_rate, 2)

def usd_to_eur(usd):
    print(f'{round(usd / usd_exchange_rate, 2):,}')
    return round(usd / usd_exchange_rate, 2)

def num_combinations(choice_amt, length):  # 1st is for example 26 for alphabet, 2nd is length of code (4 letters).
    original_choice_amt = choice_amt

    for i in range(length - 1):
        choice_amt *= original_choice_amt

    print(f'{round(choice_amt, 2):,}')
    return round(choice_amt, 2)

def savings_goal(investment, quarter_yearly_rate, goal):
    fraction_rate = quarter_yearly_rate / 100
    total = investment
    years = 0

    while total < goal:
        total += total * fraction_rate
        years += 0.25

    print(f'{round(years, 2):,}')
    return round(years, 2)

# Identifier:
# E1CFAC71-A97B-4CB8-A5AB-53C6F52C22C4

# Recovery Key:
# 496903-396847-363693-524293-615263-149611-702042-465102

def tax_calculator(country_code, income):
    income_copy = int(income * nok_exchange_rate)
    common_tax_rate = 22  # Common Tax - 22%
    nic_rate = 7.8  # National Insurance Contribution - 7.8%
    yearly_income = income * 12

    if country_code.upper() == 'N':
        if yearly_income <= 208_050:
            bracket_tax_rate = 0
        elif 208_051 <= yearly_income >= 292_850:
            bracket_tax_rate = 1.7
        elif 292_851 <= yearly_income >= 670_000:
            bracket_tax_rate = 4
        elif 670_001 <= yearly_income >= 937_900:
            bracket_tax_rate = 13.6
        elif 937_901 <= yearly_income >= 1_350_000:
            bracket_tax_rate = 16.6
        else:
            bracket_tax_rate = 17.6
        
        income_copy -= income_copy * (bracket_tax_rate / 100)
        income_copy -= income_copy * (nic_rate / 100)
        income_copy -= income_copy * (common_tax_rate / 100)
        result = round(income_copy / nok_exchange_rate, 2)

        print(f'{result:,}')
        return result

def click(x, y):
    SetCursorPos((x, y))
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.01)
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)

def catclicker():
    while not is_pressed('q'):
        pos_x = randint(0, 1271) # 0, 2542 # Half: 0, 1271
        pos_y = randint(115, 1363) # 115, 1363 # Half: 115, 682

        click(pos_x, pos_y)

def autoclicker():
    while not is_pressed('q'):
        mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.01)
        mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)

        sleep(uniform(0.01, 0.05))

def autoclicker_amt(click_amt):
    for i in range(click_amt):
        mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.01)
        mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)

        if is_pressed('q'):
            quit()

def autoclicker_no_limit():
    while not is_pressed('q'):
        mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
        mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)

def chance_in_row(chance, times):
    fraction = chance / 100
    for i in range(times):
        fraction *= fraction
    
    final_chance = fraction * 100

    print(f'{round(final_chance, 2)}')
    return f'{round(final_chance, 2)}'

def typing(text):
    write(text, delay=0.02)

def sun_vs_moon():
    moon = driver.find_element(By.ID, 'moon-btn')
    cookies = driver.find_element(By.CSS_SELECTOR, 'body > div.fc-consent-root > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-consent.fc-primary-button > p')

    sleep(3)
    cookies.click()

    sleep(1)
    while True:
        moon.click()

def convert_temps():
    c_or_f = input('''Would you like to convert to:
    1. Celsius
    or
    2. Fahrenheit?\n''')
    
    if c_or_f == "1":
        fahrenheit_amt = input('How many Fahrenheit? ')
        return (float(fahrenheit_amt) - 32) * 5 / 9
    elif c_or_f == "2":
        celsius_amt = input('How many Celsius? ')
        return float(celsius_amt) * (9 / 5) + 32
"""



# Vienna, AT -> Maribor, SLO -> Zagreb, HR -> Sarajevo, BIH -> Budapest, H -> Bratislava, SK -> Brno, CZ -> Prague, CZ
# -> Warsaw, PL -> Berlin, D -> Amsterdam, NL -> Brussels, B -> Paris, F -> Dijon, F -> Zürich, CH -> Milan, I -> Turin,
# I -> Nice, MC -> Marseille, F -> Avignon, F -> Montpellier, F -> Béziers, F -> Andorra la Vella, AND -> Huesca, E ->
# Zaragoza, E -> Madrid, E -> Cáceres, E -> Badajoz, E -> Lisbon, P -> Porto, P -> Vigo, P -> Oviedo, E -> Bilbao, E ->
# Pau, F -> Bordeaux, F -> Nantes, F -> Quimper, F -> Morlaix, F -> Rennes, F -> Rouen, F -> Amiens, F -> Calais, F ->
# Dover, GB -> London, GB -> Cambridge, GB -> Peterborough, GB -> Leicester, GB -> Derby, GB -> Nottingham, GB ->
# Sheffield, GB -> Manchester, GB -> York, GB -> Middlesbrough, GB -> Newcastle, GB -> Vienna, AT
# 133 hr Roadtrip
