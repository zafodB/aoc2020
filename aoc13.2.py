import math

def open_file(location:str='13.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines

def process_input(lines: list) -> (str, int, dict):
    departure_times = []

    for item in lines[1].replace('\n', '').split(','):
        if item != 'x':
            departure_times.append(int(item, base=10))
        else:
            departure_times.append('x')    

    return departure_times

# departures = process_input(open_file())
# departures = process_input(open_file('13.1.input.test.2.txt'))
departures = process_input(open_file('13.1.input.test.kvaky.txt'))

# print(departures)
# print(adjusted_departures)

# From StackOverflow: https://math.stackexchange.com/questions/2218763/how-to-find-lcm-of-two-numbers-when-one-starts-with-an-offset
def combine_phased_rotations(a_period, a_phase, b_period, b_phase):
    """Combine two phased rotations into a single phased rotation

    Returns: combined_period, combined_phase

    The combined rotation is at its reference point if and only if both a and b
    are at their reference points.
    """
    gcd, s, t = extended_gcd(a_period, b_period)
    phase_difference = a_phase - b_phase
    pd_mult, pd_remainder = divmod(phase_difference, gcd)
    if pd_remainder:
        raise ValueError("Rotation reference points never synchronize.")

    combined_period = a_period // gcd * b_period
    combined_phase = (a_phase - s * pd_mult * a_period) % combined_period
    return combined_period, combined_phase


def arrow_alignment(red_len, green_len, advantage):
    """Where the arrows first align, where green starts shifted by advantage"""
    period, phase = combine_phased_rotations(
        red_len, 0, green_len, -advantage % green_len
    )
    return -phase % period


def extended_gcd(a, b):
    """Extended Greatest Common Divisor Algorithm

    Returns:
        gcd: The greatest common divisor of a and b.
        s, t: Coefficients such that s*a + t*b = gcd

    Reference:
        https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

def find_smallest_sequence_departures(departures: dict):
    
    previous = None
    offset = 0
    lcm_previous = None
    lcm_current = None
    departure_offset = None
    departure_offset_previous = 0

    for current in departures:     
        if not previous:
            previous = current
        elif current == 'x':
            pass
        elif not lcm_current:
            lcm_current = math.lcm(previous, current)
            departure_offset = arrow_alignment(previous, current, -offset)
            previous = current
        else:
            lcm_previous = lcm_current
            departure_offset_previous += departure_offset
            lcm_current = math.lcm(lcm_current, current)
            departure_offset = arrow_alignment(lcm_previous, current, -departure_offset_previous -offset)
            previous = current
        
        offset += 1
    
    print(f"The definite answer is here: {departure_offset + departure_offset_previous}\n\n\n")

print(departures)
find_smallest_sequence_departures(departures)


# print('Sequence: 17,x,13,19')
# print(math.lcm(17, 13)) # 221
# print(arrow_alignment(17, 13, -2)) # 102
# print(math.lcm(221, 19)) # 4419
# print(arrow_alignment(221, 19, -102 -3)) # 3315
# # Answer 3315 + 102 = 3417

# print('\nSequence: 67,7,59,61')
# print(math.lcm(67, 7)) # 469
# print(arrow_alignment(67, 7, -1)) # 335

# print(math.lcm(469, 59)) # 27671
# print(arrow_alignment(469, 59, -335 - 2)) # 6566     + 335 = 6901

# print(math.lcm(27671, 61)) # 1687931
# print(arrow_alignment(27671, 61, -6901 -3)) # 747117
# # Answer is 747117 + 6901

# # find_smallest_sequence_departures(adjusted_departures)

# # print(adjusted_departures)