needed_exp_nc = float(input())
battles_nc = int(input())

total_exp_nc = 0
num_of_battles_nc = 0

for battle_nc in range(1, battles_nc+1):
    exp_per_battle_nc = float(input())
    if battle_nc % 3 == 0:
        exp_per_battle_nc = exp_per_battle_nc * 1.15
    if battle_nc % 5 == 0:
        exp_per_battle_nc = exp_per_battle_nc * 0.90
    if battle_nc % 15 == 0:
        exp_per_battle_nc = exp_per_battle_nc * 1.05
    total_exp_nc += exp_per_battle_nc
    num_of_battles_nc = battle_nc
    if total_exp_nc >= needed_exp_nc:
        break

if total_exp_nc >= needed_exp_nc:
    print(f"Player successfully collected his needed experience for {num_of_battles_nc} battles.")
else:
    missing_exp_nc = abs(total_exp_nc - needed_exp_nc)
    print(f"Player was not able to collect the needed experience, {missing_exp_nc:.2f} more needed.")
