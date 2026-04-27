from collections import defaultdict

log_file = "logs/sample.log"

failed_attempts = defaultdict(int)

with open(log_file, "r") as file:
    logs = file.readlines()

for log in logs:
    parts = log.strip().split()
    ip = parts[0]
    status = " ".join(parts[1:])

    if status == "FAILED LOGIN":
        failed_attempts[ip] += 1

print("\n--- Security Log Analysis Report ---\n")

for ip, count in failed_attempts.items():
    print(f"{ip}: {count} failed login attempts")

    if count >= 3:
        print(f"⚠ Suspicious IP detected: {ip}\n")