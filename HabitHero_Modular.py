# --- Habit Hero Weekly Tracker (Refactored) ---
# Habit Hero Modular Version
# Tracks weekly habits using modular functions.        ** NOTE use split view with original to see what needs to be changed for modularizing **


SLEEP_ENERGY_MULTIPLIER = 9                 #  Constants 
EFFORT_ENERGY_MULTIPLIER = 0.5

EXERCISE_POINTS = 20
MEDITATION_POINTS = 15
CHORES_HIGH_POINTS = 15
CHORES_MEDIUM_POINTS = 10
CHORES_LOW_POINTS = 5


def get_yes_no(prompt):         # Input Validation Functions 

    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'yes' or user_input == 'no':
            return user_input
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def get_positive_int(prompt):

    while True:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Invalid input. Please enter a number greater than 0.")

def collect_day_data(day_number):       # Data Collection Function
    print(f"\n--- Day {day_number} ---")
    
    exercised = get_yes_no("Have you exercised today? (yes/no): ")
    meditated = get_yes_no("Did you meditate today? (yes/no): ")
    total_chores = get_positive_int("How many chores do you have? (> 0): ")
    
    while True:
            chores_completed = int(input(f"How many chores have you completed? (0 to {total_chores}): "))
            if 0 <= chores_completed <= total_chores:
                break
            else:
                print(f"Error: Number must be between 0 and {total_chores}.")

    hours_slept = get_positive_int("How many hours of sleep did you get last night? > 0: ")
    
    return exercised, meditated, total_chores, chores_completed, hours_slept


def calculate_habit_points(exercised, meditated, total_chores, chores_completed):
    points = 0                          # Calculation Functions 
    
    if exercised == 'yes':
        points += EXERCISE_POINTS
    if meditated == 'yes':
        points += MEDITATION_POINTS
        
    if total_chores > 0:                    # Calculate chore points
        chores_percentage = (chores_completed / total_chores) * 100
    else:
        chores_percentage = 0
        
    if chores_percentage >= 80:
        points += CHORES_HIGH_POINTS
    elif chores_percentage >= 50:
        points += CHORES_MEDIUM_POINTS
    elif chores_percentage > 0:
        points += CHORES_LOW_POINTS
        
    return points, chores_percentage

def calculate_energy_balance(habit_points, hours_slept):

    sleep_balance = hours_slept * SLEEP_ENERGY_MULTIPLIER
    habit_balance = habit_points * EFFORT_ENERGY_MULTIPLIER
    return sleep_balance - habit_balance

def get_hero_day(exercised, meditated, completion_percent):

    is_active = (exercised == 'yes')
    is_calm = (meditated == 'yes')
    is_responsible = (completion_percent >= 80)
    
    return is_active and is_calm and is_responsible

def update_streak(current_streak, is_hero):     # Tracking Functions (Extra Credit)

    if is_hero:
        return current_streak + 1
    else:
        return 0

def update_best_worst(day, energy_balance, best_day, best_balance, worst_day, worst_balance):

    if energy_balance > best_balance:           # Check for new best
        best_balance = energy_balance
        best_day = day
        
    if energy_balance < worst_balance:         # Check for new worst
        worst_balance = energy_balance
        worst_day = day
        
    return best_day, best_balance, worst_day, worst_balance

def print_weekly_summary(name, total_points, total_sleep, total_energy, balance_days, hero_days, longest_streak, 
    best_day, best_bal, worst_day, worst_bal):              # Output Function

    avg_energy = total_energy / 7           # Calculate Averages
    avg_sleep = total_sleep / 7

    print("\n" + "=" * 40)                  # Print Weekly Summary; this structure kept from original
    print(f"{name}'s Weekly Summary!")
    print("=" * 40 + "\n")
    print("--- Totals ---")
    print(f"Total Habit Points: {total_points}")
    print(f"Total Sleep Hours: {total_sleep} hours")
    print(f"Total Energy Balance: {total_energy:.1f}\n")
    print("--- Averages ---")
    print(f"Average Daily Energy Balance: {avg_energy:.1f}")
    print(f"Average Sleep Per Night: {avg_sleep:.1f} hours")
    print(f"Days with Positive Energy: {balance_days} / 7 days\n")
    print("--- Hero Status ---")
    print(f"Hero Status Days: {hero_days} / 7 days")
    print(f"Longest Hero Streak: {longest_streak} days\n")
    print("--- Energy Highlights ---")
    print(f"Best Energy Day: Day {best_day} (Balance: {best_bal:.1f})")
    print(f"Worst Energy Day: Day {worst_day} (Balance: {worst_bal:.1f})")
    print("\n" + "=" * 40)
    print("--- Analysis Complete ---")
    print("=" * 40 + "\n")


def main():
    print("\n" + "=" * 45)
    print("--- Welcome to Habit Hero Weekly Checkin! ---")
    print("=" * 45 + "\n")
    hero_name = input("What is your Hero name? ")
    print("=" * 45)
    print(f"\nWelcome, {hero_name}! Let's Begin!\n")
    print("=" * 45)

    total_habit_points = 0              # Initialize Accumulators
    total_sleep_hours = 0
    total_energy_balance = 0.0
    total_balance_days = 0
    total_hero_status_days = 0

    current_hero_streak = 0                 # Initialize Streak Variables
    longest_hero_streak = 0

    best_energy_balance = 0.0               # Initialize Best/Worst Variables (Will be set on Day 1)
    worst_energy_balance = 0.0
    best_day = 0
    worst_day = 0

    for day in range(1, 8):         # Main Loop (7 Days)
        
        exercised, meditated, total_chores, chores_completed, hours_slept = collect_day_data(day)    # Collect Data

        habit_points, chores_percent = calculate_habit_points(exercised, meditated, total_chores, chores_completed)
        energy_balance = calculate_energy_balance(habit_points, hours_slept)                            
        hero_status_today = get_hero_day(exercised, meditated, chores_percent)          # Calculate Daily Stats

        total_habit_points += habit_points                      # Update Weekly Totals
        total_sleep_hours += hours_slept
        total_energy_balance += energy_balance
        if energy_balance > 0:
            total_balance_days += 1

        if hero_status_today:                       # Update Streaks (Extra Credit)
            total_hero_status_days += 1
            
        current_hero_streak = update_streak(current_hero_streak, hero_status_today)
        
        if current_hero_streak > longest_hero_streak:
            longest_hero_streak = current_hero_streak

        if day == 1:                                # Update Best/Worst (Extra Credit)
            best_energy_balance = energy_balance
            worst_energy_balance = energy_balance
            best_day = day
            worst_day = day
        else:
            best_day, best_energy_balance, worst_day, worst_energy_balance = update_best_worst(
                day, energy_balance, best_day, best_energy_balance, worst_day, worst_energy_balance
            )

        print("\n--- Daily Summary ---")                    # Print Daily Summary
        print(f"Habit Points Earned: {habit_points}")
        print(f"Energy Balance: {energy_balance:.1f}")
        if hero_status_today:
            print("Status: HERO STATUS ACHIEVED!")
        else:
            print("Status: Good Effort!")
            
    print_weekly_summary(hero_name, total_habit_points, total_sleep_hours, total_energy_balance,        # End of Week            
    total_balance_days, total_hero_status_days, longest_hero_streak, best_day, best_energy_balance,
    worst_day, worst_energy_balance)             

if __name__ == "__main__":
    main()