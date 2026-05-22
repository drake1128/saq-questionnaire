"""Verify required dependencies for the CAS 2026 image pipeline."""
import sys
import importlib

REQUIRED = ['fitz', 'jinja2']
if sys.platform == 'win32':
    REQUIRED.append('win32com.client')

def main():
    missing = []
    for mod in REQUIRED:
        try:
            importlib.import_module(mod)
            print(f'  OK   {mod}')
        except ImportError:
            print(f'  FAIL {mod}')
            missing.append(mod)

    if missing:
        print(f'\nMissing modules: {missing}')
        print('Install with: pip install -r tools/cas-2026-pipeline/requirements.txt')
        sys.exit(1)

    if sys.platform == 'win32':
        try:
            import win32com.client
            ppt = win32com.client.Dispatch('PowerPoint.Application')
            print('  OK   PowerPoint COM dispatch')
            ppt.Quit()
        except Exception as e:
            print(f'  FAIL PowerPoint COM: {e}')
            sys.exit(1)

    print('\nAll dependencies OK.')

if __name__ == '__main__':
    main()
