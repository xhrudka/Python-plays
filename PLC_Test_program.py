
class periphery():
    def __init__(self,name,manufacturer="Wago", firmware_version=4):
        self.name=name
        self.manufacturer=manufacturer
        self.firmware_version=firmware_version
    def firmware_check(self):
        if self.firmware_version ==5:
            return " The latest firmware is installed"
        elif self.firmware_version != 5:
            return "Upgrade the firmware"
      
new_device=periphery("460","Siemens",2)
print(new_device.firmware_check())



