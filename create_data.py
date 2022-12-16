import random

class Data:

    def __init__(self):
        """Initialize class"""

    def create_random_data(self):
        """Create random data files"""
        for number in range(1, 51):

            with open(f"data/{number}.txt", "w") as f:

                for numbers in range(0, 55):
                    f.write(f"{random.randint(1,15)} {random.randint(1,15)}\n")

                for selected in self.select_random_times_of_more_processes():
                    for numbers in range(0, 15):
                        f.write(f"{selected} {random.randint(1, 15)}\n")

                f.close()

    def select_random_times_of_more_processes(self):
        """Select three random times that will receive more data than others"""

        choices = []
        if_true = True
        while if_true:
            a = random.randint(1, 15)
            if a not in choices:
                choices.append(a)

                if len(choices) == 3:
                    if_true = False

        return choices
