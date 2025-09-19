# This is a global counter, where the number of requisitions created in the system is monitored.
#  It is primarily applied to create unique requisition IDs in order to be able to easily identify and manage the requisition.
#  Its implementation is based on K.I.S.S (Keep It Simple, Stupid) principle as the implementation is a very simple counter mechanism to guarantee the uniqueness without any unnecessary complexity.
requisition_number = 0  


# REQUISITION SYSTEM CLASS
# This class defines everything about a requisition: staff info, item details, approval, responses, and display.
# The SRP Principle has been used, means that One class groups all requisition-related behavior.
class RequisitionSystem:

    # CONSTRUCTOR
    # It Sets default values for each requisition when object is created.
    # The K.I.S.S Principle has been used. It clear initialization makes it easy to understand.
    def __init__(self, staff_id, staff_name, date):
        self.staff_id = staff_id            
        self.staff_name = staff_name         
        self.date = date                    
        self.items = []                      
        self.total = 0                       
        self.status = "Pending"              
        self.approval_ref = None             
        self.requisition_id = None           

    # STAFF INFORMATION
    # It Collect staff details from user and generate unique requisition ID
    # The SRP Principle has been used. This method only collects staff details and sets ID.
    def staff_info(self):
        global requisition_number
        self.staff_id = input("Enter staff ID: ")             
        self.staff_name = input("Enter staff name: ")         
        self.date = input("Enter an actual date (YYYY/MM/DD): ")  
        requisition_number += 1                               
        self.requisition_id = str(10000 + requisition_number) 

    # REQUISITION DETAILS
    # It collects list of items (name, quantity, price) and calculates total amount.
    # The DRY Principle has been used. It will Use one loop to collect multiple items instead of repeating code.
    def requisitions_details(self):
        num_item = int(input("Enter number of items: "))  
        for n in range(num_item):
            item_name = input(f"Item {n+1} name: ")       
            item_qty = int(input(f"Quantity for '{item_name}': ")) 
            item_price = int(input(f"Price per '{item_name}': "))   
            self.items.append({"item": item_name, "quantity": item_qty, "price": item_price})  
            self.total += item_qty * item_price 

    # REQUISITION APPROVAL 
    # Automatically decides if requisition is approved, pending, or not approved.
    # The K.I.S.S Principle has been used. It use Simple if-elif-else keeps logic straightforward.
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

    # MANAGER RESPONSE
    # If requisition is pending, manager can approve or reject.
    # The SRP Principle has been used. It only handles manager decision-making.
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

    # DISPLAY REQUISITION
    # Prints all requisition details clearly.
    # The K.I.S.S Principle has been used. Straightforward printing of attributes.
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


# REQUISITION STATISTICS
# Shows the summary of all requisitions (submitted, approved, pending, not approved).
# The DRY Principle has been used. It use one loop to count all statuses instead of separate code.
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

    # Print results
    print("\nRequisition Statistics\n")
    print("The total number of requisitions submitted:", total_submitted)
    print("The total number of approved requisitions:", approved)
    print("The total number of pending requisitions:", pending)
    print("The total number of not approved requisitions:", not_approved)


# MAIN PROGRAM
# Controls the workflow through a menu.
# The K.I.S.S Principle has been used. It is a Simple menu-driven structure.
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
            # It cretaes new requisition.
            req = RequisitionSystem("", "", "")
            req.staff_info()             
            req.requisitions_details()  
            req.requisition_approval()  
            requisitions_list.append(req)

        elif choice == "2":
            # Display all requisitions if any exist
            if not requisitions_list:
                print("No requisitions submitted yet.")
            else:
                for z in requisitions_list:
                    z.display_requisition()

        elif choice == "3":
            # Display statistics if requisitions exist
            if not requisitions_list:
                print("No requisitions submitted yet.")
            else:
                requisition_statistics(requisitions_list)

        elif choice == "4":
            # Manager responds to pending requisitions
            pending_found = False
            for z in requisitions_list:
                if z.status == "Pending":
                    pending_found = True
                    z.respond_requisition()
            if not pending_found:
                print("No pending requisitions are here to respond.")

        elif choice == "5":
            # Leave the program
            print("Leaving the Requisition System.")
            break

        else:
            # Not a valid input 
            print("Not a valid choice. Please enter the number between 1–5.")


# START PROGRAM
# Ensures that code runs only when executed directly, not when imported.
if __name__ == "__main__":
    main()
