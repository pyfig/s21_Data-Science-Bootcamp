import sys

def call_center(clients, recipients):
    clients_set = set(clients)
    recipients_set = set(recipients)
    return list(clients_set - recipients_set)

def potential_clients(participants, clients):
    participants_set = set(participants)
    clients_set = set(clients)
    return list(participants_set - clients_set)

def loyalty_program(clients, participants):
    clients_set = set(clients)
    participants_set = set(participants)
    return list(clients_set - participants_set)

def marketing():
    clients = [
        'andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
        'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
        'elon@paypal.com', 'jessica@gmail.com'
    ]
    participants = [
        'walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org',
        'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org',
        'mr@robot.gov', 'eleven@yahoo.com'
    ]
    recipients = [
        'andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is'
    ]

    if len(sys.argv) != 2:
        print("Usage: python3 marketing.py <Задача>")
        print("Задачи: call_center, potential_clients, loyalty_program")
        sys.exit(1)

    task = sys.argv[1]
    
    if task == "call_center":
        result = call_center(clients, recipients)
    elif task == "potential_clients":
        result = potential_clients(participants, clients)
    elif task == "loyalty_program":
        result = loyalty_program(clients, participants)
    else:
        raise ValueError("Неверно задана задача, выбери одну из списка: call_center, potential_clients, loyalty_program")

    for email in result:
        print(email)

if __name__ == "__main__":
    marketing()