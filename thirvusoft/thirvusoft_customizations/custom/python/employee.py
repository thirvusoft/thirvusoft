def employee_abbreviation(doc,event):
    if doc.employment_type:
        doc.abbr = doc.employment_type[0:3].upper()
    else:
        doc.abbr = 'EMP'
    