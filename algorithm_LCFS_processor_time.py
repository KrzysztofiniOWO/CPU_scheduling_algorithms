class algorithm_LCFS:

    def __init__(self):
        """Inicjalizacja zasobow klasy"""


    def przydzial_czasu_LCFS(self, numer):
        """Calculate waiting time and turn around time for every file"""

        waiting_and_turn_around_times = []

        data_all = self.sort_data(self.load_times(numer))

        sum_of_all = 15

        for data in data_all:
            sum_of_all = sum_of_all + data[1]

            turn_around_time = sum_of_all - data[0]

            waiting_time = turn_around_time - data[1]

            waiting_and_turn_around_times.append([waiting_time, turn_around_time])

        return waiting_and_turn_around_times


    def load_times(self, number):
        """Calculate waiting tome and turn around time for every file"""

        waiting_and_turn_around_times = []

        with open(f"data/{number}.txt", "r") as f:
            data_list = [x.split() for x in f.readlines()]

            for element in data_list:
                waiting_and_turn_around_times.append([int(element[0]), int(element[1])])

            f.close()

            return waiting_and_turn_around_times

    def sort_data(self, list_of_times):
        """Sort by reversed arrival times"""

        return_list = []

        for number in range(15, 0, -1):
            for element in list_of_times:
                if element[0] == number:
                    return_list.append(element)
            return_list.sort(key=lambda x: x[0], reverse=True)

        return return_list

    def save_waiting_and_turn_around_times(self, calculations, number):
        """Save calculations to a file"""

        data = self.sort_data(self.load_times(number))

        with open(f"LCFS_results/{number}.txt", "w") as f:
            for iterator in range(0, 100):
                f.write(f"{data[iterator][0]} {data[iterator][1]} ")
                f.write(f"{calculations[iterator][0]} {calculations[iterator][1]}\n")

            f.close()
