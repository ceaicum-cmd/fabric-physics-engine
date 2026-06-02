"""Material control prompt module."""

from dataclasses import asdict, dataclass
from typing import Any, Dict


@dataclass
class MaterialControl:
    """Material-specific visual and mechanical controls."""

    name: str = "Material Control"
    description: str = "Controls fabric stiffness, thickness, sheen, grain, and stretch"
    stiffness_response: float = 0.7
    thickness_preservation: float = 0.9
    weave_visibility: float = 0.55
    material_identity_lock: bool = True

    def generate_prompt(self) -> str:
        return (
            f"Material control: stiffness response {self.stiffness_response}, "
            f"thickness preservation {self.thickness_preservation}, weave visibility {self.weave_visibility}, "
            f"material identity {'locked' if self.material_identity_lock else 'flexible'}"
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
