"""
CECS 277 Lab 5 
Authors: Phan Ngo - Lucas Seitz
Date: 09/23/2025
Description: Contact class used by Rolodex program.
"""

class Contact:
    #Represents a single contact entry.

    def __init__(self, fn, ln, ph, addr, city, zip):
        #Initialize a contact.
        self.first_name = fn
        self.last_name = ln
        self.phone = ph
        self.address = addr
        self.city = city
        self.zip = zip

    def __lt__(self, other):
        #Returns:
        #    bool: True if self should come before other (by last name, then first name).

        if self.last_name != other.last_name:
            return self.last_name < other.last_name
        return self.first_name < other.first_name

    def __str__(self):
        #Returns:
        #    str: Formatted string for user display.

        return (f"{self.first_name} {self.last_name}\n"
                f"{self.phone}\n"
                f"{self.address}\n"
                f"{self.city} {self.zip}")

    def __repr__(self):
        #Returns:
        #    str: 'f_name,l_name,phone,address,city,zip'
        return f"{self.first_name},{self.last_name},{self.phone},{self.address},{self.city},{self.zip}"
