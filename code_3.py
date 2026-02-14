#QUESTION:Count how many INFO,WARNING AND ERROR messages are present in a list of system logs.
logs = [
    "INFO: User logged in",
    "ERROR: Payment failed",
    "WARNING: Low disk space",
    "INFO: Item added to cart",
    "ERROR: Timeout"
]
info=0
warning=0
error=0

for line in logs:
    if "INFO" in line:
        info+=1
    if "WARNING" in line:
        warning+=1
    if "ERROR" in line:
        error+=1
print("INFO:",info)
print("WARNING:",warning)
print("ERROR:",error)
