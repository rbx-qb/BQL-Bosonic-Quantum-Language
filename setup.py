from setuptools import setup, find_packages

setup(
    name="BQL",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "qiskit",
        "matplotlib",
        "numpy"
    ],
    author="Rafael Brayan",
    description="Bosonic Quantum Language (BQL) para emaranhamento quântico",
    url="https://github.com/seu-usuario/BQL",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)


