from tqdm import tqdm

door_pubkey = 14222596
card_pubkey = 4057428
# door_pubkey = 17807724
# card_pubkey = 5764801


def make_loops(loop_size: int, subject_number: int) -> int:
    value = 1
    for i in range(loop_size):
        value = value * subject_number
        value = value % 20201227
    
    return value

first_found = False

subject_number = 14222596
value = 1
# value = 5764801
for i in tqdm(range(2918888)):
    
    # subjectnr = make_loops(i, 7)

    value = value * subject_number
    value = value % 20201227

    subjectnr = value

    if subjectnr == door_pubkey:
        print(f'The door loop size is: {i}')
        
        if first_found:
            break
        else:
            first_found = True
    
    if subjectnr == card_pubkey:
        print(f'The card loop size is: {i}')
        
        if first_found:
            break
        else:
            first_found = True

print(subjectnr)

# The card loop size is: 2918888
# The door loop size is: 3616052
# print(f'The answer is: {i}')
# 10975256
    