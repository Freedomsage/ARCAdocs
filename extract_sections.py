#!/usr/bin/env python3
"""
Script to extract sections from manual-arca-source.md and create grouped documentation files
"""

import re
from pathlib import Path

def read_file(filepath):
    """Read file content"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Write file content"""
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_section(content, start_pattern, end_pattern=None, include_start=True):
    """Extract section between patterns"""
    start_match = re.search(start_pattern, content, re.IGNORECASE | re.MULTILINE)
    if not start_match:
        return None
    
    start_pos = start_match.start() if include_start else start_match.end()
    
    if end_pattern:
        end_match = re.search(end_pattern, content[start_pos:], re.IGNORECASE | re.MULTILINE)
        if end_match:
            end_pos = start_pos + end_match.start()
        else:
            end_pos = len(content)
    else:
        end_pos = len(content)
    
    return content[start_pos:end_pos].strip()

def create_header(source_info):
    """Create header with source information"""
    return f"""---
# Source of Truth / Fuente de Verdad / Источник истины
# Source Document: {source_info['file']}
# Version: {source_info['version']}
# Revision Date: {source_info['date']}
# Organization: {source_info['org']}
---

"""

def extract_all_sections():
    """Extract all sections and create documentation files"""
    
    source_file = "manual-arca-source.md"
    content = read_file(source_file)
    
    source_info = {
        'file': 'manual-desarrollador-ARCA-COMPG-v4-0.pdf',
        'version': 'v4.0 (RG 4291 – Proyecto FE v4.0)',
        'date': '17 de Marzo de 2025',
        'org': 'ARCA-SDG SIT (Agencia de Recaudación y Control Aduanero)'
    }
    
    header = create_header(source_info)
    
    # Extract Introduction section
    intro = extract_section(content, r'^## Introducción', r'^## (Autenticación|WS de Negocio)')
    if intro:
        intro_content = header + intro + "\n\n---\n\n*This section is extracted directly from the source PDF without modifications.*"
        write_file("docs/introduction.md", intro_content)
        print("✓ Created docs/introduction.md")
    
    # Extract Authentication section
    auth = extract_section(content, r'^## Autenticación', r'^## (Estructura|Tratamiento|Dirección|WS de Negocio)')
    if auth:
        auth_content = header + auth + "\n\n---\n\n*This section is extracted directly from the source PDF without modifications.*"
        write_file("docs/authentication/README.md", auth_content)
        print("✓ Created docs/authentication/README.md")
    
    # Extract Error handling section
    errors = extract_section(content, r'^## Tratamiento de errores en el WS', r'^## (Tratamiento de eventos|Dirección|WS de Negocio)')
    events = extract_section(content, r'^## Tratamiento de eventos', r'^## (Dirección|WS de Negocio)')
    if errors or events:
        errors_content = header
        if errors:
            errors_content += errors + "\n\n"
        if events:
            errors_content += events + "\n\n"
        errors_content += "---\n\n*This section is extracted directly from the source PDF without modifications.*"
        write_file("docs/errors/README.md", errors_content)
        print("✓ Created docs/errors/README.md")
    
    # Extract CAE methods
    cae = extract_section(content, r'^## Método\s+de autorización de comprobantes electrónicos por\s+CAE', r'^## (Método\s+de obtención|Recuperador|Método\s+para|Método\s+Dummy|WS de Negocio)')
    if cae:
        cae_content = header + cae + "\n\n---\n\n*This section is extracted directly from the source PDF without modifications.*"
        write_file("docs/cae/README.md", cae_content)
        print("✓ Created docs/cae/README.md")
    
    # Extract CAEA methods
    caea_solicitar = extract_section(content, r'^## Método\s+de obtención de CAEA', r'^## (Método\s+de consulta|Recuperador|Método\s+para|Método\s+Dummy)')
    caea_consultar = extract_section(content, r'^## Método\s+de consulta de CAEA', r'^## (Recuperador|Método\s+para|Método\s+Dummy)')
    caea_sin_mov = extract_section(content, r'^## Método\s+para informar CAEA sin movimiento', r'^## (Método\s+Dummy|Recuperador|Método\s+para informar comprobantes)')
    caea_reg_info = extract_section(content, r'^## Método\s+para informar comprobantes emitidos con\s+CAEA', r'^## (Método\s+para consultar CAEA sin movimiento|Método\s+para consultar Comprobantes|Recuperador)')
    caea_sin_mov_consultar = extract_section(content, r'^## Método\s+para consultar CAEA sin movimiento', r'^## (Método\s+para consultar Comprobantes|Recuperador|Método\s+para consultar valores)')
    
    if any([caea_solicitar, caea_consultar, caea_sin_mov, caea_reg_info, caea_sin_mov_consultar]):
        caea_content = header
        if caea_solicitar:
            caea_content += caea_solicitar + "\n\n"
        if caea_consultar:
            caea_content += caea_consultar + "\n\n"
        if caea_sin_mov:
            caea_content += caea_sin_mov + "\n\n"
        if caea_reg_info:
            caea_content += caea_reg_info + "\n\n"
        if caea_sin_mov_consultar:
            caea_content += caea_sin_mov_consultar + "\n\n"
        caea_content += "---\n\n*This section is extracted directly from the source PDF without modifications.*"
        write_file("docs/caea/README.md", caea_content)
        print("✓ Created docs/caea/README.md")
    
    # Extract Parameter methods
    param_patterns = [
        (r'^## Recuperador de valores referenciales de códigos de Tipos de comprobante', 'FEParamGetTiposCbte'),
        (r'^## Recuperador de valores referenciales de códigos de Tipos de Conceptos', 'FEParamGetTiposConcepto'),
        (r'^## Recuperador de valores referenciales de códigos de Tipos de Documentos', 'FEParamGetTiposDoc'),
        (r'^## Recuperador de valores referenciales de códigos de Tipos de Alícuotas', 'FEParamGetTiposIva'),
        (r'^## Recuperador de valores referenciales de códigos de Tipos de Monedas', 'FEParamGetTiposMonedas'),
        (r'^## Recuperador de valores referenciales de códigos de Tipos de datos Opcionales', 'FEParamGetTiposOpcional'),
        (r'^## Recuperador de valores referenciales de códigos de Tipos de Tributos', 'FEParamGetTiposTributos'),
        (r'^## Recuperador de los puntos de venta asignados', 'FEParamGetPtosVenta'),
        (r'^## Recuperador de cotización de moneda', 'FEParamGetCotizacion'),
        (r'^## Método\s+para consultar valores referenciales de códigos de países', 'FEParamGetTiposPaises'),
        (r'^## Método\s+para consultar las actividades', 'FEParamGetActividades'),
        (r'^## Método\s+para consultar valores referenciales de los identificadores de la condición frente al IVA del receptor', 'FEParamGetCondicionIvaReceptor'),
    ]
    
    params_content = header
    for pattern, name in param_patterns:
        # Try different end patterns
        section = extract_section(content, pattern, r'^## (Recuperador|Método\s+para|Método\s+Dummy|Recuperador de ultimo|Recuperador de cantidad|Método\s+para consultar Comprobantes)')
        if not section:
            # Try without end pattern
            section = extract_section(content, pattern, None)
        if section:
            # Limit section to reasonable length and find next section
            lines = section.split('\n')
            # Find where next section starts
            next_section_idx = None
            for i, line in enumerate(lines):
                if line.startswith('## ') and not line.startswith('## ' + name.split('Get')[-1] if 'Get' in name else name):
                    # Check if this is a new method section
                    if any(keyword in line for keyword in ['Recuperador', 'Método', 'FEParam', 'FEComp']):
                        next_section_idx = i
                        break
            if next_section_idx:
                section = '\n'.join(lines[:next_section_idx])
            params_content += f"## {name}\n\n" + section + "\n\n---\n\n"
    
    if len(params_content) > len(header):
        params_content += "*This section is extracted directly from the source PDF without modifications.*"
        write_file("docs/parameters/README.md", params_content)
        print("✓ Created docs/parameters/README.md")
    
    # Extract Comprobantes methods
    comp_ultimo = extract_section(content, r'^## Recuperador de ultimo valor de comprobante registrado', r'^## (Recuperador de cantidad|Método\s+para)')
    comp_tot = extract_section(content, r'^## Recuperador de cantidad máxima de registros', r'^## (Método\s+para informar|Método\s+para consultar)')
    comp_consultar = extract_section(content, r'^## Método\s+para consultar Comprobantes Emitidos y su código', r'^## (Método\s+para consultar valores|Método\s+para consultar las actividades)')
    
    if any([comp_ultimo, comp_tot, comp_consultar]):
        comp_content = header
        if comp_ultimo:
            comp_content += comp_ultimo + "\n\n"
        if comp_tot:
            comp_content += comp_tot + "\n\n"
        if comp_consultar:
            comp_content += comp_consultar + "\n\n"
        comp_content += "---\n\n*This section is extracted directly from the source PDF without modifications.*"
        write_file("docs/comprobantes/README.md", comp_content)
        print("✓ Created docs/comprobantes/README.md")
    
    # Extract Utils methods
    dummy = extract_section(content, r'^## Método\s+Dummy para verificación de funcionamiento', r'^## (Recuperador|Método\s+para|WS de Negocio)')
    if dummy:
        utils_content = header + dummy + "\n\n---\n\n*This section is extracted directly from the source PDF without modifications.*"
        write_file("docs/utils/README.md", utils_content)
        print("✓ Created docs/utils/README.md")
    
    print("\n✓ All sections extracted successfully!")

if __name__ == "__main__":
    extract_all_sections()

