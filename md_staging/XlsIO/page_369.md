```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_369.jpeg
document_name: XlsIO
page_number: 369
page_id: XlsIO#page_369
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:13:58Z
fidelity: lossless
-->

## ExcelToPdfConverterSettings

```csharp
ExcelToPdfConverterSettings
settings.TemplateDocument = pdfDoc
settings.DisplayGridLines = GridLinesDisplayStyle.Invisible

' Convert the Excel document to PDF document
pdfDoc = converter.Convert(settings)

' Save the PDF file
pdfDoc.Save("ExceltoPdf.pdf")
```

### Supported Elements

This feature provides support for the following elements:

- Styles
- Character formatting
- Headers and footers
- Images
- Text boxes
- Hyperlinks
- Document properties
- Comments
- Encryption
- TableStyle Support
- Text Rotations
- Excel Page Setup Options
- Unicode Support
- Background Images
- Printing Titles when Converting the Excel to PDF
- Page Break Support
- Print Area Support
- Print Order Support
- Unicode in Headers and Footers

### Styles

This feature supports almost all the styles supported by Excel 2007.

### Character formatting
```markdown

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a  
  bullet/numbered list with links/text as shown. Do not create links that don’t exist.
(locale site TOC or breadcrumbs unless the page explicitly describes them.)

## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

## RAG Annotations
- At the end, add an HTML comment with tags and keywords derived ONLY from  
  visible content:
  <!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
 - Add optional per-section anchors as HTML comments before each H2/H3 to aid chunking, using IDs derived from the heading (kebab-case), e.g., <!-- anchor: XlsIO#page_369#getting-started -->. Do not add if the heading text is unclear.
```  
<!-- tags: Syncfusion, XlsIO, Winforms, ExcelToPdfConverterSettings, Supported Elements, Styles, Character formatting, GridLinesDisplayStyle, Unicode Support, Printing Titles, Page Break Support, Print Area Support, Print Order Support, Unicode in Headers and Footers, Excel 2007 -->
```