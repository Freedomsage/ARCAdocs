---
# Source of Truth / Fuente de Verdad / Источник истины
# Source Document: manual-desarrollador-ARCA-COMPG-v4-0.pdf
# Version: v4.0 (RG 4291 – Proyecto FE v4.0)
# Revision Date: 17 de Marzo de 2025
# Organization: ARCA-SDG SIT (Agencia de Recaudación y Control Aduanero)
---

## Recuperador de ultimo valor de comprobante registrado (FECompUltimoAutorizado)

Retorna el ultimo comprobante autorizado para el tipo de comprobante / cuit / punto de venta ingresado / Tipo de Emisión

## Dirección URL (Homologación)

Este servicio se llama desde:

```
https://wswhomo.afip.gov.ar/wsfev1/service.asmx? op=FECompUltimoAutorizado
```

## Mensaje de solicitud

Recibe las credenciales de autenticación y la cuit del usuario representado.

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/ envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECompUltimoAutorizado> <ar:Auth> <ar:Token>string</ar:Token> <ar:Sign>string</ar:Sign> <ar:Cuit>long</ar:Cuit> </ar:Auth> <ar:PtoVta>int</ar:PtoVta> <ar:CbteTipo>int</ar:CbteTipo> </ar:FECompUltimoAutorizado> </soapenv:Body> </soapenv:Envelope>
```

<!-- image -->

donde:

## FECompUltimoAutorizado:

| Campo  Detalle  Obligatorio  Auth  Información de la autenticación. Contiene los datos de  Token, Sign y Cuit  S  Token  Token devuelto  por  el  WSAA  S  Sign  Sign devuelto  por  el  WSAA  S  Cuit  Cuit contribuyente (representado o Emisora)  S   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Campo  Detalle  Obligatorio  PtoVta  Punto  de venta  S  CbteTipo  Tipo de comprobante  S   |
|---------------------------------------------------------------------------------------------|

## Mensaje de respuesta

Retorna el  último número de comprobante registrado para el punto de venta y tipo de comprobante enviado.

```
<?xml version='1.0' encoding='utf-8'?> <soap:Envelope xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:xsd='http://www.w3.org/2001/XMLSchema' xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/'> <soap:Body> <FECompUltimoAutorizadoResponse xmlns='http://ar.gov.afip.dif.FEV1/'> <FECompUltimoAutorizadoResult> <PtoVta> int </PtoVta> <CbteTipo> int </CbteTipo> <CbteNro> int </CbteNro> <Errors> <Err> <Code> int </Code> <Msg> string </Msg> </Err> <Err> <Code> int </Code> <Msg> string </Msg> </Err> </Errors> <Events> <Evt>
```

<!-- image -->

```
<Code> int </Code> <Msg> string </Msg> </Evt> <Evt> <Code> int </Code> <Msg> string </Msg> </Evt> </Events> </FECompUltimoAutorizadoResult> </FECompUltimoAutorizadoResponse> </soap:Body> </soap:Envelope>
```

## donde:

## FECompUltimoAutorizadoResult :

| Campo  Detalle  Obligatorio  FECompUltimoAut  orizadoResul  Información completa del  CAEA sin movimientos. Contiene  PtoVta, CbteTipo, CbteNro, Errors y Events  S  Errors  Información de errores detectados  N  Events  Información de eventos  N   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Campo  Tipo  Detalle  Obligatorio  PtoVta  Int (5)  Punto  de venta  S  CbteTipo  Int (3)  Tipo de comprobante  S  CbteNro  Long (8)  Número de comprobante  N   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Validaciones, acciones y errores

Controles aplicados:

| Campo /  Grupo  Código de  Error  Validación  &lt;PtoVta&gt;  11000  El PtoVta debe ser válido comprendido entre 1 y 99998  &lt;CbteTipo&gt;  11001  Debe de ser algunos de los habilitados en este WS. Consultar método  FEParamGetTiposCbte  &lt;PtoVta&gt;  11002  Debe ser un punto de venta habilitado en este WS. Consultar método  FEParamGetPtosVenta   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

<!-- image -->

## Recuperador de cantidad máxima de registros FECAESolicitar / FECAEARegInformativo (FECompTotXRequest)

Retorna la cantidad máxima de registros que se podrá incluir en un request al  método FECAESolicitar / FECAEARegInformativo.

## Dirección URL (Homologación)

Este servicio se llama desde:

https://wswhomo.afip.gov.ar/wsfev1/service.asmx?op= FECompTotXRequest

## Mensaje de solicitud

Recibe las credenciales de autenticación y la cuit del usuario representado.

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/ envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECompTotXRequest> <ar:Auth> <ar:Token>string</ar:Token> <ar:Sign>string</ar:Sign> <ar:Cuit>long</ar:Cuit> </ar:Auth> </ar:FECompTotXRequest> </soapenv:Body> </soapenv:Envelope>
```

## donde:

| Campo  Detalle  Obligatorio  Auth  Información de la autenticación. Contiene los datos de  Token, Sign y Cuit  S  Token  Token devuelto  por  el  WSAA  S  Sign  Sign devuelto  por  el  WSAA  S  Cuit  Cuit contribuyente (representado o Emisora)  S   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Mensaje de respuesta

