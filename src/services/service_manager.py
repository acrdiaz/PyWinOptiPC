import subprocess
import time

class ServiceManager:
    @staticmethod
    def stop_service(service_name):
        max_attempts = 3
        attempt = 1
        
        while attempt <= max_attempts:
            result = subprocess.run(
                f'net stop {service_name}', 
                shell=True, 
                capture_output=True, 
                text=True
            )
            
            if "is not started" in result.stderr:
                print(f"{service_name} =s=")
                return True
            
            if "starting or stopping" in result.stdout.lower():
                print(f"{service_name} is in transition state. Skipping...")
                return False
            
            if "FAILED" in result.stderr or "ERROR" in result.stderr:
                print(f"Cannot stop {service_name} (might be in idle state or locked)")
                return False
                
            if result.returncode == 0:
                time.sleep(2)
                verify = subprocess.run(
                    f'sc query {service_name}', 
                    shell=True, 
                    capture_output=True, 
                    text=True
                )
                
                if "STOPPED" in verify.stdout:
                    print(f"{service_name} has been successfully stopped.")
                    return True
                    
            print(f"Attempt {attempt}/{max_attempts} to stop {service_name}")
            attempt += 1
            time.sleep(2)
            
        print(f"Failed to stop {service_name} after {max_attempts} attempts. Moving to next task.")
        return False
    
    @staticmethod
    def kill_process(process_name):
        try:
            result = subprocess.run(
                f'taskkill /F /IM {process_name}',
                shell=True,
                capture_output=True,
                text=True
            )
            
            if "SUCCESS" in result.stdout:
                print(f"Successfully terminated {process_name}")
                return True
            elif "not found" in result.stderr:
                print(f"{process_name} =s=")
                return True
            else:
                print(f"Failed to terminate {process_name}: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"Error killing process {process_name}: {str(e)}")
            return False