---
# Source of Truth / Fuente de Verdad / Источник истины
# Source Document: manual-desarrollador-ARCA-COMPG-v4-0.pdf
# Version: v4.0 (RG 4291 – Proyecto FE v4.0)
# Revision Date: 17 de Marzo de 2025
# Organization: ARCA-SDG SIT (Agencia de Recaudación y Control Aduanero)
---

## Método  de obtención de CAEA (FECAEASolicitar)

Esta operación permite solicitar un CAEA. El cliente envía el requerimiento, el cual es atendido por el WS, superadas las validaciones se otorgará un CAEA y su respectivo periodo de vigencia (fecha de validez desde y fecha de validez hasta).

<!-- image -->

Podrá ser solicitado dentro de cada quincena y hasta  5 (cinco) días corridos anteriores al comienzo de cada quincena. Habrá dos quincenas, la primera abarca desde el primero hasta el quince de cada mes y la segunda desde el dieciséis hasta el último día del mes.

## Dirección URL (Homologación)

Este servicio se llama desde:

https://wswhomo.afip.gov.ar/wsfev1/service.asmx ?op= FECAEASolicitar

## Mensaje de solicitud

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/ envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECAEASolicitar> <ar:Auth> <ar:Token>string</ar:Token> <ar:Sign>string</ar:Sign> <ar:Cuit>long</ar:Cuit> </ar:Auth> <ar:Periodo>int</ar:Periodo> <ar:Orden>short</ar:Orden> </ar:FECAEASolicitar> </soapenv:Body> </soapenv:Envelope>
```

| Campo  Detalle  Obligatorio  Auth  Información de la autenticación. Contiene los datos de  Token, Sign y Cuit  S  Token  Token devuelto  por  el  WSAA  S  Sign  Sign devuelto  por  el  WSAA  S  Cuit  Cuit contribuyente (representado o Emisora)  S   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Campo  Detalle  Obligatorio  FeCAEAReq  Información del periodo y orden del CAEA que se está  solicitando  S   |
|----------------------------------------------------------------------------------------------------------------|

## FeCAEAReq:

| Campo  Tipo  Detalle  Obligatorio  Periodo  Int (6)  Periodo del CAEA.  (yyyymm)  S  Orden  Short (1)  Orden del CAEA dentro del periodo.  S   |
|------------------------------------------------------------------------------------------------------------------------------------------------|

## Mensaje de respuesta

Retorna los detalles de un CAEA autorizado.

```
<?xml version='1.0' encoding='utf-8'?> <soap12:Envelope xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:xsd='http://www.w3.org/2001/XMLSchema' xmlns:soap12='http://www.w3.org/2003/05/soap-envelope'> <soap12:Body> <FECAEASolicitarResponse xmlns='http://ar.gov.afip.dif.FEV1/'> <FECAEASolicitarResult> <ResultGet> <CAEA> string </CAEA> <Periodo> int </Periodo> <Orden> short </Orden> <FchVigDesde> string </FchVigDesde> <FchVigHasta> string </FchVigHasta> <FchTopeInf> string </FchTopeInf> <FchProceso> string </FchProceso> <Observaciones> <Obs> <Code> int </Code> <Msg> string </ Msg> </Obs> </Observaciones> </ResultGet> <Errors> <Err> <Code> int </Code> <Msg> string </Msg> </Err> <Err> <Code> int </Code> <Msg> string </Msg> </Err> </Errors> <Events> <Evt> <Code> int </Code> <Msg> string </Msg> </Evt> <Evt> <Code> int </Code> <Msg> string </Msg> </Evt> </Events> </FECAEASolicitarResult> </FECAEASolicitarResponse> </soapenv:Body> </soap:Envelope>
```

## Donde:

Quincena 1, Quincena 2

<!-- image -->

## FECAEASolicitarResult :

<!-- image -->

| Campo  Detalle  Obligatorio  ResultGet  Información completa del  CAEA autorizado  S  Errors  Información de errores detectados  N  Events  Información de eventos  N   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## ResultGet: está compuesto por los siguientes campos:

| Campo  Tipo  Detalle  Obligatorio  CAEA  String (14)  Código de Autorización electrónico anticipado  N  Periodo  Int (6)  Periodo (yyyymm)  S  Orden  Short (1)  Orden. Quincena 1, quincena 2  S  FchVigDesde  String (8)  Fecha de vigencia de CAEA desde  N  FchVigHasta  String (8)  Fecha de vigencia de CAEA hasta  N  FchTopeInf  String (c8)  Fecha de tope para informar los  comprobantes vinculados al  CAEA  N  FchProceso  String (14)  Fecha de proceso, formato yyyymmddhhmiss  N  Observaciones  Array  Detalle de observaciones, del comprobante  N   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Observaciones : La estructura de datos Obs muestra el  detalle de observaciones para el CAEA generado; estará compuesta por los siguientes campos:

| Campo  Tipo  Detalle  Obligatorio  Code  Int (5)  Código  de observación  S  Msg  String (255)  Mensaje  S   |
|--------------------------------------------------------------------------------------------------------------|

## Validaciones y errores

## Controles aplicados al elemento &lt;FeCAEAReq&gt;

## Validaciones Excluyentes

| Campo /  Grupo  Código de  error  Descripción de la validación  &lt;Cuit&gt;  15000  Campo  CUIT: Debe encontrarse activa en el Sistema Registral y  activo en el Régimen para solicitar CAEA   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo /  Grupo  Código de  error  Descripción de la validación  &lt;Cuit&gt;  15001  Campo  CUIT: Deberá estar registrado como Autoimpresor  &lt;Cuit&gt;  15003  Campo  CUIT: Deberá poseer al menos un punto de venta activo  correspondiente al régimen CAEA  &lt;Periodo&gt;  15004  Campo  Periodo: Debe tener el formato AAAAMM, donde AAAA  indica el año y MM el mes en números.  &lt;Orden&gt;  15005  Campo  Orden: Debe ser igual a 1 ó 2.  Fecha de envío  15006  Al momento de solicitar CAEA, la fecha de envío podrá ser desde  5 (cinco) días corridos anteriores al inicio de cada quincena  hasta  el último día de la misma quincena.  &lt;Periodo&gt; /  &lt;Orden&gt;  15008  No debe existir un CAEA otorgado para la CUIT solicitante con  igual periodo y orden.  &lt;Cuit&gt;  15009  Campo  CUIT: Registra problemas de domicilio  &lt;Cuit&gt;  15010  Campo  CUIT: Deberá estar inscripto  en alguno de los sig.  impuestos:  20 - MONOTRIBUTO  30 - IVA  32 - IVA EXENTO  &lt;Cuit&gt;  15011  Campo  CUIT: Deberá tener al menos una actividad económica  declarada  &lt;Cuit&gt;  15012  Campo  CUIT: Deberá estar empadronado en  el  régimen de  emisión de comprobantes electrónicos   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Validaciones No Excluyentes

| Campo / Grupo  Código de  Observ.  Descripción de la validación  &lt;Cuit&gt;/  &lt;Periodo&gt; / &lt;Orden&gt;  15014  Que No adeude la presentación del Régimen por 2 periodos  mensuales consecutivos ó 3 periodos mensuales alternados  en los últimos 12 meses calendario.  &lt;Cuit&gt;  15015  Campo  CUIT: Registra problemas en el domicilio fiscal  electrónico. No se encuentra adherido.   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Ejemplo sin Observaciones:

## Request

<!-- image -->

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECAEASolicitar> <!--Optional:--> <ar:Auth> <!--Optional:--> <ar:Token>un string</ar:Token> <ar:Sign>un string</ar:Sign> <ar:Cuit>33333333333</ar:Cuit> </ar:Auth> <ar:Periodo>201011</ar:Periodo> <ar:Orden>1</ar:Orden> </ar:FECAEASolicitar> </soapenv:Body> </soapenv:Envelope>
```

## Response

```
<?xml version='1.0' encoding='utf-8'?> <soap12:Envelopexmlns:xsi='http://www.w3.org/2001/ XMLSchema-instance' xmlns:xsd='http://www.w3.org/2001/ XMLSchema' xmlns:soap12='http://www.w3.org/2003/05/soapenvelope'> <soap12:Body> <FECAEASolicitarResponse xmlns='http://ar.gov.afip.dif.FEV1/'> <FECAEASolicitarResult> <ResultGet> <CAEA> 12345678901234 </CAEA> <Periodo> 201011 </Periodo> <Orden> 1 </Orden> <FchVigDesde> 20101101 </FchVigDesde> <FchVigHasta> 20101115 </FchVigHasta> <FchTopeInf> 20101215 </FchTopeInf> <FchProceso> 20101028 </FchProceso> </ResultGet> </FECAEASolicitarResult> </FECAEASolicitarResponse> </soapenv:Body> </soap:Envelope>
```

## Ejemplo  con observaciones:

## Request

<!-- image -->

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECAEASolicitar> <!--Optional:--> <ar:Auth> <!--Optional:--> <ar:Token>un string</ar:Token> <ar:Sign>un string</ar:Sign> <ar:Cuit>33333333333</ar:Cuit> </ar:Auth> <ar:Periodo>201011</ar:Periodo> <ar:Orden>1</ar:Orden> </ar:FECAEASolicitar> </soapenv:Body> </soapenv:Envelope>
```

## Response

```
<?xml version='1.0' encoding='utf-8'?> <soap12:Envelopexmlns:xsi='http://www.w3.org/2001/ XMLSchema-instance' xmlns:xsd='http://www.w3.org/2001/ XMLSchema' xmlns:soap12='http://www.w3.org/2003/05/soapenvelope'> <soap12:Body> <FECAEASolicitarResponse xmlns='http://ar.gov.afip.dif.FEV1/'> <FECAEASolicitarResult> <ResultGet> <CAEA> 12345678901234 </CAEA> <Periodo> 201011 </Periodo> <Orden> 1 </Orden> <FchVigDesde> 20101101 </FchVigDesde> <FchVigHasta> 20101115 </FchVigHasta> <FchTopeInf> 20101215 </FchTopeInf> <FchProceso> 20101028 </FchProceso> <Observaciones> <Obs> <Code>15015</Code> <Msg> Registra problemas en el domicilio fiscal electrónico. No se encuentra adherido </Msg> </Obs> </Observaciones> </ResultGet> </FECAEASolicitarResult> </FECAEASolicitarResponse> </soapenv:Body> </soap:Envelope>
```

## Método  de consulta de CAEA (FECAEAConsultar)

Este método permite consultar la información correspondiente a un CAEA previamente otorgado para un periodo/orden.

## Dirección URL (Homologación)

Este servicio se llama desde:

https://wswhomo.afip.gov.ar/wsfev1/service.asmx ?op= FECAEAConsultar

## Mensaje de solicitud

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/ envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECAEAConsultar> <ar:Auth> <ar:Token>string</ar:Token> <ar:Sign>string</ar:Sign> <ar:Cuit>long</ar:Cuit> </ar:Auth> <ar:Periodo>int</ar:Periodo> <ar:Orden>short</ar:Orden> </ar:FECAEAConsultar> </soapenv:Body> </soapenv:Envelope>
```

## Donde:

| Campo  Detalle  Obligatorio  Auth  Información de la autenticación. Contiene los datos de Token,  Sign y Cuit  S  Token  Token devuelto  por  el  WSAA  S  Sign  Sign devuelto  por  el  WSAA  S  Cuit  Cuit contribuyente (representado o Emisora)  S   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Campo  Tipo  Detalle  Obligatorio  Periodo  int (6)  Periodo del CAEA.  (yyyymm)  S   |
|---------------------------------------------------------------------------------------|

<!-- image -->

<!-- image -->

| Orden  short (1)  Orden del CAEA dentro del periodo. Quincena 1, Quincena 2  S   |
|----------------------------------------------------------------------------------|

## Mensaje de respuesta

Retorna los detalles de los CAEA autorizados para el periodo y orden consultado.

```
<?xml version='1.0' encoding='utf-8'?> <soap12:Envelope xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:xsd='http://www.w3.org/2001/XMLSchema' xmlns:soap12='http://www.w3.org/2003/05/soap-envelope'> <soap12:Body> <FECAEAConsultarResponse xmlns='http://ar.gov.afip.dif.FEV1/'> <FECAEAConsultarResult> <ResultGet> <CAEA> string </CAEA> <Periodo> int </Periodo> <Orden> short </Orden> <FchVigDesde> string </FchVigDesde> <FchVigHasta> string </FchVigHasta> <FchTopeInf> string </FchTopeInf> <FchProceso> string </FchProceso> <Observaciones> <Obs> <Code> int </Code> <Msg> string </ Msg> </Obs> </Observaciones> </ResultGet> <Errors> <Err> <Code> int </Code> <Msg> string </Msg> </Err> <Err> <Code> int </Code> <Msg> string </Msg> </Err> </Errors> <Events> <Evt> <Code> int </Code> <Msg> string </Msg> </Evt> <Evt> <Code> int </Code> <Msg> string </Msg> </Evt> </Events> </FECAEAConsultarResult> </FECAEAConsultarResponse> </soapenv:Body>
```

## &lt;/soapenv:Envelope&gt;

Donde:

## FECAEAConsultarResult:

| Campo  Detalle  Obligatorio  ResultGet  Información completa de los CAEA Autorizados.  S  Errors  Información de errores detectados  N  Events  Información de eventos  N   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## ResultGet: Detalle de un CAEA válido;  esta compuesto por los siguientes campos:

| Campo  Tipo  Detalle  Obligatorio  CAEA  String (14)  Código de Autorización electrónico anticipado  N  Periodo  Int (6)  Periodo (yyyymm)  S  Orden  Short (1)  Orden. Quincena 1, quincena 2  S  FchVigDesde  String (8)  Fecha de vigencia de CAEA desde  N  FchVigHasta  String (8)  Fecha de vigencia de CAEA hasta  N  FchTopeInf  String (8)  Fecha de tope para informar los  comprobantes vinculados al  CAEA  N  FchProceso  String (8)  Fecha de proceso  N   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Validaciones, acciones y errores

Controles aplicados al objeto &lt; FECAEAConsultar&gt;

Validaciones Excluyentes

| Campo /  Grupo  Código de  error  Descripción de la validación  &lt;Periodo&gt;  15004  El valor indicado en el campo &lt;Periodo&gt; es obligatorio.. Debe  tener formato AAAAMM, donde AAAA indica el año y MM el mes  en números.  &lt;Orden&gt;  15005  El valor indicado en el campo &lt;Orden&gt; es obligatorio. Valores  permitidos 1 o 2.   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

## Ejemplo:

<!-- image -->

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECAEAConsultar> <ar:Auth> <ar:Token>un string</ar:Token> <ar:Sign>un string</ar:Sign> <ar:Cuit>33000000007</ar:Cuit> </ar:Auth> <ar:Periodo>201011</ar:Periodo> <ar:Orden>1</ar:Orden> </ar:FECAEAConsultar> </soapenv:Body> </soapenv:Envelope>
```

```
<?xml version='1.0' encoding='utf-8'?> <soap12:Envelope xmlns:xsi='http://www.w3.org/2001/ XMLSchema-instance' xmlns:xsd='http://www.w3.org/2001/ XMLSchema' xmlns:soap12='http://www.w3.org/2003/05/soapenvelope'> <soap12:Body> <FECAEAConsultarResponse xmlns='http://ar.gov.afip.dif.FEV1/'> <FECAEAConsultarResult> <ResultGet> <CAEA> 12345678901234 </CAEA> <Periodo> 201011 </Periodo> <Orden> 1 </Orden> <FchVigDesde> 20101101 </FchVigDesde> <FchVigHasta> 20101115 </FchVigHasta> <FchTopeInf> 20101215 </FchTopeInf> <FchProceso> 20101028 </FchProceso> </ResultGet> </FECAEAConsultarResult> </FECAEAConsultarResponse> </soapenv:Body> </soap:Envelope>
```

## Método  para informar CAEA sin movimiento (FECAEASinMovimientoInformar)

Esta operación permite informar a la administración cuales fueron los CAEA's otorgados que no sufrieron movimiento alguno para un determinado punto de venta. El cliente envía el requerimiento, el cual es atendido por el WS, superadas las validaciones de seguridad se registrara la fecha por la cual se informo la falta de movimientos.

## Dirección URL (Homologación)

Este servicio se llama desde:

https://wswhomo.afip.gov.ar/wsfev1/service.asmx ?op= FECAEASinMovimientoInformar

## Mensaje de solicitud

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/ envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECAEASinMovimientoInformar> <ar:Auth> <ar:Token>string</ar:Token> <ar:Sign>string</ar:Sign> <ar:Cuit>long</ar:Cuit> </ar:Auth> <ar:PtoVta>int</ar:PtoVta> <ar:CAEA>string</ar:CAEA> </ar:FECAEASinMovimientoInformar> </soapenv:Body> </soapenv:Envelope>
```

<!-- image -->

## donde:

| Campo  Detalle  Obligatorio  Auth  Información de la autenticación. Contiene los datos de  Token, Sign y Cuit  S  Token  Token devuelto  por  el  WSAA  S  Sign  Sign devuelto  por  el  WSAA  S  Cuit  Cuit contribuyente (representado o Emisora)  S   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Campo  Detalle  Obligatorio  PtoVta  Punto de Venta para el que no se utilizó el CAEA informado  S  CAEA  CAEA que se está informando como no utilizado para el  punto de venta indicado  S   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Mensaje de respuesta

Retorna el resultado del proceso de informar un CAEA como no utilizado.

