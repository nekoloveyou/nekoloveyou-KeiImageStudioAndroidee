from pathlib import Path

root = Path('engine/app')
build = root / 'build.gradle.kts'
source = build.read_text(encoding='utf-8')
old = '''        debug {
            signingConfig = signingConfigs.getByName("release")
        }
'''
new = '''        debug {
            signingConfig = signingConfigs.getByName("debug")
        }
'''
if old not in source:
    raise RuntimeError('Upstream signing configuration changed; inspect app/build.gradle.kts')
build.write_text(source.replace(old, new, 1), encoding='utf-8')

strings = root / 'src/main/res/values/strings.xml'
s = strings.read_text(encoding='utf-8')
old_name = '<string name="app_name">Local Dream</string>'
if old_name not in s:
    raise RuntimeError('Upstream app name changed')
strings.write_text(s.replace(old_name, '<string name="app_name">凱伊 AI 繪圖室</string>', 1), encoding='utf-8')

print('Kei branding and default Android debug signing applied')
