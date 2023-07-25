from setuptools import setup, find_packages

requirements = [
    "srt",
    "moviepy",
    "opencc-python-reimplemented",
    "torchaudio",
    "parameterized",
    "openai-whisper",
    "tqdm",
]


setup(
    name="autocut",
    long_description_content_type='text/markdown',
    install_requires=requirements,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "autocut = autocut.main:main",
        ]
    },
)