```
<?xml version='1.0' encoding='utf-8'?> <soap12:Envelope xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:xsd='http://www.w3.org/2001/XMLSchema' xmlns:soap12='http://www.w3.org/2003/05/soap-envelope'> <soap12:Body> <FECAEASinMovimientoResponse xmlns='http://ar.gov.afip.dif.FEV1/'> <FECAEASinMovimientoResult> <CAEA> string </CAEA> <FchProceso> string </FchProceso> <Resultado> string </Resultado> <PtoVta> int </PtoVta> <Errors> <Err> <Code> int </Code> <Msg> string </Msg> </Err> <Err> <Code> int </Code> <Msg> string </Msg> </Err> </Errors> <Events> <Evt> <Code> int </Code> <Msg> string </Msg> </Evt> <Evt> <Code> int </Code>
```

<!-- image -->

```
<Msg> string </Msg> </Evt> </Events> </FECAEASinMovimientoResult> </FECAEASinMovimientoResponse> </soapenv:Body> </soapenv:Envelope>
```

## donde:

| Campo  Detalle  Obligatorio  FECAEASinMovimi  entoResult  Información completa del  CAEA sin movimientos. Contiene  los datos CAEA, FchProceso, Resultado, PtoVta, Errors y  Events.  S  Errors  Información de errores detectados  N  Events  Información de eventos  N   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

FECAEASinMovimientoResult: El objeto resultante informante del resultado del proceso contiene los siguientes campos:

| Campo  Tipo  Detalle  Obligatorio  CAEA  String (14)  Código de Autorización electrónico  anticipado  S  FchProceso  String (8)  Fecha de Procesamiento del CAEA  informado como sin movimientos  N  Resultado  String (1)  Aprobado o Rechazado  N  PtoVta  Int (5)  Punto de venta vinculado al CAEA  informado.  S   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Validaciones y errores

Controles aplicados:

| Campo /  Grupo  Código de  Error  Validación  &lt;CAEA&gt;  1200  El código de CAEA que se está informando debe ser del tipo de código   |
|------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

<!-- image -->

| de autorización CAEA  &lt;CUIT&gt;  1201  Corresponda a la CUIT del Emisor indicada en &lt;Auth&gt;&lt;Cuit&gt;  &lt;CAEA&gt; /  &lt;PtoVta&gt;  1202  Que el CAEA / PtoVta no esté informado como utilizado en algún  comprobante  Fecha de  envío de la  solicitud  1203  La fecha de envío de la solicitud debe ser mayor a la fecha de inicio de  vigencia del CAEA que se está informando.  &lt;PtoVta&gt;  1204  El PtoVta debe corresponder a un punto de venta habilitado para el  régimen CAEA  &lt;PtoVta&gt;  1205  El punto de venta deberá haber estado activo durante la vigencia del  CAEA  &lt;PtoVta&gt;  1206  El punto de venta deberá haber estar comprendido  entre 1 y 99998  &lt;CAEA&gt;  1207  CAEA y formato válido  PtoVta  1209  El punto de venta informado como sin movimiento ya fue notificado   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Método para informar comprobantes emitidos con  CAEA (FECAEARegInformativo)

Este método permite informar para cada CAEA otorgado, la totalidad de los comprobantes emitidos y asociados a cada CAEA. Por cada comprobante se enviará una solicitud, la cual será procesada por el WS pudiendo producirse alguna de las siguientes situaciones:

-  Supere todas las validaciones, la solicitud es aprobada.
-  No supere alguna de las validaciones excluyentes, la solicitud será rechazada.
-  No supere alguna de las validaciones no excluyentes, la solicitud es aprobada con observaciones.

## Dirección URL (Homologación)

Este servicio se llama desde:

```
https://wswhomo.afip.gov.ar/wsfev1/service.asmx? op=FECAEARegInformativo
```

## Mensaje de solicitud

