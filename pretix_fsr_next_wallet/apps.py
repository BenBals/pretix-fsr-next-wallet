from django.utils.translation import gettext_lazy
from . import __version__

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginApp(PluginConfig):
    default = True
    name = "pretix_fsr_next_wallet"
    verbose_name = "FSR Next Wallet"

    class PretixPluginMeta:
        name = gettext_lazy("FSR Next Wallet")
        author = "Ben Bals"
        description = gettext_lazy("Allowing payments at VerDE events and at the student coffee machine powered by a pretix backend")
        visible = True
        version = __version__
        category = "INTEGRATION"
        compatibility = "pretix>=2.7.0"

    def ready(self):
        from . import signals  # NOQA


