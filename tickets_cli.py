import csv

def load_tickets(path):
    """Converts a csv file with tickets into a list of dicts and returns a normalized version of the list."""
    with open(path, newline='') as f:
        ticket_list = list(csv.DictReader(f))

        for row in ticket_list:
            for key, value in row.items():
                if key == "status":
                    row[key] = value.strip().lower()

        return ticket_list
    
def filter_by_status(tickets, status):
    wanted = status.strip().lower()
    return [t for t in tickets if t["status"] == wanted]

def display_tickets(tickets):
    """Takes a list of tickets and prints each ticket as a string with id, customer, subject, and status separated by |"""
    if not tickets:
        print("No tickets found") 
        return
    for t in tickets:
        print(f"{t['id']} | {t['customer']} | {t['subject']} | {t['status'].title()}")

def count_by_status(tickets):
    """Takes a list of tickets and returns a dict with the number of open, closed, pending and unknown tickets."""

    ticket_counts = {
        "open": 0,
        "closed": 0,
        "pending": 0,
        "unknown": 0
    }

    for t in tickets:
        ticket_status = t["status"]

        if ticket_status not in ticket_counts:
            ticket_counts["unknown"] += 1
        else:
            ticket_counts[ticket_status] += 1
    
    return ticket_counts


def get_ticket(tickets, ticket_id):
    """Takes a list of tickets and ticket_id and returns a ticket dict matching the provided id or None if there isn't one."""
    wanted_id = str(ticket_id)
    # Look through the tickets
    for ticket in tickets:
        # find the ticket that matches the id
        if ticket["id"] == wanted_id:
            # Return the ticket
            return ticket
    

    # Return None if no ticket matches
    return None
        



def main():
    tickets = load_tickets("tickets.csv")

    ticket_counts = count_by_status(tickets)

    print(f"=========== Ticket Stats ==============\n")
    print(f"Open Tickets ({ticket_counts['open']}). Closed Tickets ({ticket_counts['closed']}). Pending Tickets ({ticket_counts['pending']}). Other Tickets ({ticket_counts['unknown']})\n")

    print(f"=========== All Tickets ({len(tickets)}) ==============\n")

    display_tickets(tickets)

    print(f"\n=========== Open Tickets ==============\n")
    display_tickets(filter_by_status(tickets, "open"))

    wanted = get_ticket(tickets, "99")
    print(wanted)


if __name__ == "__main__":
    main()