<!-- image -->

```
<?xml version='1.0' encoding='utf-8'?> <soap:Envelope xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:xsd='http://www.w3.org/2001/XMLSchema' xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/'> <soap:Body> <FECompTotXRequestResponse xmlns='http://ar.gov.afip.dif.FEV1/'> <FECompTotXRequestResult> <RegXReq> int </RegXReq> <Errors> <Err> <Code> int </Code> <Msg> string </Msg> </Err> <Err> <Code> int </Code> <Msg> string </Msg> </Err> </Errors> <Events> <Evt> <Code> int </Code> <Msg> string </Msg> </Evt> <Evt> <Code> int </Code> <Msg> string </Msg> </Evt> </Events> </FECompTotXRequestResult> </FECompTotXRequestResponse> </soap:Body> </soap:Envelope>
```

## Dónde:

## FECompTotXRequestResult:

| Campo  Detalle  Obligatorio  FECompTotXRequ  estResult  Contiene los datos RegXReq, Errors y Events.  S  Errors  Información de errores detectados  N  Events  Información de eventos  N   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Campo  Tipo  Detalle  Obligatorio  RegXReq  Int (4)  Cantidad máxima de registros que se pueden  incluir en un Request de solicitud de CAE e  Informar CAEA.  S   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

## Método  para consultar Comprobantes Emitidos y su código (FECompConsultar)

Esta operación permite consultar mediante tipo, numero de comprobante y punto de venta los datos de un comprobante ya emitido. Dentro de los datos del comprobante resultante se obtiene el tipo de emisión utilizado para generar el código de autorización.

## Dirección URL (Homologación)

Este servicio se llama desde:

https://wswhomo.afip.gov.ar/wsfev1/service.asmx ?op= FECompConsultar

<!-- image -->

## Mensaje de solicitud

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/ envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECompConsultar> <ar:Auth> <ar:Token>string</ar:Token> <ar:Sign>string</ar:Sign> <ar:Cuit>long</ar:Cuit> </ar:Auth> <ar:FeCompConsReq> <ar:CbteTipo>int</ar:CbteTipo> <ar:CbteNro>long</ar:CbteNro> <ar:PtoVta>int</ar:PtoVta> </ar:FeCompConsReq> </ar:FECompConsultar> </soapenv:Body> </soapenv:Envelope>
```

## donde:

| Campo  Detalle  Obligatorio  Auth  Información de la autenticación. Contiene los datos de  Token, Sign y Cuit  S  Token  Token devuelto  por  el  WSAA  S  Sign  Sign devuelto  por  el  WSAA  S  Cuit  Cuit contribuyente (representado o Emisora)  S   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Campo  Detalle  Obligatorio  FeCompConsReq  Información del comprobante que se desea consultar.  S   |
|------------------------------------------------------------------------------------------------------|

| Campo  Detalle  Obligatorio  CbteTipo  Tipo de Comprobante  S  CbteNro  Número de comprobante  S  PtoVta  Punto de venta  S   |
|-------------------------------------------------------------------------------------------------------------------------------|

## Mensaje de respuesta

Retorna los datos del Comprobante coincidente con los parámetros ingresados.

<!-- image -->

<!-- image -->

```
<soap12:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soap12:Header/> <soap12:Body> <FECompConsultarResponse> <FECompConsultarResult> <ResultGet> <Concepto> int </Concepto> <DocTipo> int </DocTipo> <DocNro> long </DocNro> <CbteDesde> long </CbteDesde> <CbteHasta> long </CbteHasta> <CbteFch> string </CbteFch> <ImpTotal> double </ImpTotal> <ImpTotConc> double </ImpTotConc> <ImpNeto> double </ImpNeto> <ImpOpEx> double </ImpOpEx> <ImpTrib> double </ImpTrib> <ImpIVA> double </ImpIVA> <FchServDesde> string </FchServDesde> <FchServHasta> string </FchServHasta> <FchVtoPago> string </FchVtoPago> <MonId> string </MonId> <MonCotiz> double </MonCotiz> <CbtesAsoc> <CbteAsoc> <Tipo> int </Tipo> <PtoVta> int </PtoVta> <Nro> long </Nro> </CbteAsoc> </CbtesAsoc> <Tributos> <Tributo> <Id> int </Id> <Desc> string </Desc> <BaseImp> double </BaseImp> <Alic> double </Alic> <Importe> double </Importe> </Tributo> </Tributos> <Iva> <AlicIva> <Id> int </Id> <BaseImp> double </BaseImp> <Importe> double </Importe> </AlicIva> </Iva> <Opcionales> <Opcional> <Id> string </Id> <Valor> string </Valor> </Opcional> </Opcionales> <Compradores> <Comprador> <DocTipo> int </DocTipo> <DocNro> long </DocNro>
```

<!-- image -->

```
<Porcentaje> double </Porcentaje> </Comprador> </Compradores> <ar:PeriodoAsoc> <ar:FchDesde> string </ar:FchDesde> <ar:FchHasta> string </ar:FchHasta> </ar:PeriodoAsoc> <Resultado> string </Resultado> <CodAutorizacion> string </CodAutorizacion> <EmisionTipo> string </EmisionTipo> <FchVto> string </FchVto> <FchProceso> string </FchProceso> <Observaciones> <Obs> <Code> int </Code> <Msg> string </Msg> </Obs> </Observaciones> <PtoVta> int </PtoVta> <CbteTipo> int </CbteTipo> </ResultGet> <Errors> <Err> <Code> int </Code> <Msg> string </Msg> </Err> </Errors> <Events> <Evt> <Code> int </Code> <Msg> string </Msg> </Evt> </Events> </FECompConsultarResult> </FECompConsultarResponse> </soapenv:Body> </soapenv:Envelope>
```

## dónde:

| Campo  Detalle  Obligatorio  FECompConsultarResult  Nodo contenedor correspondiente a él comprobante  solicitado. Contiene los datos ResultGet, Errors y  Events  S  Errors  Información de errores detectados  N  Events  Información de eventos  N   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

ResultGet: El objeto resultante informante del resultado del proceso contiene los campos identificados como valores de entrada FECAEDetRequest (request) en el método FECAESolicitar + los siguientes atributos.

<!-- image -->

| Campo  Detalle  Obligatorio  Resultado  Resultado del procesamiento del comprobante  S  CodAutorizacion  Código de Autorización  S  EmisionTipo  Tipo de emisión, si corresponde a CAE o CAEA  S  FchVto  Vencimiento del código de autorización.  Si tipo de emisión es  igual a CAE esta es la fecha de vencimiento obtenida cuando  se autorizó el comprobante.  Si tipo de emisión es igual a  CAEA esta es la fecha de 'vigencia hasta' del CAEA obtenida  cuando gestionó el CAEA.  S  FchProceso  Fecha de procesamiento del comprobante  S  Observaciones  Observaciones identificadas al momento de generar el  comprobante.  N  PtoVta  Punto de venta  S  CbteTipo  Tipo de Comprobante  S   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Validaciones y errores

## Controles aplicados

| Campo / Grupo  Código de error  Validación  PtoVta  10200  No ingreso el Punto de Venta o el formato es  inválido.  CbteTipo  10201  No ingreso el Tipo de Comprobante, o el tipo  de comprobante es inválido.  PtoVta  10104  El punto de venta ingresado no se encuentra  registrado.  CbteNro  10202  No ingreso el número de comprobante o el  formato es inválido.   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Ejemplo

## REQUEST

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECompConsultar> <ar:Auth> <ar:Token>string</ar:Token> <ar:Sign>string</ar:Sign> <ar:Cuit>33693450239</ar:Cuit> </ar:Auth> <ar:FeCompConsReq> <ar:CbteTipo>1</ar:CbteTipo> <ar:CbteNro>1</ar:CbteNro> <ar:PtoVta>12</ar:PtoVta> </ar:FeCompConsReq> </ar:FECompConsultar> </soapenv:Body> </soapenv:Envelope>
```

