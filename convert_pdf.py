#!/usr/bin/env python3
"""
Script to convert PDF to Markdown using Docling
Source: manual-desarrollador-ARCA-COMPG-v4-0.pdf
"""

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from pathlib import Path

def convert_pdf_to_markdown(pdf_path: str, output_path: str):
    """Convert PDF to Markdown using Docling"""
    print(f"Converting {pdf_path} to Markdown...")
    
    # Configure PDF pipeline options for better quality
    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = False  # PDF already has text, no need for OCR
    pipeline_options.do_table_structure = False  # Disable to avoid dependency issues
    
    # Create converter with PDF options
    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(
                pipeline_options=pipeline_options
            )
        }
    )
    
    # Convert PDF
    result = converter.convert(pdf_path)
    
    # Check if conversion was successful
    from docling.datamodel.base_models import ConversionStatus
    if result.status == ConversionStatus.SUCCESS:
        # Export to Markdown
        markdown_content = result.document.export_to_markdown()
        
        # Save to file
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(markdown_content, encoding='utf-8')
        
        print(f"✓ Successfully converted to {output_path}")
        return True
    else:
        print(f"✗ Conversion failed: {result.status}")
        if hasattr(result, 'document') and result.document:
            # Try to export anyway
            try:
                markdown_content = result.document.export_to_markdown()
                output_file = Path(output_path)
                output_file.parent.mkdir(parents=True, exist_ok=True)
                output_file.write_text(markdown_content, encoding='utf-8')
                print(f"⚠ Exported despite status {result.status}")
                return True
            except Exception as e:
                print(f"✗ Could not export: {e}")
        return False

if __name__ == "__main__":
    pdf_file = "manual-desarrollador-ARCA-COMPG-v4-0.pdf"
    output_file = "manual-arca-source.md"
    
    if not Path(pdf_file).exists():
        print(f"Error: {pdf_file} not found!")
        exit(1)
    
    convert_pdf_to_markdown(pdf_file, output_file)

