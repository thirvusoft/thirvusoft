from thirvusoft.thirvusoft_customizations.utils.support.issue import issue_customization
from thirvusoft.thirvusoft_customizations.utils.crm.lead import lead_customize_field


def after_install():
    issue_customization()
    lead_customize_field()
