"""Fabric compression prompt module."""

from dataclasses import asdict, dataclass
from typing import Any, Dict


@dataclass
class CompressionSystem:
    """Controls compression folds and pressure-zone deformation."""

    name: str = "Compression System"
    description: str = "Contact compression, bunching, and pressure-zone deformation"
    compression_strength: float = 0.65
    contact_deformation: float = 0.8
    bunching_density: float = 0.5
    soft_tissue_response: bool = True

    def generate_prompt(self) -> str:
        return (
            f"Compression: contact deformation {self.contact_deformation}, "
            f"compression strength {self.compression_strength}, bunching density {self.bunching_density}, "
            f"soft-tissue response {'enabled' if self.soft_tissue_response else 'disabled'}"
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
