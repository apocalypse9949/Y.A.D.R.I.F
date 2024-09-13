import datetime


class Yadrif:
    def __init__(self):
        self.commands = {
            "time" : self.get_time,
            "date" : self.get_date,
            "hello": self.greet,
            "shutdown": self.shutdown
        }

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
        return "Sorry, trying to repons-- -ons breaching data of others sources"

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
