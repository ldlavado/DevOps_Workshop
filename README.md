# Taller práctico de DevOps: De código a producción

## Objetivo

Documentar el flujo completo realizado en este taller:

**Código → Pruebas → Git → GitHub → GitHub Actions → Docker → Feedback → Corrección**

El proyecto es una calculadora de consola en Python. El trabajo incluye la implementación de las operaciones, sus pruebas automatizadas, la integración continua en GitHub Actions, la construcción de una imagen Docker y la observación de un fallo intencional seguido de su corrección.

## Qué quedó implementado

- `calculator.py`: `suma`, `resta`, `multiplicacion` y `division`. La división lanza `ValueError` si `b == 0`.
- `main.py`: menú de opciones 1 a 6 con las cuatro operaciones, healthcheck y salida.
- `test_calculator.py`: 5 tests para resta, multiplicación, suma, división y división entre cero.
- `Dockerfile`: imagen basada en `python:3.12-slim` que ejecuta `main.py`.
- `.github/workflows/ci.yml`: ejecución de `pytest` y `docker build -t devops-workshop .` en pushes y pull requests hacia `main`.

## Estructura del proyecto

```text
DevOps_WorkShop/
├── .github/
│   └── workflows/
│       └── ci.yml
├── evidence/
│   ├── CI.png
│   ├── CI-1.png
│   ├── CI-2.png
│   ├── CI-3.png
│   ├── CI-4.png
│   └── CI-5.png
├── .gitignore
├── Dockerfile
├── README.md
├── calculator.py
├── main.py
├── requirements.txt
└── test_calculator.py
```

## Requisitos y arranque

Requisitos:

- Python 3.12 o superior
- Git
- Docker
- Cuenta y acceso al repositorio de GitHub

Repositorio: <https://github.com/ldlavado/DevOps_Workshop>

```bash
git clone git@github.com:ldlavado/DevOps_Workshop.git
cd DevOps_WorkShop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
pytest
```

El menú final de la aplicación es:

```text
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Healthcheck
6. Salir
```

El healthcheck muestra el estado `OK` de la aplicación. La opción de división informa el error cuando se intenta dividir entre cero sin cerrar el programa.

## Flujo completado

### 1. Implementación y primer pipeline exitoso

Se agregaron `suma` y `division`, junto con sus pruebas. El primer pipeline terminó correctamente después del commit `Agregar suma y division con pruebas`.

![Pipeline inicial exitoso](evidence/CI.png)

### 2. Validación con Docker

La imagen se construyó con el nombre `devops-workshop` y el contenedor se ejecutó de forma interactiva. La captura muestra el menú completo de la calculadora dentro del contenedor.

![Docker build y menú de la aplicación](evidence/CI-1.png)

### 3. Fallo intencional en las pruebas

Se introdujo un error intencional en la función de suma para comprobar que las pruebas y la integración continua detectaran una regresión. La ejecución local falló en `test_suma` con la aserción `5 == 15`.

![Fallo local del test de suma](evidence/CI-2.png)

El mismo cambio provocó que GitHub Actions quedara en rojo en los runs asociados a `Introducir error intencional`.

![GitHub Actions en rojo](evidence/CI-3.png)

### 4. Corrección y recuperación

Se corrigió la función `suma`, se verificaron nuevamente las cinco pruebas y se enviaron los cambios con el commit `Corregir funcion suma`.

![Pruebas corregidas y push](evidence/CI-4.png)

El historial final de Actions muestra la secuencia esperada: pipeline verde para la implementación de suma y división, pipeline rojo para el error intencional y pipeline verde después de la corrección.

![Historial completo de GitHub Actions](evidence/CI-5.png)

## Comandos principales

Ejecutar las pruebas locales:

```bash
source .venv/bin/activate
pytest
```

Construir y ejecutar la aplicación con Docker:

```bash
docker build -t devops-workshop .
docker run -it devops-workshop
```

El pipeline de GitHub Actions ejecuta automáticamente:

```bash
pytest
docker build -t devops-workshop .
```

## Resultado

El taller quedó completado con el flujo de feedback verificado: una implementación funcional pasó las pruebas y el pipeline, un error intencional fue detectado localmente y en GitHub Actions, y la corrección restauró el estado verde con las cinco pruebas aprobadas.
# Taller práctico de DevOps: De código a producción

## Descripción

En este taller construiremos un flujo básico de DevOps utilizando una aplicación de calculadora desarrollada en Python.

El proyecto inicial contiene dos operaciones:

- Resta
- Multiplicación

Durante el taller se deberán incorporar dos nuevas funcionalidades:

- Suma
- División

Además, se crearán pruebas automatizadas para las funcionalidades agregadas y se configurará un pipeline de Integración Continua utilizando GitHub Actions.

Finalmente, la aplicación será ejecutada mediante Docker y se provocará intencionalmente un error para observar cómo el pipeline lo detecta.