Recibe la información del comprobante o lote de comprobantes.

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/ envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECAEARegInformativo> <ar:Auth> <ar:Token> string </ar:Token> <ar:Sign> string </ar:Sign> <ar:Cuit> long </ar:Cuit> </ar:Auth> <ar:FeCAEARegInfReq> <ar:FeCabReq> <ar:CantReg> int </ar:CantReg> <ar:PtoVta> int </ar:PtoVta> <ar:CbteTipo> int </ar:CbteTipo> </ar:FeCabReq> <ar:FeDetReq> <ar:FECAEADetRequest> <ar:Concepto> int </ar:Concepto> <ar:DocTipo> int </ar:DocTipo> <ar:DocNro> long </ar:DocNro> <ar:CbteDesde> long </ar:CbteDesde> <ar:CbteHasta> long </ar:CbteHasta> <ar:CbteFch> string </ar:CbteFch> <ar:ImpTotal> double </ar:ImpTotal> <ar:ImpTotConc> double </ar:ImpTotConc> <ar:ImpNeto> double </ar:ImpNeto> <ar:ImpOpEx> double </ar:ImpOpEx> <ar:ImpIVA> double </ar:ImpIVA> <ar:ImpTrib> double </ar:ImpTrib>
```

<!-- image -->

```
<ar:FchServDesde> string </ar:FchServDesde> <ar:FchServHasta> string </ar:FchServHasta> <ar:FchVtoPago> string </ar:FchVtoPago> <ar:MonId> string </ar:MonId> <ar:MonCotiz> double </ar:MonCotiz> <ar:CanMisMonExt> string </ar:CanMisMonExt> <ar:CondicionIVAReceptorId> int </ar:CondicionIVAReceptorId> <ar:CbtesAsoc> <ar:CbteAsoc> <ar:Tipo> short </ar:Tipo> <ar:PtoVta> int </ar:PtoVta> <ar:Nro> long </ar:Nro> <ar:Cuit> String </ar:Cuit> <ar:CbteFch> String </ar:CbteFch> </ar:CbteAsoc> </ar:CbtesAsoc> <ar:Tributos> <ar:Tributo> <ar:Id> short </ar:Id> <ar:Desc> string </ar:Desc> <ar:BaseImp> double </ar:BaseImp> <ar:Alic> double </ar:Alic> <ar:Importe> double </ar:Importe> </ar:Tributo> </ar:Tributos> <ar:Iva> <ar:AlicIva> <ar:Id> short </ar:Id> <ar:BaseImp> double </ar:BaseImp> <ar:Importe> double </ar:Importe> </ar:AlicIva> </ar:Iva> <ar:Opcionales> <ar:Opcional> <ar:Id> string </ar:Id> <ar:Valor> string </ar:Valor> </ar:Opcional> </ar:Opcionales> <ar:PeriodoAsoc> <ar:FchDesde> string </ar:FchDesde> <ar:FchHasta> string </ar:FchHasta> </ar:PeriodoAsoc> <ar:CAEA> string </ar:CAEA> <ar:CbteFchHsGen> string </ar:CbteFchHsGen> <ar:Actividades> <ar:Actividad> <ar:Id> Long </ar:Id> </ar:Actividad> </ar:Actividades> </ar:FECAEADetRequest> </ar:FeDetReq> </ar:FeCAEARegInfReq> </ar:FECAEARegInformativo> </soapenv:Body> </soapenv:Envelope>
```

## Dónde:

<!-- image -->

| Campo  Detalle  Obligatorio  Auth  Información de la autenticación. Contiene los datos de  Token, Sign y Cuit  S  Token  Token devuelto  por  el  WSAA  S  Sign  Sign devuelto  por  el  WSAA  S  Cuit  Cuit contribuyente (representado o Emisora)  S   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Campo  Detalle  Obligatorio  FeCAEARegInfReq  Información del comprobante o lote de comprobantes de  ingreso. Contiene los datos de FeCabReq y FeDetReq  S  FeCabReq  Información de la cabecera del comprobante o lote de  comprobantes de ingreso  S  FeDetReq /  FECAEADetRequest  Información del detalle del comprobante o lote de  comprobantes de ingreso.  S   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

FeCabReq : La cabecera del comprobante o lote de comprobantes de ingreso está compuesta por los siguientes campos:

| Campo  Tipo  Detalle  Obligatorio  CantReg  Int (4)  Cantidad de registros del detalle del comprobante o  lote de comprobantes de ingreso  S  CbteTipo  Int (3)  Tipo de comprobante que se está informando.  Si se  informa más de un comprobante, todos deben ser del  mismo tipo.  S  PtoVta  Int (5)  Punto de Venta del comprobante que se está  informando. Si se informa más de un comprobante,  todos deben corresponder al mismo punto de venta.  S   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

FeDetReq : El detalle del comprobante o lote de comprobantes de ingreso esta compuesto por los siguientes campos:

| Campo  Tipo  Detalle  Obligatorio  Concepto  Int (2)  Concepto del comprobante. Valores  permitidos  1 Productos  2 Servicios  3 Productos y Servicios  S  DocTipo  Int (2)  Código de documento identificatorio del  comprador  S   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo  Tipo  Detalle  Obligatorio  DocNro  Long (11)  Nro.  De identificación del comprador  S  CbteDesde  Long (8)  Nro. De comprobante desde  Rango 1- 99999999  S  CbteHasta  Long (8)  Nro. De comprobante registrado hasta  Rango 1- 99999999  S  CbteFch  String (8)  Fecha del comprobante (yyyymmdd). Para  Concepto igual a 1, la fecha de emisión del  comprobante puede ser hasta más 5 días  respecto de la fecha de generación. La misma  no podrá exceder el mes de presentación. Si se  indica Concepto igual a 2 ó 3 puede ser hasta  10 días anteriores o posteriores a la fecha de  generación  N  ImpTotal  Double  (13+2)  Importe  total  del  comprobante, Debe ser  igual a Importe neto no gravado + Importe  exento + Importe neto gravado + todos los  campos de IVA  al XX% + Importe de tributos  S  ImpTotConc  Double  (13+2)  Importe neto no gravado.  Debe ser menor o igual a Importe total y no  puede ser menor a cero.  S  ImpNeto  Double  (13+2)  Importe neto  gravado. Debe ser menor o igual  a Importe total y no puede ser menor a cero.  S  ImpOpEx  Double  (13+2)  Importe exento. Debe ser menor o igual a  Importe total y no puede ser menor a cero.  S  ImpIVA  Double  (13+2)  Suma de los importes del  array de IVA  S  ImpTrib  Double  (13+2)  Suma de los importes del  array de tributos  S  FchServDesde  String (8)  Fecha de inicio  del abono para el  servicio a  facturar. Dato  obligatorio  para concepto  2 o  3 (Servicios / Productos y Servicios). Formato  yyyymmdd  N  FchServHasta  String (8)  Fecha de fin del abono para el  servicio a  facturar. Dato  obligatorio  para concepto  2 o  3 (Servicios / Productos y Servicios). Formato  yyyymmdd. FchServHasta no puede ser menor  a FchServDesde  N  FchVtoPago  String (8)  Fecha de vencimiento  del  pago servicio a  facturar. Dato  obligatorio  para concepto  2 o  3 (Servicios / Productos y Servicios). Formato  N   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo  Tipo  Detalle  Obligatorio  yyyymmdd. Debe ser igual o posterior a la  fecha del comprobante.  MonId  String (3)  Código  de moneda del  comprobante.  Consultar método  FEParamGetMonedas para  valores posibles  S  MonCotiz  Double  (4+6)  Cotización de la moneda informada. Para PES,  pesos  argentinos  la misma debe ser 1. De  informar el campo, el mismo no puede quedar  vacío.  N  CanMisMonExt  String (1)  Marca que identifica si el comprobante se  cancela en misma moneda del comprobante  (moneda extranjera). Valores posibles S o N.  N  CondicionIVARec  eptorId  Int (2)  Condición Frente al IVA del receptor. Consultar  método 'FEParamGetCondicionIvaReceptor'  Campo obligatorio. Si el valor informado no es  valido, para CAE rechazará y en CAEA  observará. Si el valor no existe rechazará en  ambos casos.  N  CbtesAsoc  Array  Array para informar los comprobantes  asociados &lt;CbteAsoc&gt;  N  Tributos  Array  Array para informar los tributos asociados a un  comprobante &lt;Tributo&gt;.  N  IVA  Array  Array para informar las alícuotas y sus  importes asociados a un comprobante.  N  Opcionales  Array  Array  de campos  auxiliares. Reservado  usos  futuros. Adicionales por R.G.  N  PeriodoAsoc  Periodo  Estructura compuesta por la fecha desde y la  fecha hasta del periodo que se quiere  identificar  N  CAEA  String (14)  Código de Autorización electrónico anticipado  S  CbteFchHsGen  String(14)  Fecha y Hora de generación del comprobante  por  contingencia  . Formato yyyymmddhhmiss  N  Actividades  Actividad  Array para informar las actividades asociadas a  un comprobante.  N   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

CbteAsoc : Detalle de los comprobantes relacionados con el comprobante que se está informando (array).

| Campo  Tipo  Detalle  Obligatorio  Tipo  Int (3)  Código  de tipo de comprobante. Consultar  método  FEParamGetTiposCbte  S   |
|-------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo  Tipo  Detalle  Obligatorio  PtoVta  Int (5)  Punto  de venta  S  Nro  Long (8)  Numero de comprobante  S  Cuit  Long (11)  Cuit Emisor del comprobante  N  CbteFch  String(8)  Fecha del comprobante asociado . Formato  yyyymmdd  N   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Tributos : Detalle de tributos relacionados con el  comprobante que se está informando (array).

| Campo  Tipo  Detalle  Obligatorio  Id  Int  Código  tributo según método  FEParamGetTiposTributos  S  Desc  String (80)  Descripción del  tributo.  N  BaseImp  Double (13+2)  Base imponible para la determinación del  tributo.  S  Alic  Double (3+2)  Alícuota  S  Importe  Double (13+2)  Importe del  tributo  S   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## IVA: Detalle de alícuotas relacionadas con el comprobante que se está informando (array).

| Campo  Tipo  Detalle  Obligatorio  Id  Int (2)  Código  de tipo de iva. Consultar método  FEParamGetTiposIva  S  BaseImp  Double (13+2)  Base imponible para la determinación de la  alícuota.  S  Importe  Double (13+2)  Importe  S   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Opcionales: Campos auxiliares (array). Adicionales por R.G.

Los datos opcionales sólo deberán ser incluidos si el emisor pertenece al conjunto de emisores habilitados a informar opcionales. En ese caso podrá incluir el o los datos opcionales que correspondan, especificando el identificador de dato opcional de acuerdo a la situación del emisor. El listado de tipos de datos opcionales se puede consultar con el método FEParamGetTiposOpcional.

Ejemplo: si el emisor está incluido en el 'Régimen de Promoción Industrial', deberá incluir un array de opcionales con un registro como el sig

&lt;ar:Opcionales&gt;

&lt;ar:Opcional&gt;

&lt;ar:Id&gt;2&lt;/ar:Id&gt;

&lt;ar:Valor&gt;12345678&lt;/ar:Valor&gt;

&lt;/ar:Opcional&gt;

&lt;/ar:Opcionales&gt;

| Campo  Tipo  Detalle  Obligatorio  Id  String(4)  Código  de Opcional, consultar método  FEParamGetTiposOpcional  S  Valor  String (250)  Valor  S   |
|------------------------------------------------------------------------------------------------------------------------------------------------------|

## Periodo : Estructura que permite soportar un rango de fechas.

| Campo  Tipo  Detalle  Obligatorio  FchDesde  String(8)  Fecha correspondiente al inicio del perio-  do de los comprobantes que se quiere  identiricar  S  FchHasta  String(8)  Fecha correspondiente al fin del periodo  de los comprobantes que se quiere iden-  tificar  S   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Actividad : Detalle de la actividad relacionada con las actividades (array) que se indican en el comprobante a autorizar.

| Campo  Tipo  Detalle  Obligatorio  Id  Long (6)  Código  actividad según método  FEParamGetActividades  S   |
|-------------------------------------------------------------------------------------------------------------|

## Mensaje de respuesta

Retorna la información del comprobante o lote de comprobantes de ingreso. Ante cualquier anomalía se retorna un array errores detectados (Errors) o un array de observaciones según corresponda.

```
<soap:Envelope xmlns:soap='http://www.w3.org/2003/05/soap-envelope' xmlns:ar='http://ar.gov.afip.dif.fev1/'> <soap:Header/> <soap:Body>
```

<!-- image -->

```
<FECAEARegInformativoResponse> <FECAEARegInformativoResult> <FeCabResp> <Cuit> long </Cuit> <PtoVta> int </PtoVta> <CbteTipo> int </CbteTipo> <FchProceso> string </FchProceso> <CantReg> int </CantReg> <Resultado> string </Resultado> </FeCabResp> <FeDetResp> <FECAEADetResponse> <Concepto> int </Concepto> <DocTipo> int </DocTipo> <DocNro> long </DocNro> <CbteDesde> long </CbteDesde> <CbteHasta> long </CbteHasta> <Resultado> string </Resultado> <CAEA> string </CAEA> <CbteFch> string </CbteFch> <Obs> <Observaciones> <Code> int </Code> <Msg> string </Msg> </Observaciones> </Obs> </FECAEADetResponse> </FeDetResp> <Events> <Evt> <Code> int </Code> <Msg> string </Msg> </Evt> </Events> <Errors> <Err> <Code> int </Code> <Msg> string </Msg> </Err> </Errors> </FECAEARegInformativoResult> </FECAEARegInformativoResponse> </soap:Body> </soap:Envelope>
```

## Dónde:

| Campo  Detalle  Obligatorio  FECAEARegInformativo  Result  Información del comprobante o lote de comprobantes de  ingreso,  S  FeCabResp  Información de la cabecera del comprobante o lote de  comprobantes enviada en el request + atributos  adicionales como resultado y fecha de proceso.  S  FeDetResp /  Información del detalle del comprobante o lote de  S   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

<!-- image -->

| FECAEADetResponse  comprobantes de ingreso + atributos adicionales como  ser:  resultado del procesamiento.  Fecha del comprobante.  Observaciones sobre el comprobante.  Errors  Información de errores detectados  N  Events  Información de eventos  N   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

FeCabResp : La cabecera del comprobante o lote de comprobantes de ingreso estará compuesta por los siguientes campos:

| Campo  Tipo  Detalle  Obligatorio  Cuit  Long (11)  Cuit del contribuyente  S  PtoVta  Int (5)  Punto  de venta  S  CbteTipo  Int (3)  Tipo  de comprobante  S  FchProceso  String (14)  Fecha de proceso  formato  yyyymmddhhmiss  S  CantReg  Int (4)  Cantidad de registros del detalle del comprobante  o lote de comprobantes de ingreso  S  Resultado  String (1)  Resultado  S   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

FeDetResp: El detalle del comprobante o lote de comprobantes de ingreso estará compuesto por los siguientes campos:

| Campo  Tipo  Detalle  Obligatorio  Concepto  Int (2)  Concepto  S  DocTipo  Int (2)  Código de documento identificatorio del  comprador  S  DocNro  Long (11)  Nro.  De identificación del comprador  S  CbteDesde  Long (8)  Nro. De comprobante desde  S  CbteHasta  Long (8)  Nro. De comprobante registrado hasta  S  CbteFch  String (8)  Fecha del comprobante  N  Resultado  String (1)  Resultado  S  CAEA  String (14)  Código de Autorización electrónico anticipado  N   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo  Tipo  Detalle  Obligatorio  Observaciones  Array  Detalle de observaciones, del comprobante  N   |
|---------------------------------------------------------------------------------------------------------|

Observaciones : La estructura de datos Obs muestra el  detalle de observaciones para un comprobante determinado;   estará compuesta por los siguientes campos:

| Campo  Tipo  Detalle  Obligatorio  Code  Int (5)  Código  de observación  S  Msg  String (255)  Mensaje  S   |
|--------------------------------------------------------------------------------------------------------------|

## Validaciones y errores

## Controles aplicados al objeto &lt; Auth&gt;

Validaciones Excluyentes

| Campo /  Grupo  Código de  error  Descripción de la validación  &lt;Auth&gt;&lt;Cuit&gt;  10000  La CUIT del emisor debe estar registrada y activa en las bases de la  Administración.   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Controles aplicados al objeto &lt;FeCabReq&gt;

Validaciones Excluyentes

| Campo /  Grupo  Código de  error  Descripción de la validación  &lt;CantReg&gt;  10001  Cantidad de registros de detalle del comprobante o lote de comprobantes  de ingreso &lt;CantReg&gt; debe estar comprendido entre 1 y 9998  &lt;CantReg&gt;  10002  La cantidad de registros del detalle del comprobante o lote de  comprobantes de ingreso debe ser igual a lo informado en cabecera del  comprobante o lote de comprobantes de ingreso &lt;CantReg&gt;.  Cantidad de  registros  incluidos  10003  La cantidad de registros en detalle debe ser menor igual al valor permitido.  Consulte método FECompTotXRequest para obtener cantidad máxima de  registros por cada requerimiento. Para comprobantes del tipo MiPyMEs  (FCE), la cantidad habilitada es 1 comprobante por request  CbteTipo  700  Obligatorio.  Valores permitidos:  1: Factura A  2: Nota de Débito A  3: Nota de Crédito A   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo /  Grupo  Código de  error  Descripción de la validación  4: Recibo A  6: Factura B  7: Nota de Débito B  8: Nota de Crédito B  9: Recibo B  11: Factura C  12: Nota de Débito C  13: Nota de Crédito C  15: Recibo C  51: Factura M  (CAEA observa comprobante)  52: Nota de Débito M  (CAEA observa comprobante)  53: Nota de Crédito M  (CAEA observa comprobante)  54: Recibo M  201: Factura de Crédito electrónica MiPyMEs (FCE) A  202: Nota de Débito electrónica MiPyMEs (FCE) A  203: Nota de Crédito electrónica MiPyMEs (FCE) A  206: Factura de Crédito electrónica MiPyMEs (FCE) B  207: Nota de Débito electrónica MiPyMEs (FCE) B  208: Nota de Crédito electrónica MiPyMEs (FCE) B  211: Factura de Crédito electrónica MiPyMEs (FCE) C  212: Nota de Débito electrónica MiPyMEs (FCE) C  213: Nota de Crédito electrónica MiPyMEs (FCE) C  Consultar método  FEParamGetTiposCbte  PtoVta  1300  Campo PtoVta debe estar comprendido entre 1 y 99998.  PtoVta  701  El punto de Venta debe ser del tipo habilitado para CAEA - Fact. Elect.  (RECE) - RI IVA / CAEA - Fact. Elect. (RECE) -  Contingencias / CAEA - Fact.  Elect. (RECE) - Exento en IVA - Contingencias / CAEA - Fact. Elect. (RECE) -  Monotributo - Contingencias y no debe estar bloqueado a la fecha en que  se emitió el comprobante. Consultar método  FEParamGetPtosVenta.   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Validaciones Excluyentes

| Campo / Grupo  Código de  Error  Validación  CbteFch  702  Debe estar comprendida dentro de la fecha desde  y fecha hasta de vigencia del CAEA  CbteDesde / CbteHasta / PtoVta /  CbteTipo  703  El número de comprobante informado debe ser  mayor en 1 al último informado para igual punto  de venta y tipo de comprobante. Consultar  método FECompUltimoAutorizado  CbteFch / PtoVta / CbteTipo  704  La fecha del comprobante debe ser mayor o igual  a la fecha del último comprobante informado para  igual tipo de comprobante y punto de venta.  CAEA  705  Debe corresponder a la CUIT que está informando  Fecha de envío de la solicitud  1414  Al informar un comprobante con la modalidad  CAEA, la fecha en la que se informa el  comprobante debe ser mayor a la fecha de  entrada en vigencia del CAEA vinculado  CAEA / PtoVta  709  La fecha de alta del  punto  de venta deberá ser  menor o  igual a la fecha de vigencia 'hasta' del  CAEA  MonId  1401  El campo MonId es obligatorio  y debe  corresponder a algún valor devuelto  por  el  método FEParamGetTiposMonedas.  Concepto  713  Valores permitidos:  1 Productos  2 Servicios  3 Productos y Servicios  Consultar método FEParamGetTiposConcepto  ImpIVA / Iva / AlicIva  715  Si ImpIVA es igual a 0 los objetos Iva y AlicIva solo  deben informarse con ImpIVA = 3 (iva 0)  Si ImpIVA es mayor a 0 el objeto Iva y AlicIva son  obligatorios.  El objeto AlicIva es obligatorio y no debe ser nulo  si ingresa Iva.  &lt;ImpTotConc&gt;  717  El campo ImpTotConc (Importe neto no gravado)  no puede ser menor a cero (0).   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

<!-- image -->

| Campo / Grupo  Código de  Error  Validación  El campo ImpTotConc soporta 13 números para la  parte entera y 2 para los decimales.  &lt;ImpOpEx&gt;  718  El campo ImpOpEx soporta 13 números para la  parte entera y 2 para los decimales.  El campo ImpOpEx (importe exento) no puede ser  menor a cero (0).  &lt;ImpNeto&gt;  719  El campo ImpNeto (Importe neto  gravado) no  puede ser menor a cero (0)  El campo ImpNeto soporta 13 números para la  parte entera y 2 para los decimales.  &lt;ImpTrib&gt;  723  El campo ImpTrib (Importe de tributos) no puede  ser menor a cero (0).  El campo ImpTrib soporta 13 números para la  parte entera y 2 para los decimales.  &lt;ImpIVA&gt;  1407  El campo ImpIVA (Importe de IVA) no puede ser  menor a cero (0).  El campo ImpIVA soporta 13 números para la  parte entera y 2 para los decimales.  &lt;MonCotiz&gt;  726  El campo MonCotiz es obligatorio y mayor a 0  Debe ser igual a 1 (uno) si &lt;MonId&gt; es igual a PES.  Si &lt;MonId&gt; es diferente a PES que &lt;MonCotiz&gt; sea  Mayor a 0.  El campo MonCotiz es opcional  si  informa el  campo CanMisMonExt con el valor S y el tipo de  comprobante es factura y la moneda tiene  cotización en Banco Nación.  El campo MonCotiz soporta 4 números para la  parte entera y 6 para los decimales.  CAEA  780  Deberá corresponder a un CAEA registrado en las  bases de la Administración  PtoVta / CbteFch  781  La fecha de alta del punto  de venta deberá ser  menor o igual a la fecha del comprobante  CAEA  782  Obligatorio, numérico de 14 posiciones  CbteFch  783  Obligatorio, formato  yyyymmdd  CbteDesde / CbteHasta  784  Obligatorio, entero; valores comprendidos entre 1  y 99999999.  &lt;CbteHasta&gt; / &lt;CbteDesde&gt;  1416  Para comprobantes tipo B, &lt;CbteHasta&gt; sea mayor   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo / Grupo  Código de  Error  Validación  o igual a &lt;CbteDesde&gt;  &lt;CbteTipo&gt; / &lt;CbteDesde&gt; /  &lt;CbteHasta&gt;  1415  Para comprobantes tipo  B (CbteDesde distinto a  CbteHasta) y el resultado de la operación ImpTotal  / (CbteHasta - CbteDesde + 1 ) &lt; monto en pesos  resultante según RG4444, el campo  DocNro  deberá ser cero (0) y el campo 138DocTipo 99.  DocTipo / DocNro / CbteDesde /  CbteHasta  1417  Para comprobantes B o C (CbteDesde igual a  CbteHasta) mayor o igual a monto en pesos  resultante según RG4444, DocTipo debe ser uno  de los valores devueltos por el método  FEParamGetTiposDoc distinto a 99 y DocNro  deberá ser mayor a 0.  DocTipo / DocNro / CbteDesde /  CbteHasta  1418  Para comprobantes B o C (CbteDesde igual a  CbteHasta) menor a monto en pesos resultante  según RG4444, si DocTipo = 99 DocNro debe ser  igual a 0.  DocTipo / DocNro / CbteDesde /  CbteHasta  1419  Para comprobantes B o C (CbteDesde igual a  CbteHasta) menor a monto en pesos resultante  según RG4444, si DocTipo es distinto a 99, DocNro  debe ser mayor a 0.  &lt;CbteTipo&gt; / &lt;CbteDesde&gt; /  &lt;CbteHasta&gt;  1422  Para comprobantes tipo B, &lt;CbteDesde&gt; distinto a  &lt;CbteHasta&gt; el resultado de la operación  ImpTotal / (CbteHasta - CbteDesde + 1 ) &lt; monto  en pesos resultante según RG4444.  &lt;CbteTipo&gt; / &lt;CbteDesde&gt; /  &lt;CbteHasta&gt;  711  Para comprobantes clase A y comprobantes  MiPyMEs (FCE) el campo CbteDesde debe ser igual  al campo CbteHasta  &lt;CbteTipo&gt; / &lt;DocTipo&gt;  1403  Para comprobantes clase A el campo  DocTipo  debe ser igual a 80 (CUIT)  &lt;ImpTotal&gt;  1409  El campo ImpTotal no puede ser menor a cero (0).  El campo ImpTotal soporta 13 números para la  parte entera y 2 para los decimales.  &lt;DocTipo&gt; / &lt;DocNro&gt;  1404  Para comprobantes tipo B o tipo C, si informa  &lt;DocTipo&gt; y &lt;DocNro&gt;, &lt;DocTipo&gt; debe ser un  valor devuelto por el método  FEParamGetTiposDoc.  &lt;CbteTipo&gt; / &lt;DocNro&gt;  1405  Para comprobantes tipo B o tipo C el campo  DocNro debe ser un valor comprendido entre 0 y  99999999999  &lt;CbteTipo&gt; / &lt;DocNro&gt;  1421  Para comprobantes tipo A el campo  DocNro debe  ser un valor comprendido entre 20000000000 y   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo / Grupo  Código de  Error  Validación  60000000000  DocTipo / DocNro  788  Cuando se informa tipo de comprobante 80, el  documento informado no puede ser el mismo al  ingresado en el campo &lt;Auth&gt;&lt;Cuit&gt;  &lt;ImpTrib&gt; / &lt;Tributos&gt; /  &lt;Tributo&gt;  1423  Si ImpTrib es igual a 0 el objeto Tributos y Tributo  no deben informarse.  Si ImpTrib es mayor a 0 el objeto Tributos y  Tributo son obligatorios.  Si ImpTrib mayor a 0, Tributos y Tributo no pueden  venir vacíos.  &lt;Opcionales&gt;&lt;CbteTipo&gt;  1426  El array &lt;Opcionales&gt; no es obligatorio. Solo  puede informarse si &lt;CbteTipo&gt; es 1, 2, 3, 6, 7,8  &lt;Compradores&gt;  1432  No se encuentra habilitado informar compradores  en el régimen de información para la modalidad  CAEA.  &lt;CbteTipo&gt;/  &lt;CbteDesde&gt;/  &lt;CbteHasta&gt;  1433  Para comprobantes tipo C &lt;CbteHasta&gt; debe ser  igual a &lt;CbteDesde&gt;.  &lt;CbteTipo&gt;/  &lt;ImpTotConc&gt;  1434  Para comprobantes tipo C, el campo 'Importe  neto no gravado'  &lt;ImpTotConc&gt; debe ser igual a  cero (0).  &lt;CbteTipo&gt;/  &lt;ImpOpEx&gt;  1435  Para comprobantes tipo C, el campo &lt;ImpOpEx&gt;  debe ser igual a cero (0).  &lt;CbteTipo&gt;/  &lt;ImpNeto&gt;  1436  Para comprobantes tipo C el campo &lt;ImpNeto&gt;  corresponde al Importe del Sub Total.  &lt;CbteTipo&gt;/  &lt;ImpTrib&gt;  1437  Para comprobantes tipo C, el campo 'Importe de  tributos'  &lt;ImpTrib&gt;. No puede ser menor a cero  (0).  &lt;CbteTipo&gt;/  &lt;ImpIVA&gt;  1438  Para comprobantes tipo C, el campo 'Importe de  IVA' &lt; ImpIVA&gt; debe ser igual a cero (0).  &lt;CbteTipo&gt;/  &lt;ImpTotal&gt;/  &lt;ImpNeto&gt; /  &lt;ImpTrib&gt; /  1439  Para comprobantes tipo C, el campo  'Importe  Total' &lt;ImpTotal&gt;, debe ser igual  a la  suma de  ImpNeto + ImpTrib.  Margen de error:  Error relativo porcentual deberá ser &lt;= 0.01% o el   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo / Grupo  Código de  Error  Validación  error absoluto &lt;=0.01  &lt;CbteFchHsGen&gt;  1440  Si el punto de venta es para CONTINGENCIAS  CAEA el campo es obligatorio informarlo  &lt;CbteFchHsGen&gt;  1441  Si informa el campo, el mismo tiene que contener  un valor según lo definido en la estructura.  Formato yyyymmddhhmiss  &lt;Iva&gt;  1443  Si el tipo de comprobante es C, el array de IVA no  debe informarse.  &lt;PtoVta&gt; /&lt;CbteTipo&gt;  1444  Si el comprobante es tipo A, B, M los puntos de  venta habilitados son CAEA - Fact. Elect. (RECE) - RI  IVA / CAEA - Fact. Elect. (RECE) - RI IVA -  Contingencias.  Si el comprobante es tipo C, los puntos de venta  habilitados son CAEA - Fact. Elect. (RECE) - Exento  en IVA - Contingencias /  CAEA - Fact. Elect. (RECE) - Monotributo -  Contingencias  &lt;FeCabReq&gt;&lt;CbteTipo&gt; /  &lt;CbteTipo&gt; / &lt;DocNro&gt;  1445  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), el campo DocNro para  comprobantes deberá ser un valor registrado en el  padrón de arca, en condición activa.  &lt;CbteTipo&gt; / &lt;DocNro&gt;  1446  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), el campo DocNro para  comprobantes deberá ser un valor registrado en el  padrón de arca, en condición activa.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;FECAEDetRequest&gt;&lt;CbtesAsoc&gt;  1450  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE) y corresponde a un comprobante  de débito o crédito, es obligatorio informar  comprobantes asociados.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;CbteAsoc&gt;&lt;Tipo&gt;&lt;PtoVta&gt;&lt;Nro  &gt;&lt;Cuit&gt;  1451  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE) y corresponde a un comprobante  de débito o crédito. Tener en cuenta que:  - sí el comprobante asociado  se encuentra  rechazado por el comprador hay que informar el  código de anulación correspondiente sobre el  campo "Adicionales por RG",  códigos 22  -  Anulación. Valor 'S'  - sí el comprobante asociado  no se encuentra  rechazado por el comprador hay que informar el  código de no anulación correspondiente sobre el  campo "Adicionales por RG",  códigos 22  -   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo / Grupo  Código de  Error  Validación  Anulación. Valor 'N'  &lt;Auth&gt;&lt;Cuit&gt;  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;CbteAsoc&gt;&lt;Cuit&gt;  1452  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), el CUIT del emisor del  comprobante asociado debe coincidir con el CUIT  del emisor del comprobante a autorizar.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;CbteAsoc&gt;&lt;Tipo&gt;  1453  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), Débito o Crédito sin código de  Anulación siempre debe asociar 1 solo  comprobante tipo factura.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;CbteAsoc&gt;&lt;Tipo&gt;  1454  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), Débito o Crédito sin código de  Anulación solo puede asociar:  Para comprobantes A, asociar 201 o  (91, 88, 988,  990, 991, 993, 994, 995, 996, 997).  Para comprobantes B, asociar 206 o  (91, 88, 988,  990, 991, 993, 994, 995, 996, 997).  Para comprobantes C, asociar 211 o  (91, 88, 988,  990, 991, 993, 994, 995, 996, 997).  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;CbteAsoc&gt; / &lt;Tipo&gt; / &lt;PtoVta&gt; /  &lt;Nro&gt; / &lt;Cuit&gt; / &lt;CbteFch&gt;  1455  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), Débito o Crédito, es obligatorio  informar la fecha del comprobante asociado  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;FeDetReq&gt;/&lt;CbteFch&gt;/  &lt;CbteAsoc&gt; / &lt;Tipo&gt; / &lt;PtoVta&gt; /  &lt;Nro&gt; / &lt;Cuit&gt; / &lt;CbteFch&gt;  1456  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), Débito o Crédito, la fecha del  comprobante asociado tiene que ser igual o  menor a la fecha del comprobante que se está  autorizando  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;CbteAsoc&gt; / &lt;Tipo&gt; / &lt;PtoVta&gt; /  &lt;Nro&gt; / &lt;Cuit&gt; / &lt;CbteFch&gt;  1457  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), Débito o Crédito, el comprobante  debe existir autorizado en las bases de esta  Administración con la misma fecha informada en  el asociado.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;FECAEDetRequest&gt;&lt;DocTipo&gt;&lt;  DocNro&gt;  1458  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), el receptor del comprobante debe  tener habilitado el domicilio fiscal electrónico  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;Opcionales&gt;  1459  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE)  es obligatorio informar &lt;Opcionales&gt;   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo / Grupo  Código de  Error  Validación  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;FchVtoPago&gt;  1460  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), Tipo 201 - FACTURA DE CREDITO  ELECTRONICA MiPyMEs (FCE) A / 206 - FACTURA  DE CREDITO ELECTRONICA MiPyMEs (FCE) B / 211  - FACTURA DE CREDITO ELECTRONICA MiPyMEs  (FCE) C,  es obligatorio informar FchVtoPago  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;FchVtoPago&gt; /  &lt;FECAEDetRequest&gt;&lt;CbteFch&gt;  1461  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), la fecha de vencimiento de pago  (FchVtoPago) debe ser posterior o igual a la fecha  de emisión (CbteFch) o fecha de presentación (fe-  cha actual), la que sea posterior  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;Opcionales&gt;&lt;Id&gt;&lt;Valor&gt;  1462  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), informa opcionales, el valor co-  rrecto para el código 2101 es un CBU numérico de  22 caracteres.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;Opcionales&gt;&lt;Id&gt;&lt;Valor&gt;  1463  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), informa opcionales, el valor co-  rrecto para el código 2102 es un ALIAS alfanuméri-  co de 6 a 20 caracteres.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;Opcionales&gt;&lt;Id&gt;&lt;Valor&gt;  1464  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), informa opcionales, el valor co-  rrecto para el código 22 es 'S' o 'N':  S = Es de Anulación  N = No es de Anulación  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;Opcionales&gt;&lt;Id&gt;&lt;Valor&gt;  1465  Si el tipo de comprobante que está autorizando es  Factura (201, 206, 211) del tipo MiPyMEs (FCE), in-  forma opcionales, es obligatorio informar CBU.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;Opcionales&gt;&lt;Id&gt;&lt;Valor&gt;  1466  Si el tipo de comprobante que está autorizando  NO es MiPyMEs (FCE), no informar los códigos  2101, 2102, 22, 27  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;Opcionales&gt;&lt;Id&gt;&lt;Valor&gt;  1467  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), es obligatorio informar al menos  uno de los sig. códigos 2101, 22, 27  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;Opcionales&gt;&lt;Id&gt;&lt;Valor&gt;  1468  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), Factura (201, 206, 211), no infor-  mar Código de Anulación  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;Opcionales&gt;&lt;Id&gt;&lt;Valor&gt;  1469  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), Debito (202, 207, 212) o Crédito  (203, 208, 213) No informar CBU y ALIAS.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;Opcionales&gt;&lt;Id&gt;&lt;Valor&gt;  1470  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), Debito (202, 207, 212) o Crédito  (203, 208, 213) informar Código de Anulación  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;Opcionales&gt;&lt;Id&gt;&lt;Valor&gt;  1471  Si el tipo de comprobante que está autorizando es  factura MiPyMEs (FCE), el CBU debe estar registra-  do en las bases de esta administración, vigente y  pertenecer al emisor del comprobante.   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo / Grupo  Código de  Error  Validación  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;FchVtoPago&gt;  1472  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), el campo 'fecha de vencimiento  para el pago'  &lt;FchVtoPago&gt;  no debe informarse  si NO es Factura de Crédito. En el caso de ser  Débito o Crédito, solo puede informarse si es de  Anulación.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;CbteTipo&gt; / &lt;DocNro&gt;  1474  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE) del tipo A, el receptor del  comprobante informado en DocTipo y  DocNro  debe corresponder a un contribuyente activo en el  Impuesto al Valor Agregado o Responsable  Monotributo.  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE) del tipo B, el receptor del  comprobante informado en DocTipo y  DocNro  debe corresponder a un contribuyente activo en el  Impuesto Iva, Monotributo o Exento.  Si el tipo de comprobante que esta autorizando es  MiPyMEs (FCE) del tipo C, el receptor del  comprobante informado en DocTipo y  DocNro  debe corresponder a un contribuyente activo en el  Impuesto Iva, Monotributo o Exento.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;CbteTipo&gt; / &lt;DocNro&gt;  1475  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE) no se permite informar DocNro  23000000000 (No Categorizado)  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;CbteTipo&gt; / &lt;DocNro&gt;  1476  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), el receptor del comprobante  informado en DocTipo y  DocNro debe  corresponder a un contribuyente caracterizado  como GRANDE o que opto por PYME. Su activida  principal debe corresponderse con alguna de las  alcanzadas por el régimen.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;MonId&gt;  &lt;CbteAsoc&gt;  1477  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), débito o crédito, el mismo debe  tener la misma moneda que el comprobante aso-  ciado o Pesos para ajuste en las diferencias de  cambio (post aceptación/rechazo)  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;FECAEDetRequest&gt;&lt;DocTipo&gt;&lt;  DocNro&gt;/  &lt;CbteAsoc&gt;  1478  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), es débito o crédito, deben  coincidir emisores y receptores.  Si el comprobante ES de anulación, para autorizar  un débito, el tipo de comprobante a asociar debe   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo / Grupo  Código de  Error  Validación  ser crédito y para autorizar un crédito, el tipo de  comprobante a asociar debe ser una factura o un  débito.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;MonId&gt;  &lt;CbteAsoc&gt;/  &lt;FeCabReq&gt;&lt;ImpTotal&gt;  1479  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), es crédito el monto del  comprobante a autorizar no puede ser mayor o  igual al saldo actual de la cuenta corriente. Ver  micrositio factura de crédito  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;CbteAsoc&gt;/  1480  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), es crédito o débito A, de  anulación, solo se encuentra habilitado asociar un  comprobante de crédito A. Utilizar debito para  anular crédito o utilizar crédito para anular débito  o factura.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;CbteAsoc&gt;/  1481  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), es crédito o débito B, de  anulación, solo se encuentra habilitado asociar un  comprobante de crédito B. Utilizar debito para  anular crédito o utilizar crédito para anular débito  o factura.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;Opcionales&gt;&lt;Id&gt;&lt;Valor&gt;  1482  Puede identificar una o varias Referencias  Comerciales según corresponda. Informar bajo el  código 23. Campo alfanumérico de 50 caracteres  como máximo.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;Opcionales&gt;&lt;Id&gt;&lt;Valor&gt;  1483  Si informa opcionales con más de un identificador  23 - Referencia Comercial, no repetir el valor.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;CbteAsoc&gt;/  1486  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), es crédito o débito C, de  anulación, solo se encuentra habilitado asociar un  comprobante de crédito C. Utilizar debito para  anular crédito o utilizar crédito para anular débito  o factura.  &lt;CbteTipo&gt; / &lt;DocTipo&gt; /  &lt;DocNro&gt;  1487  Para comprobantes MiPyMEs (FCE) el documento  del receptor debe ser 80 CUIT.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;CbteAsoc&gt; / &lt;Tipo&gt; / &lt;PtoVta&gt; /  &lt;Nro&gt; / &lt;Cuit&gt; / &lt;CbteFch&gt;  1488  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), Débito o Crédito, el comprobante  debe existir autorizado en las bases de esta  Administración.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;FECAEADetRequest&gt;&lt;PeriodoAs  oc&gt;  1490  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), no se encuentra habilitado  informar PeriodoAsoc.   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo / Grupo  Código de  Error  Validación  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;FECAEADetRequest&gt;&lt;CbtesAsoc  &gt;/  &lt;FECAEADetRequest&gt;&lt;PeriodoAs  oc&gt;  1491  Si el comprobante es Debito o Crédito, se deberá  informar de forma obligatoria los campos Fecha  Comprobantes Asociados Desde/Hasta, o al menos  un comprobante asociado.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;FECAEADetRequest&gt;&lt;PeriodoAs  oc&gt;  1492  Si el comprobante es Factura no se deberá  informar los campos Fecha Comprobantes  Asociados Desde/Hasta  &lt;FECAEADetRequest&gt;&lt;PeriodoAs  oc&gt;&lt;FchDesde&gt;  1493  Si envía estructura PeriodoAsoc es obligatorio  enviar FchDesde.  &lt;FECAEADetRequest&gt;&lt;PeriodoAs  oc&gt;&lt;FchHasta&gt;  1494  Si envía estructura PeriodoAsoc es obligatorio  enviar FchHasta.  &lt;FECAEADetRequest&gt;&lt;PeriodoAs  oc&gt;&lt;FchDesde&gt;  1495  El campo PeriodoAsoc.FchDesde debe  corresponder a una fecha valida con formato  YYYYMMDD  &lt;FECAEADetRequest&gt;&lt;PeriodoAs  oc&gt;&lt;FchHasta&gt;  1496  El campo PeriodoAsoc.FchHasta debe  corresponder a una fecha valida con formato  YYYYMMDD  &lt;FECAEADetRequest&gt;&lt;PeriodoAs  oc&gt;&lt;FchDesde&gt;/  &lt;FECAEADetRequest&gt;&lt;PeriodoAs  oc&gt;&lt;FchHasta&gt;  1497  Las fechas informadas en PeriodoAsoc deben ser  superiores a 01/01/2006  &lt;FECAEADetRequest&gt;&lt;PeriodoAs  oc&gt;&lt;FchDesde&gt;/  &lt;FECAEADetRequest&gt;&lt;PeriodoAs  oc&gt;&lt;FchHasta&gt;  1498  Las fechas informadas en PeriodoAsoc , FchHasta  debe ser superior o igual a FchDesde.  &lt;FECAEADetRequest&gt;&lt;PeriodoAs  oc&gt;&lt;FchHasta&gt;  1499  Las fecha informada en PeriodoAsoc.FchHasta  debe ser anterior o igual a la fecha de emisión del  comprobante que estamos autorizando  &lt;FECAEADetRequest  &gt;&lt;CbtesAsoc&gt;&lt;CbteFch&gt;  1502  Informar de forma obligatoria la fecha de Emisión  del comprobante asociado si el punto de venta del  comprobante asociado es Controlador Fiscal o  FactuWeb y el tipo de Comprobante asociado es  Factura, Recibo, Nota de Débito/Nota de Crédito  &lt;FECAEADetRequest  &gt;&lt;CbtesAsoc&gt;&lt;CbteFch&gt;  1503  De informar fecha de Emisión del comprobante  asociado y el punto de venta es Controlador Fiscal  o FactuWeb, la fecha no puede ser posterior al día  de hoy.  &lt;FECAEADetRequest&gt;&lt;CbtesAsoc  1504  Si se informan deben tener el siguiente formato   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo / Grupo  Código de  Error  Validación  &gt;&lt;CbteFch&gt;  yyyymmdd.  &lt;FECAEADetRequest&gt;/  &lt;Opcionales&gt;&lt;Id&gt;/&lt;CbteTipo&gt;  1505  Si el comprobante es del tipo A (1, 2, 3, 4, 5, 34,  39, 60, 63) e intenta informar datos opcionales  según Resolución General 3668, los valores  posibles para los identificadores son 5, 61, 62, 7.  &lt;FECAEADetRequest&gt;/  &lt;Opcionales&gt;&lt;Id&gt;/  &lt;Opcionales&gt;&lt;Valor&gt;  1506  Si informa Id = 5, el valor ingresado no puede ser  blanco y debe ser alfanumérico de 2 caracteres.  &lt;FECAEADetRequest&gt;/  &lt;Opcionales&gt;&lt;Id&gt;/  &lt;Opcionales&gt;&lt;Valor&gt;  1507  Si informa Id = 5, el contenido del campo &lt;Valor&gt;  debe corresponder a un código de EXCEPCION  válido comprendido por alguno de los sig:  01 - Locador / Prestador del mismo  02 - Congresos / Eventos  03 - Operación contemplada en RG 74  04 - Bienes de Cambio  05 - Ropa de trabajo  06 - Intermediario  &lt;FECAEADetRequest&gt;/  &lt;Opcionales&gt;&lt;Id&gt;/  &lt;Opcionales&gt;&lt;Valor&gt;  1508  Si informa Id = 61, el valor ingresado no puede ser  blanco y debe ser numérico de 2 caracteres.  &lt;FECAEADetRequest&gt;/  &lt;Opcionales&gt;&lt;Id&gt;/  &lt;Opcionales&gt;&lt;Valor&gt;  1509  Si informa Id = 61, el contenido del campo &lt;Valor&gt;  debe corresponder a un código que represente el  tipo de documento del firmante. Ver método  FEParamGetTiposDoc.  &lt;FECAEADetRequest&gt;/  &lt;Opcionales&gt;&lt;Id&gt;/  &lt;Opcionales&gt;&lt;Valor&gt;  1510  Si informa Id = 62, el valor ingresado no puede ser  blanco y debe ser numérico de 11 caracteres como  máximo.  &lt;FECAEADetRequest&gt;/  &lt;Opcionales&gt;&lt;Id&gt;/  &lt;Opcionales&gt;&lt;Valor&gt;  1511  Si informa Id = 7, el valor ingresado no puede ser  blanco y debe ser numérico de 2 caracteres.  &lt;FECAEADetRequest&gt;/  &lt;Opcionales&gt;&lt;Id&gt;/  &lt;Opcionales&gt;&lt;Valor&gt;  1512  Si informa Id = 7, el contenido del campo &lt;Valor&gt;  debe corresponder a un código de carácter  firmante válido comprendido por alguno de los sig:  01 - Titular   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo / Grupo  Código de  Error  Validación  02 - Director / Presidente  03 - Apoderado  04 - Empleado  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;Opcionales&gt;&lt;Id&gt;&lt;Valor&gt;  1513  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), informa opcionales, el tipo de  dato correcto para el código 27 es un alfanumérico  de 3 caracteres.  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;Opcionales&gt;&lt;Id&gt;&lt;Valor&gt;  1514  Si el tipo de comprobante que está autorizando es  MiPyMEs (FCE), informa opcionales y el código es  27, los valores posibles son:  SCA = "TRANSFERENCIA AL SISTEMA DE  CIRCULACION ABIERTA"  ADC = "AGENTE DE DEPOSITO COLECTIVO"  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;Opcionales&gt;&lt;Id&gt;&lt;Valor&gt;  1515  Si el tipo de comprobante que está autorizando es  Factura del tipo MiPyMEs (201, 206, 211),  es  obligatorio informar &lt;Opcionales&gt; con id = 27. Los  valores posibles son SCA o ADC.  &lt;FECAEADetRequest&gt; /  &lt;CanMisMonExt&gt;  820  Si informa el campo CanMisMonExt, los valores  posibles son S o N y no debe quedar vacío.  &lt;FECAEADetRequest&gt; /  &lt;CondicionIVAReceptorId&gt;  823  El campo de identificación de la Condición de IVA  del receptor no es un valor permitido. Para mayor  detalle consular el método  FEParamGetCondicionIvaReceptor.  &lt;FECAEADetRequest&gt; /  &lt;CondicionIVAReceptorId&gt;  826  Campo Condición Frente al IVA del receptor es  obligatorio conforme a lo reglamentado por la  Resolución General N° 5616. Para mas información  consular método  FEParamGetCondicionIvaReceptor.   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Validaciones NO Excluyentes

| Campo  Código de  Observ.  Validación  &lt;CbteTipo&gt; / &lt;DocNro&gt;  708  El campo DocNro para comprobantes Tipo A  deberá ser un valor registrado y ACTIVO en el  padrón de arca.  &lt;ImpTotConc&gt; / &lt;ImpOpEx&gt; /  &lt;ImpNeto&gt; / &lt;ImpTrib&gt; /  724  El campo  'Importe Total' &lt;ImpTotal&gt;, debe ser  igual  a la  suma de ImpTotConc + ImpNeto +   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo  Código de  Observ.  Validación  &lt;ImpIVA&gt; / &lt;ImpTotal&gt;  ImpOpEx + ImpTrib + ImpIVA  Margen de error:  Error relativo porcentual deberá ser &lt;= 0.01% o el  error absoluto &lt;=0.01  FchServHasta  728  Debe informarse solo si &lt;Concepto&gt; es igual a 2 ó  3. En otro caso no corresponde.  &lt;ImpIVA&gt;  725  Debe ser igual a la sumatoria de la totalidad de los  campos &lt;importe&gt; (dentro de &lt;AlicIVA&gt;)  Margen de error:  Error relativo porcentual deberá ser &lt;= 0.01% o el  error absoluto &lt;=0.01 * cantidad de alícuotas de  IVA  ingresadas*  &lt;CbteTipo&gt; / 148&lt;DocTipo&gt; /  &lt;DocNro&gt;  1402  Para comprobantes Tipo A deberá encontrarse  registrado en condición activa en el Impuesto al  Valor Agregado o Responsable Monotributo.  &lt;FchServDesde&gt;  727  FchServDesde debe informarse solo si Concepto es  igual a 2 o 3. En otro caso no corresponde.  &lt;CbteTipo&gt; / &lt;DocTipo&gt; /  &lt;DocNro&gt;  1420  Para comprobantes tipo B o C (CbteDesde igual a  CbteHasta) y DocTipo 80, 86, 87, DocNro deberá  ser un valor registrado en el padrón de arca. Si  DocTipo es 80 y DocNro es 23000000000 (No  Categorizado) esta validación no se tendrá en  cuenta.  &lt;ImpNeto&gt; / &lt;AlicIva&gt; &lt;BaseImp&gt;  1408  La suma de los campos &lt;BaseImp&gt; en  &lt;AlicIva&gt;  debe  ser igual al valor ingresado  en  ImpNeto.  Esta validación no deberá ser tenida en cuenta,  cuando el &lt;CbteTipo&gt; sea 02, 03, 07, 08.  Margen de error:  Error relativo porcentual deberá ser &lt;= 0.01% o el  error absoluto &lt;=0.01 * cantidad de alícuotas de  IVA ingresadas *  FchVtoPago  1411  Debe ser mayor o igual a la fecha del comprobante.  FchVtoPago  729  Debe informarse solo si &lt;Concepto&gt; es igual a 2 ó  3. En otro caso no corresponde.  &lt;FchServDesde&gt;/ &lt;FchServHasta&gt;  1412  &lt;FchServDesde&gt; no puede ser posterior al campo  &lt;FchServHasta&gt;.  &lt;ImpTrib&gt;  1406  Debe ser igual a la sumatoria de la totalidad de los   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo  Código de  Observ.  Validación  campos &lt;Importe&gt; (dentro de &lt;Tributos&gt;).  Margen de error:  Error relativo porcentual deberá ser &lt;= 0.01% o el  error absoluto &lt;=0.01 * cantidad de tributos *  CAEA /  &lt;PtoVta&gt;  1424  El CAEA y punto de venta no debe estar informado  sin movimientos.  &lt;ImpTrib&gt; &lt;DocTipo&gt;&lt;DocNro&gt;  1425  Para comprobantes tipo B, si &lt;DocTipo&gt; es 80 y  &lt;DocNro&gt; es 23000000000 (No Categorizado),  &lt;ImpTrib&gt; debe ser mayor a 0.  &lt;FchServDesde&gt;/  &lt;FchServHasta&gt;/ &lt;FchVtoPago&gt;  1413  Si se informan deben tener el siguiente formato  yyyymmdd.  &lt;ImpNeto&gt;/  &lt;Iva&gt;.&lt;AlicIva&gt;  1427  Si ImpNeto es mayor a 0, el objeto AlicIva es  obligatorio y no debe ser nulo.  &lt;Auth&gt;&lt;Cuit&gt; /  &lt;CbteTipo&gt; /  &lt;CbteFch&gt;  1429  No se encuentra habilitado a emitir comprobantes  'A' a la fecha de emisión del comprobante. El  comprobante  queda observado.  &lt;Auth&gt;&lt;Cuit&gt; /  &lt;CbteTipo&gt; /  &lt;CbteFch&gt;  1431  Al momento de emitir el comprobante, debe estar  dado de alta en el Impuesto.  &lt;CbteFchHsGen&gt;  1442  Si el punto de venta informado no es para  CONTINGENCIA no informar el campo  &lt;CbteFchHsGen&gt;  &lt;CbteFch&gt;/  &lt;CbteFchHsGen&gt;/  &lt;Concepto&gt;  1445  El campo &lt;CbteFch&gt; podrá estar  comprendido  en  el  rango  N-5 y N+5 siendo  N la fecha  CbteFchHsGen (contingencia) para Concepto= 01  Productos.  -  Para Concepto 02, 03 el  campo CbteFch debe  estar  comprendido  en el  rango  N-10 y N+10  siendo N la fecha CbteFchHsGen (contingencia).  &lt;Auth&gt;&lt;Cuit&gt;/  &lt;FeCabReq&gt;&lt;CbteTipo&gt;/  &lt;FECAEDetRequest&gt;&lt;DocNro&gt;/  &lt;FECAEDetRequest&gt;&lt;ImpTotal&gt; /  &lt;FECAEDetRequest&gt;&lt;MonCotiz&gt;  / Tope  1485  Según la categorización de las CUITs emisora y  receptora y el monto facturado debe realizar una  factura  de crédito electrónica MiPyMEs (FCE). Ver  micrositio.  &lt;DocTipo&gt;/  1489  Si el tipo de documento del receptor del   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo  Código de  Observ.  Validación  &lt;DocNro&gt;/  comprobante que está autorizando es CUIT (código  Tipo de Documento 80) y la CUIT se encuentra  inactiva por haber sido incluida en la consulta de  facturas apócrifas, no podrá computarse el crédito  fiscal.  &lt;FECAEADetRequest&gt;&lt;Tributos&gt;&lt;  Id&gt;/  &lt;FECAEADetRequest&gt;&lt;PeriodoAs  oc&gt;&lt;FchDesde&gt;/  &lt;FECAEADetRequest&gt;&lt;PeriodoAs  oc&gt;&lt;FchHasta&gt;  1500  Si en la estructura Tributos informa percepciones,  PeriodoAsoc.FchDesde y PeriodoAsoc.FchHasta  deben corresponder al mismo Mes/Anio  &lt;FECAEADetRequest&gt;&lt;CbteFch&gt;/  &lt;FECAEADetRequest&gt;&lt;CbtesAsoc  &gt;&lt;CbteFch&gt;  1501  Si el comprobante asociado se autorizó de forma  electrónica y tiene una fecha de emisión posterior  a la fecha de emisión del comprobante por el cual  se está solicitando la autorización, ambos deberán  ser del mismo mes/año.  &lt;CbteTipo&gt; / &lt;DocNro&gt;  1516  Para comprobantes Clase A y M, donde el receptor  del comprobante informado en &lt;DocTipo&gt; y  &lt;DocNro&gt; se encuentra activo en el Impuesto  Responsable Monotributo, 'El crédito fiscal  discriminado en el presente comprobante solo  podrá ser computado a efectos del Procedimiento  permanente de transición al Régimen General.'  &lt;CbteTipo&gt; / &lt;DocNro&gt;  814  Para comprobantes Clase A y M, se ha detectado  que esta pendiente de presentación el formulario  de habilitación de comprobantes o su fecha de  presentación es anterior a la fecha de alta en IVA.  Para el caso que el comprobante no sea una Nota  de Crédito, se debe proceder a anular la operación  clase "A" o "M" emitida, mediante una Nota de  Crédito.  &lt;CbteTipo&gt; / &lt;DocNro&gt; /  &lt;FECAEADetRequest&gt;&lt;CbteFch&gt;/  815  A la fecha de emisión del comprobante, no te  encontrabas habilitado a la emisión de  comprobantes clase "A"/"M". Tenés que proceder  a emitir la Nota de Crédito, o anular la operación,  según corresponda.  &lt;CbteTipo&gt; / &lt;DocNro&gt; /  &lt;FECAEADetRequest&gt; / ImpTotal  816  El monto total del comprobante emitido, excede el  límite establecido para la categoría máxima de  Monotributo. Por tal motivo, quedarías excluido  automáticamente teniendo que solicitar el alta de  los tributos (impositivos y de los recursos de la  seguridad social) en el régimen general de acuerdo   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo  Código de  Observ.  Validación  con tu actividad.  &lt;CbteTipo&gt; / &lt;DocNro&gt; /  &lt;FECAEADetRequest&gt; / ImpTotal  817  El monto del comprobante emitido, excede el  límite establecido para su categoría de  Monotributo. Tenelo en cuenta para la próxima  recategorización.  &lt;FECAEADetRequest&gt; /  ImpTotal / &lt;CbteAsoc&gt;  818  El importe de la nota de crédito supera el monto  del comprobante asociado que estás ajustando.  Verificá los montos ingresados y de tratarse de un  error, tenés que efectuar el ajuste o anulación de  la operación según corresponda.  &lt;FECAEADetRequest&gt; / &lt;DocNro&gt;  819  La CUIT receptora ingresada no existe.  &lt;FECAEADetRequest&gt; /  &lt;CanMisMonExt&gt;  821  Si informa el campo MonCotiz, el mismo no podrá  superar en 1 a la cotizacion oficial. Ver Método  FEParamGetCotizacion.  &lt;FECAEADetRequest&gt; /  &lt;CanMisMonExt&gt;  822  Si informa MonId = PES, el campo CanMisMonExt  no debe informarse.  &lt;FECAEADetRequest&gt; /  &lt;CondicionIVAReceptorId&gt;  824  El campo de identificación de Condición de IVA del  receptor no es valido para la clase de comprobante  informado. Para mas detalle consultar el Método:  FEParamGetCondicionIvaReceptor  &lt;FECAEADetRequest&gt; /  &lt;CondicionIVAReceptorId&gt;  825  El campo Condición Frente al IVA del receptor  resultará obligatorio conforme lo reglamentado  por la Resolución General N° 5616. Para mas  información consular método  FEParamGetCondicionIvaReceptor.   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Verificaciones que se realizan sobre el elemento &lt;CbtesAsoc&gt;

## Validaciones Excluyentes

| Campo  Código de Error  Validación  CbtesAsoc  800  Si envía CbtesAsoc, CbteAsoc es obligatorio y  no debe estar vacío.  PtoVta  802  De enviarse el tag CbtesAsoc, CbteAsoc debe  enviarse con PtoVta mayor a 0 y &lt; a 99999  Nro  803  De enviarse el tag CbtesAsoc, CbteAsoc debe   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| enviarse con Nro mayor a 0 y menor a  99999999  Tipo / PtoVta / Nro  804  Los comprobantes informados no podrán  repetirse.  Tipo  805  De enviarse el tag CbtesAsoc, CbteAsoc debe  enviarse con Tipo mayor a 0  CbteTipo / CbtesAsoc  807  CbtesAsoc es opcional, solamente podrá  informarse si CbteTipo es igual a 1, 2, 3, 6, 7,  8, 12, 13, 51, 52, 53, 201, 202, 203, 206, 207,  208, 211, 212, 213.  &lt;CbteAsoc&gt;&lt;Cuit&gt;  808  Si informa Cuit en comprobantes asociados,  no informar en blanco, el mismo debe ser un  valor de 11 caracteres numericos. Para  comprobante del tipo MiPyMEs (FCE) del tipo  débito o crédito es obligatorio informar el  campo.  CbteTipo / CbtesAsoc  812  Para comprobantes MiPyMEs (FCE) 201, 206  o 211 puede asociarse los comprobantes (91,  990, 991, 993, 994, 995).  Para comprobantes MiPyMEs (FCE) A 202 y  203, puede asociar 201,202 o 203.  Para comprobantes MiPyMEs (FCE) B 207,  208 puede asociar 206, 207, 208.  Para comprobantes MiPyMEs (FCE) C 212,  213 puede asociarse 211, 212, 213.  &lt;Opcionales&gt;&lt;Id&gt;  813  Si intenta informar datos opcionales según  Resolución General, recordar que en un  mismo comprobante solo puede informar  identificadores opcionales para solo 1  resolución por comprobante.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Validaciones NO Excluyentes

| Campo  Código de Observ.  Validación  Tipo  806  Obligatorio.  Deberá ser igual a 1, 2, 3, 04, 05, 34,  39, 60, 63, 88 o 991  si el tipo de comprobante que  se informa es igual a 2 ó 3.  Deberá ser igual a 6, 7, 8, 09, 10, 35, 40, 61, 64 ,88   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| o 991 si el tipo de comprobante que se informa es  igual a 7 ú 8.  Deberá ser igual a 11, 12, 13, 15 si el tipo de  comprobante que informa es igual a 12 o 13  Deberá ser igual a 51, 52, 53, 54  si el tipo de  comprobante que se informa es igual a 52 o 53.  Deberá ser 91, 88, 988, 990, 991, 993, 994, 995,  996, 997 si el tipo de comprobante que se informa  es 1, 6 o 51  Tipo/ PtoVta / Nro  801  Si el punto de venta del comprobante asociado  (campo PtoVta de CbtesAsoc) es electrónico, el  número de comprobante debe obrar en las bases  del organismo para el punto de venta y tipo de  comprobante informado.  &lt;CbteAsoc&gt;&lt;Tipo&gt; /  &lt;CbteAsoc&gt;&lt;PtoVta&gt; /  &lt;CbteAsoc&gt;&lt;Nro&gt;  809  Si informa comprobantes asociados, y sus códigos  son 91, 88, 988, 990, 991, 993, 994, 995, 996, 997,  los mismos deben encontrarse registrados.  &lt;CbteAsoc&gt;&lt;Tipo&gt; /  &lt;CbteAsoc&gt;&lt;PtoVta&gt; /  &lt;CbteAsoc&gt;&lt;Nro&gt;  810  Si informa comprobantes asociados, y sus códigos  son 91, 88, 988, 990, 991, 993, 994, 995, 996, 997,  los mismos deben encontrarse confirmados.  &lt;DocTipo&gt; / &lt;DocNro&gt;  &lt;CbteAsoc&gt;&lt;Cuit&gt;  811  Si informa comprobantes asociados y sus códigos  son 91, 88, 988, 990, 991, 993, 994, 995, 996, 997,  el receptor del comprobante debe ser igual al  receptor del comprobante asociado.   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Controles que se realizan sobre el elemento &lt;Tributo&gt;

## Validaciones Excluyentes

| Campo  Código de Error  Validación  Id  900  Obligatorio. Valores permitidos: consultar método  FEParamGetTiposTributos  Desc  908  Opcional.  Debe informarse si &lt;codigo&gt; es igual a 99.   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Campo  Código de Error  Validación  Importe  907  El valor informado debe ser mayor o igual a 0.  El campo Importe de Tributos soporta 13 números para  la parte entera y 2 para los decimales.  BaseImp  905  El campo BaseImp en Tributo es obligatorio, mayor o  igual 0 cero.  El campo BaseImp de Tributos soporta 13 números para  la parte entera y 2 para los decimales.  Alic  906  El campo Alic en Tributo es obligatorio, mayor o igual  0  cero.  El campo Alic de Tributos soporta 3 números para la  parte entera y 2 para los decimales.   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Controles que se realizan sobre el elemento &lt;IVA&gt;

## Validaciones Excluyentes

| Campo  Código de Error  Validación  Id  1000  Consultar el método FEParamGetTiposIva. Es opcional  para comprobantes 2, 3, 7, 8.  Id  1003  El  campo  Id en AlicIVA no debe repetirse. Deberá  totalizarse por alícuota.  Importe  1008  El  campo  Importe  en AlicIVA es obligatorio , mayor o  igual  0 cero.  El campo Importe de AlicIva soporta 13 números para la  parte entera y 2 para los decimales.  BaseImp  1009  El  campo  BaseImp  en AlicIVA es obligatorio  y debe ser  mayor a 0 cero. Excepto para comprobantes 2, 3, 7, 8  que puede ser cero o no ser informado.  El campo BaseImp de AlicIva soporta 13 números para  la parte entera y 2 para los decimales.   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Validaciones NO Excluyentes

<!-- image -->

| Campo  Código de  Observ.  Validación  Importe / AlicIva /  BaseImp  1006  Los importes informados en AlicIVA no se corresponden  con los porcentajes. Excepto para comprobantes 2, 3, 7,  8 que puede ser cero o no ser informado.  Margen de error:  Error relativo porcentual deberá ser &lt;= 0.01% o el error  absoluto &lt;=0.01   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Controles que se realizan sobre el elemento &lt;Opcionales&gt;

## Validaciones Excluyentes

| Campo  Código de Error  Validación  Id  1100  El  campo Id en Opcionales es obligatorio  y debe ser  igual a 2 (Régimen de Promoción Industrial).  Id  1101  El  campo Id en Opcionales es obligatorio  y no debe  repetirse.  Valor  1105  El  campo Valor en Opcionales es obligatorio.  &lt;Opcionales&gt;&lt;Opcional  &gt;&lt;Id&gt;&lt;Valor&gt;  1103  Si envía Opcionales, Opcional, Id y Valor son  obligatorios.  Valor  1104  Si selecciona Id = 2 el valor ingresado debe ser un  numérico de 8 (ocho) dígitos mayor o igual a 0 (cero).   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Validaciones NO Excluyentes

| Campo  Código de  Observ.  Validación  Valor  1106  Si Id = 2 y el comprobante corresponde a una actividad  alcanzada por el beneficio de Promoción Industrial en el  campo &lt;Valor&gt; se deberá informar el número   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

identificatorio del proyecto (el mismo deberá corresponder a la cuit emisora del comprobante), si no corresponde a una actividad alcanzada por el beneficio el campo &lt;Valor&gt; deberá ser 0 (cero).

## Controles que se realizan sobre el elemento &lt;Actividades&gt;

## Validaciones Excluyentes

| &lt;FeCAEARegInfReq&gt;&lt;Actividades&gt;&lt;Actividad&gt;  16000  Si envía estructura de Actividades,  Actividad es obligatorio enviarlo.  &lt;FeCAEARegInfReq&gt;&lt;Actividades&gt;&lt;Actividad&gt;&lt;Id&gt;  16001  Si envía estructura de Actividades,  Actividad es obligatorio enviarlo y no  debe estar vacío.  &lt;FeCAEARegInfReq&gt;&lt;Actividades&gt;&lt;Actividad&gt;&lt;Id&gt;  16002  El identificador de actividad  informado tiene que ser una de las  actividades habilitadas. Consultar  método FEParamGetActividades.  &lt;FeCAEARegInfReq&gt;&lt;Actividades&gt;&lt;Actividad&gt;&lt;Id&gt;  16003  De enviarse el tag Actividades, las  actividades no deben repetirse.  &lt;FeCAEARegInfReq&gt;&lt;Actividades&gt;&lt;Actividad&gt;&lt;Id&gt;  16004  De enviarse actividades, las mismas  no deben corresponder a distintos  grupos según RG. Es decir, si informa  actividades Cárnicas, no pueden estar  combinadas con actividades  Harineras, de Tabaco, etc.  &lt;FeCAEARegInfReq&gt;&lt;Actividades&gt;&lt;Actividad&gt;&lt;Id&gt;  16005  De enviarse actividades, las mismas  deben encontrarse activas para el  emisor del comprobante. Ver método  FEParamGetActividades.  &lt;FeCAEARegInfReq&gt;&lt;Actividades&gt;&lt;Actividad&gt;&lt;Id&gt; /  &lt;Concepto&gt;  16006  De enviarse actividades  pertenecientes al grupo de  actividades Cárnicas, las mismas  deben enviarse con comprobantes  con Concepto del tipo Producto o  Productos y Servicios.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

## Controles que se realizan sobre el elemento &lt;Actividades&gt; y &lt;CbtesAsoc&gt; Validaciones Excluyentes

| &lt;FeCAEARegInfReq&gt;&lt;Actividades&gt;&lt;Actividad&gt;&lt;Id&gt;  /&lt;CbtesAsoc&gt;&lt;CbteAsoc&gt;&lt;Tipo&gt;  16007  Si las actividades informadas  corresponden a actividades Cárnicas,  informar remito asociado 995 -  Remito Electrónico Cárnico.  &lt;FeCAEARegInfReq&gt;&lt;Actividades&gt;&lt;Actividad&gt;&lt;Id&gt;  /&lt;CbtesAsoc&gt;&lt;CbteAsoc&gt;&lt;Tipo&gt;  16008  Si las actividades informadas  corresponden a actividades Harinas,  informar remito asociado 993 -  Remito Electrónico Harinero -  Automotor o  994 - Remito Electrónico Harinero -  Ferroviario.  &lt;FeCAEARegInfReq&gt;&lt;Actividades&gt;&lt;Actividad&gt;&lt;Id&gt;  /&lt;CbtesAsoc&gt;&lt;CbteAsoc&gt;&lt;Tipo&gt;  16009  Si las actividades informadas  corresponden a actividades Tabaco  en Hebras, informar remito asociado  88 - Remito Electrónico de Tabaco  Acondicionado.  &lt;FeCAEARegInfReq&gt;&lt;Actividades&gt;&lt;Actividad&gt;&lt;Id&gt;  /&lt;CbtesAsoc&gt;&lt;CbteAsoc&gt;&lt;Tipo&gt;  16010  Si informa remito 995 - Remito  Electrónico Cárnico, es obligatorio  informar una actividad Cárnica.  &lt;FeCAEARegInfReq&gt;&lt;Actividades&gt;&lt;Actividad&gt;&lt;Id&gt;  /&lt;CbtesAsoc&gt;&lt;CbteAsoc&gt;&lt;Tipo&gt;  16011  Si informa remito 993 - Remito  Electrónico Harinero - Automotor o  994 - Remito Electrónico Harinero -  Ferroviario, es obligatgorio informar  una actividad Harinera.  &lt;FeCAEARegInfReq&gt;&lt;Actividades&gt;&lt;Actividad&gt;&lt;Id&gt;  /&lt;CbtesAsoc&gt;&lt;CbteAsoc&gt;&lt;Tipo&gt;  16012  Si informa remito 88 - Remito  Electrónico de Tabaco  Acondicionado., es obligatorio  informar una actividad  correspondiente a Tabaco  Acondicionado.  &lt;FeCAEARegInfReq&gt;&lt;Actividades&gt;&lt;Actividad&gt;&lt;Id&gt;  /&lt;CbtesAsoc&gt;&lt;CbteAsoc  16013  Si informa actividades indicadas en  la RG, es obligatorio informar  comprobantes asociados.  &lt;CbteAsoc&gt;&lt;Tipo&gt; / &lt;CbteAsoc&gt;&lt;PtoVta&gt; /  &lt;CbteAsoc&gt;&lt;Nro&gt;  16014  Si informa comprobantes asociados,  y sus códigos corresponden a 91, 88,  988, 990, 991, 993, 994, 995, 996,  997, los mismos no deben  encontrarse asociado a otro  comprobante.   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Operatoria ante errores

Metodología sugerida ante el rechazo de un requerimiento con múltiples comprobantes:

Suponiendo  que se envían 100 comprobantes en un request y  el  mismo  es de Facturas A, punto  de venta 1 y los comprobantes son desde el número  51 al  150, se nos plantean 3 situaciones.

-  Aceptación total: donde, cada uno de  los 100  comprobantes fue aprobado. El campo Resultado será igual A
-  Rechazo  total: se puede dar por  dos grandes causas, una por problemas del emisor y/o inconsistencia en la cabecera, y otra por el  rechazo  de cada uno de los 100 comprobantes. En el primer caso el response contendrá solamente en  el  tag Errors con todas las causas involucradas; en el  segundo  caso se incluirá el tag FeCabResp, FeDetResp y Observaciones o Errors con el  motivo de rechazo de cada uno de los comprobantes.  El campo Resultado será igual a R.
-  Rechazo parcial: se da cuando alguno de los comprobantes incluidos en el  request es rechazado. A modo  de ejemplo y con los parámetros antes descriptos,  se aprueban los comprobantes del  51 al 100, 101 saldrá rechazado y del 102 al  150 saldrá como no procesado; esto se debe a que como debe existir correlatividad numérica y de fecha, ante una inconsistencia los comprobantes subsiguientes también se rechazaran. Si se diese este caso, y para proseguir con la autorización de comprobantes se deberá subsanar los errores del comprobante 102 y así  enviar un nuevo  request. El campo Resultado será igual a P.

Operatoria con errores de comunicación:

En el diseño del WsfeV1 se ha previsto que dada la complejidad actual de las comunicacionespueden ocurrir interrupciones en la comunicación entre el cliente y el WsfeV1 básicamente, el problema podría resumirse al siguiente escenario: el cliente envía una solicitud de informar comprobantes con CAEA y se queda esperando una respuesta que no llega, hasta que transcurrido algún tiempo, se produce una condición de time-out.

<!-- image -->

<!-- image -->

En ese caso, el usuario no sabrá si la solicitud le llegó al WsfeV1 y fue procesado fallando la comunicación durante el retorno, o bien si la falla ocurrió durante el envío de la solicitud y simplemente WsfeV1 nunca la recibió.

En el segundo caso, con simplemente enviar la misma solicitud todo quedaría resuelto, pero en el primer caso, si el cliente envía nuevamente la misma solicitud para la/s misma/s factura, WsfeV1 devolvería un error de consecutividad puesto que en la base de datos de arca ese comprobante ya figura como emitido.

Para estos casos, se utiliza el  método FECompConsultar, que dado  el tipo de comprobante, punto  de venta y numero  de comprobante, retorna toda la información enviada en  el método  de registración de comprobantes con CAEA  (FECAEARegInformativo)  más  el resultado (A: Aprobado), tipo de emisión  (en este caso CAEA), fecha de vencimiento, fecha de proceso y de corresponder las observaciones realizadas al comprobante.

El WsfeV1 también ofrece un método para consultar el  último comprobante autorizado (FECompUltimoAutorizado) para un determinado tipo de comprobante y punto de venta.

## Operatoria ante errores, Ejemplos

Se envía un request informando una Factura A.   La totalidad del comprobante es No Gravado. Sin errores.

## REQUEST

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECAEARegInformativo> <ar:Auth> <ar:Token>PD…</ar:Token> <ar:Sign>IT…</ar:Sign> <ar:Cuit>23000000004</ar:Cuit> </ar:Auth> <ar:FeCAEARegInfReq> <ar:FeCabReq> <ar:CantReg>1</ar:CantReg> <ar:PtoVta>9800</ar:PtoVta> <ar:CbteTipo>1</ar:CbteTipo> </ar:FeCabReq> <ar:FeDetReq> <ar:FECAEADetRequest> <ar:Concepto>1</ar:Concepto> <ar:DocTipo>80</ar:DocTipo> <ar:DocNro>30000000007</ar:DocNro> <ar:CbteDesde>33</ar:CbteDesde> <ar:CbteHasta>33</ar:CbteHasta> <ar:CbteFch>20110211</ar:CbteFch>
```

