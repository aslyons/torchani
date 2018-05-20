import pkg_resources
import torch

buildin_const_file = pkg_resources.resource_filename(
    __name__, 'resources/rHCNO-4.6R_16-3.1A_a4-8_3.params')

buildin_sae_file = pkg_resources.resource_filename(
    __name__, 'resources/sae_linfit.dat')

buildin_network_dir = pkg_resources.resource_filename(
    __name__, 'resources/networks/')

buildin_dataset_dir = pkg_resources.resource_filename(
    __name__, 'resources/')

default_dtype = torch.float32
default_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

from .energyshifter import EnergyShifter
from .nn import ModelOnAEV, PerSpeciesFromNeuroChem
from .aev import SortedAEV
import logging

__all__ = ['SortedAEV', 'EnergyShifter', 'ModelOnAEV', 'PerSpeciesFromNeuroChem', 'data',
           'buildin_const_file', 'buildin_sae_file', 'buildin_network_dir', 'buildin_dataset_dir',
           'default_dtype', 'default_device']

try:
    from .neurochem_aev import NeuroChemAEV
    __all__.append('NeuroChemAEV')
except ImportError:
    logging.log(logging.WARNING,
                'Unable to import NeuroChemAEV, please check your pyNeuroChem installation.')
