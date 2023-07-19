
# Test Python

El proyecto se encarga de obtener una carpeta de archivos de texto (TXT), agruparlos en uno solo, convertirlo en un archivo PDF y enviarlo vía correo.


## Instalación

El código está diseñado para funcionar con Python 9 en adelante.

- Clonar el repositorio de GitHub.
- Navegar a la ruta del proyecto clonado.
- (Opcional) Crear un entorno virtual.
```bash
py -3.9 -m venv venv
```
- Activar el entorno virtual.
```bash
.\venv\Scripts\activate
```
- Importar módulos desde un archivo de requerimientos.
```bash
pip install -r requirements.txt
```

## Ejecución

- Ejecutar el comando
```bash
python app.py
```
- Se verificará que la carpeta "report" exista dentro del proyecto, de no existir se creará.
- Se creará un solo archivo de texto con toda la información de los demás archivos.
- Se convertirá el archivo de texto en un archivo PDF.
- En la consola se le solicitará un correo, donde se le enviaran los resultados del test (PDF).
- De existir cualquier error se desplegará el mensaje en la consola.