<!-- image -->

```
<ar:ImpTotal>100.00</ar:ImpTotal> <ar:ImpTotConc>100.00</ar:ImpTotConc> <ar:ImpNeto>0</ar:ImpNeto> <ar:ImpOpEx>0.00</ar:ImpOpEx> <ar:ImpIva>0</ar:ImpIva> <ar:ImpTrib>0</ar:ImpTrib> <ar:MonId>PES</ar:MonId> <ar:MonCotiz>1</ar:MonCotiz> <ar:CondicionIVAReceptorId>1</ar:CondicionIVAReceptorId> <ar:CAEA>21064126523746</ar:CAEA> </ar:FECAEADetRequest> </ar:FeDetReq> </ar:FeCAEARegInfReq> </ar:FECAEARegInformativo> </soapenv:Body> </soapenv:Envelope>
```

## RESPONSE

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"> <soap:Body> <FECAEARegInformativoResponse xmlns="http://ar.gov.afip.dif.FEV1/"> <FECAEARegInformativoResult> <FeCabResp> <Cuit>23000000004</Cuit> <PtoVta>9800</PtoVta> <CbteTipo>1</CbteTipo> <FchProceso>20110306</FchProceso> <CantReg>1</CantReg> <Resultado>A</Resultado> <Reproceso>N</Reproceso> </FeCabResp> <FeDetResp> <FECAEADetResponse> <Concepto>1</Concepto> <DocTipo>80</DocTipo> <DocNro>30000000007</DocNro> <CbteDesde>33</CbteDesde> <CbteHasta>33</CbteHasta> <CbteFch>20110211</CbteFch> <Resultado>A</Resultado> <CAEA>21064126523746</CAEA> </FECAEADetResponse> </FeDetResp> </FECAEARegInformativoResult> </FECAEARegInformativoResponse> </soap:Body> </soap:Envelope>
```

Informa una Factura A.   La totalidad del comprobante es No Gravado, donde no se supera la totalidad de las validaciones de la CUIT emisora.

## REQUEST

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECAEARegInformativo> <ar:Auth> <ar:Token>PD…</ar:Token> <ar:Sign>IT…</ar:Sign> <ar:Cuit>23000000000</ar:Cuit> CUIT no supera las validaciones del ticket de acceso </ar:Auth> <ar:FeCAEARegInfReq> <ar:FeCabReq> <ar:CantReg>1</ar:CantReg> <ar:PtoVta>9800</ar:PtoVta> <ar:CbteTipo>1</ar:CbteTipo> </ar:FeCabReq> <ar:FeDetReq> <ar:FECAEADetRequest> <ar:Concepto>1</ar:Concepto> <ar:DocTipo>80</ar:DocTipo> <ar:DocNro>30000000007</ar:DocNro> <ar:CbteDesde>34</ar:CbteDesde> <ar:CbteHasta>34</ar:CbteHasta> <ar:CbteFch>20110211</ar:CbteFch> <ar:ImpTotal>100.00</ar:ImpTotal> <ar:ImpTotConc>100.00</ar:ImpTotConc> <ar:ImpNeto>0</ar:ImpNeto> <ar:ImpOpEx>0.00</ar:ImpOpEx> <ar:ImpIva>0</ar:ImpIva> <ar:ImpTrib>0</ar:ImpTrib> <ar:MonId>PES</ar:MonId> <ar:MonCotiz>1</ar:MonCotiz> <ar:CondicionIVAReceptorId>1</ar:CondicionIVAReceptorId> <ar:CAEA>21064126523746</ar:CAEA> </ar:FECAEADetRequest> </ar:FeDetReq> </ar:FeCAEARegInfReq> </ar:FECAEARegInformativo> </soapenv:Body> </soapenv:Envelope>
```

