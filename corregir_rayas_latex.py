#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para corregir palabras cortadas con rayas en archivos LaTeX
Autor: Asistente IA
Fecha: 12 de julio de 2025
"""

import re
import os
from typing import Dict, List, Tuple

class CorregirRayasLatex:
    def __init__(self):
        # Diccionario de palabras comunes que suelen cortarse
        self.diccionario_palabras = {
            # Palabras técnicas comunes
            'configura-': 'configuración',
            'configu-': 'configuración',
            'aplica-': 'aplicación',
            'implementa-': 'implementación',
            'documen-': 'documentación',
            'comunica-': 'comunicación',
            'autenti-': 'autenticación',
            'autoriza-': 'autorización',
            'administra-': 'administración',
            'navega-': 'navegación',
            'compati-': 'compatibilidad',
            'escalabi-': 'escalabilidad',
            'mantenibi-': 'mantenibilidad',
            'accesibi-': 'accesibilidad',
            'disponibili-': 'disponibilidad',
            'seguri-': 'seguridad',
            'rendi-': 'rendimiento',
            'usabili-': 'usabilidad',
            'funciona-': 'funcionalidad',
            'platafor-': 'plataforma',
            'desenvo-': 'desarrollo',
            'desarro-': 'desarrollo',
            'arquitec-': 'arquitectura',
            'especifica-': 'especificación',
            'requeri-': 'requerimiento',
            'requisi-': 'requisito',
            'informa-': 'información',
            'organiza-': 'organización',
            'universi-': 'universidad',
            'ingenie-': 'ingeniería',
            'sistémi-': 'sistémico',
            'automáti-': 'automático',
            'electróni-': 'electrónico',
            'informáti-': 'informático',
            'tecnológi-': 'tecnológico',
            'monito-': 'monitoreo',
            'valida-': 'validación',
            'verifica-': 'verificación',
            'optimi-': 'optimización',
            'localiza-': 'localización',
            'genera-': 'generación',
            'registra-': 'registración',
            'sincroniza-': 'sincronización',
            'actua-': 'actualización',
            'modifica-': 'modificación',
            'transfor-': 'transformación',
            'integra-': 'integración',
            'colabora-': 'colaboración',
            'evalua-': 'evaluación',
            'procesa-': 'procesamiento',
            'almacena-': 'almacenamiento',
            'transfór-': 'transformación',
            
            # Palabras en contexto específico
            'contraseña-': 'contraseñas',
            'formula-': 'formularios',
            'disposi-': 'dispositivos',
            'navega-': 'navegadores',
            'usua-': 'usuarios',
            'servi-': 'servicios',
            'móvi-': 'móviles',
            'tempora-': 'temporales',
            'emplea-': 'empleadores',
            'trabaja-': 'trabajadores',
            'rura-': 'rurales',
            'labora-': 'laborales',
            'geográfi-': 'geográficos',
            'jerárqui-': 'jerárquicos',
            'automáti-': 'automáticamente',
            'significa-': 'significativa',
            'descripti-': 'descriptivo',
            'alterna-': 'alternativo',
            'compati-': 'compatible',
            'responsi-': 'responsive',
            'interacti-': 'interactivo',
            'concurren-': 'concurrentes',
            'simultánea-': 'simultáneamente',
            'horizontal-': 'horizontalmente',
            'modifica-': 'modificaciones',
            'especifica-': 'especificaciones',
            'degrada-': 'degradación',
            'retroalimenta-': 'retroalimentación',
            'valida-': 'validaciones',
            'encripta-': 'encriptadas',
            'protec-': 'protección',
            'monito-': 'monitoreo',
            'falli-': 'fallidos',
            'entra-': 'entrada',
            'salí-': 'salida',
            'reuti-': 'reutilizables',
            'acopla-': 'acoplamiento',
            'regis-': 'registrados',
            'ofertas-': 'ofertas',
            'acti-': 'activas',
            'módu-': 'módulos',
            'exis-': 'existente',
            'respal-': 'respaldo',
            'recu-': 'recuperación',
            'progra-': 'programado',
            'tráfi-': 'tráfico',
            'encripta-': 'encriptación',
            'intuiti-': 'intuitiva',
            'horizon-': 'horizontal',
            'documen-': 'documentado',
            'críti-': 'críticos',
            'esen-': 'esencial',
            'adop-': 'adopción',
            'univer-': 'universal',
            'manteni-': 'mantenimiento',
            'plazo-': 'plazo',
            'crecimien-': 'crecimiento',
            'confiabili-': 'confiabilidad',
            'servi-': 'servicio'
        }
        
        # Patrones regex para encontrar palabras cortadas
        self.patron_rayas = re.compile(r'(\w+)-\s*&')
        self.patron_final_linea = re.compile(r'(\w+)-\s*\\\\')
        
    def encontrar_palabras_cortadas(self, texto: str) -> List[Tuple[str, str]]:
        """
        Encuentra todas las palabras cortadas con rayas en el texto
        """
        palabras_encontradas = []
        
        # Buscar patrones en tablas (antes de &)
        matches_tabla = self.patron_rayas.findall(texto)
        for match in matches_tabla:
            palabra_cortada = match + '-'
            if palabra_cortada in self.diccionario_palabras:
                palabras_encontradas.append((palabra_cortada, self.diccionario_palabras[palabra_cortada]))
        
        # Buscar patrones al final de línea
        matches_linea = self.patron_final_linea.findall(texto)
        for match in matches_linea:
            palabra_cortada = match + '-'
            if palabra_cortada in self.diccionario_palabras:
                palabras_encontradas.append((palabra_cortada, self.diccionario_palabras[palabra_cortada]))
        
        return palabras_encontradas
    
    def corregir_texto(self, texto: str) -> str:
        """
        Corrige todas las palabras cortadas en el texto
        """
        texto_corregido = texto
        correcciones_aplicadas = []
        
        for palabra_cortada, palabra_completa in self.diccionario_palabras.items():
            # Patrón para palabra cortada seguida de & (en tablas)
            patron_tabla = re.compile(rf'{re.escape(palabra_cortada[:-1])}-\s*&')
            if patron_tabla.search(texto_corregido):
                texto_corregido = patron_tabla.sub(f'{palabra_completa} &', texto_corregido)
                correcciones_aplicadas.append(f"{palabra_cortada} → {palabra_completa}")
            
            # Patrón para palabra cortada al final de línea
            patron_linea = re.compile(rf'{re.escape(palabra_cortada[:-1])}-\s*\\\\')
            if patron_linea.search(texto_corregido):
                texto_corregido = patron_linea.sub(f'{palabra_completa} \\\\', texto_corregido)
                correcciones_aplicadas.append(f"{palabra_cortada} → {palabra_completa}")
        
        return texto_corregido, correcciones_aplicadas
    
    def procesar_archivo(self, ruta_archivo: str) -> bool:
        """
        Procesa un archivo LaTeX y corrige las palabras cortadas
        """
        try:
            # Leer el archivo
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido_original = archivo.read()
            
            # Crear backup
            ruta_backup = ruta_archivo + '.backup'
            with open(ruta_backup, 'w', encoding='utf-8') as backup:
                backup.write(contenido_original)
            
            print(f"✅ Backup creado: {ruta_backup}")
            
            # Corregir el texto
            contenido_corregido, correcciones = self.corregir_texto(contenido_original)
            
            if correcciones:
                # Guardar el archivo corregido
                with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                    archivo.write(contenido_corregido)
                
                print(f"\n🔧 CORRECCIONES APLICADAS ({len(correcciones)}):")
                for i, correccion in enumerate(correcciones, 1):
                    print(f"   {i}. {correccion}")
                
                print(f"\n✅ Archivo corregido guardado: {ruta_archivo}")
                return True
            else:
                print("ℹ️  No se encontraron palabras cortadas para corregir.")
                # Eliminar backup si no hubo cambios
                os.remove(ruta_backup)
                return False
                
        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo {ruta_archivo}")
            return False
        except Exception as e:
            print(f"❌ Error procesando el archivo: {str(e)}")
            return False
    
    def analizar_archivo(self, ruta_archivo: str):
        """
        Analiza un archivo sin modificarlo, solo muestra las palabras cortadas encontradas
        """
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
            
            palabras_cortadas = self.encontrar_palabras_cortadas(contenido)
            
            if palabras_cortadas:
                print(f"\n🔍 PALABRAS CORTADAS ENCONTRADAS ({len(palabras_cortadas)}):")
                for i, (cortada, completa) in enumerate(palabras_cortadas, 1):
                    print(f"   {i}. {cortada} → {completa}")
            else:
                print("ℹ️  No se encontraron palabras cortadas conocidas.")
                
        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo {ruta_archivo}")
        except Exception as e:
            print(f"❌ Error analizando el archivo: {str(e)}")

def main():
    print("🔧 CORRECTOR DE PALABRAS CORTADAS EN LATEX")
    print("=" * 50)
    
    # Ruta del archivo
    ruta_archivo = "Requisitos_No_Funcionales_Llamkay.tex"
    
    if not os.path.exists(ruta_archivo):
        print(f"❌ No se encontró el archivo: {ruta_archivo}")
        print("   Asegúrate de ejecutar el script en la carpeta correcta.")
        return
    
    corrector = CorregirRayasLatex()
    
    print(f"📄 Procesando archivo: {ruta_archivo}")
    
    # Analizar primero
    print("\n1️⃣ ANÁLISIS DEL ARCHIVO:")
    corrector.analizar_archivo(ruta_archivo)
    
    # Preguntar si aplicar correcciones
    respuesta = input("\n¿Aplicar correcciones automáticamente? (s/n): ").lower().strip()
    
    if respuesta in ['s', 'sí', 'si', 'y', 'yes']:
        print("\n2️⃣ APLICANDO CORRECCIONES:")
        exito = corrector.procesar_archivo(ruta_archivo)
        
        if exito:
            print("\n🎉 PROCESO COMPLETADO EXITOSAMENTE!")
            print("   - Se creó un backup del archivo original")
            print("   - Se aplicaron todas las correcciones")
            print("   - El archivo está listo para usar en LaTeX")
        else:
            print("\n⚠️  No se realizaron cambios en el archivo.")
    else:
        print("\n❌ Operación cancelada. No se modificó el archivo.")

if __name__ == "__main__":
    main()
