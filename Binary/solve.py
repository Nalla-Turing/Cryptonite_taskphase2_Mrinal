def replace_commas_with_spaces(input_string):
    # Replace all commas with spaces
    return input_string.replace(',', ' ')

# Example string
example_string = "402118,0,7d1d3020ca00,0,173d880,a347834,7ffefcf57120,7d1d2fffde60,7d1d302224d0,1,7ffefcf571f0,0,0,7b4654436f636970,355f31346d316e34,3478345f33317937,35625f673431665f,7d663839623764,7,7d1d302248d8,2300000007,206e693374307250,a336c797453,9,7d1d30235de9,7d1d30006098,7d1d302224d0,0,7ffefcf57200,6c6c252c786c6c25,252c786c6c252c78,786c6c252c786c6c"

# Apply the function
result = replace_commas_with_spaces(example_string)
print(result)
print("\n")

def hex_to_ascii(hex_string):
    # Ensure the string has an even length by padding if necessary
    hex_string = hex_string.replace(" ", "")  # Remove any spaces
    if len(hex_string) % 2 != 0:
        hex_string = "0" + hex_string  # Pad with a leading zero if the length is odd

    # Convert the hex string into ASCII
    ascii_result = ""
    for i in range(0, len(hex_string), 2):
        hex_pair = hex_string[i:i+2]
        try:
            # Convert hex pair to ASCII character
            ascii_result += chr(int(hex_pair, 16))
        except ValueError:
            ascii_result += '?'  # Use '?' for invalid hex codes

    return ascii_result

# Example usage
hex_string = "40211807d1d3020ca000173d880a3478347ffefcf571207d1d2fffde607d1d302224d017ffefcf571f0007b4654436f636970355f31346d316e343478345f3331793735625f673431665f7d66383962376477d1d302248d82300000007206e693374307250a336c7974537d1d30235de97d1d300060987d1d302224d07ffefcf572006c6c252c786c6c25252c786c6c252c78786c6c252c786c6c"
ascii_text = hex_to_ascii(hex_string)
print(ascii_text)
