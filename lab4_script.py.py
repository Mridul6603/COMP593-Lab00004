from log_analysis import get_log_file_path_from_cmd_line, filter_log_by_regex
import pandas as pd
import re
def main():
    log_file = get_log_file_path_from_cmd_line(1)
    port_traffic = tally_port_traffic(log_file)
    
    for port_num, count in port_traffic.items():
        if count >=100:
             generate_port_traffic_report(log_file, 40686)

    log_file_path = "C:\Users\Owner\Desktop\SEMESTER4\Scripting\COMP593-Lab00004\gateway.log"
    source_ip = "220.195.35.40"
    generate_source_ip_log(log_file, source_ip)
    

    pass
    

def tally_port_traffic(log_file):
    data = filter_log_by_regex(log_file, r'DPT=(.+?) ')[1]
    port_traffic = {}
    for d in data:
        port = d[0]
        port_traffic[port] = port_traffic.get(port, 0) + 1
    return port_traffic


def generate_port_traffic_report(log_file, port_number):
   
    regex_filter = r'^(.{6}) (.*) muth.*SRC=(.?) DST=(.?) .*SPT=(.*?) ' + f'DPT=({port_number}) '
    report_records = filter_log_by_regex(log_file, regex_filter)[1]

    report_df = pd.DataFrame(report_records)
    header_row = ('Date', 'Time', 'Source IP Address', 'Destination IP Address', 'Source Port', 'Destination Port')
    report_df.to_csv(f'destination_port_{port_number}_report.csv', index=False, header=header_row)

    return

# TODO: Step 11
def generate_invalid_user_report(log_file):

# Define regular expression pattern to match lines indicating attempted login by invalid user
    pattern = r'^(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2}).*Failed password for invalid user (\S+) from (\d+\.\d+\.\d+\.\d+)'

# Open log file for reading and CSV file for writing
    with open('gateway.log', 'r') as logfile, open('output.csv', 'w') as csv_file:
    # Write header row to CSV file
        csv_file.write('Date,Time,Username,IP address\n')
        match = 0
    # Loop over lines in log file
        for line in logfile:
        # Check if line matches pattern for attempted login by invalid user
            match = re.match(pattern, line)
            if match:
                # Extract information from match object
                date = match.group(1)
                time = match.group(2)
                username = match.group(3)
                ip_address = match.group(4)
                
                # Write information to CSV file
                csv_file.write(f'{date},{time},{username},{ip_address}\n')

    

# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
    return

if __name__ == '__main__':
    main()