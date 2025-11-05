---
# Source of Truth / Fuente de Verdad / Источник истины
# Source Document: manual-desarrollador-ARCA-COMPG-v4-0.pdf
# Version: v4.0 (RG 4291 – Proyecto FE v4.0)
# Revision Date: 17 de Marzo de 2025
# Organization: ARCA-SDG SIT (Agencia de Recaudación y Control Aduanero)
---

## Método Dummy para verificación de funcionamiento de infraestructura (FEDummy)

## Dirección URL (Homologación)

Este servicio se llama desde:

https://wswhomo.afip.gov.ar/wsfev1/service.asmx?op= FEDummy

## Mensaje de solicitud

El método no posee parámetros de ingreso

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/ envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FEDummy/> </soapenv:Body> </soapenv:Envelope>
```

## Mensaje de respuesta

Retorna  la comprobación vía 'ping' de los elementos principales de infraestructura del servicio.

```
<?xml version='1.0' encoding='utf-8'?> stance' xmlns:xsd='http://www.w3.org/2001/XMLSchema' xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/'> <soap:Body>
```

```
<soap:Envelope xmlns:xsi='http://www.w3.org/2001/XMLSchema-in<FEDummyResponse xmlns='http://ar.gov.afip.dif.FEV1/'>
```

```
<FEDummyResult> <AppServer> string </AppServer> <DbServer> string </DbServer> <AuthServer> string </AuthServer> </FEDummyResult> </FEDummyResponse> </soap:Body> </soap:Envelope>
```

## donde:

| Campo  Tipo  Detalle  Obligatorio  AppServer  String (2)  Servidor de aplicaciones  S  DbServer  String (2)  Servidor de base de datos  S  AuthServer  String (2)  Servidor de autenticación  S   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

---

*This section is extracted directly from the source PDF without modifications.*