import os

readable = os.access('C:/Windows/System32', os.R_OK)
print(readable)

writable = os.access('C:/Windows/System32', os.W_OK)
print(writable)