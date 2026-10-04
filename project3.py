import re

print("========================================")
print("       PHISHING AWARENESS ANALYSIS")
print("========================================")

message = input("\nEnter the email or message to analyze:\n")

# Convert message to lowercase
text = message.lower()

# Suspicious keywords commonly used in phishing
suspicious_keywords = [
    "urgent",
    "verify your account",
    "verify",
    "password",
    "click here",
    "account suspended",
    "confirm your account",
    "login",
    "bank",
    "winner",
    "prize",
    "free",
    "immediately",
    "security alert"
]

# Check for suspicious keywords
found_keywords = []

for keyword in suspicious_keywords:
    if keyword in text:
        found_keywords.append(keyword)

# Find links
links = re.findall(r'https?://\S+|www\.\S+', message)

# Display results
print("\n========== ANALYSIS RESULT ==========")

if found_keywords:
    print("\n[!] Suspicious Keywords Found:")
    for keyword in found_keywords:
        print(" -", keyword)
else:
    print("\n[+] No suspicious keywords found.")

if links:
    print("\n[!] Suspicious Links Found:")
    for link in links:
        print(" -", link)
else:
    print("\n[+] No links found.")

# Red flags
red_flags = []

if found_keywords:
    red_flags.append("The message contains suspicious or urgent keywords.")

if links:
    red_flags.append("The message contains a link that may be unsafe.")

if "urgent" in text or "immediately" in text:
    red_flags.append("The message creates a sense of urgency.")

if "password" in text or "login" in text:
    red_flags.append("The message may be trying to obtain login information.")

if "prize" in text or "winner" in text or "free" in text:
    red_flags.append("The message may contain a fake reward or offer.")

print("\n========== RED FLAGS ==========")

if red_flags:
    for flag in red_flags:
        print("[!] " + flag)
else:
    print("[+] No major phishing red flags detected.")

# Final decision
print("\n========== FINAL ANALYSIS ==========")

if len(red_flags) >= 2:
    print("[DANGER] This message is likely a PHISHING ATTEMPT.")
    print("\nWhy is it unsafe?")
    print("The message contains multiple warning signs.")
    print("Do not click suspicious links or provide personal information.")
elif len(red_flags) == 1:
    print("[WARNING] This message may be suspicious.")
    print("Verify the sender before taking any action.")
else:
    print("[SAFE] No obvious phishing signs were detected.")
    print("However, always verify unknown messages before trusting them.")

print("\n========================================")
print("           Analysis Complete")
print("========================================")