# --------------------------------------------------------
# clinical_task_management_system.py
# Patient Follow-Up & Clinical Task Tracker
# --------------------------------------------------------

def clinical_task_system():
    tasks = []

    while True:
        print("\n=== Clinical Task Management System ===")
        print("1. Add Clinical Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_name = input("Enter Patient Name: ").strip().capitalize()
            task_type = input("Enter Task Type (Medication/Lab/Imaging/Follow-up): ").strip()
            priority = input("Enter Priority (Low/Medium/High): ").strip().capitalize()

            task = {
                "patient": patient_name,
                "type": task_type,
                "priority": priority,
                "status": "Pending"
            }

            tasks.append(task)
            print("Clinical task added successfully.")

        elif choice == "2":
            if not tasks:
                print("No clinical tasks available.")
            else:
                print("\n--- Current Clinical Tasks ---")
                for i, task in enumerate(tasks):
                    print(f"{i+1}. Patient: {task['patient']} | "
                            f"Task: {task['type']} | "
                            f"Priority: {task['priority']} | "
                            f"Status: {task['status']}")

        elif choice == "3":
            task_index = int(input("Enter task number to mark as completed: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["status"] = "Completed"
                print("Task marked as completed.")
            else:
                print("Invalid task number.")

        elif choice == "4":
            task_index = int(input("Enter task number to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks.pop(task_index)
                print("Task removed successfully.")
            else:
                print("Invalid task number.")

        elif choice == "5":
            print("Exiting Clinical Task System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    clinical_task_system()clinical_task_management_system.py
