def employee_abbreviation(doc,event):
    doc.abbr = doc.employment_type[0:3].upper()
    