## RESPONSE

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"> <soap:Body> <FECAEARegInformativoResponse xmlns="http://ar.gov.afip.dif.FEV1/"> <FECAEARegInformativoResult> <Errors>  ERROR <Err> <Code>600</Code>
```

<!-- image -->

<!-- image -->

```
<Msg>ValidacionDeToken: No apareció CUIT en lista de relaciones: 23000000000</Msg> </Err> </Errors> </FECAEARegInformativoResult> </FECAEARegInformativoResponse> </soap:Body> </soap:Envelope>
```

Informa una Factura A, con error en la cabecera (FeCabReq) del comprobante, tipo de comprobante inválido.  Genera un Rechazo del comprobante.

## REQUEST

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECAEARegInformativo> <ar:Auth> <ar:Token>PD..</ar:Token> <ar:Sign>IT…</ar:Sign> <ar:Cuit>23000000004</ar:Cuit> </ar:Auth> <ar:FeCAEARegInfReq> <ar:FeCabReq> <ar:CantReg>1</ar:CantReg> <ar:PtoVta>9800</ar:PtoVta> <ar:CbteTipo>0</ar:CbteTipo>  Tipo de Comprobante Inválido </ar:FeCabReq> <ar:FeDetReq> <ar:FECAEADetRequest> <ar:Concepto>1</ar:Concepto> <ar:DocTipo>80</ar:DocTipo> <ar:DocNro>30000000007</ar:DocNro> <ar:CbteDesde>34</ar:CbteDesde> <ar:CbteHasta>34</ar:CbteHasta> <ar:CbteFch>20110211</ar:CbteFch> <ar:ImpTotal>100.00</ar:ImpTotal> <ar:ImpTotConc>100.00</ar:ImpTotConc> <ar:ImpNeto>0</ar:ImpNeto> <ar:ImpOpEx>0.00</ar:ImpOpEx> <ar:ImpIva>0</ar:ImpIva> <ar:ImpTrib>0</ar:ImpTrib> <ar:MonId>PES</ar:MonId> <ar:MonCotiz>1</ar:MonCotiz> <ar:CondicionIVAReceptorId>1</ar:CondicionIVAReceptorId> <ar:CAEA>21064126523746</ar:CAEA> </ar:FECAEADetRequest> </ar:FeDetReq> </ar:FeCAEARegInfReq>
```

