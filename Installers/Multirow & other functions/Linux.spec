# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['Builder.py'],
             pathex=['.'],
             binaries=[],
             datas=[("icon.gif", ".")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
             
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          Tree('.//utils', prefix="utils"),
          Tree('.//root', prefix="root"),
          Tree('.//functions', prefix="functions"),
          a.zipfiles,
          a.datas,
          [],
          name='Multirow-Patcher-Quantum-Nox-Installer-Linux-x.y.z.elf',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False)
