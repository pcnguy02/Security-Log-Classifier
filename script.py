import re


# stored_logs = []

records = [
    {"username": "rgilardi0", "ip": "224.187.190.102", "result": "FAILURE"},
    {"username": "dwildin1", "ip": "239.238.162.240", "result": "SUCCESS"},
    {"username": "kughi2", "ip": "86.191.0.119", "result": "FAILURE"},
    {"username": "skopfer3", "ip": "111.144.93.1", "result": "FAILURE"},
]

def internal_check(ip):

    if ip.startswith("192.168.") or ip.startswith("10."):
        print(f"{ip} is an internal address.")
        return True

        
    for i in range(16, 32): # Loops through IP within range of 2nd octet in 172
        if ip.startswith(f"172.{i}."):
            print(f"{ip} is an internal address.")
            return True
    
    return False

def main():  
    failed_logins = 0
    successful_logins = 0
    internal_count = 0
    external_count = 0
    
    for record in records:
        if record["result"] == "FAILURE":
            failed_logins += 1
        else:
            successful_logins += 1
    
        ip = record["ip"]
        is_internal = internal_check(ip)
        
        if is_internal:
            internal_count += 1
        else:
            external_count += 1
        
        
            
            
            

    print(f"Total login attempts: {failed_logins + successful_logins}")
    print(f"Successful logins:  {successful_logins}")
    print(f"Failed logins:  {failed_logins}")
    print(f"Internal IPs:  {internal_count}")
    print(f"External IPs:  {external_count}")
        

        
    
    


if __name__=="__main__":
    main()
    

    



