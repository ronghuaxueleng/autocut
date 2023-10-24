from setuptools import setup, find_packages

requirements = [
    "moviepy",
    "openai",
    "openai-whisper",
    "opencc-python-reimplemented",
    "parameterized",
    "pydub",
    "srt",
    "torchaudio",
    "tqdm",
]


setup(
    name="autocut-fix",
    long_description_content_type='text/markdown',
    install_requires=requirements,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "autocut-fix = autocut.main:main",
        ]
    },
)
