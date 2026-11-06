# Demonstration: broad except/pass hides programming mistakes.
try:
    presnt = 10
    print(present)  # typing mistake: present was never defined
except Exception:
    pass
print("Program continued, but the NameError was hidden.")
