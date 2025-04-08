import random
import time

def run_sim():
    global monthly_salary
    global work_years

    work_years = 65 - 22
    monthly_salary = 6900 * 0.536 # in €

    income = [monthly_salary * 12]  # To track investment during loop
    invested_amount = 0

    for i in range(work_years):
        yearly_income_investing = monthly_salary * 12
        yearly_income_investing *= 0.03
        yearly_investment = yearly_income_investing * 0.2
        invested_amount += yearly_investment  # Add new investment
        invested_amount *= random.uniform(0.93, 1.25)  # Apply growth to invested amount
        total_income = yearly_income_investing + invested_amount  # Combine yearly income and investments
        income.append(total_income)
    
    for i in range(work_years):
        yearly_income *= 1.03

    without_investing = round(yearly_income * work_years, 2)
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


'''
Bachelor (46.4% Tax in Norway, 89k):
Without Investing: 1,965,625.63€
With Investing: 7,907,395.49€
Difference: 5,941,769.86€

Master's (46.4% Tax in Norway, 102k):
Without Investing: 2,268,055.06€
With Investing: 7,769,804.2€
Difference: 5,501,749.15€

PhD (46.4% Tax in Norway, just barely under the 114k w/ 112k):
Without Investing: 2,353,848.29€
With Investing: 6,361,718.8€
Difference: 4,007,870.51€


Leaderboard:
1. Bachelor w/ €7.91 mio
2. Master's w/ €7.77 mio
3. PhD w/ €4.01 mio
'''