```
</ar:FECAEARegInformativo>
```

```
</soapenv:Body> </soapenv:Envelope>
```

## RESPONSE

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"> <soap:Body> <FECAEARegInformativoResponse xmlns="http://ar.gov.afip.dif.FEV1/"> <FECAEARegInformativoResult> <FeCabResp> <Cuit>23000000004</Cuit> <PtoVta>9800</PtoVta> <CbteTipo>0</CbteTipo> <FchProceso>20110306</FchProceso> <CantReg>1</CantReg> <Resultado>R</Resultado>  Rechazo <Reproceso>N</Reproceso> </FeCabResp> <FeDetResp> <FECAEADetResponse> <Concepto>1</Concepto> <DocTipo>80</DocTipo> <DocNro>30000000007</DocNro> <CbteDesde>34</CbteDesde> <CbteHasta>34</CbteHasta> <CbteFch>20110211</CbteFch> <Resultado>R</Resultado> <CAEA>21064126523746</CAEA> </FECAEADetResponse> </FeDetResp> <Errors>  Detalle del error <Err> <Code>700</Code> <Msg>Campo CbteTipo no se corresponde con alguno de los habilitados 1, 2 ,3, 6, 7 u 8.</Msg> </Err> </Errors> </FECAEARegInformativoResult> </FECAEARegInformativoResponse> </soap:Body> </soap:Envelope>
```

Informa una Factura A, con error en el detalle (FeDetReq) del comprobante tipo de concepto inválido.  Genera un Rechazo del comprobante

## REQUEST

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECAEARegInformativo>
```

<!-- image -->

<!-- image -->

```
<ar:Auth> <ar:Token>PD..</ar:Token> <ar:Sign>IT…</ar:Sign> <ar:Cuit>23000000004</ar:Cuit> </ar:Auth> <ar:FeCAEARegInfReq> <ar:FeCabReq> <ar:CantReg>1</ar:CantReg> <ar:PtoVta>9800</ar:PtoVta> <ar:CbteTipo>1</ar:CbteTipo> </ar:FeCabReq> <ar:FeDetReq> <ar:FECAEADetRequest> <ar:Concepto>4</ar:Concepto>  4 valor no permitido <ar:DocTipo>80</ar:DocTipo> <ar:DocNro>30000000007</ar:DocNro> <ar:CbteDesde>34</ar:CbteDesde> <ar:CbteHasta>34</ar:CbteHasta> <ar:CbteFch>20110211</ar:CbteFch> <ar:ImpTotal>100.00</ar:ImpTotal> <ar:ImpTotConc>100.00</ar:ImpTotConc> <ar:ImpNeto>0</ar:ImpNeto> <ar:ImpOpEx>0.00</ar:ImpOpEx> <ar:ImpIva>0</ar:ImpIva> <ar:ImpTrib>0</ar:ImpTrib> <ar:MonId>PES</ar:MonId> <ar:MonCotiz>1</ar:MonCotiz> <ar:CondicionIVAReceptorId>1</ar:CondicionIVAReceptorId> <ar:CAEA>21064126523746</ar:CAEA> </ar:FECAEADetRequest> </ar:FeDetReq> </ar:FeCAEARegInfReq> </ar:FECAEARegInformativo> </soapenv:Body> </soapenv:Envelope>
```

