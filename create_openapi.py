#!/usr/bin/env python3
"""
Script to create OpenAPI 3.0 specification from WSDL and documentation
"""

import xml.etree.ElementTree as ET
import yaml
import json
from pathlib import Path

def parse_wsdl_operations(wsdl_file):
    """Parse WSDL to extract operations"""
    tree = ET.parse(wsdl_file)
    root = tree.getroot()
    
    # Namespace mapping
    namespaces = {
        'wsdl': 'http://schemas.xmlsoap.org/wsdl/',
        'soap': 'http://schemas.xmlsoap.org/wsdl/soap/',
        's': 'http://www.w3.org/2001/XMLSchema',
        'tns': 'http://ar.gov.afip.dif.FEV1/'
    }
    
    operations = []
    
    # Find all portTypes/operations
    for port_type in root.findall('.//wsdl:portType', namespaces):
        for operation in port_type.findall('wsdl:operation', namespaces):
            op_name = operation.get('name')
            if op_name:
                operations.append(op_name)
    
    return operations

def create_openapi_spec(wsdl_file, environment, base_url):
    """Create OpenAPI 3.0 specification"""
    
    operations = parse_wsdl_operations(wsdl_file)
    
    # Source information
    source_info = {
        'file': 'manual-desarrollador-ARCA-COMPG-v4-0.pdf',
        'version': 'v4.0 (RG 4291 – Proyecto FE v4.0)',
        'date': '17 de Marzo de 2025',
        'org': 'ARCA-SDG SIT'
    }
    
    # OpenAPI structure
    openapi_spec = {
        'openapi': '3.0.3',
        'info': {
            'title': f'ARCA AFIP - Facturación Electrónica Web Service ({environment})',
            'description': f'''# ARCA AFIP - Facturación Electrónica API

**Source of Truth / Fuente de Verdad / Источник истины:**
- Source Document: {source_info['file']}
- Version: {source_info['version']}
- Revision Date: {source_info['date']}
- Organization: {source_info['org']}

This API provides access to the Electronic Invoicing service (RG 4291) for Argentina.

**Environment:** {environment}
**Base URL:** {base_url}

## Authentication

All methods require a Ticket de Acceso (Access Ticket) provided by the WSAA (Web Service de Autenticación y Autorización).

To obtain a ticket:
1. Get a digital certificate from Clave Fiscal
2. Associate it with the "Facturación Electrónica" business web service
3. Request an Access Ticket from WSAA with service="wsfe"
4. Ticket duration: 12 hours

For more information, visit: www.arca.gob.ar/ws
''',
            'version': '4.0.0',
            'contact': {
                'name': 'ARCA Support',
                'url': 'http://www.arca.gob.ar/ws/',
                'email': 'wsfev1@arca.gov.ar'
            }
        },
        'servers': [
            {
                'url': base_url,
                'description': f'{environment} environment'
            }
        ],
        'tags': [],
        'paths': {},
        'components': {
            'schemas': {
                'FEAuthRequest': {
                    'type': 'object',
                    'required': ['Token', 'Sign', 'Cuit'],
                    'description': 'Authentication information / Información de autenticación',
                    'properties': {
                        'Token': {
                            'type': 'string',
                            'description': 'Token returned by WSAA / Token devuelto por el WSAA'
                        },
                        'Sign': {
                            'type': 'string',
                            'description': 'Sign returned by WSAA / Sign devuelto por el WSAA'
                        },
                        'Cuit': {
                            'type': 'integer',
                            'format': 'int64',
                            'description': 'CUIT of the taxpayer (represented or issuer) / CUIT del contribuyente (representado o emisor)'
                        }
                    }
                },
                'Error': {
                    'type': 'object',
                    'description': 'Error information / Información de error',
                    'properties': {
                        'Code': {
                            'type': 'integer',
                            'description': 'Error code / Código de error'
                        },
                        'Msg': {
                            'type': 'string',
                            'description': 'Descriptive error message / Mensaje descriptivo del error'
                        }
                    }
                },
                'Errors': {
                    'type': 'object',
                    'description': 'Array of errors / Array de errores',
                    'properties': {
                        'Err': {
                            'type': 'array',
                            'items': {'$ref': '#/components/schemas/Error'}
                        }
                    }
                },
                'Event': {
                    'type': 'object',
                    'description': 'Event information / Información de evento',
                    'properties': {
                        'Code': {
                            'type': 'integer',
                            'description': 'Event code / Código de evento'
                        },
                        'Msg': {
                            'type': 'string',
                            'description': 'Event message / Mensaje del evento'
                        }
                    }
                },
                'Events': {
                    'type': 'object',
                    'description': 'Array of events / Array de eventos',
                    'properties': {
                        'Evt': {
                            'type': 'array',
                            'items': {'$ref': '#/components/schemas/Event'}
                        }
                    }
                }
            }
        }
    }
    
    # Add operations as paths
    for operation in operations:
        tag_name = operation.replace('FE', '').replace('ParamGet', '').replace('Comp', '')
        openapi_spec['tags'].append({
            'name': tag_name,
            'description': f'{operation} method'
        })
        
        # Create path
        path = f'/{operation}'
        openapi_spec['paths'][path] = {
            'post': {
                'tags': [tag_name],
                'summary': operation,
                'description': f'{operation} method documentation from source PDF',
                'operationId': operation.lower(),
                'requestBody': {
                    'required': True,
                    'content': {
                        'application/xml': {
                            'schema': {
                                'type': 'object',
                                'description': 'SOAP request body'
                            },
                            'example': f'<soap:Envelope>...</soap:Envelope>'
                        },
                        'application/json': {
                            'schema': {
                                'type': 'object',
                                'properties': {
                                    'Auth': {'$ref': '#/components/schemas/FEAuthRequest'}
                                }
                            }
                        }
                    }
                },
                'responses': {
                    '200': {
                        'description': 'Successful response / Respuesta exitosa',
                        'content': {
                            'application/xml': {
                                'schema': {'type': 'string'},
                                'example': '<soap:Envelope>...</soap:Envelope>'
                            },
                            'application/json': {
                                'schema': {
                                    'type': 'object',
                                    'properties': {
                                        'Errors': {'$ref': '#/components/schemas/Errors'},
                                        'Events': {'$ref': '#/components/schemas/Events'}
                                    }
                                }
                            }
                        }
                    },
                    '400': {
                        'description': 'Bad request / Solicitud incorrecta',
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/Errors'}
                            }
                        }
                    },
                    '500': {
                        'description': 'Internal server error / Error interno del servidor',
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/Errors'}
                            }
                        }
                    }
                }
            }
        }
    
    return openapi_spec

def main():
    """Main function"""
    # Create OpenAPI for Homologación
    homologacion_spec = create_openapi_spec(
        'openapi/homologacion.wsdl',
        'Homologación (Testing)',
        'https://wswhomo.afip.gov.ar/wsfev1/service.asmx'
    )
    
    # Create OpenAPI for Producción
    produccion_spec = create_openapi_spec(
        'openapi/produccion.wsdl',
        'Producción (Production)',
        'https://servicios1.afip.gov.ar/wsfev1/service.asmx'
    )
    
    # Save as YAML
    with open('openapi/homologacion.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(homologacion_spec, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    
    with open('openapi/produccion.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(produccion_spec, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    
    print("✓ Created openapi/homologacion.yaml")
    print("✓ Created openapi/produccion.yaml")

if __name__ == "__main__":
    try:
        import yaml
    except ImportError:
        print("Installing PyYAML...")
        import subprocess
        subprocess.run(['pip3', 'install', 'pyyaml', '--break-system-packages', '--quiet'])
        import yaml
    
    main()

