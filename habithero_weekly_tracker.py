# --- Habit Hero Weekly Tracker ---

SLEEP_ENERGY_MULTIPLIER = 9
EFFORT_ENERGY_MULTIPLIER = 0.5

EXERCISE_POINTS = 20            # --- Point Constants ---
MEDITATION_POINTS = 15
CHORES_HIGH_POINTS = 15
CHORES_MEDIUM_POINTS = 10
CHORES_LOW_POINTS = 5

# --- Greet User and Get Info ---

print("\n" + "=" * 45)      # "=" * 45 for formatting title border
print("--- Welcome to Habit Hero Weekly Checkin! ---")
print("=" * 45 + "\n")      
hero_name = input("What is your Hero name? ")
print("=" * 45)
print(f"\nWelcome, {hero_name}! Let's Begin!\n")
print("=" * 45)


total_habit_points = 0              # We must initialize weekly totals 
total_sleep_hours = 0
total_energy_balance = 0.0
total_balance_days = 0
total_hero_status_days = 0

current_hero_streak = 0            # EC Streak tracking
longest_hero_streak = 0

best_energy_balance = 0.0         # We will initialize these on the first day
worst_energy_balance = 0.0
best_day = 0
worst_day = 0

for day in range(1, 8):                 # Start of the main Loop (7 days)
    print(f"\n Day {day}.")

    while True:                         # I like to add this to the end it takes all input and lowercases it- .lower()
        exercised = input("Have you exercised today? (yes/no): ").lower() 
        if exercised == 'yes' or exercised == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    while True:
        meditated = input("Did you meditate today? (yes/no): ").lower()
        if meditated == 'yes' or meditated == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.") 

    while True:
        total_chores = int(input("How many chores do you have? (> 0): "))        # these are all validators ^
        if total_chores >= 1:
            break
        else:
            print("Invalid input. Please enter a number greater than 0.")

    while True:
        chores_completed = int(input(f"How many chores have you completed? (0 to {total_chores}): "))
        if chores_completed < 0:
            print("Error: Number must be > 0")
        elif chores_completed > total_chores:
            print(f"Error: Number must be <= {total_chores}")
        else:
            break

    while True:
        hours_slept = int(input("How many hours of sleep did you get last night? > 0: "))
        if hours_slept >= 1:
            break
        else:
            print("Number must be > 1")

    habit_points = 0
    if exercised == 'yes':  # Calculates daily values
        habit_points += EXERCISE_POINTS  # Habit points first
    if meditated == 'yes':
        habit_points += MEDITATION_POINTS

    if total_chores > 0:
        chores_percentage = (chores_completed / total_chores) * 100
    else:
        chores_percentage = 0
    if chores_percentage >= 80:
        habit_points += CHORES_HIGH_POINTS  # Chore points next
    elif chores_percentage >= 50:
        habit_points += CHORES_MEDIUM_POINTS
    elif chores_percentage > 0:
        habit_points += CHORES_LOW_POINTS

    sleep_balance = hours_slept * SLEEP_ENERGY_MULTIPLIER           # the energy balance
    habit_balance = habit_points * EFFORT_ENERGY_MULTIPLIER
    energy_balance = sleep_balance - habit_balance

    is_active = exercised == 'yes'              # This part was fun, knowing what this does and how it works made my skin tingle.
    is_calm = meditated == 'yes'                
    is_responsible = chores_percentage >= 80

    hero_status_today = is_active and is_calm and is_responsible

    
    print("\n--- Daily Summary ---")                     # --- Daily Summary ---
    print(f"Habit Points Earned: {habit_points}")
    print(f"Energy Balance: {energy_balance:.1f}")
    if hero_status_today:
        print("Status: HERO STATUS ACHIEVED!")
    else:
        print("Status: Good Effort!")

    total_habit_points += habit_points              # Updating weekly totals
    total_sleep_hours += hours_slept
    total_energy_balance += energy_balance

    if energy_balance > 0:
        total_balance_days += 1

    if hero_status_today:                           # Updating Hero status and streaks
        total_hero_status_days += 1
        current_hero_streak += 1
    else:
        current_hero_streak = 0

    if current_hero_streak > longest_hero_streak:
        longest_hero_streak = current_hero_streak

    if day == 1:                                 # On the first day, set the initial best/worst values.
        best_energy_balance = energy_balance
        worst_energy_balance = energy_balance
        best_day = day
        worst_day = day
    else:
        if energy_balance > best_energy_balance:      # For other days, compare and update if needed.
            best_energy_balance = energy_balance
            best_day = day
        if energy_balance < worst_energy_balance:
            worst_energy_balance = energy_balance
            worst_day = day

average_energy_balance = total_energy_balance / 7   # --- Weekly Calculations ---
average_sleep_per_night = total_sleep_hours / 7

print("\n" + "=" * 40)                          # prints so many prints!!
print(f"{hero_name}'s Weekly Summary!")
print("=" * 40 + "\n")
print("--- Totals ---")
print(f"Total Habit Points: {total_habit_points}")
print(f"Total Sleep Hours: {total_sleep_hours} hours")
print(f"Total Energy Balance: {total_energy_balance:.1f}\n")
print("--- Averages ---")
print(f"Average Daily Energy Balance: {average_energy_balance:.1f}")
print(f"Average Sleep Per Night: {average_sleep_per_night:.1f} hours")
print(f"Days with Positive Energy: {total_balance_days} / 7 days\n")
print("--- Hero Status ---")
print(f"Hero Status Days: {total_hero_status_days} / 7 days")
print(f"Longest Hero Streak: {longest_hero_streak} days\n")
print("--- Energy Highlights ---")
print(f"Best Energy Day: Day {best_day} (Balance: {best_energy_balance:.1f})")
print(f"Worst Energy Day: Day {worst_day} (Balance: {worst_energy_balance:.1f})")
print("\n" + "=" * 40)
print("--- Analysis Complete ---")
print("=" * 40 + "\n")



    

    
