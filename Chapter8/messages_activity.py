def show_messages(texts):
    for text in texts:
        print(f"Message: {text}")

def send_messages(messages, sent_messages):
    while messages:
        pending_send = messages.pop()
        print(f"Message: {pending_send}")
        sent_messages.append(pending_send)

def show_sent(sent_messages):
    print("\nThese messages have been sent: ")
    for sent in sent_messages: 
        print(sent)

def send_messages2(messages, sent_messages):
    while messages:
        pending_send = messages.pop()
        print(f"Message: {pending_send}")
        sent_messages.append(pending_send)

def show_sent2(sent_messages):
    print("\nThese messages have been sent: ")
    for sent in sent_messages: 
        print(sent)