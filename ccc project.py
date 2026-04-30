# Activity Selection using Greedy Algorithm

def activity_selection(activities):
    """
    Selects maximum number of non-overlapping activities
    activities: list of tuples (start_time, finish_time)
    """
    # Sort activities based on finish time
    activities.sort(key=lambda x: x[1])
    
    selected = []
    last_finish_time = 0

    for activity in activities:
        start, finish = activity
        
        # Select activity if it doesn't overlap
        if start >= last_finish_time:
            selected.append(activity)
            last_finish_time = finish

    return selected


def get_activities():
    """Get activities input from user"""
    n = int(input("Enter number of activities: "))
    activities = []

    for i in range(n):
        print(f"\nActivity {i+1}")
        start = int(input("Start time: "))
        finish = int(input("Finish time: "))
        activities.append((start, finish))

    return activities


def display(selected):
    """Display selected activities"""
    print("\nSelected activities (max non-overlapping):")
    for i, (start, finish) in enumerate(selected, 1):
        print(f"Activity {i}: Start = {start}, Finish = {finish}")
    
    print(f"\nTotal activities selected: {len(selected)}")


def main():
    print("===== ACTIVITY SELECTION (GREEDY ALGORITHM) =====")
    
    activities = get_activities()
    
    result = activity_selection(activities)
    
    display(result)


if __name__ == "__main__":
    main()