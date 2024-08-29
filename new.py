import datetime

class StepCounter:
    def __init__(self):
        self.steps = 0
        self.log = {}

    def add_steps(self, steps):
        self.steps += steps
        self.log[datetime.date.today()] = self.steps

    def get_total_steps(self):
        return self.steps

    def get_daily_log(self):
        return self.log

def main():
    step_counter = StepCounter()

    while True:
        print("1. Add steps")
        print("2. View total steps")
        print("3. View daily log")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            steps = int(input("Enter number of steps: "))
            step_counter.add_steps(steps)
        elif choice == "2":
            print("Total steps:", step_counter.get_total_steps())
        elif choice == "3":
            print("Daily log:")
            for date, steps in step_counter.get_daily_log().items():
                print(f"{date}: {steps} steps")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()