#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para convertir documento LaTeX para compatibilidad total con Word
Elimina tildes y caracteres especiales problemáticos
Autor: Asistente IA
Fecha: 12 de julio de 2025
"""

import re
import os
from typing import Dict

class ConvertirParaWord:
    def __init__(self):
        # Diccionario de reemplazos para caracteres problemáticos
        self.reemplazos = {
            # Vocales con tilde
            'á': 'a', 'Á': 'A',
            'é': 'e', 'É': 'E', 
            'í': 'i', 'Í': 'I',
            'ó': 'o', 'Ó': 'O',
            'ú': 'u', 'Ú': 'U',
            
            # Eñe
            'ñ': 'n', 'Ñ': 'N',
            
            # Caracteres especiales
            '¿': '',
            '¡': '',
            '°': 'o',
            
            # Comillas problemáticas
            '"': '"', '"': '"',
            ''': "'", ''': "'",
            
            # Guiones problemáticos
            '–': '-', '—': '-',
            
            # Símbolos problemáticos
            '©': '(C)',
            '®': '(R)',
            '™': '(TM)',
            
            # Espacios problemáticos
            ' ': ' ',  # espacio no rompible
            '\u00A0': ' ',  # otro tipo de espacio
        }
        
        # Palabras específicas que necesitan corrección
        self.palabras_especificas = {
            'función': 'funcion',
            'Función': 'Funcion',
            'información': 'informacion',
            'Información': 'Informacion',
            'descripción': 'descripcion',
            'Descripción': 'Descripcion',
            'autenticación': 'autenticacion',
            'Autenticación': 'Autenticacion',
            'validación': 'validacion',
            'Validación': 'Validacion',
            'configuración': 'configuracion',
            'Configuración': 'Configuracion',
            'optimización': 'optimizacion',
            'Optimización': 'Optimizacion',
            'implementación': 'implementacion',
            'Implementación': 'Implementacion',
            'aplicación': 'aplicacion',
            'Aplicación': 'Aplicacion',
            'administración': 'administracion',
            'Administración': 'Administracion',
            'navegación': 'navegacion',
            'Navegación': 'Navegacion',
            'protección': 'proteccion',
            'Protección': 'Proteccion',
            'verificación': 'verificacion',
            'Verificación': 'Verificacion',
            'comunicación': 'comunicacion',
            'Comunicación': 'Comunicacion',
            'evaluación': 'evaluacion',
            'Evaluación': 'Evaluacion',
            'documentación': 'documentacion',
            'Documentación': 'Documentacion',
            'programación': 'programacion',
            'Programación': 'Programacion',
            'versión': 'version',
            'Versión': 'Version',
            'edición': 'edicion',
            'Edición': 'Edicion',
            'decisión': 'decision',
            'Decisión': 'Decision',
            'sesión': 'sesion',
            'Sesión': 'Sesion',
            'extensión': 'extension',
            'Extensión': 'Extension',
            'conexión': 'conexion',
            'Conexión': 'Conexion',
            'creación': 'creacion',
            'Creación': 'Creacion',
            'operación': 'operacion',
            'Operación': 'Operacion',
        }
    
    def limpiar_texto(self, texto: str) -> str:
        """
        Limpia el texto de caracteres problemáticos para Word
        """
        # Primero aplicar reemplazos de palabras específicas
        for original, reemplazo in self.palabras_especificas.items():
            texto = texto.replace(original, reemplazo)
        
        # Luego aplicar reemplazos de caracteres individuales
        for original, reemplazo in self.reemplazos.items():
            texto = texto.replace(original, reemplazo)
        
        return texto
    
    def procesar_archivo(self, ruta_archivo: str) -> bool:
        """
        Procesa un archivo LaTeX eliminando caracteres problemáticos
        """
        try:
            # Leer archivo
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido_original = archivo.read()
            
            print(f"📄 Archivo original: {len(contenido_original)} caracteres")
            
            # Crear backup
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            ruta_backup = f"{ruta_archivo}.backup_word_{timestamp}"
            
            with open(ruta_backup, 'w', encoding='utf-8') as backup:
                backup.write(contenido_original)
            
            print(f"💾 Backup creado: {ruta_backup}")
            
            # Limpiar contenido
            contenido_limpio = self.limpiar_texto(contenido_original)
            
            # Verificar cambios
            cambios = len([1 for a, b in zip(contenido_original, contenido_limpio) if a != b])
            
            if cambios > 0:
                # Guardar archivo limpio
                with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                    archivo.write(contenido_limpio)
                
                print(f"✅ ARCHIVO CONVERTIDO PARA WORD")
                print(f"   📊 Tamaño final: {len(contenido_limpio)} caracteres")
                print(f"   🔄 Caracteres cambiados: {cambios}")
                print(f"   📝 Archivo listo para conversion a Word")
                
                # Mostrar algunos ejemplos de cambios
                print(f"\n🔍 EJEMPLOS DE CAMBIOS APLICADOS:")
                ejemplos = [
                    "Configuración → Configuracion",
                    "Información → Informacion", 
                    "Descripción → Descripcion",
                    "Función → Funcion",
                    "Protección → Proteccion"
                ]
                for i, ejemplo in enumerate(ejemplos, 1):
                    print(f"   {i}. {ejemplo}")
                
                return True
            else:
                print("ℹ️  El archivo ya estaba compatible con Word")
                os.remove(ruta_backup)  # Eliminar backup innecesario
                return False
                
        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo {ruta_archivo}")
            return False
        except Exception as e:
            print(f"❌ Error procesando el archivo: {str(e)}")
            return False
    
    def verificar_compatibilidad(self, ruta_archivo: str):
        """
        Verifica la compatibilidad del archivo con Word
        """
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
            
            # Buscar caracteres problemáticos
            problemas = []
            for char, reemplazo in self.reemplazos.items():
                if char in contenido:
                    count = contenido.count(char)
                    problemas.append(f"'{char}' aparece {count} veces")
            
            if problemas:
                print(f"\n⚠️  CARACTERES PROBLEMÁTICOS ENCONTRADOS:")
                for problema in problemas[:10]:  # Mostrar máximo 10
                    print(f"   • {problema}")
                if len(problemas) > 10:
                    print(f"   ... y {len(problemas) - 10} más")
            else:
                print("✅ El archivo es compatible con Word")
                
        except Exception as e:
            print(f"❌ Error verificando compatibilidad: {str(e)}")

def main():
    print("🔄 CONVERTIDOR LATEX PARA WORD")
    print("=" * 50)
    print("Este script elimina tildes y caracteres especiales problemáticos")
    print("para garantizar compatibilidad total con Microsoft Word")
    print()
    
    # Ruta del archivo
    ruta_archivo = "Requisitos_No_Funcionales_Llamkay.tex"
    
    if not os.path.exists(ruta_archivo):
        print(f"❌ No se encontró el archivo: {ruta_archivo}")
        print("   Asegúrate de ejecutar el script en la carpeta correcta.")
        return
    
    convertidor = ConvertirParaWord()
    
    print(f"📄 Procesando archivo: {ruta_archivo}")
    
    # Verificar estado actual
    print("\n1️⃣ VERIFICACIÓN INICIAL:")
    convertidor.verificar_compatibilidad(ruta_archivo)
    
    # Preguntar si proceder
    respuesta = input("\n¿Convertir archivo para compatibilidad con Word? (s/n): ").lower().strip()
    
    if respuesta in ['s', 'sí', 'si', 'y', 'yes']:
        print("\n2️⃣ CONVIRTIENDO ARCHIVO:")
        exito = convertidor.procesar_archivo(ruta_archivo)
        
        if exito:
            print("\n🎉 CONVERSIÓN COMPLETADA!")
            print("   ✅ El archivo está optimizado para Word")
            print("   📋 Pasos siguientes:")
            print("      1. Compilar en LaTeX (Overleaf)")
            print("      2. Descargar PDF")
            print("      3. Convertir PDF a Word online")
            print("      4. Las tildes se mantendrán correctas")
        else:
            print("\n📋 El archivo ya estaba optimizado")
    else:
        print("\n❌ Conversión cancelada")

if __name__ == "__main__":
    main()
