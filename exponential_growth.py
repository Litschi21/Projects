import matplotlib.pyplot as plt

linear = [x*24000 for x in range(58)]
exponential = [1]
exponential2 = [1]
exponential3 = [1]
exponential4 = [1]

for x in range(57):
    exponential.append((exponential[-1] + 24000) * 1.04)

for x in range(57):
    exponential2.append((exponential2[-1] + 24000) * 1.05)

for x in range(57):
    exponential3.append((exponential3[-1] + 24000) * 1.06)

for x in range(57):
    exponential4.append((exponential4[-1] + 24000) * 1.07)

print(f'Without Investing: {round(linear[-1], 2):,}')
print(f'4% rate: {round(exponential[-1], 2):,}')
print(f'5% rate: {round(exponential2[-1], 2):,}')
print(f'6% rate: {round(exponential3[-1], 2):,}')
print(f'7% rate: {round(exponential4[-1], 2):,}')

plt.plot(linear)
plt.plot(exponential)
plt.plot(exponential2)
plt.plot(exponential3)
plt.plot(exponential4)

plt.grid()
plt.show()


# def invest(start, yearly_return, monthly_add, years):
#     yearly_income = [start]

#     for i in range(years):
#         income = yearly_income[-1]
#         yearly_income.append((income + monthly_add * 12) * yearly_return)
    
#     return round(yearly_income[-1], 2)

# eighteen = invest(100, 1.04, 10, 4)
# twenty_two = invest(eighteen, 1.04, 200, 4)

# fourty = invest(twenty_two, 1.04, 2000, 18)
# fifty = invest(twenty_two, 1.04, 2000, 28)

# sixty_five = invest(twenty_two, 1.04, 2000, 43)
# seventy = invest(twenty_two, 1.04, 2000, 48)
# eighty = invest(twenty_two, 1.04, 2000, 58)

# print(f'18: {eighteen:,}')
# print(f'22: {twenty_two:,}')

# print(f'18 income: {int(eighteen) * 0.04:,}')
# print(f'22 income: {int(twenty_two) * 0.04:,}')

# print('\n')

# print(f'40: {fourty:,}')
# print(f'50: {fifty:,}')
# print(f'65: {sixty_five:,}')
# print(f'70: {seventy:,}')
# print(f'80: {eighty:,}')

# print('\n')

# print(f'40 income: {int(fourty) * 0.04:,}')
# print(f'50 income: {int(fifty) * 0.04:,}')
# print(f'65 income: {int(sixty_five) * 0.04:,}')
# print(f'70 income: {int(seventy) * 0.04:,}')
# print(f'80 income: {int(eighty) * 0.04:,}')
