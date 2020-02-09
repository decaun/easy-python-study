# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['simple_eel.py'],
             pathex=['/home/deniz/Desktop/myenv/py_lerning/GUI'],
             binaries=[],
             datas=[('/usr/local/lib/python3.6/site-packages/eel/eel.js', 'eel'), ('front_end', 'front_end')],
             hiddenimports=['bottle_websocket'],
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
          a.zipfiles,
          a.datas,
          [],
          name='simple_eel',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
