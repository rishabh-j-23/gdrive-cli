cd ../bin
bash
source ../../scripts/activate
python -m nuitka --follow-imports ../__init__.py --output-filename=gdrive
