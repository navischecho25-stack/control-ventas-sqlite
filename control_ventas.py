import sqlite3
import os

DB_NOMBRE = "ventas.db"

def inicializar_base_datos():
    """Crea la base de datos y la tabla de ventas si no existen."""
    conexion = sqlite3.connect(DB_NOMBRE)
    cursor = conexion.cursor()
    
    # Crear la tabla 'ventas'
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio_unitario REAL NOT NULL,
            total REAL NOT NULL,
            fecha TEXT NOT NULL
        )
    """)
    
    conexion.commit()
    conexion.close()

def registrar_venta_prueba():
    """Inserta algunos registros de ventas iniciales para pruebas."""
    conexion = sqlite3.connect(DB_NOMBRE)
    cursor = conexion.cursor()
    
    # Verificar si ya hay datos para no duplicar en cada prueba
    cursor.execute("SELECT COUNT(*) FROM ventas")
    if cursor.fetchone()[0] == 0:
        print("🛠️ Insertando registros de ventas iniciales en la Base de Datos...")
        ventas_iniciales = [
            ("Audifonos Inalambricos X1", 2, 45000, "2026-10-28"),
            ("Smartwatch Pro", 1, 150000, "2026-10-28"),
            ("Cable Carga Magnetica", 5, 12000, "2026-10-29"),
            ("Audifonos Sport Basic", 3, 30000, "2026-10-29"),
            ("Smartwatch Lite", 2, 120000, "2026-10-29")
        ]
        
        for prod, cant, precio, fecha in ventas_iniciales:
            total = cant * precio
            cursor.execute("""
                INSERT INTO ventas (producto, cantidad, precio_unitario, total, fecha)
                VALUES (?, ?, ?, ?, ?)
            """, (prod, cant, precio, total, fecha))
            
        conexion.commit()
        print("✅ Datos insertados correctamente en SQLite.")
    
    conexion.close()

def generar_reporte_financiero():
    """Consulta la base de datos con SQL y calcula estadísticas de ventas."""
    conexion = sqlite3.connect(DB_NOMBRE)
    cursor = conexion.cursor()
    
    print("\n🔍 Consultando la Base de Datos SQLite...")
    
    # Obtener todas las ventas registradas
    cursor.execute("SELECT id, producto, cantidad, total, fecha FROM ventas")
    registros = cursor.fetchall()
    
    print("\n" + "="*55)
    print(f"{'ID':<4} | {'PRODUCTO':<26} | {'CANT':<5} | {'TOTAL (COP)':<10}")
    print("="*55)
    
    ingreso_total = 0
    total_unidades = 0
    
    for fila in registros:
        id_v, prod, cant, tot, fecha = fila
        ingreso_total += tot
        total_unidades += cant
        print(f"{id_v:<4} | {prod:<26} | {cant:<5} | ${tot:,.0f}")
        
    print("="*55)
    print(f"📦 Total de unidades vendidas: {total_unidades}")
    print(f"💰 Ingresos Totales Generados: ${ingreso_total:,.0f} COP")
    print("="*55)
    print(f"📂 Base de datos gestionada de forma segura en: '{DB_NOMBRE}'")
    
    conexion.close()

if __name__ == "__main__":
    inicializar_base_datos()
    registrar_venta_prueba()
    generar_reporte_financiero()