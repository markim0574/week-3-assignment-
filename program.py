

# Read from an existing file
try:
    with open("input.txt", "r") as infile:
        content = infile.read()
except FileNotFoundError:
    print("❌ input.txt not found.")
    exit(1)

# Modify the content (example: make it uppercase)
modified_content = content.upper()

# Write to a new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("✅ File has been modified and saved as output.txt")
# Error Handling Lab 🧪

filename = input("Enter the filename you want to open: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile content:\n")
        print(content)

except FileNotFoundError:
    print("❌ Error: The file does not exist.")
except PermissionError:
    print("❌ Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
