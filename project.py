import tkinter as tk
from tkinter import ttk, messagebox
import csv
import re

class Address:
    def __init__(self, state, city, pincode):
        self.state = state
        self.city = city
        self.pincode = pincode

class Person:
    number_of_people = 0

    def __init__(self, user_id, password, type) :
        self.status = 0
        self.user_id = user_id
        self.password = password
        self.type = type
        self.name = ""
        self.dob = ""
        self.phone = 0
        self.department = "" 
        self.gender = ""
        Person.number_of_people += 1

    def changePassword(self, new_password):
        self.password = new_password

    def changeName(self, new_name):
        self.name = new_name   

    def changeDob(self, new_dob):
        self.dob = new_dob

    def changePhone(self, new_phone):
        self.phone = new_phone

    def setDetails(self, name, dob, phone, department, gender) :
        self.name = name
        self.dob = dob
        self.phone = phone
        self.department = department
        self.gender = gender
        self.status = 1

    def deactivate(self):
        self.status = -1



    
