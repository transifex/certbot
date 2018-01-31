"""Shim around `~certbot_dns_rackspace.dns_rackspace` for backwards compatibility."""
import warnings

import zope.interface

from certbot import interfaces
from certbot_dns_rackspace import dns_rackspace


@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(dns_rackspace.Authenticator):
    """Shim around `~certbot_dns_rackspace.dns_rackspace.Authenticator` for backwards compatibility."""

    hidden = True

    def __init__(self, *args, **kwargs):
        warnings.warn("The 'authenticator' module was renamed 'dns_rackspace'",
                      DeprecationWarning)
        super(Authenticator, self).__init__(*args, **kwargs)
