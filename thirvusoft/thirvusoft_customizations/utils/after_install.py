from thirvusoft.thirvusoft_customizations.utils.support.issue import issue_customization
from thirvusoft.thirvusoft_customizations.utils.hr.employee.employee import employee_customization
from thirvusoft.thirvusoft_customizations.utils.crm.lead import customize
from thirvusoft.thirvusoft_customizations.utils.user.role.roles import create_role
from thirvusoft.thirvusoft_customizations.utils.hr.job_applicant.job_applicant import job_applicant_custom_fields
from thirvusoft.thirvusoft_customizations.utils.hr.job_applicant.job_applicant import job_applicant_property


def after_install():
    issue_customization()
    customize()
    create_role()
    employee_customization()
    job_applicant_custom_fields()
    job_applicant_property()
