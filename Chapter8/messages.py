#import messages_activity
#from messages_activity import show_messages, send_messages, show_sent, send_messages2, show_sent2
#from messages_activity import show_messages, send_messages, show_sent, send_messages2, show_sent2 as sh_msg, sd_msg, sw_st, sd_msg2, sw_st2
#import messages_activity as msg_act
from messages_activity import *

#Hands On #2
# 8-9

print("-----Exercise 8-9-----\n")

# def show_messages(texts):
#     for text in texts:
#         print(f"Message: {text}")

messages = ['Hello, there.','What time are we meeting?','Done with your homework?']
show_messages(messages)

#8-10
print("\n-----Exercise 8-10-----\n")

# def send_messages(messages, sent_messages):
#     while messages:
#         pending_send = messages.pop()
#         print(f"Message: {pending_send}")
#         sent_messages.append(pending_send)

# def show_sent(sent_messages):
#     print("\nThese messages have been sent: ")
#     for sent in sent_messages: 
#         print(sent)

messages = ['Hello, there.','What time are we meeting?','Done with your homework?']
sent_messages = []

send_messages(messages,sent_messages)
show_sent(sent_messages)

#8-11
print("\n-----Exercise 8-11-----\n")

# def send_messages2(messages, sent_messages):
#     while messages:
#         pending_send = messages.pop()
#         print(f"Message: {pending_send}")
#         sent_messages.append(pending_send)

# def show_sent2(sent_messages):
#     print("\nThese messages have been sent: ")
#     for sent in sent_messages: 
#         print(sent)

messages = ['Hello, there.','What time are we meeting?','Done with your homework?']
sent_messages = []

send_messages2(messages[:],sent_messages)
show_sent2(sent_messages)