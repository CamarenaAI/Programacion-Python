def show_messages(messages):
    print("Print messages:")
    for message in messages:
        print(f"\t{message}")

def send_messages(messages, sent_message):
    print("\nSend Messages")
    while messages:
        current_message = messages.pop()   
        print(f"\t{current_message}")
        sent_message.append(current_message)

messages = ['Hello', 'How are you?', 'Welcome']
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)