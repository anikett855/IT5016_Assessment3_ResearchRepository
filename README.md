1.	Overview:
The Requisition System is an efficient system which deals with requisitions. Staff members are able to make requisitions with details of items and the system calculates the total and initial approval is made and the managers can approve or disapprove pending requisitions. It is also able to show all the requisitions and indicate statistics. The application is user-friendly, compact, and easy to support as the application follows several key software concepts such as K.I.S.S, DRY, and SRP.



2.	Functionality:

Staff Information: The input details are staff ID, staff name and date and a unique requisition ID is generated.	Item Details: The Users add several items in quantity and price, and the program program calculate the total amount automatically.	Requisition Approval: Depending on the total, the system will automatically approve, hold pending or reject the requisition.
Manager Response: Approving and rejecting pending requisitions can be done by managers.
Display Requisitions: Prints all the information of a requisition in a readable format.
Statistics: All submitted, approved, pending and rejected requisitions will be summarized.
Program Control: It is a menu-driven system that takes the user through every action.






3.	Applying the Software Principles Concept 

In this part I have attempted to describe the software principles through concept of flowchart which I learned at the outset of this course. I have presented all the principles used throughout the code in order. I applied K.I.S.S, DRY, and SRP software principles in my code.

I.	Global Counter (requisition_number)
Purpose: hecks the amount of requisitions generated and assists in generating new IDs.
Principle:
o	K.I.S.S: he counter is not complex but efficient. It also guarantees that each requisition receives an individual ID without any complex logic, additional functions or database validation and thus the program is simple to operate and understand.
II.	Requisition System Class (RequisitionSystem)
Purpose: Defines all the requisition related data such as staff information, item, approval, manager responses and display.
Principle:
SRP: Everything within the class is focused on one task (gathering staff data, item details, approval logic, manager response, detail display), making the code kept modular, organized and simpler to maintain.
III.	Constructor (__init__())
Purpose: Assigns default values to every requisition during creation of the object..
Principle:
o	K.I.S.S: It is easy to initialize and all attributes of a requisition object are easily displayed. It becomes easy to understand the contents of a requisition.
IV.	staff_info()
Purpose: Gathers the staff information of the user and creates a special requisition ID.
Principle:
o	SRP: Required to collect information about the staff and the requisition ID. It has no management of the items, approvals, or display, and the logic is easy and limited.

V.	requisitions_details()
Purpose: Collects multiple items (name, quantity, price) and calculates the total amount.
Principle:
o	DRY: There is only one loop that repeats itself with every item rather than using separate code to run each item. This eliminates errors, repetitions, and can be easily maintained in the future.
VI.	requisition_approval()
Purpose: Making automatic decisions on whether or not to approve, pending or not approve a requisition based on the total amount.
Principle:
o	K.I.S.S: The basic if-elif-else form is used to maintain the logic of the approval as simple and fast and simple to follow without useless complexity.
VII.	respond_requisition()
Purpose: Allows the manager to approve or reject pending requisitions.
Principle:
o	SRP: Handles only the decision made by the manager and this logic is not mixed with staff information, collection of an item or initial approval, and thus test and maintenance is simpler.


VIII.	display_requisition()
Purpose: Prints all requisition details in a readable manner.
Principle:
o	K.I.S.S: Attributes are printed without the additional processing or formatting. This makes the display simple and easy to read and comprehend by the user.
IX.	requisition_statistics()
Purpose: Provides a summary of all requisitions with a total submitted, approved, pending and not approved.
Principle:
o	DRY: Counts each type of status with one loop, rather than a seperates loop. This minimizes repetition and makes the code as short as possible as well as it would be easier to change in the future.
X.	main() Function
Purpose: Manages the workflow using a menu driven system.
Principle:
o	K.I.S.S: Easy menu system presents all options to the user, and the flow of the program is not difficult to understand and follow.
XI.	Start Program (if __name__ == "__main__":)
Purpose: Makes sure that the code is only run when it is executed and not when imported.
Principle:
o	K.I.S.S: Simple and effective check prevents accidental execution in case imported to other programs, ensuring the program is safe and well-organized.




4.	Conclusion:
The Requisition System program makes good use of K.I.S.S, DRY and SRP. Every section of the program is straightforward, has one responsibility and does not need to be repeated unnecessarily. This ensures the code is simple to read, maintain as well as to extend in future and at the same time user-friendly. The program is a good example of clean and professional quality coding practices, and is not too complex to be easily understood.

Note: For this assessment, I have used my own code (Assessment2_PastB) because it helps me explain the principles easily, As I am already familiar with how this code works.
