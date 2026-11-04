ip = input("Enter IP address: ")
method = input("Enter HTTP method (e.g., POST, GET): ")
path = input("Enter URL path: ")
status = input("Enter HTTP status code: ")
bytes_sent = input("Enter bytes transferred: ")

log_line = f'{ip} - "{method} {path}" {status} {bytes_sent}'

print(log_line)