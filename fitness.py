from datetime import datetime

def main():
    gender = input("Please enter your gender (M or F):")
    birthdate = input("enter your birthdate(YYYY-MM-DD):")
    weight = float(input("enter your weight in US pounds:"))
    height = float(input("enter your height in US inches:"))

    years = compute_age(birthdate)
    kg = kg_from_lb(weight)
    cm = cm_from_in(height)
    bmi = body_mass_index(kg, cm)
    bmr = basal_metabolic_rate(gender, kg, cm, years)

    print(f"Weight (kg): {kg:.2f}")
    print(f"Height (cm): {cm:.1f}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")


def compute_age(birth_str):
   
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    years = today.year - birthdate.year

    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):

    kg = pounds * 0.45359237

    return kg


def cm_from_in(inches):
   
    cm = inches * 2.54

    return cm


def body_mass_index(weight, height):
   
    bmi =weight / (height ** 2) * 10000

    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    
    if gender == "M":

        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:

        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age

    return bmr


main()
    
    




