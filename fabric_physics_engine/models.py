"""Pre-configured garment models."""

import numpy as np
from typing import Dict
from .fabrics import FabricProperties


class GarmentModel:
    """Base class for garment models."""
    
    def __init__(self, fabric_properties: FabricProperties):
        """Initialize garment model."""
        self.fabric_properties = fabric_properties
        self.mesh = self._create_mesh()
    
    def _create_mesh(self) -> Dict[str, np.ndarray]:
        """Create garment mesh."""
        raise NotImplementedError
    
    def get_pinned_vertices(self) -> np.ndarray:
        """Get indices of pinned vertices."""
        return np.array([], dtype=int)


class ShirtModel(GarmentModel):
    """T-shirt or shirt model."""
    
    def __init__(self, fabric_properties: FabricProperties, width: float = 0.4, 
                 height: float = 0.6):
        """Initialize shirt model."""
        self.width = width
        self.height = height
        super().__init__(fabric_properties)
    
    def _create_mesh(self) -> Dict[str, np.ndarray]:
        """Create a simple shirt mesh using a grid."""
        segments_x = 20
        segments_y = 30
        
        x = np.linspace(-self.width/2, self.width/2, segments_x)
        y = np.linspace(0, self.height, segments_y)
        xx, yy = np.meshgrid(x, y)
        
        vertices = np.stack([xx.flatten(), yy.flatten(), np.zeros_like(xx).flatten()], axis=1)
        vertices = vertices.astype(np.float32)
        
        faces = []
        for i in range(segments_y - 1):
            for j in range(segments_x - 1):
                v0 = i * segments_x + j
                v1 = v0 + 1
                v2 = v0 + segments_x
                v3 = v2 + 1
                
                faces.append([v0, v1, v2])
                faces.append([v1, v3, v2])
        
        faces = np.array(faces, dtype=np.uint32)
        mass = np.ones(len(vertices)) * (self.fabric_properties.density / len(vertices))
        
        return {
            "vertices": vertices,
            "faces": faces,
            "mass": mass,
        }
    
    def get_pinned_vertices(self) -> np.ndarray:
        """Get shoulder vertices."""
        return np.array([0, 19], dtype=int)


class DressModel(GarmentModel):
    """Dress model."""
    
    def __init__(self, fabric_properties: FabricProperties, width: float = 0.5,
                 height: float = 1.2):
        """Initialize dress model."""
        self.width = width
        self.height = height
        super().__init__(fabric_properties)
    
    def _create_mesh(self) -> Dict[str, np.ndarray]:
        """Create a simple dress mesh."""
        segments_x = 25
        segments_y = 40
        
        vertices = []
        for i in range(segments_y):
            t = i / (segments_y - 1)
            current_width = self.width * (1 + 0.5 * t)
            
            for j in range(segments_x):
                angle = (j / segments_x) * 2 * np.pi
                x = current_width * np.cos(angle) / 2
                z = current_width * np.sin(angle) / 2
                y = self.height - i / (segments_y - 1) * self.height
                vertices.append([x, y, z])
        
        vertices = np.array(vertices, dtype=np.float32)
        
        faces = []
        for i in range(segments_y - 1):
            for j in range(segments_x):
                v0 = i * segments_x + j
                v1 = v0 + 1 if j < segments_x - 1 else i * segments_x
                v2 = v0 + segments_x
                v3 = v2 + 1 if j < segments_x - 1 else (i + 1) * segments_x
                
                faces.append([v0, v1, v2])
                faces.append([v1, v3, v2])
        
        faces = np.array(faces, dtype=np.uint32)
        mass = np.ones(len(vertices)) * (self.fabric_properties.density / len(vertices))
        
        return {
            "vertices": vertices,
            "faces": faces,
            "mass": mass,
        }
    
    def get_pinned_vertices(self) -> np.ndarray:
        """Get shoulder vertices."""
        return np.arange(0, 25, dtype=int)
