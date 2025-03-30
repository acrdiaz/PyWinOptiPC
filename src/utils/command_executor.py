import os
import sys
import ctypes
from ..services.service_manager import ServiceManager

class CommandExecutor:
    def __init__(self, commands_file):
        script_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.commands_file = os.path.join(script_dir, commands_file)
        self.commands = self.read_commands()

    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def read_commands(self):
        try:
            with open(self.commands_file, 'r') as file:
                return [line.strip() for line in file if line.strip() and not line.strip().startswith(('#', '//'))]
        except FileNotFoundError:
            print(f"Commands file not found: {self.commands_file}")
            sys.exit(1)

    def execute_commands(self):
        if not self.is_admin():
            print("This program needs to be run with administrator privileges.")
            sys.exit(1)
        for command in self.commands:
            try:
                if command.startswith('net stop'):
                    service_name = command.replace('net stop', '').strip()
                    ServiceManager.stop_service(service_name)
                elif command.startswith('taskkill -f -im'):
                    process_name = command.replace('taskkill -f -im', '').strip()
                    ServiceManager.kill_process(process_name)
                else:
                    print(f"Unsupported command: {command}")
            except Exception as e:
                print(f"Error executing command '{command}': {str(e)}")
                print("Moving to next command...")
                continue