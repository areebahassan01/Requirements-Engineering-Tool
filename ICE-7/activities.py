# Function to perform inception
def perform_inception():
    print("***INCEPTION ACTIVITY***")
    problem_requirements = input("Enter the problem requirements: ")
    project_constraints = input("Enter the project constraints: ")
    major_features = input("Enter the major features and functions required: ")
    print("Data has been added.")
    return problem_requirements, project_constraints, major_features

# Function to perform elicitation
def perform_elicitation():
    print("***ELICITATION ACTIVITY***")
    usage_scenarios = []
    while True:
        scenario = input("Enter a usage scenario (or type 'done' to finish): ")
        if scenario == 'done':
            break
        usage_scenarios.append(scenario)
        print("Data has been added.")
    return usage_scenarios

# Function to perform elaboration
def perform_elaboration():
    scenario_based_elements = []
    print("***ELABORATION ACTIVITY***")
    while True:
        element = input("Enter a scenario-based element (or type 'done' to finish): ")
        if element == 'done':
            break
        scenario_based_elements.append(element)
    activity_based_elements = []
    while True:
        element = input("Enter an activity-based element (or type 'done' to finish): ")
        if element == 'done':
            break
        activity_based_elements.append(element)
    class_based_elements = []
    while True:
        element = input("Enter a class-based element (or type 'done' to finish): ")
        if element == 'done':
            break
        class_based_elements.append(element)
    behavioral_elements = []
    while True:
        element = input("Enter a behavioral element (or type 'done' to finish): ")
        if element == 'done':
            break
        behavioral_elements.append(element)
        print("Data has been added.")
    return scenario_based_elements, activity_based_elements, class_based_elements, behavioral_elements

# Function to perform specification
def perform_specification():
    print("***SPECIFICATION ACTIVITY***")
    file_name = input("Enter the name of the specification file: ")
    with open(file_name, 'w') as f:
        f.write(input("Enter the specification: "))
    print("Your specifications are saved to the file")

# Function to perform validation
def perform_validation(problem_requirements, project_constraints, major_features, usage_scenarios, scenario_based_elements, activity_based_elements, class_based_elements, behavioral_elements):
    print("***VALIDATION ACTIVITY***")
    if not problem_requirements or not project_constraints or not major_features:
        print("Error: problem requirements, project constraints, and major features are required.")
        print("Validation is unsuccessful")
    else:
        print("Validation successful.")
    if not usage_scenarios:
        print("Warning: no usage scenarios were provided.")
    if not scenario_based_elements or not activity_based_elements or not class_based_elements or not behavioral_elements:
        print("Warning: the elaborated requirements model is incomplete.")


# Menu
print("*** WELCOME TO THE REQUIREMENTS ENGINEERING PROGRAM***")
while True:
    print("""
    Please select an activity from the menu below:
    1. Inception
    2. Elicitation
    3. Elaboration
    4. Specification
    5. Validation
    6. Exit
    """)
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        problem_requirements, project_constraints, major_features = perform_inception()
    elif choice == '2':
        usage_scenarios = perform_elicitation()
    elif choice == '3':
        scenario_based_elements, activity_based_elements, class_based_elements, behavioral_elements = perform_elaboration()
    elif choice == '4':
        perform_specification()
    elif choice == '5':
        perform_validation(problem_requirements, project_constraints, major_features, usage_scenarios, scenario_based_elements, activity_based_elements,class_based_elements,behavioral_elements)
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")