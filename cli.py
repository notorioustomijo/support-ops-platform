from tickets import load_tickets, count_by_status, display_tickets, filter_by_status, search_tickets, save_tickets_json, load_tickets_json
import json 

def main():
    try:
        tickets = load_tickets("tickets.csv")
    except FileNotFoundError as e:
        print(f"The file '{e.filename}' does not exist. Check the file path and try again.")
        return
    except ValueError as e:
        print(f"{e}")
        return
    except KeyError as e:
        print(f"Incorrect column name. Update the column name to '{e.args[0]}' and try again.")
        return
    
    ticket_counts = count_by_status(tickets)

    print(f"=========== Ticket Stats ==============\n")
    print(f"Open Tickets ({ticket_counts['open']}). Closed Tickets ({ticket_counts['closed']}). Pending Tickets ({ticket_counts['pending']}). Other Tickets ({ticket_counts['unknown']})\n")

    print(f"=========== All Tickets ({len(tickets)}) ==============")
    display_tickets(tickets)

    print(f"\n=========== Open Tickets ==============")
    display_tickets(filter_by_status(tickets, "open"))

    print(f"\n=========== Other Operations ==============")
    print("Search Tickets - keyword: 'domain '")
    try:
        retrieved_tickets = search_tickets(tickets, "domain ")
        display_tickets(retrieved_tickets)
    except ValueError as e:
        print(f"{e}")
    print("\n")

    print("Save Tickets to JSON file")
    save_tickets_json(tickets, "tickets.json")
    print("Tickets saved.\n")

    print("Load Tickets from JSON file")
    try:
        json_tickets = load_tickets_json("tickets.json")
        print(f"{json_tickets}\n")
        if json_tickets == tickets:
            print("JSON tickets matches original csv.")
        else:
            print("Mismatch between JSON and csv file detected!")
    except FileNotFoundError as e:
        print(f"The file '{e.filename}' does not exist. Correct the file path and try again.")
    except (UnicodeDecodeError, PermissionError) as e:
        print(f"File Error: Could not read the file. Details: {e}")
    except json.JSONDecodeError:
        print("The JSON file contains property names without double quotes. Correct them and try again.")



if __name__ == "__main__":
    main()
