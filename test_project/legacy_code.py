import time

global_config_timeout = 30

def process_data_and_save_and_notify(data_input):
    global global_config_timeout
    
    # Process
    result = data_input * 2
    time.sleep(1)
    
    # Save
    db_status = True
    if db_status:
        print(f"Data {result} saved with timeout {global_config_timeout}")
        
    # Notify
    print("Notification sent to admin.")
    
    return result

if __name__ == "__main__":
    process_data_and_save_and_notify(50)
