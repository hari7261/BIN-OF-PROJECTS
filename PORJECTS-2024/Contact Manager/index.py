# Import necessary libraries
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Global variable for theme (light or dark mode)
current_theme = "light"  # Default theme

# Function to toggle theme (light/dark mode)
def toggle_theme():
    global current_theme
    if current_theme == "light":
        # Switch to dark mode
        root.config(bg="#333333")
        # Update all widgets with dark theme colors
        current_theme = "dark"
    else:
        # Switch to light mode
        root.config(bg="#ffffff")
        # Update all widgets with light theme colors
        current_theme = "light"

# Function to export contacts to a CSV file
def export_contacts():
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `member`")
    contacts = cursor.fetchall()
    conn.close()
    
    if contacts:
        try:
            with open("contacts.csv", "w", newline="") as file:
                writer = csv.writer(file)
                # Write header row
                writer.writerow(["MemberID", "Firstname", "Lastname", "Gender", "Age", "Address", "Contact"])
                # Write data rows
                for contact in contacts:
                    writer.writerow(contact)
            messagebox.showinfo("Export Successful", "Contacts exported to contacts.csv")
        except Exception as e:
            messagebox.showerror("Export Error", f"Error: {str(e)}")
    else:
        messagebox.showwarning("No Contacts", "No contacts to export.")

# Function to search contacts by name or contact number
def search_contacts():
    keyword = search_var.get().strip().lower()
    if keyword:
        conn = sqlite3.connect("contact.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `member` WHERE LOWER(firstname) LIKE ? OR LOWER(lastname) LIKE ? OR contact LIKE ?", ('%'+keyword+'%', '%'+keyword+'%', '%'+keyword+'%'))
        contacts = cursor.fetchall()
        conn.close()
        
        tree.delete(*tree.get_children())
        for contact in contacts:
            tree.insert("", "end", values=contact)
    else:
        # If search box is empty, display all contacts
        Database()

# Initialize Tkinter
root = tk.Tk()
root.title("Contact Management System")

# Add widgets and implement functionalities as per your design

# Example: Adding a search box
search_var = tk.StringVar()
search_entry = ttk.Entry(root, textvariable=search_var)
search_entry.pack()

search_button = ttk.Button(root, text="Search", command=search_contacts)
search_button.pack()

# Example: Toggle Theme button
theme_button = ttk.Button(root, text="Toggle Theme", command=toggle_theme)
theme_button.pack()

# Example: Export Contacts button
export_button = ttk.Button(root, text="Export Contacts", command=export_contacts)
export_button.pack()

# Run the main loop
if __name__ == "__main__":
    root.mainloop()