---

## Objetivo

Aplicar un flujo básico de DevOps pasando por las siguientes etapas:

**Código → Pruebas → Git → GitHub → Integración Continua → Docker → Feedback → Corrección**

Al finalizar el taller, el proyecto deberá tener:

- Las operaciones de suma, resta, multiplicación y división.
- Pruebas automatizadas.
- Un pipeline de GitHub Actions.
- Una imagen Docker.
- La aplicación ejecutándose dentro de un contenedor.
- Una validación básica del estado de la aplicación mediante un healthcheck.
- Un ejemplo de fallo detectado automáticamente por el pipeline.

---

## 1. Estructura inicial

```text
DevOps_WorkShop/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── Dockerfile
├── README.md
├── calculator.py
├── main.py
├── requirements.txt
└── test_calculator.py
```

---

## 2. Requisitos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.12 o superior.
- Git.
- Docker Desktop.
- Visual Studio Code.
- Una cuenta de GitHub.

Puedes comprobar las instalaciones ejecutando:

```bash
python --version
git --version
docker --version
```

---

## 3. Obtener el proyecto

Clona el repositorio proporcionado:

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresa a la carpeta:

```bash
cd DevOps_WorkShop
```

Abre el proyecto en Visual Studio Code:

```bash
code .
```

---

## 4. Revisar la aplicación inicial

La aplicación inicial contiene:

- Resta.
- Multiplicación.
- Healthcheck.

La lógica matemática está en `calculator.py`.

La interfaz de consola está en `main.py`.

Las pruebas iniciales están en `test_calculator.py`.

---

## 5. Instalar las dependencias

Se recomienda crear un entorno virtual:

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## 6. Ejecutar la aplicación

Ejecuta:

```bash
python main.py
```

La aplicación mostrará:

```text
=================================
       CALCULADORA DEVOPS
=================================
1. Restar
2. Multiplicar
3. Healthcheck
4. Salir
=================================
Seleccione una opción:
```

Prueba las operaciones disponibles.

---

## 7. Healthcheck

Selecciona:

```text
3. Healthcheck
```

Deberás obtener:

```text
=================================
           HEALTHCHECK
=================================
Estado: OK
Aplicación: Calculadora DevOps
```

Este healthcheck es una comprobación sencilla implementada dentro de la aplicación. Su objetivo es introducir el concepto de que una aplicación puede proporcionar información sobre su estado.

---

# PARTE 1 — Agregar funcionalidades

## 8. Agregar la función de suma

La función debe recibir dos números y devolver su suma.

Ejemplo:

```python
suma(10, 5)
```

Resultado:

```text
15
```

---

## 9. Agregar la función de división

En `calculator.py`,

La función debe:

- Dividir correctamente dos números.
- Evitar la división entre cero.
- Generar un `ValueError` cuando el divisor sea `0`.

---

## 10. Actualizar la interfaz

Ahora modifica `main.py`.

Agrega las nuevas funciones a la importación:

Agrega las opciones:

```text
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Healthcheck
6. Salir
```

La interfaz debe permitir utilizar las cuatro operaciones.

---

# PARTE 2 — Pruebas automatizadas

## 11. Crear la prueba de suma

## 12. Crear las pruebas de división

## 13. Ejecutar las pruebas localmente

Ejecuta:

```bash
pytest
```

Todas las pruebas deberán pasar.

El número de pruebas esperado después de completar el ejercicio será:

```text
5 passed
```

### Evidencia 1

Incluye en el informe:

- Código de `suma()`.
- Código de `division()`.
- Pruebas creadas.
- Prueba de división entre cero.
- Captura de `pytest` mostrando las pruebas exitosas.

---

# PARTE 3 — Git y GitHub

## 14. Guardar los cambios

Comprueba el estado:

```bash
git status
```

Agrega los cambios:

```bash
git add .
```

Crea un commit:

```bash
git commit -m "Agregar suma y division con pruebas"
```

Envía los cambios:

```bash
git push
```

---

# PARTE 4 — Integración Continua

## 15. Revisar GitHub Actions

El proyecto ya contiene:

```text
.github/workflows/ci.yml
```

Este workflow ejecuta automáticamente las pruebas cuando se realiza un `push` o un `pull request` hacia la rama `main`.

El flujo es:

```text
GitHub
   ↓
GitHub Actions
   ↓
Configurar Python
   ↓
Instalar dependencias
   ↓
Ejecutar pytest
   ↓
Resultado
```

En GitHub, entra a:

**Actions → CI**

Comprueba que el pipeline finalice correctamente.

### Evidencia 2

Incluye una captura del pipeline exitoso mostrando las pruebas aprobadas.

---

# PARTE 5 — Docker

## 16. Revisar el Dockerfile

El proyecto contiene un `Dockerfile` que permite construir una imagen de la aplicación:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY calculator.py main.py ./

