#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import difflib
import os

def load_medications_from_csv(filename):
    medications_df = pd.read_csv(filename)
    medications = medications_df.to_dict(orient='records')
    return medications

def get_closest_match(tablet_name, medication_names):
    closest_matches = difflib.get_close_matches(tablet_name, medication_names, n=1, cutoff=0.6)
    if closest_matches:
        return closest_matches[0]
    else:
        return None

def get_tablet_uses(tablet_name, medications):
    medication_names = [med['Composition'] for med in medications]
    closest_match = get_closest_match(tablet_name, medication_names)
    if closest_match:
        for med in medications:
            if med['Composition'] == closest_match:
                return med['Uses']
    return "Uses not found for the tablet: {}".format(tablet_name)

if __name__ == "__main__":
    filename = r'F:\\B.tech\\Medicine_Details.csv'

    if os.path.isfile(filename):
        medications = load_medications_from_csv(filename)
        tablet_name = input("Enter the name of the tablet:")
        uses = get_tablet_uses(tablet_name, medications)
        print("Uses:")
        print(uses)
    else:
        print(f"File not found: {filename}. Please ensure the file exists and the path is correct.")
    input()

