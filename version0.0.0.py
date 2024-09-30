import datetime
import csv

class Yadrif:
    def __init__(self):

        self.commands = {
            "time": self.get_time,
            "date": self.get_date,
            "hello": self.greet,
            "shutdown": self.shutdown,
            "character": self.get_character_info
        }


        self.characters = self.load_csv_data('genshin_characters_v1.csv')

    def load_csv_data(self, file_path):

        characters = {}
        try:

            with open(file_path, mode='r', encoding='utf-8', errors='replace') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    name = row['name'].lower()
                    characters[name] = row
        except Exception as e:
            print(f"Error loading CSV: {e}")
        return characters

    def get_character_info(self):
        character_name = input("Enter the character name: ").lower()
        if character_name in self.characters:
            character_data = self.characters[character_name]
            return f"{character_data['name']} - Element: {character_data['element']}, Weapon: {character_data['weapon']}, Region: {character_data['region']}"
        else:
            return "Character not found."

    def get_time(self):
        now = datetime.datetime.now()
        return now.strftime("The current time is %H:%M")

    def get_date(self):
        today = datetime.date.today()
        return today.strftime("Today is %B %d, %Y")

    def greet(self):
        return "Hello! How can I assist you today?"

    def shutdown(self):
        return "Shutting down yadrif"

    def response(self, input_text):
        for command in self.commands:
            if command in input_text.lower():
                return self.commands[command]()
        return "Sorry, searching from online sources."

    def run(self):
        print("Activating yadrif services")
        while True:
            user_input = input("You: ")
            respond = self.response(user_input)
            print(f"Y.A.D.R.I.F: {respond}")
            if user_input.lower() == "shutdown":
                break

if __name__ == "__main__":
    assist = Yadrif()
    assist.run()