## RESPONSE

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"> <soap:Body> <FECAEARegInformativoResponse xmlns="http://ar.gov.afip.dif.FEV1/"> <FECAEARegInformativoResult> <FeCabResp> <Cuit>23000000004</Cuit> <PtoVta>9800</PtoVta> <CbteTipo>1</CbteTipo> <FchProceso>20110306</FchProceso> <CantReg>1</CantReg> <Resultado>R</Resultado>  Rechazo <Reproceso>N</Reproceso> </FeCabResp> <FeDetResp>
```

<!-- image -->

```
<FECAEADetResponse> <Concepto>4</Concepto> <DocTipo>80</DocTipo> <DocNro>30000000007</DocNro> <CbteDesde>34</CbteDesde> <CbteHasta>34</CbteHasta> <CbteFch>20110211</CbteFch> <Resultado>R</Resultado> <Observaciones>  Detalle de la causa del rechazo <Obs> <Code>713</Code> <Msg>El campo  Concepto  es obligatorio  y debe  corresponder con algún valor devuelto  por  el  método FEParamGetTiposConcepto</Msg> </Obs> </Observaciones> <CAEA>21064126523746</CAEA> </FECAEADetResponse> </FeDetResp> </FECAEARegInformativoResult> </FECAEARegInformativoResponse> </soap:Body> </soap:Envelope>
```

Informa una Factura A, con error en el detalle del comprobante (FeDetReq) que no supera alguna de las validaciones No Excluyentes.  Genera una Aprobación del comprobante con Observaciones.

## REQUEST

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECAEARegInformativo> <ar:Auth> <ar:Token>PD..</ar:Token> <ar:Sign>IT…</ar:Sign> <ar:Cuit>23000000004</ar:Cuit> </ar:Auth> <ar:FeCAEARegInfReq> <ar:FeCabReq> <ar:CantReg>1</ar:CantReg> <ar:PtoVta>9800</ar:PtoVta> <ar:CbteTipo>1</ar:CbteTipo> </ar:FeCabReq> <ar:FeDetReq> <ar:FECAEADetRequest> <ar:Concepto>1</ar:Concepto> <ar:DocTipo>80</ar:DocTipo> <ar:DocNro>30000000007</ar:DocNro> <ar:CbteDesde>34</ar:CbteDesde> <ar:CbteHasta>34</ar:CbteHasta> <ar:CbteFch>20110211</ar:CbteFch> <ar:ImpTotal>101.00</ar:ImpTotal>  Importe total incorrecto
```

<!-- image -->

```
<ar:ImpTotConc>100.00</ar:ImpTotConc> <ar:ImpNeto>0</ar:ImpNeto> <ar:ImpOpEx>0.00</ar:ImpOpEx> <ar:ImpIva>0</ar:ImpIva> <ar:ImpTrib>0</ar:ImpTrib> <ar:MonId>PES</ar:MonId> <ar:MonCotiz>1</ar:MonCotiz> <ar:CondicionIVAReceptorId>1</ar:CondicionIVAReceptorId> <ar:CAEA>21064126523746</ar:CAEA> </ar:FECAEADetRequest> </ar:FeDetReq> </ar:FeCAEARegInfReq> </ar:FECAEARegInformativo> </soapenv:Body> </soapenv:Envelope>
```

## RESPONSE

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"> <soap:Body> <FECAEARegInformativoResponse xmlns="http://ar.gov.afip.dif.FEV1/"> <FECAEARegInformativoResult> <FeCabResp> <Cuit>23000000004</Cuit> <PtoVta>9800</PtoVta> <CbteTipo>1</CbteTipo> <FchProceso>20110306</FchProceso> <CantReg>1</CantReg> <Resultado>A</Resultado>  Aprobado <Reproceso>N</Reproceso> </FeCabResp> <FeDetResp> <FECAEADetResponse> <Concepto>1</Concepto> <DocTipo>80</DocTipo> <DocNro>30000000007</DocNro> <CbteDesde>34</CbteDesde> <CbteHasta>34</CbteHasta> <CbteFch>20110211</CbteFch> <Resultado>A</Resultado> <Observaciones>  Con Observaciones <Obs> <Code>724</Code> <Msg>El campo  'Importe Total' ImpTotal, debe ser igual  a la  suma de ImpTotConc + ImpNeto + ImpOpEx + ImpTrib + ImpIVA.</Msg> </Obs> </Observaciones> <CAEA>21064126523746</CAEA> </FECAEADetResponse> </FeDetResp> </FECAEARegInformativoResult> </FECAEARegInformativoResponse> </soap:Body>
```

<!-- image -->

Se envía un Request con tres Facturas A, que superan la totalidad de las validaciones. Genera una aprobación total de la solicitud.

## REQUEST

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECAEARegInformativo> <ar:Auth> <ar:Token>PD…</ar:Token> <ar:Sign>jd..</ar:Sign> <ar:Cuit>23000000004</ar:Cuit> </ar:Auth> <ar:FeCAEARegInfReq> <ar:FeCabReq> <ar:CantReg>3</ar:CantReg> <ar:PtoVta>9800</ar:PtoVta> <ar:CbteTipo>1</ar:CbteTipo> </ar:FeCabReq> <ar:FeDetReq> <ar:FECAEADetRequest> <ar:Concepto>1</ar:Concepto> <ar:DocTipo>80</ar:DocTipo> <ar:DocNro>30000000007</ar:DocNro> <ar:CbteDesde>35</ar:CbteDesde> <ar:CbteHasta>35</ar:CbteHasta> <ar:CbteFch>20110211</ar:CbteFch> <ar:ImpTotal>200.00</ar:ImpTotal> <ar:ImpTotConc>100.00</ar:ImpTotConc> <ar:ImpNeto>0</ar:ImpNeto> <ar:ImpOpEx>100.00</ar:ImpOpEx> <ar:ImpIva>0</ar:ImpIva> <ar:ImpTrib>0</ar:ImpTrib> <ar:MonId>PES</ar:MonId> <ar:MonCotiz>1</ar:MonCotiz> <ar:CondicionIVAReceptorId>1</ar:CondicionIVAReceptorId> <ar:CAEA>21064126523746</ar:CAEA> </ar:FECAEADetRequest> <ar:FECAEADetRequest> <ar:Concepto>1</ar:Concepto> <ar:DocTipo>80</ar:DocTipo> <ar:DocNro>30000000007</ar:DocNro> <ar:CbteDesde>36</ar:CbteDesde> <ar:CbteHasta>36</ar:CbteHasta> <ar:CbteFch>20110211</ar:CbteFch> <ar:ImpTotal>101.00</ar:ImpTotal> <ar:ImpTotConc>100.00</ar:ImpTotConc> <ar:ImpNeto>0</ar:ImpNeto> <ar:ImpOpEx>0.00</ar:ImpOpEx> <ar:ImpIva>0</ar:ImpIva>
```

```
<ar:ImpTrib>1</ar:ImpTrib> <ar:MonId>PES</ar:MonId> <ar:MonCotiz>1</ar:MonCotiz> <ar:Tributos> <ar:Tributo> <ar:Id>99</ar:Id> <ar:Desc>Otro tributo</ar:Desc> <ar:BaseImp>100</ar:BaseImp> <ar:Alic>1</ar:Alic> <ar:Importe>1</ar:Importe> </ar:Tributo> </ar:Tributos> <ar:CAEA>21064126523746</ar:CAEA> </ar:FECAEADetRequest> <ar:FECAEADetRequest> <ar:Concepto>1</ar:Concepto> <ar:DocTipo>80</ar:DocTipo> <ar:DocNro>30000000007</ar:DocNro> <ar:CbteDesde>37</ar:CbteDesde> <ar:CbteHasta>37</ar:CbteHasta> <ar:CbteFch>20110211</ar:CbteFch> <ar:ImpTotal>100.00</ar:ImpTotal> <ar:ImpTotConc>0.00</ar:ImpTotConc> <ar:ImpNeto>0</ar:ImpNeto> <ar:ImpOpEx>100.00</ar:ImpOpEx> <ar:ImpIva>0</ar:ImpIva> <ar:ImpTrib>0</ar:ImpTrib> <ar:MonId>PES</ar:MonId> <ar:MonCotiz>1</ar:MonCotiz> <ar:CAEA>21064126523746</ar:CAEA> </ar:FECAEADetRequest> </ar:FeDetReq> </ar:FeCAEARegInfReq> </ar:FECAEARegInformativo> </soapenv:Body> </soapenv:Envelope>
```

## RESPONSE

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"> <soap:Body> <FECAEARegInformativoResponse xmlns="http://ar.gov.afip.dif.FEV1/"> <FECAEARegInformativoResult> <FeCabResp> <Cuit>23000000004</Cuit> <PtoVta>9800</PtoVta> <CbteTipo>1</CbteTipo> <FchProceso>20110308</FchProceso> <CantReg>3</CantReg> <Resultado>A</Resultado>  Aprobación total del envío <Reproceso>N</Reproceso> </FeCabResp>
```

<!-- image -->

<!-- image -->

```
<FeDetResp> <FECAEADetResponse> <Concepto>1</Concepto> <DocTipo>80</DocTipo> <DocNro>30000000007</DocNro> <CbteDesde>35</CbteDesde> <CbteHasta>35</CbteHasta> <CbteFch>20110211</CbteFch> <Resultado>A</Resultado>  Aprobación del comprob. <CAEA>21064126523746</CAEA> </FECAEADetResponse> <FECAEADetResponse> <Concepto>1</Concepto> <DocTipo>80</DocTipo> <DocNro>30000000007</DocNro> <CbteDesde>36</CbteDesde> <CbteHasta>36</CbteHasta> <CbteFch>20110211</CbteFch> <Resultado>A</Resultado>  Aprobación del comprob. <CAEA>21064126523746</CAEA> </FECAEADetResponse> <FECAEADetResponse> <Concepto>1</Concepto> <DocTipo>80</DocTipo> <DocNro>30000000007</DocNro> <CbteDesde>36</CbteDesde> <CbteHasta>36</CbteHasta> <CbteFch>20110211</CbteFch> <Resultado>A</Resultado>  Aprobación del comprob. <CAEA>21064126523746</CAEA> </FECAEADetResponse> </FeDetResp> </FECAEARegInformativoResult> </FECAEARegInformativoResponse> </soap:Body> </soap:Envelope>
```

Se envía un Request con tres Facturas A (número 38, 39 y 40), donde la número  38 supera todas las validaciones excluyentes y la número 39 no supera una de las validaciones excluyentes. Genera una aprobación parcial de la solicitud, el comprobante 38 es aprobado, el 39 rechazado y el 40 no es procesado generando su rechazo.

## REQUEST

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECAEARegInformativo> <ar:Auth> <ar:Token>PD…</ar:Token> <ar:Sign>jd..</ar:Sign> <ar:Cuit>23000000004</ar:Cuit> </ar:Auth>
```

<!-- image -->

```
<ar:FeCAEARegInfReq> <ar:FeCabReq> <ar:CantReg>3</ar:CantReg> <ar:PtoVta>9800</ar:PtoVta> <ar:CbteTipo>1</ar:CbteTipo> </ar:FeCabReq> <ar:FeDetReq> <ar:FECAEADetRequest> <ar:Concepto>1</ar:Concepto> <ar:DocTipo>80</ar:DocTipo> <ar:DocNro>30000000007</ar:DocNro> <ar:CbteDesde>38</ar:CbteDesde> <ar:CbteHasta>38</ar:CbteHasta> <ar:CbteFch>20110211</ar:CbteFch> <ar:ImpTotal>200.00</ar:ImpTotal> <ar:ImpTotConc>100.00</ar:ImpTotConc> <ar:ImpNeto>0</ar:ImpNeto> <ar:ImpOpEx>100.00</ar:ImpOpEx> <ar:ImpIva>0</ar:ImpIva> <ar:ImpTrib>0</ar:ImpTrib> <ar:MonId>PES</ar:MonId> <ar:MonCotiz>1</ar:MonCotiz> <ar:CondicionIVAReceptorId>1</ar:CondicionIVAReceptorId> <ar:CAEA>21064126523746</ar:CAEA> </ar:FECAEADetRequest> <ar:FECAEADetRequest> <ar:Concepto>1</ar:Concepto> <ar:DocTipo>80</ar:DocTipo> <ar:DocNro>30000000007</ar:DocNro> <ar:CbteDesde>39</ar:CbteDesde> <ar:CbteHasta>39</ar:CbteHasta> <ar:CbteFch>20110211</ar:CbteFch> <ar:ImpTotal>101.00</ar:ImpTotal> <ar:ImpTotConc>100.00</ar:ImpTotConc> <ar:ImpNeto>0</ar:ImpNeto> <ar:ImpOpEx>0.00</ar:ImpOpEx> <ar:ImpIva>0</ar:ImpIva> <ar:ImpTrib>1</ar:ImpTrib>  Se informa ImpTrib mayor a cero y no se informa el detalle <Tributos> <ar:MonId>PES</ar:MonId> <ar:MonCotiz>1</ar:MonCotiz> <ar:CondicionIVAReceptorId>1</ar:CondicionIVAReceptorId> <ar:CAEA>21064126523746</ar:CAEA> </ar:FECAEADetRequest> <ar:FECAEADetRequest> <ar:Concepto>1</ar:Concepto> <ar:DocTipo>80</ar:DocTipo> <ar:DocNro>30000000007</ar:DocNro> <ar:CbteDesde>40</ar:CbteDesde> <ar:CbteHasta>40</ar:CbteHasta> <ar:CbteFch>20110211</ar:CbteFch> <ar:ImpTotal>100.00</ar:ImpTotal> <ar:ImpTotConc>0.00</ar:ImpTotConc> <ar:ImpNeto>0</ar:ImpNeto> <ar:ImpOpEx>100.00</ar:ImpOpEx> <ar:ImpIva>0</ar:ImpIva>
```

<!-- image -->

```
<ar:ImpTrib>0</ar:ImpTrib> <ar:MonId>PES</ar:MonId> <ar:MonCotiz>1</ar:MonCotiz> <ar:CondicionIVAReceptorId>1</ar:CondicionIVAReceptorId> <ar:CAEA>21064126523746</ar:CAEA> </ar:FECAEADetRequest> </ar:FeDetReq> </ar:FeCAEARegInfReq> </ar:FECAEARegInformativo> </soapenv:Body> </soapenv:Envelope>
```

## RESPONSE

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"> <soap:Body> <FECAEARegInformativoResponse xmlns="http://ar.gov.afip.dif.FEV1/"> <FECAEARegInformativoResult> <FeCabResp> <Cuit>23000000004</Cuit> <PtoVta>9800</PtoVta> <CbteTipo>1</CbteTipo> <FchProceso>20110308</FchProceso> <CantReg>3</CantReg> <Resultado>P</Resultado>  Aprobación Parcial de la solicitud <Reproceso>N</Reproceso> </FeCabResp> <FeDetResp> <FECAEADetResponse> <Concepto>1</Concepto> <DocTipo>80</DocTipo> <DocNro>30000000007</DocNro> <CbteDesde>38</CbteDesde> <CbteHasta>38</CbteHasta> <CbteFch>20110211</CbteFch> <Resultado>A</Resultado>  Aprobación del Comprobante <CAEA>21064126523746</CAEA> </FECAEADetResponse> <FECAEADetResponse> <Concepto>1</Concepto> <DocTipo>80</DocTipo> <DocNro>30000000007</DocNro> <CbteDesde>39</CbteDesde> <CbteHasta>39</CbteHasta> <CbteFch>20110211</CbteFch> <Resultado>R</Resultado>  Rechazo del Comprobante <Observaciones>  Motivo del rechazo <Obs> <Code>900</Code>
```

<!-- image -->

```
<Msg>Si ImpTrib es mayor a 0 el objeto Tributos y Tributo son obligatorios.</Msg> </Obs> </Observaciones> <CAEA>21064126523746</CAEA> </FECAEADetResponse> <FECAEADetResponse> <Concepto>1</Concepto> <DocTipo>80</DocTipo> <DocNro>30000000007</DocNro> <CbteDesde>40</CbteDesde> <CbteHasta>40</CbteHasta> <CbteFch>20110211</CbteFch> <Resultado>R</Resultado>  Rechazo del comprobante no fue procesado por haber sido rechazado el comprobante anterior Comprobante. No prosedadote <CAEA>21064126523746</CAEA> </FECAEADetResponse> </FeDetResp> </FECAEARegInformativoResult> </FECAEARegInformativoResponse> </soap:Body> </soap:Envelope>
```

Se envía un Request con tres Facturas A (número 39, 40 y 41), donde la información enviada en la cabecera del comprobante tiene alguna inconsistencia (se informa que el Request contiene dos comprobantes y se envían tres) entonces se genera un rechazo total de la solicitud.

## REQUEST

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECAEARegInformativo> <ar:Auth> <ar:Token>PD…</ar:Token> <ar:Sign>jd..</ar:Sign> <ar:Cuit>23000000004</ar:Cuit> </ar:Auth> <ar:FeCAEARegInfReq> <ar:FeCabReq> <ar:CantReg>2</ar:CantReg> <ar:PtoVta>9800</ar:PtoVta> <ar:CbteTipo>1</ar:CbteTipo> </ar:FeCabReq> <ar:FeDetReq> <ar:FECAEADetRequest> <ar:Concepto>1</ar:Concepto> <ar:DocTipo>80</ar:DocTipo> <ar:DocNro>30000000007</ar:DocNro> <ar:CbteDesde>39</ar:CbteDesde> <ar:CbteHasta>39</ar:CbteHasta>
```

