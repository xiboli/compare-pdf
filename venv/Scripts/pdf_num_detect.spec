# -*- mode: python -*-

block_cipher = None


a = Analysis(['pdf_num_detect.py'],
             pathex=['C:\\Users\\lixib\\Desktop\\Hiwi_job\\Code\\2018.04.23\\venv\\Lib\\site-packages\\scipy\\extra-dll', 'C:\\Users\\lixib\\Desktop\\Hiwi_job\\Code\\2018.04.23\\venv\\Scripts'],
             binaries=[],
             datas=[],
             hiddenimports=['scipy._lib.messagestream'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pdf_num_detect',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
