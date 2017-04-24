# Imports are done here.
import json

# Try to open A-Skill definition. If fail, exit.
def read_askill_defs(filepath):
    try:
        with open (filepath) as json_data:
            definitions = json.load(json_data)
        return definitions
    except IOError as e:
        print("Cannot load A-Skill definitions!")

# Main A-Skill class. Do all work here.
class ASkill:

    # Class initialiser.
    def __init__(self, definitions):
        self.definitions = definitions

        defs_file = read_askill_defs(input("A-Skill definitions file to open (.json): "))

    # Get skill name.
    def __str__(self):
        return self.definitions["skill-name"]
        