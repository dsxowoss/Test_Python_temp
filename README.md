
# Test Python

El proyecto se encarga de obtener una carpeta de archivos de texto (txt), agruparlos en uno solo, convertirlo en un archivo PDF y enviarlo via correo.


## Instalación

El codigo esta diseñado para funcionar con Python 9 en adelante.

- Clonar el repositorio de GitHub.
- Navegar a la ruta del proyecto clonado.
- (Opcional) Crear un entorno virtual.
```bash
  py -m venv venv
```
- Activar el entorno virtual.
```bash
  .\venv\Scripts\activate
```
- Importar modulos desde un archivo de requerimientos.
```bash
  pip install -r requirements.txt
```

## Ejecución

- Ejecutar el comando
```bash
  python app.py
```
- En la consola se le solicitara un correo, donde se le enviaran los resultados del test.
- De existir cualquier error se desplegara el mensaje en la consola.
