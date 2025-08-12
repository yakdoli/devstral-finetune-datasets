```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_027.jpeg
document_name: pdf
page_number: 027
page_id: pdf#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:25:34Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Discusses deployment scenarios in medium or partial trust settings.
- Focuses on the behavior of Syncfusion assemblies in such environments.
- Highlights supported and unsupported features under medium trust.

## Content

### Deploying in Medium Trust or Partial Trust Scenarios
This section discusses the deployment of Syncfusion assemblies in medium or partial trust scenarios.

There are two such scenarios in which Syncfusion assemblies might be deployed.

#### Example 1
If the Syncfusion Assemblies are in **GAC** (Global Assembly Cache), and the **Web Application** is running in **medium** trust, then the Syncfusion assemblies actually run in full trust. Hence, this scenario is **fully supported** and there are **no additional steps necessary for deployment**.

#### Example 2
If the Syncfusion Assemblies are present in the application's **bin** folder and the **Web Application** is running in **medium** trust, then the Syncfusion assemblies will run in medium trust.

**Essential PDF** allows work in medium trust by using the following assemblies:

- Syncfusion.Core.dll
- Syncfusion.Compression.Base.dll
- Syncfusion.Pdf.Web.dll

However, the following features are **not currently supported** under this scenario:

- Digital Signature (including) PdfSignatureField and PdfLoadedSignature Fields.
- PDF/A
- PdfHtmlTextElement
- Images
  - Metafile
  - RtfToImage
- Fonts
  - PdfTrueTypeFont
- RTL Support
- Html To PDF

## API Reference (if applicable)
Not applicable for this page.

## Code Examples (multi-language supported)
No code examples provided in this section.

## Page-level Navigation/TOC (if applicable)
Not applicable for this page.

## Cross References
- No cross-references are present on this page.

<!-- tags: [medium trust, partial trust, syncfusion assemblies, global assembly cache, gac, web application, essential pdf, unsupported features] keywords: [medium trust, partial trust, syncfusion assemblies, gac, essential pdf, unsupported features, Syncfusion.Core.dll, Syncfusion.Compression.Base.dll, Syncfusion.Pdf.Web.dll, digital signature, pdf/a, pdfhtmltextelement, images, fonts, rtl support, html to pdf] -->
```