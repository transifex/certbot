"""Certbot Rackspace CloudDNS authenticator plugin."""
import logging

import pyrax
import zope.interface

from certbot import interfaces
from certbot.plugins import dns_common


logger = logging.getLogger(__name__)

INSTRUCTIONS = (
    "To use certbot-dns-rackspace, configure credentials as described at "
    "https://github.com/pycontribs/pyrax/blob/master/docs/getting_started.md#set-up-authentication "  # pylint: disable=line-too-long
    "and make sure your user has read-write access to the CloudDNS API.")


@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(dns_common.DNSAuthenticator):
    """Rackspace CloudDNS Authenticator

    This authenticator solves a DNS01 challenge by uploading the answer to Rackspace
    CloudDNS.
    """

    description = ("Obtain certificates using a DNS TXT record (if you are"
                   " using Rackspace CloudDNS for DNS).")
