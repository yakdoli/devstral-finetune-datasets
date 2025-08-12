```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_408.jpeg
document_name: grid
page_number: 408
page_id: grid#page_408
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:15:14Z
fidelity: lossless
--> 

# Essential Grid for Windows Forms

## Overview
- Discusses exporting events triggered before and after exporting a grid to PDF.
- Provides examples of hooking these events in an application.
- References a demo available in the Syncfusion Studio for versions of the Essential Grid.

## Content

### Exporting Events
The following table details the events triggered during the export process:

| Trigger | Description | Parameters | Type | Additional Information |
|---------|-------------|------------|------|------------------------|
| Exporting | This will be triggered before exporting grid to PDF. | (`object sender, Eventargs e`) | event | N/A |
| Exported | This will be triggered after exporting grid to PDF. | (`object sender, Eventargs e`) | event | N/A |

### Sample Link
A demo of this feature is available in the following location:

```
%LocalAppData%\Syncfusion\EssentialStudio\{Version}\Windows\Grid.Windows\Samples\2.0\Export\PDF Export Demo
```

### Hooking the events in an application
You can hook the events using the `ExportToPdf()` method of `PDFconverter`. The following code illustrates this:

#### C#

```csharp
GridPDFConverter pdfConvertor = new GridPDFConverter();
pdfConvertor.Exporting += new GridPDFConverter.PDFExportingEventHandler(pdfConvertor_Exporting);
pdfConvertor.Exported += new GridPDFConverter.PDFExportedEventHandler(pdfConvertor_Exported);
```

#### VB.NET

```vb
Dim pdfConvertor As GridPDFConverter = New GridPDFConverter()
AddHandler pdfConvertor.Exporting, AddressOf pdfConvertor_Exporting
AddHandler pdfConvertor.Exported, AddressOf pdfConvertor_Exported
```

## Code Examples
### C#

```csharp
GridPDFConverter pdfConvertor = new GridPDFConverter();
pdfConvertor.Exporting += new GridPDFConverter.PDFExportingEventHandler(pdfConvertor_Exporting);
pdfConvertor.Exported += new GridPDFConverter.PDFExportedEventHandler(pdfConvertor_Exported);
```

### VB.NET

```vb
Dim pdfConvertor As GridPDFConverter = New GridPDFConverter()
AddHandler pdfConvertor.Exporting, AddressOf pdfConvertor_Exporting
AddHandler pdfConvertor.Exported, AddressOf pdfConvertor_Exported
```

## RAG Annotations
<!-- tags: [syncfusion, essential grid, event handling, pdf export, windows forms, export to pdf] keywords: [exporting, exported, GridPDFConverter, PDFExportingEventHandler, PDFExportedEventHandler, eventargs, pdfconverter, sample link, demo, version, localappdata] -->
``` 
