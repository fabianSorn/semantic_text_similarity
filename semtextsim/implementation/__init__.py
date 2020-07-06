from typing import Dict, Type, Optional, Any
from abc import ABC
import logging
_logger = logging.getLogger(__name__)

from semtextsim.interface import Encoder as AbcEncoder
from semtextsim.interface import Comparer as AbcComparer
from .bert import Encoder
from .cosinus import Comparer


_providers: Dict[Type[ABC], Type] = {AbcEncoder: Encoder(),
                                     AbcComparer: Comparer()}


def inject(interface: Type[ABC]) -> Optional[Any]:
    global _providers
    instance = _providers.get(interface, None)
    if instance is None:
        _logger.warning(f"Could not find provider for "
                        f"interface {interface} in {str(__file__)}")
    return instance