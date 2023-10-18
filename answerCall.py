# answerCall.py
# by Patrick Hudson

# For instructions on what to do, see README.md
# or visit (https://github.com/HundredVisionsGuy/answerCall) 

# Write function defintion: answerCall()
def answerCall(caller_code, sameAreaCode, cur_time):
    response = True
    hour, minute = cur_time.split(":")
    if int(hour) < int(7):
        response = False
    if int(hour) > int(22):
        response = False
    if caller_code == 'T':
        response = False
    if caller_code == 'U' and sameAreaCode == False:
        response = False
    
    return response

# Make sure it returns a value

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    answerCall("F", False, "13:00")