<!-- image -->

```
<ar:CbteFch>20110211</ar:CbteFch> <ar:ImpTotal>200.00</ar:ImpTotal> <ar:ImpTotConc>100.00</ar:ImpTotConc> <ar:ImpNeto>0</ar:ImpNeto> <ar:ImpOpEx>100.00</ar:ImpOpEx> <ar:ImpIva>0</ar:ImpIva> <ar:ImpTrib>0</ar:ImpTrib> <ar:MonId>PES</ar:MonId> <ar:MonCotiz>1</ar:MonCotiz> <ar:CondicionIVAReceptorId>1</ar:CondicionIVAReceptorId> <ar:CAEA>21064126523746</ar:CAEA> </ar:FECAEADetRequest> <ar:FECAEADetRequest> <ar:Concepto>1</ar:Concepto> <ar:DocTipo>80</ar:DocTipo> <ar:DocNro>30000000007</ar:DocNro> <ar:CbteDesde>40</ar:CbteDesde> <ar:CbteHasta>40</ar:CbteHasta> <ar:CbteFch>20110211</ar:CbteFch> <ar:ImpTotal>100.00</ar:ImpTotal> <ar:ImpTotConc>100.00</ar:ImpTotConc> <ar:ImpNeto>0</ar:ImpNeto> <ar:ImpOpEx>0.00</ar:ImpOpEx> <ar:ImpIva>0</ar:ImpIva> <ar:ImpTrib>0</ar:ImpTrib> <ar:MonId>PES</ar:MonId> <ar:MonCotiz>1</ar:MonCotiz> <ar:CondicionIVAReceptorId>1</ar:CondicionIVAReceptorId> <ar:CAEA>21064126523746</ar:CAEA> </ar:FECAEADetRequest> <ar:FECAEADetRequest> <ar:Concepto>1</ar:Concepto> <ar:DocTipo>80</ar:DocTipo> <ar:DocNro>30000000007</ar:DocNro> <ar:CbteDesde>41</ar:CbteDesde> <ar:CbteHasta>41</ar:CbteHasta> <ar:CbteFch>20110211</ar:CbteFch> <ar:ImpTotal>100.00</ar:ImpTotal> <ar:ImpTotConc>0.00</ar:ImpTotConc> <ar:ImpNeto>0</ar:ImpNeto> <ar:ImpOpEx>100.00</ar:ImpOpEx> <ar:ImpIva>0</ar:ImpIva> <ar:ImpTrib>0</ar:ImpTrib> <ar:MonId>PES</ar:MonId> <ar:MonCotiz>1</ar:MonCotiz> <ar:CondicionIVAReceptorId>1</ar:CondicionIVAReceptorId> <ar:CAEA>21064126523746</ar:CAEA> </ar:FECAEADetRequest> </ar:FeDetReq> </ar:FeCAEARegInfReq> </ar:FECAEARegInformativo> </soapenv:Body> </soapenv:Envelope>
```

RESPONSE

<!-- image -->

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"> <soap:Body> <FECAEARegInformativoResponse xmlns="http://ar.gov.afip.dif.FEV1/"> <FECAEARegInformativoResult> <FeCabResp> <Cuit>23000000004</Cuit> <PtoVta>9800</PtoVta> <CbteTipo>1</CbteTipo> <FchProceso>20110308</FchProceso> <CantReg>2</CantReg> <Resultado>R</Resultado>  Rechazo total del envío <Reproceso>N</Reproceso> </FeCabResp> <FeDetResp> <FECAEADetResponse> <Concepto>1</Concepto> <DocTipo>80</DocTipo> <DocNro>30000000007</DocNro> <CbteDesde>39</CbteDesde> <CbteHasta>39</CbteHasta> <CbteFch>20110211</CbteFch> <Resultado>R</Resultado> <CAEA>21064126523746</CAEA> </FECAEADetResponse> <FECAEADetResponse> <Concepto>1</Concepto> <DocTipo>80</DocTipo> <DocNro>30000000007</DocNro> <CbteDesde>40</CbteDesde> <CbteHasta>40</CbteHasta> <CbteFch>20110211</CbteFch> <Resultado>R</Resultado> <CAEA>21064126523746</CAEA> </FECAEADetResponse> <FECAEADetResponse> <Concepto>1</Concepto> <DocTipo>80</DocTipo> <DocNro>30000000007</DocNro> <CbteDesde>41</CbteDesde> <CbteHasta>41</CbteHasta> <CbteFch>20110211</CbteFch> <Resultado>R</Resultado> <CAEA>21064126523746</CAEA> </FECAEADetResponse> </FeDetResp> <Errors> <Err>  Motivo del Rechazo <Code>10002</Code> <Msg>Campo CantReg debe ser igual a lo informado en detalle. Informado: 2, Enviado:3</Msg> </Err> </Errors> </FECAEARegInformativoResult> </FECAEARegInformativoResponse>
```

## &lt;/soap:Body&gt; &lt;/soap:Envelope&gt;

Se envía un Request con una Facturas B con Importe Gravado y alícuota de IVA al 21%, supera la totalidad de las validaciones.  El comprobante es aprobado.

## REQUEST

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECAEARegInformativo> <ar:Auth> <ar:Token>PD…</ar:Token> <ar:Sign>jd..</ar:Sign> <ar:Cuit>23000000004</ar:Cuit> </ar:Auth> <ar:FeCAEARegInfReq> <ar:FeCabReq> <ar:CantReg>1</ar:CantReg> <ar:PtoVta>9800</ar:PtoVta> <ar:CbteTipo>6</ar:CbteTipo> </ar:FeCabReq> <ar:FeDetReq> <ar:FECAEADetRequest> <ar:Concepto>2</ar:Concepto> <ar:DocTipo>80</ar:DocTipo> <ar:DocNro>30000000007</ar:DocNro> <ar:CbteDesde>45</ar:CbteDesde> <ar:CbteHasta>45</ar:CbteHasta> <ar:CbteFch>20110211</ar:CbteFch> <ar:ImpTotal>121.00</ar:ImpTotal> <ar:ImpTotConc>0.00</ar:ImpTotConc> <ar:ImpNeto>100</ar:ImpNeto>  Imp Neto Gravado <ar:ImpOpEx>0.00</ar:ImpOpEx> <ar:ImpIVA>21</ar:ImpIVA>  Importe IVA liquidado <ar:ImpTrib>0</ar:ImpTrib> <ar:FchServDesde>20110101</ar:FchServDesde> <ar:FchServHasta>20110102</ar:FchServHasta> <ar:FchVtoPago>20110220</ar:FchVtoPago> <ar:MonId>PES</ar:MonId> <ar:MonCotiz>1</ar:MonCotiz> <ar:CondicionIVAReceptorId>1</ar:CondicionIVAReceptorId> <ar:Iva> <ar:AlicIva> <ar:Id>5</ar:Id>  Alícuota de IVA 21% <ar:BaseImp>100</ar:BaseImp>  Base Imponible para la Alícuota indicada en Id <ar:Importe>21</ar:Importe>  Imp IVA liquidado </ar:AlicIva> </ar:Iva>
```

<!-- image -->

```
<ar:CAEA>21064126523746</ar:CAEA> </ar:FECAEADetRequest> </ar:FeDetReq> </ar:FeCAEARegInfReq> </ar:FECAEARegInformativo> </soapenv:Body> </soapenv:Envelope>
```

## RESPONSE

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"> <soap:Body> <FECAEARegInformativoResponse xmlns="http://ar.gov.afip.dif.FEV1/"> <FECAEARegInformativoResult> <FeCabResp> <Cuit>23000000004</Cuit> <PtoVta>9800</PtoVta> <CbteTipo>6</CbteTipo> <FchProceso>20110314</FchProceso> <CantReg>1</CantReg> <Resultado>A</Resultado> <Reproceso>N</Reproceso> </FeCabResp> <FeDetResp> <FECAEADetResponse> <Concepto>2</Concepto> <DocTipo>80</DocTipo> <DocNro>30000000007</DocNro> <CbteDesde>45</CbteDesde> <CbteHasta>45</CbteHasta> <CbteFch>20110211</CbteFch> <Resultado>A</Resultado> <CAEA>21064126523746</CAEA> </FECAEADetResponse> </FeDetResp> </FECAEARegInformativoResult> </FECAEARegInformativoResponse> </soap:Body> </soap:Envelope>
```

Se envía un Request con una Facturas A con Importe Gravado, alícuota de IVA al 21%,  27% y al 0%,  Importes Exentos y No Gravados y con importes de Tributos (IIBB), supera la totalidad de las validaciones.  El comprobante es aprobado.

## REQUEST

```
<soapenv:Envelope <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/">
```

<!-- image -->

<!-- image -->

```
<soapenv:Header/> <soapenv:Body> <ar:FECAEARegInformativo> <ar:Auth> <ar:Token>PD…</ar:Token> <ar:Sign>jd..</ar:Sign> <ar:Cuit>23000000004</ar:Cuit> </ar:Auth> <ar:FeCAEARegInfReq> <ar:FeCabReq> <ar:CantReg>1</ar:CantReg> <ar:PtoVta>9800</ar:PtoVta> <ar:CbteTipo>1</ar:CbteTipo> </ar:FeCabReq> <ar:FeDetReq> <ar:FECAEADetRequest> <ar:Concepto>1</ar:Concepto> <ar:DocTipo>80</ar:DocTipo> <ar:DocNro>30000000007</ar:DocNro> <ar:CbteDesde>40</ar:CbteDesde> <ar:CbteHasta>40</ar:CbteHasta> <ar:CbteFch>20110211</ar:CbteFch> <ar:ImpTotal>549.00</ar:ImpTotal> <ar:ImpTotConc>100.00</ar:ImpTotConc>  No Gravado <ar:ImpNeto>300</ar:ImpNeto>  Gravado.  Igual a la sumatoria de BaseImp del Array de Iva. <ar:ImpOpEx>100.00</ar:ImpOpEx>  Imp Exento <ar:ImpIVA>48</ar:ImpIVA>  Importe total de IVA liquidado. Es igual a la sumatoria de Importe del Array de Iva. <ar:ImpTrib>1</ar:ImpTrib>  Importe total de tributos. Es igual a la sumatoria de Importe del Array de Tributos. <ar:MonId>PES</ar:MonId> <ar:MonCotiz>1</ar:MonCotiz> <ar:CondicionIVAReceptorId>1</ar:CondicionIVAReceptorId> <ar:Tributos>  Detalle de Tributos <ar:Tributo> <ar:Id>2</ar:Id> <ar:Desc>IIBB Pcia Bs AS</ar:Desc> <ar:BaseImp>100</ar:BaseImp> <ar:Alic>1</ar:Alic> <ar:Importe>1</ar:Importe> </ar:Tributo> </ar:Tributos> <ar:Iva>  Detalle IVA Liquidado <ar:AlicIva> <ar:Id>5</ar:Id>  21% IVA <ar:BaseImp>100</ar:BaseImp>  Base Imponible para la Alícuota indicada en Id <ar:Importe>21</ar:Importe>  Imp IVA liquidado según Alícuota y Base Imponible. </ar:AlicIva> <ar:AlicIva> <ar:Id>3</ar:Id>  0% IVA <ar:BaseImp>100</ar:BaseImp>  Base Imponible para la alícuota indicada en Id
```

<!-- image -->

```
<ar:Importe>0</ar:Importe>  Imp IVA liquidado según Alícuota y Base Imponible. </ar:AlicIva> <ar:AlicIva> <ar:Id>6</ar:Id>  27% IVA <ar:BaseImp>100</ar:BaseImp>  Base Imponible para la Alícuota indicada en Id <ar:Importe>27</ar:Importe>  Imp IVA liquidado según Alícuota y Base Imponible. </ar:AlicIva> </ar:Iva> <ar:CAEA>21064126523746</ar:CAEA> </ar:FECAEADetRequest> </ar:FeDetReq> </ar:FeCAEARegInfReq> </ar:FECAEARegInformativo> </soapenv:Body> </soapenv:Envelope>
```

## RESPONSE

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"> <soap:Body> <FECAEARegInformativoResponse xmlns="http://ar.gov.afip.dif.FEV1/"> <FECAEARegInformativoResult> <FeCabResp> <Cuit>23000000004</Cuit> <PtoVta>9800</PtoVta> <CbteTipo>6</CbteTipo> <FchProceso>20110314</FchProceso> <CantReg>1</CantReg> <Resultado>A</Resultado> <Reproceso>N</Reproceso> </FeCabResp> <FeDetResp> <FECAEADetResponse> <Concepto>1</Concepto> <DocTipo>80</DocTipo> <DocNro>30000000007</DocNro> <CbteDesde>40</CbteDesde> <CbteHasta>40</CbteHasta> <CbteFch>20110211</CbteFch> <Resultado>A</Resultado> <CAEA>21064126523746</CAEA> </FECAEADetResponse> </FeDetResp> </FECAEARegInformativoResult> </FECAEARegInformativoResponse> </soap:Body> </soap:Envelope>
```

<!-- image -->

## Método  para consultar CAEA sin movimiento (FECAEASinMovimientoConsultar)

Esta operación permite consultar mediante un CAEA, cuáles fueron los puntos de venta que fueron notificados como sin movimiento. El cliente envía el requerimiento, el cual es atendido por el WS, superadas las validaciones de seguridad se informa el CAEA, puntos de venta identificados como sin movimientos y fecha de proceso. En caso de informar el punto de venta, se informan los datos vinculados a ese punto de venta en particular.

## Dirección URL (Homologación)

Este servicio se llama desde:

https://wswhomo.afip.gov.ar/wsfev1/service.asmx ?op= FECAEASinMovimientoConsultar

## Mensaje de solicitud

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/ envelope/" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soapenv:Header/> <soapenv:Body> <ar:FECAEASinMovimientoConsultar> <ar:Auth> <ar:Token>string</ar:Token> <ar:Sign>string</ar:Sign> <ar:Cuit>long</ar:Cuit> </ar:Auth> <ar:CAEA>string</ar:CAEA> <ar:PtoVta>int</ar:PtoVta> </ar:FECAEASinMovimientoConsultar> </soapenv:Body> </soapenv:Envelope>
```

## dónde:

| Campo  Detalle  Obligatorio  Auth  Información de la autenticación. Contiene los datos de  Token, Sign y Cuit  S  Token  Token devuelto  por  el  WSAA  S  Sign  Sign devuelto  por  el  WSAA  S  Cuit  Cuit contribuyente (representado o Emisora)  S   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Campo  Detalle  Obligatorio  CAEA  CAEA otorgado, e identificado como 'Sin Movimientos'  S   |
|----------------------------------------------------------------------------------------------|

<!-- image -->

| para determinados puntos de venta.  PtoVta  Punto de venta vinculado al CAEA informado.  S   |
|----------------------------------------------------------------------------------------------|

## Mensaje de respuesta

Retorna los puntos de venta vinculados al CAEA ingresado por parámetro donde los mismos estén registrados como sin movimientos.

```
<soap12:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:ar="http://ar.gov.afip.dif.FEV1/"> <soap12:Header/> <soap12:Body> <FECAEASinMovimientoConsultarResponse> <FECAEASinMovimientoConsultarResult> <ResultGet> <FECAEASinMov> <CAEA> string </CAEA> <FchProceso> string </FchProceso> <PtoVta> int </PtoVta> </FECAEASinMov> </ResultGet> <Errors> <Err> <Code> int </Code> <Msg> string </Msg> </Err> </Errors> <Events> <Evt> <Code> int </Code> <Msg> string </Msg               </Evt> </Events> </FECAEASinMovimientoConsultarResult> </FECAEASinMovimientoConsultarResponse> </soapenv:Body> </soapenv:Envelope>
```

dónde:

## FECAEASinMovimientoResult

| Campo  Detalle  Obligatorio  ResultGet  Nodo contenedor del array de elementos correspondientes  a él o los puntos de venta identificados como sin  movimientos para el CAEA identificado.  S  Errors  Información de errores detectados  N  Events  Información de eventos  N   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## ResultGet : contiene la información de los puntos de venta informados

| Campo  Tipo  Detalle  Obligatorio  CAEA  String (14)  Código de Autorización electrónico anticipado  S  FchProceso  String (8)  Fecha de en que se informó cómo sin  movimiento al CAEA Pto Vta indicados.  S  PtoVta  Int (5)  Punto de venta vinculado al CAEA  informado.  S   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Validaciones y errores

## Controles aplicados

| Campo / Grupo  Código de  error  Validación  CAEA  10100  No ingreso el CAEA o el formato es inválido.  PtoVta  10101  No ingreso el Punto de Venta o el formato es inválido.  CAEA  10102  El CAEA informado no se encuentra registrado en las  bases de la Administración como sin movimientos.  CAEA / PtoVta  10105  El punto de venta ingresado registra comprobantes  informados   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

---

*This section is extracted directly from the source PDF without modifications.*