import create_data as data
import algorithm_FCFS_processor_time as FCFS
import algorithm_LCFS_processor_time as LCFS
import calculations as calc

data_creation = data.Data()
algorithm_FCFS = FCFS.algorithm_FCFS()
algorithm_LCFS = LCFS.algorithm_LCFS()
calc_data = calc.Calculations()

data_creation.create_random_data()

for number in range(1, 51):
    algorithm_FCFS.save_waiting_and_turn_around_times(algorithm_FCFS.przydzial_czasu_FCFS(number), number)
    algorithm_LCFS.save_waiting_and_turn_around_times(algorithm_LCFS.przydzial_czasu_LCFS(number), number)

calc_data.calc_individual_averages()
calc_data.calculate_average_of_averages()
calc_data.count_standard_deviation()


