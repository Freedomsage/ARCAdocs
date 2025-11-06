# ARCA AFIP - Facturación Electrónica Documentation

**Source of Truth / Fuente de Verdad / Источник истины**

- **Source Document**: `manual-desarrollador-ARCA-COMPG-v4-0.pdf`
- **Version**: v4.0 (RG 4291 – Proyecto FE v4.0)
- **Revision Date**: 17 de Marzo de 2025
- **Organization**: ARCA-SDG SIT (Agencia de Recaudación y Control Aduanero - Subdirección General de Sistemas y Telecomunicaciones)

---

## Table of Contents / Tabla de Contenidos / Содержание

### Introduction / Introducción / Введение

- [Introduction & Scope](./introduction.md) - Document scope, authentication, and general information
- [Authentication](./authentication/README.md) - WSAA authentication and authorization details
- [Error Handling](./errors/README.md) - Error codes and event handling

### Business Web Services / Servicios Web de Negocio / Бизнес веб-сервисы

#### CAE Methods / Métodos CAE / Методы CAE

- [FECAESolicitar](./cae/README.md) - Authorization of electronic invoices by CAE (Código de Autorización Electrónico)

#### CAEA Methods / Métodos CAEA / Методы CAEA

- [FECAEASolicitar](./caea/README.md) - CAEA request method
- [FECAEAConsultar](./caea/README.md#fecaeaconsultar) - CAEA consultation method
- [FECAEASinMovimientoInformar](./caea/README.md#fecaeasinmovimientoinformar) - Inform CAEA without movement
- [FECAEARegInformativo](./caea/README.md#fecaeareginformativo) - Inform issued invoices with CAEA
- [FECAEASinMovimientoConsultar](./caea/README.md#fecaeasinmovimientoconsultar) - Consult CAEA without movement

#### Parameter Methods / Métodos de Parámetros / Методы параметров

- [FEParamGetTiposCbte](./parameters/README.md#feparamgettiposcbte) - Get invoice types / Obtener tipos de comprobante
- [FEParamGetTiposConcepto](./parameters/README.md#feparamgettiposconcepto) - Get concept types / Obtener tipos de concepto
- [FEParamGetTiposDoc](./parameters/README.md#feparamgettiposdoc) - Get document types / Obtener tipos de documento
- [FEParamGetTiposIva](./parameters/README.md#feparamgettiposiva) - Get IVA rates / Obtener tipos de alícuotas IVA
- [FEParamGetTiposMonedas](./parameters/README.md#feparamgettiposmonedas) - Get currency types / Obtener tipos de monedas
- [FEParamGetTiposOpcional](./parameters/README.md#feparamgettiposopcional) - Get optional data types / Obtener tipos de datos opcionales
- [FEParamGetTiposTributos](./parameters/README.md#feparamgettipostributos) - Get tax types / Obtener tipos de tributos
- [FEParamGetPtosVenta](./parameters/README.md#feparamgetptosventa) - Get sales points / Obtener puntos de venta
- [FEParamGetCotizacion](./parameters/README.md#feparamgetcotizacion) - Get currency exchange rate / Obtener cotización de moneda
- [FEParamGetTiposPaises](./parameters/README.md#feparamgettipospaises) - Get country codes / Obtener códigos de países
- [FEParamGetActividades](./parameters/README.md#feparamgetactividades) - Get activities / Obtener actividades
- [FEParamGetCondicionIvaReceptor](./parameters/README.md#feparamgetcondicionivareceptor) - Get IVA condition codes for receiver / Obtener condición IVA del receptor

#### Invoice Methods / Métodos de Comprobantes / Методы работы с документами

- [FECompUltimoAutorizado](./comprobantes/README.md#fecompultimoautorizado) - Get last authorized invoice / Obtener último comprobante autorizado
- [FECompTotXRequest](./comprobantes/README.md#fecomptotxrequest) - Get maximum records per request / Obtener cantidad máxima de registros
- [FECompConsultar](./comprobantes/README.md#fecompconsultar) - Consult issued invoices / Consultar comprobantes emitidos

#### Utility Methods / Métodos Utilitarios / Утилитарные методы

- [FEDummy](./utils/README.md) - Dummy method for infrastructure verification / Método dummy para verificación de infraestructura

---

## OpenAPI Specifications / Especificaciones OpenAPI / Спецификации OpenAPI

- [Homologación (Testing Environment)](../openapi/homologacion.yaml) - Testing WSDL converted to OpenAPI 3.0
- [Producción (Production Environment)](../openapi/produccion.yaml) - Production WSDL converted to OpenAPI 3.0

---

## Additional Resources / Recursos Adicionales / Дополнительные ресурсы

### URLs / Direcciones URL

**Homologación (Testing):**
- Service: `https://wswhomo.afip.gov.ar/wsfev1/service.asmx`
- WSDL: `https://wswhomo.afip.gov.ar/wsfev1/service.asmx?WSDL`

**Producción (Production):**
- Service: `https://servicios1.afip.gov.ar/wsfev1/service.asmx`
- WSDL: `https://servicios1.afip.gov.ar/wsfev1/service.asmx?WSDL`

### Support Channels / Canales de Atención / Каналы поддержки

- **Homologación queries**: Consultas sobre el ambiente de homologación
- **Certificates and access**: Acerca de certificados y accesos - consultar sitio www.arca.gob.ar/ws
- **Functional aspects**: Sobre aspectos funcionales del Web Services
- **Production queries**: Consultas sobre el ambiente de producción
- **Regulatory queries**: Consultas sobre normativa

### Documentation Sites / Sitios de Consulta / Сайты документации

- ABC – Consultas y Respuestas Frecuentes
- Help and support documentation

---

## Notes / Notas / Примечания

- This documentation is generated from the official ARCA manual v4.0
- All content is extracted directly from the source PDF without modifications
- Comments and descriptions are provided in Spanish (original) and English (translation)
- XML examples are preserved exactly as in the original document
- Error codes and validations are documented comprehensively

---

## License / Licencia / Лицензия

This documentation is based on official ARCA (Agencia de Recaudación y Control Aduanero) documentation. Please refer to ARCA's official terms and conditions for usage rights.


