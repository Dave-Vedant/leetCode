"""
Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:

Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.


Input
["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
Output
[null, true, true, false, false, false, true]

"""
# hash_table
def shouldPrintMessage(timeStamp, message):

    msg_dict = {}       # hash

    if message not in msg_dict:
        msg_dict[message] = timeStamp
        return True                        # first message, no need of 10 sec diff.
    
    if timeStamp - msg_dict[message] >= 10:
        msg_dict[message] = timeStamp
        return True              # time between both messages > 10, and add the new message time stamp
    else:
        return False   

    # time complexity = O(1), space complexity = O(N)

# Queue + Set:
from collections import deque
def shouldPrintMessage(timeStamp, message):
    msg_set = set()     # set
    msg_queue = deque()

    while msg_queue:
        msg, ts = msg_queue[0]
        print((msg,ts))
        if timeStamp - ts >= 10:       # condition, if satisfy remove the elements
            msg_queue.popleft()
            msg_set.remove(msg)
        else:
            break
    
    if message not in msg_set:   # if not, then add the message
        msg_set.add(message)
        msg_queue.append(message, timeStamp)
        return True
    else:
        return False

    # time complexity = O(N), space complexity = O(N)

# execution...


    