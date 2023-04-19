
import re
email=input("what is your email? ").strip()


if re.match(r"[^@]^"):
    print("valid")
        
        
else:
    print("invalid")