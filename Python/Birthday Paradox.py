import datetime, random


def getBirthdays(number_Birthdays):

    birthdays = []

    for i in range(number_Birthdays):
        start_Y = datetime.time (2001, 1, 1)

        random_D = datetime.timedelta (random.randint(0, 364))

        birthday = start_Y + random_D
        birthdays.append(birthday)
    return birthdays


def birthday_M(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a +1 :]):
            if birthdayA == birthdayB:
                return birthdayA


print('''It's a high chance for two people, even in a small group, having the same birthday.
This is refer as the birthday paradox. So, let's test this.
    
This is just a interest thing, it isn't a actually Paradox.''')


months = ("Jan.", "Feb.", "Mar.", "Apr.", "May.", "Jun.",
          "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec.")


while True:
    print("How many hypothetical birthdays I should generate? (Max 100)")
    answer =  input("> ")
    if answer.isdecimal() or (0 < int(answer) <= 100):
        number_B = int(answer)
        break

print("Here are", number_B, "birthdays:")
birthdays = birthday_M(number_B)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(", ", end = "")
    month_N = months(birthday.month -1)
    dateText = "{} {}".format(month_N, birthday.day)
    print(datetext, end = "")


match =  birthday_M(birthdays)

print("In this simulation, ", end = "")
if match != None:
    month_N = months(match.month -1)
    dateText = "{} {}".format(month_N, match.day)
else:
    print("There are no matching birthdays.")


print("Generating", number_B, "random birthdays 100,000 times...")
input("Press Enter to begin...")

print("Let's run another 100,000 simulations.")
simMatch = 0

for i in range(100_000):
    if i % 10_000 == 0:
        print(i, "simulations run...")
    birthdays = getBirthdays(number_B)
    if birthday_M(birthdays) != None:
        simMatch += 1

print("100,000 simulations run.")


probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', number_B, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', number_B, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')