## RESPONSE

```
<soap12:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soap12:Header/> <soap12:Body> <FECompConsultarResponse> <FECompConsultarResult> <ResultGet> <Concepto> 1 </Concepto> <DocTipo> 80 </DocTipo> <DocNro> 20111111112 </DocNro> <CbteDesde> 1 </CbteDesde> <CbteHasta> 1 </CbteHasta> <CbteFch> 20100903 </CbteFch> <ImpTotal> 184.05 </ImpTotal> <ImpTotConc> 0 </ImpTotConc> <ImpNeto> 150 </ImpNeto> <ImpOpEx> 0 </ImpOpEx> <ImpTrib> 7.8 </ImpTrib> <ImpIVA>26.25</ImpIVA> <FchServDesde></FchServDesde> <FchServHasta></FchServHasta> <FchVtoPago></FchVtoPago> <MonId> PES </MonId> <MonCotiz> 1 </MonCotiz> <Tributos> <Tributo> <Id> 99 </Id> <Desc> Impuesto Municipal Matanza </Desc> <BaseImp> 150 </BaseImp> <Alic> 5.2 </Alic> <Importe> 7.8 </Importe>
```

<!-- image -->

<!-- image -->

```
</Tributo> </Tributos> <Iva> <AlicIva> <Id> 5 </Id> <BaseImp> 100 </BaseImp> <Importe> 21 </Importe> </AlicIva> <AlicIva> <Id> 4 </Id> <BaseImp> 50 </BaseImp> <Importe>5.25</Importe> </AlicIva> </Iva> <Resultado>A</Resultado> <CodAutorizacion> 41124578989845 </CodAutorizacion> <EmisionTipo>CAE</EmisionTipo> <FchVto>20100913</FchVto> <FchProceso>20100902</FchProceso> <PtoVta>12</PtoVta> <CbteTipo>1</CbteTipo> </ResultGet> </FECompConsultarResult> </FECompConsultarResponse> </soapenv:Body> </soapenv:Envelope>
```

---

*This section is extracted directly from the source PDF without modifications.*