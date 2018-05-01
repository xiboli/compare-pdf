# -*- mode: python -*-

block_cipher = None


a = Analysis(['pdf2jpg.py'],
             pathex=['C:\\Users\\lixib\\Desktop\\Hiwi_job\\Code\\2018.04.23\\venv\\Scripts'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          name='pdf2jpg',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
