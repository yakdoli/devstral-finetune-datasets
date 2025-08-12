```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_026.jpeg
document_name: pdf
page_number: 026
page_id: pdf#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:25:24Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Lists referenced assemblies for different trust modes in the application for the usage of Essential PDF.
- Explains which assemblies to use in Full Trust Mode and Medium/Partial Trust Mode for various platforms and frameworks, including WPF, Windows Forms, ASP.NET, MVC, and Silverlight.

## Content

### 2.3.1 DLLs

The following assemblies need to be referenced in your application for the usage of Essential PDF.

#### Full Trust Mode

In full trust mode, add references to the following assemblies corresponding to the platform:

- **PDF (Full-Trust) – WPF, Windows Forms, ASP.NET, MVC**
  - Syncfusion.Core.dll
  - Syncfusion.Compression.Base.dll
  - Syncfusion.Pdf.Base.dll

- **PDF (Full-Trust) – Silverlight**
  - Syncfusion.Core.dll
  - syncfusion.Compression.Silverlight.dll
  - Syncfusion.Pdf.Silverlight.dll

#### Medium/Partial Trust Mode

In medium/partial trust mode, add references to the following assemblies corresponding to the platform:

- **ASP.NET – PDF (Partial-Trust) – Web**
  - Syncfusion.Core.dll
  - Syncfusion.Compression.Base.dll
  - Syncfusion.Pdf.Web.dll

- **ASP.NET MVC – PDF (Partial-Trust) – MVC**
  - Syncfusion.Core.dll
  - Syncfusion.Compression.Base.dll
  - Syncfusion.Pdf.Mvc.dll

### 2.3.2 Web Application deployment

## Cross References
- See also: Related sections on trust modes, assembly references, and deployment guidelines.

<!-- tags: [essential-pdf, dlls, assemblies, trust-mode, referencing, deployment, web-application] keywords: [full-trust, medium-trust, partial-trust, syncfusion-core, syncfusion-compression, syncfusion-pdf] -->
```