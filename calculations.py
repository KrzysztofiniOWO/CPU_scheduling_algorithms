import statistics as stat

class Calculations:

    def __init__(self):
        """Initialize class"""

    def calc_individual_averages(self):
        """Return average of both times of all files"""

        individual_averages_waiting_time_FCFS = []
        individual_averages_turn_around_time_FCFS = []
        individual_averages_waiting_time_LCFS = []
        individual_averages_turn_around_time_LCFS = []

        for number in range(1, 51):
            with open(f"FCFS_results/{number}.txt", "r") as f:
                sum_turn_around_time_FCFS = 0
                sum_waiting_time_FCFS = 0
                lines = [x.strip() for x in f.readlines()]
                for line in lines:
                    split_line = line.split()
                    sum_waiting_time_FCFS = sum_waiting_time_FCFS + int(split_line[2])
                    sum_turn_around_time_FCFS = sum_turn_around_time_FCFS + int(split_line[3])

                individual_averages_waiting_time_FCFS.append(sum_waiting_time_FCFS/50)
                individual_averages_turn_around_time_FCFS.append(sum_turn_around_time_FCFS/50)
                f.close()

        for number in range(1, 51):
            with open(f"LCFS_results/{number}.txt", "r") as f:
                sum_turn_around_time_LCFS = 0
                sum_waiting_time_LCFS = 0
                lines = [x.strip() for x in f.readlines()]
                for line in lines:
                    split_line = line.split()
                    sum_waiting_time_LCFS = sum_waiting_time_LCFS + int(split_line[2])
                    sum_turn_around_time_LCFS = sum_turn_around_time_LCFS + int(split_line[3])

                individual_averages_waiting_time_LCFS.append(sum_waiting_time_LCFS / 50)
                individual_averages_turn_around_time_LCFS.append(sum_turn_around_time_LCFS / 50)
                f.close()

        with open("individual_averages_FCFS.txt", "w") as f:
            for number in range(0, 50):
                f.write(f"{individual_averages_waiting_time_FCFS[number]} {individual_averages_turn_around_time_FCFS[number]}\n")
            f.close()

        with open("individual_averages_LCFS.txt", "w") as f:
            for number in range(0, 50):
                f.write(f"{individual_averages_waiting_time_LCFS[number]} {individual_averages_turn_around_time_LCFS[number]}\n")
            f.close()

    def calculate_average_of_averages(self):
        """Return average of averages of all files"""

        sum_average_waiting_times_FCFS = 0
        sum_average_turn_around_times_FCFS = 0
        sum_average_waiting_times_LCFS = 0
        sum_average_turn_around_times_LCFS = 0

        with open(f"individual_averages_FCFS.txt", "r") as f:
            lines = [x.strip() for x in f.readlines()]
            for line in lines:
                split_line = line.split()
                sum_average_waiting_times_FCFS = sum_average_waiting_times_FCFS + float(split_line[0])
                sum_average_turn_around_times_FCFS = sum_average_turn_around_times_FCFS + float(split_line[1])

            f.close()

        with open(f"individual_averages_LCFS.txt", "r") as f:
            lines = [x.strip() for x in f.readlines()]
            for line in lines:
                split_line = line.split()
                sum_average_waiting_times_LCFS = sum_average_waiting_times_LCFS + float(split_line[0])
                sum_average_turn_around_times_LCFS = sum_average_turn_around_times_LCFS + float(split_line[1])

            f.close()

        with open("calculations_average.txt", "w") as f:
            f.write(f"Average of waiting times FCFS: {sum_average_waiting_times_FCFS/50}\n")
            f.write(f"Average of turn around times FCFS: {sum_average_turn_around_times_FCFS / 50}\n")
            f.write(f"Average of waiting times LCFS: {sum_average_waiting_times_LCFS / 50}\n")
            f.write(f"Average of turn around times LCFS: {sum_average_turn_around_times_LCFS / 50}\n")
            f.close()


    def count_standard_deviation(self):
        """Return standard deviation of averages of all files"""

        individual_averages_waiting_time_FCFS = []
        individual_averages_turn_around_time_FCFS = []
        individual_averages_waiting_time_LCFS = []
        individual_averages_turn_around_time_LCFS = []

        with open(f"individual_averages_FCFS.txt", "r") as f:
            lines = [x.strip() for x in f.readlines()]
            for line in lines:
                split_line = line.split()
                individual_averages_waiting_time_FCFS.append(float(split_line[0]))
                individual_averages_turn_around_time_FCFS.append(float(split_line[1]))
            f.close()

        with open(f"individual_averages_LCFS.txt", "r") as f:
            lines = [x.strip() for x in f.readlines()]
            for line in lines:
                split_line = line.split()
                individual_averages_waiting_time_LCFS.append(float(split_line[0]))
                individual_averages_turn_around_time_LCFS.append(float(split_line[1]))
            f.close()

        with open("standard_deviation.txt", "w") as f:
            f.write(f"Standard deviation average waiting times FCFS: {stat.stdev(individual_averages_waiting_time_FCFS)}\n")
            f.write(f"Standard deviation average turn around times FCFS: {stat.stdev(individual_averages_turn_around_time_FCFS)}\n")
            f.write(f"Standard deviation average waiting times LCFS: {stat.stdev(individual_averages_waiting_time_LCFS)}\n")
            f.write(f"Standard deviation average turn around times LCFS: {stat.stdev(individual_averages_turn_around_time_LCFS)}\n")
            f.close()




