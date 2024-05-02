from datetime import datetime

class Case:
    def __init__(self, case_id, description, status, assigned_officers, case_category, creation_date):
        self.case_id = case_id
        self.description = description
        self.status = status
        self.assigned_officers = assigned_officers
        self.case_category = case_category
        self.creation_date = creation_date

    def to_string(self):
        assigned_officers_str = ",".join(self.assigned_officers)
        creation_date_str = self.creation_date.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.case_id},{self.description},{self.status},{assigned_officers_str},{self.case_category},{creation_date_str}"

    @staticmethod
    def from_string(case_string):
        case_data = case_string.strip().split(",")
        case_id, description, status, assigned_officers_str, case_category, creation_date_str = case_data
        assigned_officers = assigned_officers_str.split(",")
        creation_date = datetime.strptime(creation_date_str, "%Y-%m-%d %H:%M:%S")
        return Case(case_id, description, status, assigned_officers, case_category, creation_date)


class PoliceCaseManagementSystem:
    def __init__(self):
        self.file_path = "police_record.txt"
        self.options = {
            "1": self.create_case_file,
            "2": self.update_case_file,
            "3": self.read_case_file,
            "4": self.delete_case_file,
            "5": self.manage_police_cases,
            "6": self.track_case_progress,
            "7": self.exit_program
        }

    def create_case_file(self):
        with open(self.file_path, "a") as file:
            case_id = input("Enter case ID: ")
            description = input("Enter case description: ")
            status = input("Enter case status: ")
            assigned_officers_input = input("Enter assigned officers (comma-separated): ")
            assigned_officers = assigned_officers_input.split(",")
            case_category = input("Enter case category: ")
            creation_date = datetime.now()

            new_case = Case(case_id, description, status, assigned_officers, case_category, creation_date)
            file.write(new_case.to_string() + "\n")
            print("Case file created successfully")

    def update_case_file(self):
        updated_cases = []
        case_id = input("Enter case ID to update: ")
        with open(self.file_path, "r") as file:
            for line in file:
                case = Case.from_string(line)
                if case.case_id == case_id:
                    print("Enter new details:")
                    description = input(f"Enter new case description ({case.description}): ")
                    status = input(f"Enter new case status ({case.status}): ")
                    assigned_officers_input = input("Enter new assigned officers (comma-separated): ")

                    if description:
                        case.description = description
                    if status:
                        case.status = status
                    if assigned_officers_input:
                        case.assigned_officers = assigned_officers_input.split(",")

                updated_cases.append(case)

        with open(self.file_path, "w") as file:
            for case in updated_cases:
                file.write(case.to_string() + "\n")
        print("Case file updated successfully")

    def delete_case_file(self):
        case_id = input("Enter case ID to delete: ")
        with open(self.file_path, "r") as file:
            cases = [line.strip() for line in file if line.strip().split(",")[0] != case_id]

        with open(self.file_path, "w") as file:
            file.write("\n".join(cases))
        print("Case file deleted successfully")

    def read_case_file(self):
        case_id = input("Enter case ID to read: ")
        with open(self.file_path, "r") as file:
            for line in file:
                case = Case.from_string(line)
                if case.case_id == case_id:
                    print("Case ID:", case.case_id)
                    print("Description:", case.description)
                    print("Status:", case.status)
                    print("Assigned Officers:", *case.assigned_officers)
                    print("Case Category:", case.case_category)
                    print("Creation Date:", case.creation_date.strftime("%Y-%m-%d %H:%M:%S"))
                    return
            print("Case ID does not exist")

    def manage_police_cases(self):
        case_id = input("Enter case ID to manage: ")
        self.read_case_file()

    def track_case_progress(self):
        case_id = input("Enter case ID to track progress: ")
        with open(self.file_path, "r") as file:
            for line in file:
                case = Case.from_string(line)
                if case.case_id == case_id:
                    print("Case ID:", case.case_id)
                    print("Current Status:", case.status)
                    print("Creation Date:", case.creation_date.strftime("%Y-%m-%d %H:%M:%S"))
                    return
            print("Case ID does not exist")

    def exit_program(self):
        print("Thanks for using our application")

    def switch_options(self, choice):
        func = self.options.get(choice)
        if func:
            func()
        else:
            print("Invalid option")


# Example Usage
if __name__ == "__main__":
    pcm_system = PoliceCaseManagementSystem()

    while True:
        print("\nMenu:")
        print("1. Create Case File")
        print("2. Update Case File")
        print("3. Read Case File")
        print("4. Delete Case File")
        print("5. Manage Police Cases")
        print("6. Track Case Progress")
        print("7. Exit")

        choice = input("Enter your choice: ")

        pcm_system.switch_options(choice)
