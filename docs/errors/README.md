---
# Source of Truth / Fuente de Verdad / Источник истины
# Source Document: manual-desarrollador-ARCA-COMPG-v4-0.pdf
# Version: v4.0 (RG 4291 – Proyecto FE v4.0)
# Revision Date: 17 de Marzo de 2025
# Organization: ARCA-SDG SIT (Agencia de Recaudación y Control Aduanero)
---

## Tratamiento de errores en el WS

El tratamiento de errores en todos los servicios se realizará de la siguiente manera:

```
<Errors> <Err> <Code> int </Code> <Msg> string </Msg> </Err> <Err> <Code> int </Code> <Msg> string </Msg> </Err> </Errors>
```

<!-- image -->

Dónde:

| Campo  Detalle  Obligatorio  Errors  Array de objeto. Err Información correspondiente a errores  N  Code  Código de error  S  Msg  Mensaje descriptivo del   error  S   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Para errores internos de infraestructura, los errores se devuelven en la misma estructura (Errors). Los códigos de error son:

| Código de error  Causa  500  Error interno de aplicación.  501  Error interno de base de datos.  502  Error interno de base de datos -  Autorizador CAE / Régimen CAEA -  Transacción Activa  600  No se corresponden  token y firma. Usuario no autorizado  a realizar esta  operación  601  CUIT  representada no incluida en  token.  602  No existen datos en nuestros registros.   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Tratamiento de eventos

El tratamiento de eventos en todos los servicios se realizará de la siguiente manera:

```
<Events> <Evt> <Code> int </Code> <Msg> string </Msg> </Evt> <Evt> <Code> int </Code> <Msg> string </Msg> </Evt> </Events>
```

Dónde:

<!-- image -->

<!-- image -->

| Campo  Detalle  Obligatorio  Events  Array de objeto. Evt Información correspondiente al  mensaje  N  Code  Código de evento  S  Msg  Detalla el evento que se desea comunicar  S   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

---

*This section is extracted directly from the source PDF without modifications.*