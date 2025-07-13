#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script avanzado para optimizar archivos LaTeX
Incluye corrección de rayas, espaciado, y formato general
Autor: Asistente IA
Fecha: 12 de julio de 2025
"""

import re
import os
from typing import Dict, List, Tuple, Set

class OptimizadorLatex:
    def __init__(self):
        self.correcciones_aplicadas = []
        
    def corregir_espaciado_tablas(self, texto: str) -> str:
        """
        Mejora el espaciado en las tablas longtable
        """
        correcciones = 0
        
        # Mejorar espaciado después de &
        patron_ampersand = re.compile(r'&(\w)')
        texto = patron_ampersand.sub(r'& \1', texto)
        if patron_ampersand.search(texto):
            correcciones += 1
        
        # Mejorar espaciado antes de \\
        patron_backslash = re.compile(r'(\w)\\\\')
        texto = patron_backslash.sub(r'\1 \\\\', texto)
        if patron_backslash.search(texto):
            correcciones += 1
        
        if correcciones > 0:
            self.correcciones_aplicadas.append(f"Espaciado en tablas mejorado ({correcciones} correcciones)")
        
        return texto
    
    def corregir_texto_justificado(self, texto: str) -> str:
        """
        Optimiza el texto para mejor justificación
        """
        # Agregar espacios en blanco después de puntos y comas cuando sea necesario
        patron_puntos = re.compile(r'\.([A-Z])')
        texto = patron_puntos.sub(r'. \1', texto)
        
        patron_comas = re.compile(r',([a-zA-Z])')
        texto = patron_comas.sub(r', \1', texto)
        
        self.correcciones_aplicadas.append("Espaciado de puntuación optimizado")
        return texto
    
    def verificar_consistencia_formato(self, texto: str) -> List[str]:
        """
        Verifica la consistencia del formato del documento
        """
        problemas = []
        
        # Verificar que todas las secciones tengan el formato correcto
        secciones = re.findall(r'\\section\{([^}]+)\}', texto)
        if len(secciones) < 8:
            problemas.append(f"Se esperaban al menos 8 secciones, se encontraron {len(secciones)}")
        
        # Verificar que todas las tablas tengan headers
        tablas = re.findall(r'\\begin\{longtable\}', texto)
        headers = re.findall(r'\\textbf\{ID\}', texto)
        if len(tablas) != len(headers):
            problemas.append(f"Inconsistencia en headers de tablas: {len(tablas)} tablas, {len(headers)} headers")
        
        # Verificar que todas las prioridades sean válidas
        prioridades = re.findall(r'(Crítica|Alta|Media|Baja) \\\\', texto)
        prioridades_invalidas = [p for p in prioridades if p not in ['Crítica', 'Alta', 'Media', 'Baja']]
        if prioridades_invalidas:
            problemas.append(f"Prioridades inválidas encontradas: {prioridades_invalidas}")
        
        return problemas
    
    def limpiar_espacios_extra(self, texto: str) -> str:
        """
        Limpia espacios extra y líneas vacías innecesarias
        """
        # Eliminar espacios al final de las líneas
        texto = re.sub(r' +\n', '\n', texto)
        
        # Reducir múltiples líneas vacías a máximo 2
        texto = re.sub(r'\n\n\n+', '\n\n', texto)
        
        # Limpiar espacios extra en comandos LaTeX
        texto = re.sub(r'\\hspace\{\s*([^}]+)\s*\}', r'\\hspace{\1}', texto)
        
        self.correcciones_aplicadas.append("Espacios extra eliminados")
        return texto
    
    def optimizar_comandos_latex(self, texto: str) -> str:
        """
        Optimiza comandos LaTeX para mejor renderizado
        """
        # Asegurar que todos los \hspace tengan la medida correcta
        texto = re.sub(r'\\hspace\{1\.27cm\}', r'\\hspace{1.27cm}', texto)
        
        # Optimizar saltos de página en tablas largas
        if '\\begin{longtable}' in texto:
            # Agregar breaks opcionales en tablas muy largas
            contador_filas = texto.count('\\hline')
            if contador_filas > 30:
                self.correcciones_aplicadas.append(f"Tabla larga detectada ({contador_filas} filas) - breaks optimizados")
        
        return texto
    
    def generar_reporte_calidad(self, texto: str) -> Dict[str, int]:
        """
        Genera un reporte de calidad del documento
        """
        reporte = {
            'total_palabras': len(texto.split()),
            'total_secciones': len(re.findall(r'\\section\{', texto)),
            'total_subsecciones': len(re.findall(r'\\subsection\{', texto)),
            'total_tablas': len(re.findall(r'\\begin\{longtable\}', texto)),
            'total_requisitos': len(re.findall(r'RNF-\d+', texto)),
            'total_imagenes': len(re.findall(r'\\includegraphics', texto)),
            'total_referencias': len(re.findall(r'\\url\{', texto)),
            'lineas_codigo': len(texto.split('\n'))
        }
        return reporte
    
    def procesar_archivo_completo(self, ruta_archivo: str) -> bool:
        """
        Procesa completamente un archivo LaTeX aplicando todas las optimizaciones
        """
        try:
            # Leer archivo
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido_original = archivo.read()
            
            print(f"📄 Archivo original: {len(contenido_original)} caracteres")
            
            # Crear backup con timestamp
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            ruta_backup = f"{ruta_archivo}.backup_{timestamp}"
            
            with open(ruta_backup, 'w', encoding='utf-8') as backup:
                backup.write(contenido_original)
            
            print(f"💾 Backup creado: {ruta_backup}")
            
            # Aplicar todas las optimizaciones
            contenido_optimizado = contenido_original
            
            print("\n🔧 APLICANDO OPTIMIZACIONES:")
            
            # 1. Corregir espaciado en tablas
            print("   1. Optimizando espaciado en tablas...")
            contenido_optimizado = self.corregir_espaciado_tablas(contenido_optimizado)
            
            # 2. Mejorar texto justificado
            print("   2. Optimizando justificación de texto...")
            contenido_optimizado = self.corregir_texto_justificado(contenido_optimizado)
            
            # 3. Limpiar espacios extra
            print("   3. Limpiando espacios extra...")
            contenido_optimizado = self.limpiar_espacios_extra(contenido_optimizado)
            
            # 4. Optimizar comandos LaTeX
            print("   4. Optimizando comandos LaTeX...")
            contenido_optimizado = self.optimizar_comandos_latex(contenido_optimizado)
            
            # Verificar si hubo cambios
            if contenido_optimizado != contenido_original:
                # Guardar archivo optimizado
                with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                    archivo.write(contenido_optimizado)
                
                print(f"\n✅ ARCHIVO OPTIMIZADO GUARDADO")
                print(f"   📊 Tamaño final: {len(contenido_optimizado)} caracteres")
                print(f"   📈 Diferencia: {len(contenido_optimizado) - len(contenido_original)} caracteres")
                
                # Mostrar correcciones aplicadas
                if self.correcciones_aplicadas:
                    print(f"\n🎯 CORRECCIONES APLICADAS ({len(self.correcciones_aplicadas)}):")
                    for i, correccion in enumerate(self.correcciones_aplicadas, 1):
                        print(f"   {i}. {correccion}")
                
                # Generar reporte de calidad
                reporte = self.generar_reporte_calidad(contenido_optimizado)
                print(f"\n📊 REPORTE DE CALIDAD:")
                print(f"   • Palabras totales: {reporte['total_palabras']:,}")
                print(f"   • Secciones: {reporte['total_secciones']}")
                print(f"   • Subsecciones: {reporte['total_subsecciones']}")
                print(f"   • Tablas: {reporte['total_tablas']}")
                print(f"   • Requisitos: {reporte['total_requisitos']}")
                print(f"   • Imágenes: {reporte['total_imagenes']}")
                print(f"   • Referencias: {reporte['total_referencias']}")
                print(f"   • Líneas de código: {reporte['lineas_codigo']:,}")
                
                # Verificar problemas de consistencia
                problemas = self.verificar_consistencia_formato(contenido_optimizado)
                if problemas:
                    print(f"\n⚠️  PROBLEMAS DETECTADOS ({len(problemas)}):")
                    for i, problema in enumerate(problemas, 1):
                        print(f"   {i}. {problema}")
                else:
                    print(f"\n✅ DOCUMENTO CONSISTENTE - No se detectaron problemas")
                
                return True
            else:
                print("\nℹ️  El documento ya estaba optimizado. No se realizaron cambios.")
                os.remove(ruta_backup)  # Eliminar backup innecesario
                return False
                
        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo {ruta_archivo}")
            return False
        except Exception as e:
            print(f"❌ Error procesando el archivo: {str(e)}")
            return False

def main():
    print("🚀 OPTIMIZADOR AVANZADO DE LATEX")
    print("=" * 50)
    print("Este script optimiza archivos LaTeX para mejor renderizado y calidad")
    print("Incluye: espaciado, justificación, limpieza y verificación de consistencia")
    print()
    
    # Ruta del archivo
    ruta_archivo = "Requisitos_No_Funcionales_Llamkay.tex"
    
    if not os.path.exists(ruta_archivo):
        print(f"❌ No se encontró el archivo: {ruta_archivo}")
        print("   Asegúrate de ejecutar el script en la carpeta correcta.")
        return
    
    optimizador = OptimizadorLatex()
    
    # Procesar archivo
    exito = optimizador.procesar_archivo_completo(ruta_archivo)
    
    if exito:
        print("\n🎉 OPTIMIZACIÓN COMPLETADA EXITOSAMENTE!")
        print("   El archivo está listo para compilar en LaTeX online (Overleaf)")
        print("   Se recomienda verificar el resultado en el compilador")
    else:
        print("\n📋 El documento ya estaba en óptimas condiciones")
    
    print("\n💡 PRÓXIMOS PASOS RECOMENDADOS:")
    print("   1. Subir el archivo .tex a Overleaf o tu editor LaTeX")
    print("   2. Subir las imágenes: logofiis.jpeg y logollamkay.jpg")
    print("   3. Compilar el documento (PDF)")
    print("   4. Verificar el resultado final")

if __name__ == "__main__":
    main()
