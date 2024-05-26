import os
import sys

# Obtén la ruta del directorio donde se encuentra el script actual
ruta_actual = os.path.dirname(os.path.abspath(__file__))

# Si necesitas subir en la jerarquía de directorios (por ejemplo, si tu script está en un subdirectorio), puedes usar:
# ruta_base = os.path.join(ruta_actual, '..', '..')

# Asegúrate de resolver cualquier ruta relativa a una ruta absoluta
ruta_base = os.path.abspath(ruta_actual)

# Agrega la ruta base al sys.path si no está ya incluida
if ruta_base not in sys.path:
    sys.path.append(ruta_base)
print(sys.path)
