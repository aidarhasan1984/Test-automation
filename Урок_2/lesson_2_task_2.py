def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

year_2024 = is_year_leap(2024)
year_2023 = is_year_leap(2023)

print(f"год 2024: {year_2024}")
print(f"год 2023: {year_2023}")