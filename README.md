# 🗄️ Sistema de Control de Ventas con Base de Datos SQLite (`control_ventas.py`)

## 🎯 Descripción del Proyecto
Este script de automatización representa un salto técnico fundamental: la transición de archivos planos (CSV) a bases de datos relacionales. El programa crea y gestiona una base de datos local en SQLite, inserta registros comerciales mediante sentencias SQL nativas (`INSERT`), realiza consultas estructuradas (`SELECT`) y calcula métricas e ingresos financieros automáticos para un negocio de e-commerce.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.14
* **Base de Datos:** SQLite3 (motor relacional integrado nativamente en Python).
* **Módulos Nativos:** `os` (gestión de rutas).

## 🚀 Características
* **Inicialización Automática:** Crea la estructura de la base de datos y la tabla relacional `ventas` si no existen previamente.
* **Inserción Segura de Datos:** Almacena transacciones comerciales con control de unicidad para evitar duplicados.
* **Reporte Financiero Dinámico:** Consulta la base de datos en tiempo real, tabula las ventas con formato profesional y calcula el total de unidades y los ingresos consolidados en COP.

## 💻 Instrucciones de Uso
1. Ejecuta el script en tu terminal:
   ```bash
   python control_ventas.py