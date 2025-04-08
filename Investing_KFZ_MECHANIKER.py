import random
import time

def run_sim():
    global monthly_salary
    global work_years

    work_years = 65 - 19
    monthly_salary = 2219 # in €
    yearly_income = monthly_salary * 14
    if yearly_income >= 13308:
        tax_rate = 0.0
    elif 13308 < yearly_income <= 21617:
        tax_rate = 0.2
    elif 21617 < yearly_income <= 35836:
        tax_rate = 0.3
    elif 35835 < yearly_income <= 69166:
        tax_rate = 0.3
    elif 69166 < yearly_income <= 103072:
        tax_rate = 0.48
    elif 103072 < yearly_income <= 1_000_000:
        tax_rate = 0.5
    elif yearly_income > 1_000_000:
        tax_rate = 0.55
    
    monthly_salary *= (1 - tax_rate)
    monthly_salary -= (monthly_salary * 0.18125)

    lehr_years = 4
    monthly_salary_lehre = [835, 1022, 1261, 1639]
    yearly_income_lehre = [x * 12 for x in monthly_salary_lehre]

    income_investing = [yearly_income]  # To track investment during loop
    income = [yearly_income]
    invested_amount = 0

    income_lehre = [yearly_income_lehre]
    invested_amount_lehre = 0

    for i in range(lehr_years):
        yearly_income_lehre[i] *= 1.03
        yearly_investment_lehre *= 1.2
        invested_amount_lehre += yearly_investment_lehre
        invested_amount_lehre *= random.uniform(0.93, 1.25)
        total_income_lehre = yearly_income_lehre + invested_amount_lehre
        income_lehre.append(total_income_lehre)

    for i in range(work_years):
        yearly_income_investing = monthly_salary * 12
        yearly_income_investing *= 1.03
        yearly_investment *= 1.2
        invested_amount += yearly_investment  # Add new investment
        invested_amount *= random.uniform(0.93, 1.25)  # Apply growth to invested amount
        total_income = yearly_income + invested_amount  # Combine yearly income and investments
        income_investing.append(total_income)
    
    for i in range(work_years):
        yearly_income *= 1.03

    without_investing = round(yearly_income, 2)
    with_investing = round(income[-1], 2)
    diff = round(income[-1] - without_investing, 2)

    return without_investing, with_investing, diff

without_investing = []
with_investing = []
differences = []

def results_of_sims():
    for i in range(1_000_000):
        no_investing, investing, diff = run_sim()
        without_investing.append(no_investing)
        with_investing.append(investing)
        differences.append(diff)

start = time.time()
results_of_sims()
end = time.time()
print(f'Time taken: {round(end - start, 2):,} sec\n')

worst = sorted(with_investing)
best = sorted(with_investing, reverse=True)

try:
    print(f'Without Investing: {round(without_investing[0], 2):,}')
    print(f'Avg with Investing: {round(sum(with_investing) / len(with_investing), 2):,}')
    print(f'Worst with Investing: {round(worst[0], 2):,}')
    print(f'Best with Investing: {round(best[0], 2):,}')
    print(f'Avg Diff: {round(sum(differences) / len(differences), 2):,}')
except IndexError:
    pass