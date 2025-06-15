import random

nums = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10_000, 25_000, 50_000, 75_000, 100_000, 200_000, 300_000, 400_000, 500_000, 750_000, 1_000_000]
rounds = []

for i in range(1_000_000):
    cases = [random.choice(nums) for i in range(26)]
    picked_cases = []

    start_case = random.choice(cases)
    cases.remove(start_case)

    def calculate_dealer_offer():
        avg_case = sum(cases) / len(cases)
        offer = 12275.3 + (0.748 * avg_case) + (-2714.74 * len(cases)) + (-0.040 * max(cases)) + (0.0000006986 * avg_case ** 2) + (32.623 * len(cases) ** 2)

        return round(offer / 100) * 100
    
    n = 6
    for i in range(9):
        for j in range(n):
            picked_cases.append(random.choice(cases))
            cases.remove(picked_cases[-1])
        
        deal = calculate_dealer_offer()
        if n > 1:
            n -= 1
    rounds.append(deal)

print(f'{round(sum(rounds) / len(rounds), 2):,}')

"""
Average Case: $131,477.54
Keep Case (100M rounds): $142,731.67
Accept First Offer (1M rounds): $52,857.37
Accept Second Offer (1M rounds): $64,768.87
Accept Third Offer (1M rounds): $77,345.95
Accept Fourth Offer (1M rounds): $89,729.19
Accept Fifth Offer (1M rounds): $100,788.79
Accept Sixth Offer (1M rounds): $107,813.99
Accept Seventh Offer (1M rounds): $116,688.29
Accept Eighth Offer (1M rounds): $130,045.48
Accept Last Offer (1M rounds): $160,002.36
"""
