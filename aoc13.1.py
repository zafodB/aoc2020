def open_file(location:str='13.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines

def process_input(lines: list) -> (str, list):
    return(int(lines[0].replace('\n', ''), base=10), [_ for _ in lines[1].replace('\n', '').split(',')])

departures = process_input(open_file())

earliest_departure = (None, 100000000)
for bus in departures[1]:
    if bus == 'x':
        continue
    else:
        bus_time = int(bus, base=10)
        this_departure = ((departures[0] // bus_time) + 1) * bus_time
        print(this_departure)
        if this_departure < earliest_departure[1]:
            earliest_departure = (bus, this_departure)

print(f'Earliest bus you can catch is bus number {earliest_departure[0]} that departs at {earliest_departure[1]}')
print(f'The puzzle answer is: {(earliest_departure[1]-departures[0])*int(earliest_departure[0])}')
