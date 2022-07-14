
from thirvusoft.thirvusoft_customizations.utils.support.issue import issue_customization
from thirvusoft.thirvusoft_customizations.utils.hr.employee.employee import employee_customization

def after_install():
    issue_customization()
    employee_customization()