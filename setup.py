from setuptools import find_packages, setup

setup(
    name="fabric-physics-engine",
    version="0.1.0",
    description="Modular fabric physics and prompt-realism engine for AI image generation.",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "pydantic>=1.8.0",
    ],
    extras_require={"dev": ["pytest>=6.2.0"]},
    python_requires=">=3.9",
)
