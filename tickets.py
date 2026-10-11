import csv
import json

def validate_columns(rows, required):
    """Takes a list of rows and required column keys and validates that the file is not empty and the required keys are present. Raises ValueError if file is empty or keys are missing."""
    if not rows:
        raise ValueError("The csv file is empty. Check the file and try again.")
    
    present = rows[0].keys()
    
    missing = [c for c in required if c not in present]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")


def load_tickets(path):
    """
    Reads tickets from a CSV file. Returns a list of dicts.
    Raises FileNotFoundError if csv file not present. 
    Raises ValueError through validate_columns if empty csv or required columns are missing.
    """
    with open(path, newline='', encoding="utf-8") as f:
        ticket_list = list(csv.DictReader(f))

    validate_columns(ticket_list, ["id", "customer", "subject", "description", "status"])  
    
    for row in ticket_list:
        row['status'] = row['status'].strip().lower()
    
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
        
def search_tickets(tickets, keyword):
    """Reads tickets list.
    Returns list of tickets with words that matches the provided keyword."""
    cleaned_keyword = keyword.strip().lower()
    if not cleaned_keyword:
        raise ValueError("Search query cannot be empty.")
    return [t for t in tickets if cleaned_keyword in t["subject"].lower()  or cleaned_keyword in t["description"].lower()]

def save_tickets_json(tickets, path):
    """Saves a ticket list as a json file to a specific path."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=2)
    

def load_tickets_json(path):
    """Loads ticket list from json file."""
    with open(path, "r", encoding="utf-8") as file:
        tickets = json.load(file)

    return tickets