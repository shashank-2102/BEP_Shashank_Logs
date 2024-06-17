import os

#############################        CODE FROM       #############################
#### https://www.listendata.com/2023/08/python-code-to-run-windscribe-vpn.html ####

def windscribe(action, location=None):
    windscribe_cli_path = r"C:\\Program Files\\Windscribe\\windscribe-cli.exe"
    
    if location is None:
        command = f'"{windscribe_cli_path}" {action}'
    else:
        command = f'"{windscribe_cli_path}" {action} {location}'
    
    os.system(command)

# Connect
windscribe("connect", "US Central")

# Disconnect
windscribe("disconnect")



