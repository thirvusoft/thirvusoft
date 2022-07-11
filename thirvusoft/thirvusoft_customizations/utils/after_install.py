from thirvusoft.thirvusoft_customizations.utils.support.issue import issue_customization
from thirvusoft.thirvusoft_customizations.utils.crm.lead import lead_customize_field
from thirvusoft.thirvusoft_customizations.utils.user.role.roles import create_role


def after_install():
    issue_customization()
    lead_customize_field()
    create_role()
