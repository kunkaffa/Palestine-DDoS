import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("pip install asyncio")
    os.system("pip install validators")
elif c == "1":
    os.system("pip3 install asyncio")
    os.system("pip install validators")
print("Done.")
