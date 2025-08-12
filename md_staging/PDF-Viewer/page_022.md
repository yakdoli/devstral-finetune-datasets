```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_022.jpeg
document_name: PDF Viewer
page_number: 022
page_id: PDF Viewer#page_022
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:52:15Z
fidelity: lossless
-->

# Essential PDF Viewer

## Content

### Print Dialog Displayed in PDF Viewer

Figure 9: Print Dialog displayed in PDF Viewer

#### 4.1.3.1 Silent Printing

The `PrintDocument` property of `PdfViewerControl` returns `System.Drawing.Printing.PrintDocument` that helps to complete printing using `PrintDialog`. The following code sample demonstrates this:

##### C#

```csharp
PrintDialog dialog = new PrintDialog();
dialog.AllowPrintToFile = true;
dialog.Document = viewer.PrintDocument;
dialog.Document.Print();
```

##### VB.NET

```vb
Dim dialog As New PrintDialog()
dialog.AllowPrintToFile = True
dialog.Document = viewer.PrintDocument
dialog.Document.Print()
```

## API Reference

### Methods

- `PrintDocument`: Retrieves the `PrintDocument` object used for printing.
- `Print`: Initiates the printing process.

### Properties

- `AllowPrintToFile`: Enables or disables the option to print to file.

## Code Examples

#### C#

```csharp
PrintDialog dialog = new PrintDialog();
dialog.AllowPrintToFile = true;
dialog.Document = viewer.PrintDocument;
dialog.Document.Print();
```

#### VB.NET

```vb
Dim dialog As New PrintDialog()
dialog.AllowPrintToFile = True
dialog.Document = viewer.PrintDocument
dialog.Document.Print()
```

## RAG Annotations

<!-- tags: [PDF Viewer, PrintDocument, PrintDialog, Silent Printing, C#, VB.NET] keywords: [PdfViewerControl, printing, PrintDocument, PrintDialog, AllowPrintToFile, Print] -->
```