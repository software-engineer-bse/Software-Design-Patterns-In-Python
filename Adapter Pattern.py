class Old_System_Class:
    def get_data(self):
        return "This is data from old system."
    
class New_System_Class:
    def process(self, data):
        print(f"{data}")

class Adapter_Class:
    def __init__(self, old_system):
        self.old_system = old_system
    
    def get_data(self):
        data = self.old_system.get_data()
        return f"Adapter_Class {data}"
    
old_system_class = Old_System_Class()
adapter_class = Adapter_Class(old_system_class)
new_system = New_System_Class()

adapter_class_data = adapter_class.get_data()

new_system.process(adapter_class_data)

