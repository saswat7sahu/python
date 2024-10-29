import re
st="This is a complete Python Roadmap for beginners and advanced developers."
print(re.findall(r'^[A-Z]+$',st))