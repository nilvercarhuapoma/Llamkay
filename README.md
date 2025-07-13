# Llamkay 

# 🛠 Solución al Problema: "No changes detected" en Django al usar `makemigrations`

Este documento describe cómo solucionar el error común en Django donde al ejecutar `python manage.py makemigrations` no se detectan cambios, especialmente después de haber eliminado carpetas de migraciones manualmente.

---

## 💡 Problema

Al ejecutar:

```bash
python manage.py makemigrations

# 1er Paso
    En las carpetas llamadas migrations, se debe eliminar el 0001_init.py ya que este .py no permite crear migrations ya que ya fueron creados y por eso nace este .py, solamente conservar lo que dice __init__.py, entonces una vez hecho eso solamente hace falta ejecutar el comando   `python manage.py makemigrations`