requisition_number = 0  

class RequisitionSystem:
    def __init__(self, staff_id, staff_name, date):
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.date = date
        self.items = []           
        self.total = 0            
        self.status = "Pending"   
        self.approval_ref = None  
        self.requisition_id = None  

    def staff_info(self):
        global requisition_number
        self.staff_id = input("Enter staff ID: ")
        self.staff_name = input("Enter staff name: ")
        self.date = input("Enter an actual date (YYYY/MM/DD): ")
        requisition_number += 1
        self.requisition_id = str(10000 + requisition_number)

    def requisitions_details(self):
        num_item = int(input("Enter number of items: "))
        for n in range(num_item):
            item_name = input(f"Item {n+1} name: ")
            item_qty = int(input(f"Quantity for '{item_name}': "))
            item_price = int(input(f"Price per '{item_name}': "))
            self.items.append({"item": item_name, "quantity": item_qty, "price": item_price})
            self.total += item_qty * item_price

    def requisition_approval(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_ref = self.staff_id + self.requisition_id[-3:]
        elif 500 <= self.total <= 5000:  
            self.status = "Pending"
            self.approval_ref = None
        else:
            self.status = "Not approved"
            self.approval_ref = None

    def respond_requisition(self):
        if self.status == "Pending":
            response = input(f"Manager response for {self.staff_name} requisition (Approved or Not Approved): ")
            if response.lower() == "approved":
                self.status = "Approved"
                self.approval_ref = self.staff_id + self.requisition_id[-3:]
            elif response.lower() == "not approved":
                self.status = "Not approved"
                self.approval_ref = None
            else:
                print("Not a valid response. Status cannot be changed.")

    def display_requisition(self):
        print("\nPrinting Requisition:\n")
        print(f"Date: {self.date}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: ${self.total}")
        print(f"Status: {self.status}")
        if self.approval_ref:
            print(f"Approval Reference Number: {self.approval_ref}")
        else:
            print("Approval Reference Number: It is not available.")


def requisition_statistics(requisitions):
    total_submitted = 0
    approved = 0
    pending = 0
    not_approved = 0

    for z in requisitions:
        total_submitted += 1
        if z.status == "Approved":
            approved += 1
        elif z.status == "Pending":
            pending += 1
        else:  
            not_approved += 1

    print("\nRequisition Statistics\n")
    print("The total number of requisitions submitted:", total_submitted)
    print("The total number of approved requisitions:", approved)
    print("The total number of pending requisitions:", pending)
    print("The total number of not approved requisitions:", not_approved)


def main():
    requisitions_list = []

    while True:
        print("\nRequisition System Menu\n")
        print("1. Fill up a new requisition")
        print("2. Display all the requisitions")
        print("3. Display the requisition statistics")
        print("4. Manager will respond to pending requisitions")
        print("5. Leave")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            req = RequisitionSystem("", "", "")
            req.staff_info()
            req.requisitions_details()
            req.requisition_approval()
            requisitions_list.append(req)

        elif choice == "2":
            if not requisitions_list:
                print("No requisitions submitted yet.")
            else:
                for z in requisitions_list:
                    z.display_requisition()

        elif choice == "3":
            if not requisitions_list:
                print("No requisitions submitted yet.")
            else:
                requisition_statistics(requisitions_list)

        elif choice == "4":
            pending_found = False
            for z in requisitions_list:
                if z.status == "Pending":
                    pending_found = True
                    z.respond_requisition()
            if not pending_found :
                print("No pending requisitions are here to respond.")

        elif choice == "5":
            print("Leavingg the Requisition System.")
            break

        else:
            print("Not a valid choice. Please enter the number between 1–5.")


if __name__ == "__main__":
    main()
