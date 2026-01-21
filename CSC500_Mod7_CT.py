def main():
    # Dictionary 1: Course Number -> Room Number
    rooms = {
        'CSC101': '3004',
        'CSC102': '4501',
        'CSC103': '6755',
        'NET110': '1244',
        'COM241': '1411'
    }

    # Dictionary 2: Course Number -> Instructor
    instructors = {
        'CSC101': 'Haynes',
        'CSC102': 'Alvarado',
        'CSC103': 'Rich',
        'NET110': 'Burke',
        'COM241': 'Lee'
    }

    # Dictionary 3: Course Number -> Meeting Time
    times = {
        'CSC101': '8:00 a.m.',
        'CSC102': '9:00 a.m.',
        'CSC103': '10:00 a.m.',
        'NET110': '11:00 a.m.',
        'COM241': '1:00 p.m.'
    }

    # Get user input
    course = input("Enter a course number (e.g., CSC101): ").strip()

    # Look up and display the information
    if course in rooms:
        print(f"\nDetails for {course}:")
        print(f"{'Room:':<12} {rooms[course]}")
        print(f"{'Instructor:':<12} {instructors[course]}")
        print(f"{'Time:':<12} {times[course]}")
    else:
        print(f"\nCourse '{course}' was not found in our records.")

if __name__ == "__main__":
    main()