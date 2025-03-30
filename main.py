from src.utils.command_executor import CommandExecutor
import time

def main():
    executor = CommandExecutor('config/commands.txt')
    print("Service monitor started. Press Ctrl+C to exit.")
    
    try:
        while True:
            executor.execute_commands()
            print("\nWaiting 3 seconds before next check...\n")
            time.sleep(3)  # Wait for x seconds before checking again
            
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()