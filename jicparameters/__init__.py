"""jicparameters package."""

import yaml

__version__ = "0.0.1"


class Parameters(dict):
    """Class for storing, reading in and writing out parameters."""

    @classmethod
    def from_yaml(cls, string):
        """Return Parameter instance from yaml string."""
        p = cls()
        d = yaml.load(string)
        p.update(d)
        return p

    def to_yaml(self):
        """Return yaml string representation."""
        return yaml.dump(dict(self),
                         explicit_start=True,
                         default_flow_style=False)
