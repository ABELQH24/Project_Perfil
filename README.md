

```bash
source .venv/Scripts/activate
pip install -r requirements.dev.txt
python -m pip install Pillow
```
 
python manage.py makemigrations
python manage.py migrate
