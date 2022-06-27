from datetime import date

WEEK0_START = date(2019, 10, 27)

LOCATIONS = {
    0 : "IN-N-OUT",
    1 : "D'Sotos Mexican Food",
    2 : "Eat Your Heart Out II",
    3 : "Papa Duke's Deli & Grill"
}

def SelectLunch(date):
    delta = date - WEEK0_START
    week = int(delta.days / 7.0)
    location = LOCATIONS[week % len(LOCATIONS)]
    return f"Week {week} we are going to {location}"

print(SelectLunch(date.today()))