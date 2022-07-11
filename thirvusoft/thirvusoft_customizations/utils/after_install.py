from thirvusoft.thirvusoft_customizations.utils.support.issue import issue_customization
from thirvusoft.thirvusoft_customizations.utils.crm.lead import customize
from thirvusoft.thirvusoft_customizations.utils.user.role.roles import create_role


def after_install():
    issue_customization()
    customize()
    create_role()
