# 🖥️ Monitor del Sistema - Arquitectura de Computadoras

Este proyecto es un **monitor de sistema desarrollado en Django**, diseñado para mostrar en tiempo real estadísticas del equipo, como uso de CPU, memoria RAM, disco, red y temperatura del procesador.  
Fue creado como parte del **examen práctico de la clase Arquitectura de Computadoras para el segundo parcial**.

---

## 🚀 Características principales


- Visualización **en tiempo real** del estado del sistema
- Intervalo de actualización configurable manualmente (por defecto 5 segundos)
- Interfaz web moderna y minimalista desarrollada con **HTML + CSS + Tailwind**
- Recolección de datos del sistema mediante la librería **psutil**
- Información presentada en tarjetas con valores dinámicos

---

## 🧩 Estructura del proyecto
monitor-sistema/
│
├── monitor/ #Configuración principal de Django (settings, urls)
├── sistema/ #Aplicación que contiene la lógica del monitor
│ ├── templates/ #Carpeta con la interfaz web (index.html)
│ ├── views.py #Controlador principal: obtiene los datos del sistema
│ ├── urls.py #Enrutamiento hacia las vistas
│ └── models.py
│
├── manage.py #Comando principal de Django
├── requirements.txt #Dependencias del proyecto
└── README.md #Este archivo

---

## ⚙️ Instalación y ejecución local

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/JosueDJ20212015/sistema-monitor-ECC-Examen-Arqu.Comp.git
cd sistema-monitor-ECC-Examen-Arqu.Comp

### 2️⃣ Crear y activar el entorno virtual
```bash
python -m venv venv
venv\Scripts\activate

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt

### ▶️ Ejecutar el servidor
```bash
python manage.py runserver

Luego abre tu navegador y visita:
```bash
http://127.0.0.1:8000/
