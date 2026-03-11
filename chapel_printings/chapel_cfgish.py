import yamale
from pathlib import Path
import munch


def load_chapel_config(config_ish_file=None):
    installdir = Path(__file__).resolve().parent

    schema = yamale.make_schema(installdir / 'chapel_cfgish.yamale')

    if config_ish_file is None:
        config_ish_file = Path(__file__).resolve().parent / "default_chapel_cfgish.yml"

    data = yamale.make_data(config_ish_file)
    yamale.validate(schema, data)

    # yamale can handle multiple sub-schemas etc. We only use 1, so
    # pull that out for direct use
    data = data[0][0]

    as_attr = munch.munchify(data)
    return as_attr
