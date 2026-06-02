"""Core fabric physics prompt module."""

from dataclasses import asdict, dataclass
from typing import Any, Dict


@dataclass
class CoreFabricPhysics:
    """Base physical assumptions for realistic fabric behavior."""

    name: str = "Core Fabric Physics"
    description: str = "Treat garments as volumetric cloth systems rather than flat texture overlays"
    volumetric_thickness: bool = True
    surface_continuity: float = 0.9
    force_chain_propagation: float = 0.85
    contact_shadow_required: bool = True

    def generate_prompt(self) -> str:
        return (
            "Core fabric physics: volumetric garment thickness, coherent cloth surface continuity, "
            f"force-chain propagation {self.force_chain_propagation}, "
            f"contact shadows {'required' if self.contact_shadow_required else 'optional'}"
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
