from setuptools import setup, find_packages

setup(
    name='ComfyUI-ETN-Nodes',
    version='1.0',
    description='ETN Nodes for ComfyUI with Blender Integration',
    author='ETN',
    packages=find_packages(),
    package_data={
        'blendertomaomi': ['*.py'],
    },
    install_requires=[
        'torch',
        'numpy',
        'Pillow',
        'websockets',
        'aiohttp',
    ],
    python_requires='>=3.7',
    entry_points={
        'blender.addon': [
            'blendertomaomi=blendertomaomi.blender_viewport_sender:register',
        ],
    },
) 