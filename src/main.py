import numpy as np
from itertools import combinations

def assign_customers_dp(cost_matrix, representatives):
    n = len(cost_matrix)  # Temsilci ve müşteri sayısı
    dp = [float('inf')] * (1 << n)  # DP tablosu
    dp[0] = 0  # Başlangıç durumu
    trace = [-1] * (1 << n)  # Önceki durumları izlemek için

    for mask in range(1 << n):  # Tüm durumları dolaş
        x = bin(mask).count('1')  # Atanan müşteri sayısı
        if x >= n:
            continue
        for j in range(n):
            if not (mask & (1 << j)):
                new_mask = mask | (1 << j)
                new_cost = dp[mask] + cost_matrix[x][j]
                if new_cost < dp[new_mask]:
                    dp[new_mask] = new_cost
                    trace[new_mask] = (mask, j)

    assignments = [-1] * n  # Müşteri atamaları
    assigned_reps = [-1] * n  # Temsilci isimleri
    mask = (1 << n) - 1

    for i in range(n - 1, -1, -1):
        if trace[mask] is None:
            break
        prev_mask, assigned_j = trace[mask]
        assignments[i] = assigned_j + 1  # 1'den başlayan temsilci numarası
        assigned_reps[i] = representatives[assigned_j]
        mask = prev_mask

    return dp[-1], list(zip(assignments, assigned_reps))

def select_campaigns(campaigns, budget):
    best_value, best_combination = 0, []
    for r in range(1, len(campaigns) + 1):
        for subset in combinations(campaigns, r):
            cost = sum(c["cost"] for c in subset)
            roi = sum(c["roi"] for c in subset)
            if cost <= budget and roi > best_value:
                best_value, best_combination = roi, subset
    return best_value, [c["id"] for c in best_combination]

# Örnek maliyet matrisi (Temsilciler x Müşteriler)
cost_matrix = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

representatives = ["Ahmet", "Mehmet", "Ayşe", "Fatma"]  # Temsilci isimleri

# Kampanya listesi
campaigns = [
    {"id": 1, "cost": 50, "roi": 60},
    {"id": 2, "cost": 30, "roi": 40},
    {"id": 3, "cost": 20, "roi": 50},
    {"id": 4, "cost": 40, "roi": 80},
    {"id": 5, "cost": 10, "roi": 30}
]

budget = 70  # Bütçe limiti

min_cost, assignments = assign_customers_dp(cost_matrix, representatives)
best_roi, selected_campaigns = select_campaigns(campaigns, budget)

print(f"Toplam Kazanç: {best_roi}")
print("Yönlendirme:")
for i, (rep_id, rep_name) in enumerate(assignments, 1):
    print(f"Müşteri {i} -> Temsilci {rep_id} ({rep_name})")
print("\nPazarlama Kampanyası Seçimi:")
print(f"Maksimum ROI: {best_roi}")
print(f"Seçilen Kampanyalar: {selected_campaigns}")