CMD ["python", "main.py"]
```

---

## 17. Construir la imagen

Ejecuta:

```bash
docker build -t DevOps_WorkShop .
```

Comprueba que la imagen exista:

```bash
docker images
```

### Evidencia 3

Incluye una captura donde se observe la construcción exitosa de la imagen Docker.

---

## 18. Ejecutar la aplicación con Docker

Ejecuta:

```bash
docker run -it DevOps_WorkShop
```

La aplicación deberá mostrar su menú.

Prueba las operaciones y el healthcheck.

### Evidencia 4

Incluye una captura donde se observe la aplicación ejecutándose dentro del contenedor.

---

# PARTE 6 — Integrar Docker al pipeline

## 19. Modificar el workflow

Ahora modifica:

```text
.github/workflows/ci.yml
```

Después del paso de pruebas, agrega un paso para construir la imagen:

```yaml
      - name: Construir imagen Docker
        run: docker build -t DevOps_WorkShop .
```

El pipeline tendrá ahora:

```text
Código
   ↓
Instalar dependencias
   ↓
Ejecutar pruebas
   ↓
Construir imagen Docker
   ↓
Resultado
```

Guarda y sube los cambios:

```bash
git add .
git commit -m "Integrar Docker al pipeline"
git push
```

Revisa nuevamente:

**GitHub → Actions**

### Evidencia 5

Incluye una captura donde se observe:

- Las pruebas exitosas.
- La construcción exitosa de la imagen Docker.

---

# PARTE 7 — Provocar un fallo

## 20. Introducir un error intencional

Ahora vamos a provocar un error para comprobar que el pipeline puede detectarlo.

En `calculator.py`, modifica temporalmente:

```python
def suma(a, b):
    return a - b
```

La prueba continuará esperando:

```python
def test_suma():
    assert suma(10, 5) == 15
```

Ejecuta localmente:

```bash
pytest
```

La prueba deberá fallar.

---

## 21. Subir el error

Guarda los cambios:

```bash
git add .
git commit -m "Introducir error intencional"
git push
```

Ve a:

**GitHub → Actions**

El pipeline deberá fallar porque la prueba de suma no se cumple.

### Evidencia 6

Incluye una captura donde se observe:

- El pipeline fallido.
- La prueba que falló.

---

# PARTE 8 — Corregir el error

## 22. Corregir la función

Regresa a `calculator.py` y corrige:

```python
def suma(a, b):
    return a + b
```

Ejecuta:

```bash
pytest
```

Comprueba que todas las pruebas pasen.

---

## 23. Subir la corrección

Ejecuta:

```bash
git add .
git commit -m "Corregir funcion suma"
git push
```

---

## 24. Verificar el pipeline final

Regresa a:

**GitHub → Actions**

El nuevo pipeline deberá ejecutarse correctamente.

El ciclo completo será:

```text
Cambio
  ↓
Pruebas
  ↓
Pipeline
  ↓
Error
  ↓
Feedback
  ↓
Corrección
  ↓
Pruebas
  ↓
Pipeline exitoso
```

### Evidencia 7

Incluye una captura donde se observe el pipeline exitoso después de corregir el error.

---

# Evidencias del informe

El documento Word debe contener:

### Evidencia 1 — Funcionalidades y pruebas

- `suma()`.
- `division()`.
- Pruebas automatizadas.
- Prueba de división entre cero.
- Ejecución local de `pytest`.

### Evidencia 2 — Pipeline exitoso

Pipeline de GitHub Actions ejecutando correctamente las pruebas.

### Evidencia 3 — Construcción de Docker

Construcción exitosa de la imagen.

### Evidencia 4 — Aplicación en Docker

Calculadora funcionando dentro del contenedor.

### Evidencia 5 — Pipeline con Docker

Pruebas y construcción de Docker ejecutándose correctamente.

### Evidencia 6 — Pipeline fallido

Pipeline después de introducir el error intencional.

### Evidencia 7 — Pipeline corregido

Pipeline exitoso después de solucionar el error.

---

# Reflexión final

Responde:

> **¿Qué aprendí durante el taller sobre DevOps y cómo contribuyen el control de versiones, las pruebas automatizadas, la Integración Continua, la automatización y Docker al proceso de entrega de software?**

La respuesta debe relacionar la experiencia práctica del taller con los conceptos explicados durante la exposición.

---

# Flujo final

```text
       Código
          ↓
         Git
          ↓
       GitHub
          ↓
   GitHub Actions
          ↓
        Pytest
          ↓
        Docker
          ↓
     Aplicación
          ↓
       Feedback
          ↓
      Corrección
          ↓
       CI final
```

## Concepto clave

> **DevOps no consiste en utilizar muchas herramientas. Consiste en mejorar el flujo de entrega de software mediante colaboración, automatización, pruebas, integración y retroalimentación continua.**
