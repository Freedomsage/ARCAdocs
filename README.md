# ARCA AFIP - Facturación Electrónica Documentation

[![Documentation](https://img.shields.io/badge/docs-latest-blue)](./docs/README.md)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-3.0-green)](./openapi/)

Complete documentation for ARCA AFIP Electronic Invoicing Web Services (RG 4291 - Proyecto FE v4.0)

---

## English

### Source of Truth

- **Source Document**: `manual-desarrollador-ARCA-COMPG-v4-0.pdf`
- **Version**: v4.0 (RG 4291 – Proyecto FE v4.0)
- **Revision Date**: March 17, 2025
- **Organization**: ARCA-SDG SIT (Agencia de Recaudación y Control Aduanero - Subdirección General de Sistemas y Telecomunicaciones)

### Overview

This repository contains complete documentation for the ARCA AFIP Electronic Invoicing Web Services. The documentation is extracted directly from the official PDF manual without modifications, ensuring accuracy and completeness.

### Quick Start

1. **Browse Documentation**: See [docs/README.md](./docs/README.md) for the complete documentation index
2. **OpenAPI Specifications**: 
   - [Homologación (Testing)](./openapi/homologacion.yaml)
   - [Producción (Production)](./openapi/produccion.yaml)
3. **Method Documentation**: Organized by category:
   - [CAE Methods](./docs/cae/) - Authorization of electronic invoices by CAE
   - [CAEA Methods](./docs/caea/) - CAEA request, consultation, and reporting methods
   - [Parameter Methods](./docs/parameters/) - Reference value retrieval methods
   - [Invoice Methods](./docs/comprobantes/) - Invoice consultation and verification methods
   - [Utility Methods](./docs/utils/) - Infrastructure verification methods

### Documentation Structure

- `docs/` - Complete documentation organized by method categories
- `openapi/` - OpenAPI 3.0 specifications for both environments
- `manual-arca-source.md` - Source Markdown converted from PDF via Docling

### Support

- **Homologación queries**: wsfev1@arca.gov.ar
- **Certificates and access**: http://www.arca.gob.ar/ws/
- **Production queries**: sri@arca.gov.ar
- **Regulatory queries**: facturaelectronica@arca.gov.ar

### License

This documentation is based on official ARCA documentation. Please refer to ARCA's official terms and conditions for usage rights.

---

## Español

### Fuente de Verdad

- **Documento Fuente**: `manual-desarrollador-ARCA-COMPG-v4-0.pdf`
- **Versión**: v4.0 (RG 4291 – Proyecto FE v4.0)
- **Fecha de Revisión**: 17 de Marzo de 2025
- **Organización**: ARCA-SDG SIT (Agencia de Recaudación y Control Aduanero - Subdirección General de Sistemas y Telecomunicaciones)

### Resumen

Este repositorio contiene la documentación completa de los Servicios Web de Facturación Electrónica de ARCA AFIP. La documentación se extrajo directamente del manual PDF oficial sin modificaciones, garantizando precisión y completitud.

### Inicio Rápido

1. **Navegar Documentación**: Ver [docs/README.md](./docs/README.md) para el índice completo de documentación
2. **Especificaciones OpenAPI**: 
   - [Homologación (Testing)](./openapi/homologacion.yaml)
   - [Producción (Production)](./openapi/produccion.yaml)
3. **Documentación de Métodos**: Organizada por categoría:
   - [Métodos CAE](./docs/cae/) - Autorización de comprobantes electrónicos por CAE
   - [Métodos CAEA](./docs/caea/) - Métodos de solicitud, consulta e informe de CAEA
   - [Métodos de Parámetros](./docs/parameters/) - Métodos de recuperación de valores referenciales
   - [Métodos de Comprobantes](./docs/comprobantes/) - Métodos de consulta y verificación de comprobantes
   - [Métodos Utilitarios](./docs/utils/) - Métodos de verificación de infraestructura

### Estructura de Documentación

- `docs/` - Documentación completa organizada por categorías de métodos
- `openapi/` - Especificaciones OpenAPI 3.0 para ambos entornos
- `manual-arca-source.md` - Markdown fuente convertido del PDF mediante Docling

### Soporte

- **Consultas sobre homologación**: wsfev1@arca.gov.ar
- **Certificados y accesos**: http://www.arca.gob.ar/ws/
- **Consultas sobre producción**: sri@arca.gov.ar
- **Consultas sobre normativa**: facturaelectronica@arca.gov.ar

### Licencia

Esta documentación se basa en la documentación oficial de ARCA. Consulte los términos y condiciones oficiales de ARCA para los derechos de uso.

---

## Русский

### Источник истины

- **Исходный документ**: `manual-desarrollador-ARCA-COMPG-v4-0.pdf`
- **Версия**: v4.0 (RG 4291 – Proyecto FE v4.0)
- **Дата ревизии**: 17 марта 2025
- **Организация**: ARCA-SDG SIT (Agencia de Recaudación y Control Aduanero - Subdirección General de Sistemas y Telecomunicaciones)

### Обзор

Этот репозиторий содержит полную документацию для веб-сервисов электронного выставления счетов ARCA AFIP. Документация извлечена непосредственно из официального PDF-руководства без изменений, что гарантирует точность и полноту.

### Быстрый старт

1. **Просмотр документации**: См. [docs/README.md](./docs/README.md) для полного индекса документации
2. **Спецификации OpenAPI**: 
   - [Homologación (Тестирование)](./openapi/homologacion.yaml)
   - [Producción (Продакшн)](./openapi/produccion.yaml)
3. **Документация методов**: Организована по категориям:
   - [Методы CAE](./docs/cae/) - Авторизация электронных счетов через CAE
   - [Методы CAEA](./docs/caea/) - Методы запроса, консультации и отчетности CAEA
   - [Методы параметров](./docs/parameters/) - Методы получения справочных значений
   - [Методы работы с документами](./docs/comprobantes/) - Методы консультации и проверки документов
   - [Утилитарные методы](./docs/utils/) - Методы проверки инфраструктуры

### Структура документации

- `docs/` - Полная документация, организованная по категориям методов
- `openapi/` - Спецификации OpenAPI 3.0 для обеих сред
- `manual-arca-source.md` - Исходный Markdown, конвертированный из PDF через Docling

### Поддержка

- **Запросы по тестированию**: wsfev1@arca.gov.ar
- **Сертификаты и доступ**: http://www.arca.gob.ar/ws/
- **Запросы по продакшну**: sri@arca.gov.ar
- **Нормативные запросы**: facturaelectronica@arca.gov.ar

### Лицензия

Эта документация основана на официальной документации ARCA. Пожалуйста, обратитесь к официальным условиям и положениям ARCA для прав использования.

---

## Contributing

This documentation is automatically generated from the official ARCA PDF. To update:

1. Replace the source PDF with the new version
2. Re-run the conversion scripts
3. Update version information in all files

## Technical Details

- **PDF Conversion**: Using [Docling](https://github.com/docling-project/docling)
- **OpenAPI**: Version 3.0.3
- **Documentation Format**: Markdown with multi-language support

