# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import copy_metadata, collect_data_files
from os import path
import platform
plat = platform.system().lower()

datas = []
datas += collect_data_files('torch')
datas += copy_metadata('tqdm')
datas += copy_metadata('regex')
datas += copy_metadata('requests')
datas += copy_metadata('packaging')
datas += copy_metadata('filelock')
datas += copy_metadata('numpy')
datas += copy_metadata('tokenizers')
datas += copy_metadata('torch')

datas += collect_data_files('transformers', include_py_files=True)

datas += [(path.join(
    './python/Lib/site-packages',
    'moviepy'
), 'moviepy')]
datas += [(path.join(
    './python/Lib/site-packages',
    'imageio_ffmpeg'
), 'imageio_ffmpeg')]
datas += [(path.join(
    './python/Lib/site-packages',
    'torchaudio'
), 'torchaudio')]
datas += [(path.join(
    './python/Lib/site-packages',
    'whisper'
), 'whisper')]
datas += [(path.join(
    './python/Lib/site-packages',
    'opencc'
), 'opencc')]
datas += [('./snakers4_silero-vad_master', './snakers4_silero-vad_master')]

block_cipher = None


a = Analysis(
    ['autocut.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='autocut',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='autocut',
)
