
def decode_msg(msg_file):
    msg_file = open(msg_file)
    msg_buffer = msg_file.readlines()

    pyramid = []
    temp_digit = []
    code_dict = { } 
    hidden_code = []

    # Extract all line
    for line in msg_buffer:
        rec = line.split(" ")
        code_dict[int(rec[0])] = rec[1].strip('\n')
        temp_digit.append(int(rec[0]))

    temp_digit.sort()
    # Create Pyramid
    start = 0
    pos_need = 1
    start_pos = 0
    total_row = len(temp_digit)
    while start_pos < total_row:
        temp = temp_digit[start_pos:pos_need]
        pyramid.append(temp)
        hidden_code.append(temp[-1])
        start_pos = pos_need
        pos_need += len(temp) + 1

    for level in pyramid:
        print(level)
    # Now Decode message
    final_msg = ""
    for code in hidden_code:
        final_msg += code_dict[code]
        final_msg += " "

    return final_msg

msg = decode_msg("C:\\Development\\Python\\SomeInteresting\\coding_qual_input.txt")
print(msg)