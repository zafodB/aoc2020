with open('5.1.input.txt', 'r', encoding='utf8') as input_file:
    input_lines = input_file.readlines()

largest_seat_id = 0
seat_ids = set()

for line in input_lines:
    row = line.strip()[:-3]
    seat = line.strip()[-3:]
    
    row = row.replace("F", "0").replace("B", "1")
    seat = seat.replace("R", "1").replace("L", "0")

    row = int(row, base=2)
    seat = int(seat, base=2)

    seat_id = row * 8 + seat

    seat_ids.add(seat_id)
    # if seat_id > largest_seat_id:
        # largest_seat_id = seat_id

    # print(str(row) + " " + str(seat))

    # break

# print(seat_ids)

all_seats = set([_ for _ in range(54, 930)])
print(all_seats - seat_ids)