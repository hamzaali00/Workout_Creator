import random

Compound_Legs = ['Barbell Squat', 'Deadlift', 'Walking Lunges']

Accessory_Legs = ['Romanian Deadlift', 'Bulgarian Split Squats', 
'Leg Press', 'Hack Squat', 'Calf Raises', 'Walking Lunges', 'Step-ups', 'Hamstring Curl', 
'Leg Extension', 'Hip Thrusts', 'Donkey Kicks']

Compound_Push = ['Bench Press', 'Overhead Press', 'Close-grip Bench Press', 'Dips', 'Incline Bench Press']

Chest = [ 'Dumbbell Press', 'Incline Dumbbell Press', 'Pec Fly', 'Pushups', 'Incline Pushups', 'Decline Pushups']

Triceps = ['Rope Pushdown', 'Close-grip Pushups', 'Tricep Kickbacks', 'Skull Crushers', 'Tricep Extensions']

Shoulders = ['Rear Delt Fly', 'Overhead Press', 'Lateral Raises', 'Face Pulls', 'Front Raises']

Compound_Back = ['Deadlift', 'Barbell Rows', 'Pull-ups', 'Chin-ups']

Accessory_Back = ['Dumbbell Rows', 'T-bar Rows', 'Cable Rows', 'Back Extensions']

Biceps = ['Plate Curl', 'Spider Curl', 'Preacher Curl', 'Hammer Curl', 'Seated Incline Curl', 'Barbell Curl']

legs = []
Pull = []
Push = []
arms = []

def leg_day():
    workout = random.choices(Compound_Legs, k=1)
    legs.append(workout)
    workout_2 = random.choices(Accessory_Legs, k=4)
    legs.append(workout_2)
    legs_2 = sum(legs, [])
    print(legs_2)
    legs.clear()
    legs_2.clear()
    
def pull_day():
    workout = random.choices(Compound_Back, k=2)
    Pull.append(workout)
    workout_2 = random.choices(Accessory_Back, k=2)
    Pull.append(workout_2)
    workout_3 = random.choices(Biceps, k=2)
    Pull.append(workout_3)
    Pull_2 = sum(Pull, [])
    print(Pull_2)
    Pull.clear()
    Pull_2.clear()

def push_day():
    workout = random.choices(Compound_Push, k=2)
    Push.append(workout)
    workout_2 = random.choices(Chest, k=2)
    Push.append(workout_2)
    workout_3 = random.choices(Triceps, k=2)
    Push.append(workout_3)
    Push_2 = sum(Push, [])
    print(Push_2)
    Push.clear()
    Push_2.clear()

def arm_day():
    workout = random.choices(Biceps, k=2)
    arms.append(workout)
    workout_2 = random.choices(Triceps, k=2)
    arms.append(workout_2)
    workout_3 = random.choices(Shoulders, k=2)
    arms.append(workout_3)
    arms_2 = sum(arms, [])
    print(arms_2)
    arms.clear()
    arms_2.clear()

workout_type = input('What would you like to workout today?')

if workout_type == 'legs':
    leg_day()
elif workout_type == 'push':
    push_day()
elif workout_type == 'pull':
    pull_day()
elif workout_type == 'arms':
    arm_day()