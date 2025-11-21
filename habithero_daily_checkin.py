# greet user and get hero name, and habit info
# calculate habit points and energy balance

print('\nWelcome to Habit Hero!\n')
hero_name = str(input('What is your Hero name: '))
exercised = str(input('Have you exercised today? (yes/no)')).lower()
meditated = str(input('Have you meditated today? (yes/no)')).lower()
total_chores = int(input('How many chores do you have?'))
chores_completed = int(input('How many chores have you completed?')) 
hours_slept = float(input('How many hours of sleep did you get?'))

EXERCISE_POINTS = 20
MEDITATION_POINTS = 15
SLEEP_ENERGY_MULTIPLIER = 8
EFFORT_ENERGY_MULTIPLIER = .5

habit_points = 0 
if exercised == 'yes':
    habit_points += EXERCISE_POINTS 
if meditated == 'yes':
    habit_points += MEDITATION_POINTS 

chores_percentage = (chores_completed / total_chores) * 100
if chores_percentage >= 80:
    habit_points += 15
elif chores_percentage >= 50:
    habit_points += 10 
elif chores_percentage > 0:
    habit_points += 5

sleep_balance = hours_slept * SLEEP_ENERGY_MULTIPLIER
habit_balance = habit_points * EFFORT_ENERGY_MULTIPLIER
energy_balance = sleep_balance - habit_balance

is_well_restored= hours_slept > 8
is_active = exercised == 'yes'
is_calm = meditated == 'yes'
is_responsible = chores_percentage >= 80
is_balanced = energy_balance > 0

if energy_balance >= 20:
    balance_summary = "Perfectly balanced, you are working hard and recovering very well."
elif energy_balance >= 0:
    balance_summary = "Good balance today. You used your energy wisely."
else:
    balance_summary = "Running on low reserves, you should take it easy tomorrow."

if is_active and is_calm and is_responsible:
    daily_feedback = "You are a HERO! You handled body, mind, and tasks perfectly"
elif is_active or is_calm:
    daily_feedback = "Strong focus today, keep building that momentum!"
else:
    daily_feedback = "try to complete a physical or mindfulness habit tomorrow."

if not is_well_restored:
    rest_advice = "Aim for more sleep to improve tomorrows balance."
elif not is_balanced:
    rest_advice = "You worked hard today, take extra time to recharge."
else:
    rest_advice = "You're in sync, great recovery and routine!"

#output to hero
print("\n--- HABIT HERO DAILY SUMMARY ---\n")
print(f"Hero Name: {hero_name}")
print(f"Habit Points: {habit_points}")
print(f"Energy Balance: {energy_balance}")
print(f"Balance Summary: {balance_summary}") 
print(f"Daily Feedback: {daily_feedback}") 
print(f"Rest Advice: {rest_advice}") 