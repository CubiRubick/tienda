# tienda

# clonar repositorio con el git clone

#instalar las dependencias 
pip install -r requirements.txt

# realizar migraciones
py manage.py makemigrations

# migrar la base de datos 
py manage.py migrate

# crear super usuario
py manage.py createsuperuser

# correr el proyect
py manage.py runserver
