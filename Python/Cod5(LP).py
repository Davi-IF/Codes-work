cig_day = int(input(" Type how many cigarettes for day: "))
years = int(input("Type how many years: " ))


qtd_days = years * 365
tot_cig = qtd_days * cig_day
lost_minutes = tot_cig * 10
lost_days = lost_minutes/1440

print(f"lost days:{lost_days}days!")