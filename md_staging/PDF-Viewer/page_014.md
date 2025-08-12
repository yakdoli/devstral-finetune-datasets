```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_014.jpeg
document_name: PDF Viewer
page_number: 014
page_id: PDF Viewer#page_014
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:34Z
fidelity: lossless
-->

# Essential PDF Viewer

## Overview
- PDF Viewer control is available in the Syncfusion Windows Toolbox.
- Steps to incorporate the PDF Viewer control into a project.
- Appearance and behavior of the PDF Viewer can be customized via properties.

## UI Components in the Toolbox

The following components are available in the Syncfusion Windows Toolbox for PDF Viewer:

- **Pointer**
- **GridControl**
- **GridListControl**
- **PdfDocumentView**
- **PdfViewerControl** <!-- Highlighted -->
- **GridRecordNavigationControl**
- **GridAwareTextBox**
- **BannerTextProvider**
- **ButtonAdv**
- **ColorPickerButton**
- **ColorUIControl**
- **TextBoxExt**
- **CurrencyTextBox**
- **PopupControlContainer**

**Figure 5: PDF Viewer control in Toolbox**

### Procedure to Add PDF Viewer Control

1. **Drag a PDF Viewer control onto the form.**
   - This action places the PDF Viewer control within the application's form interface.

**Appearance and behavior-related aspects of the PDF Viewer can be controlled by setting the appropriate properties through the properties grid.**

---

## API Reference (if applicable)

### Properties
- **Customization Properties:**`Appearance`, `Behavior`
- **PDF Viewer Control Settings:**`PdfViewerSettings`, `ZoomLevel`

### Methods
- **Load PDF Document:**`LoadPdfDocument()`
- **Refresh Viewer:**`RefreshViewer()`

### Events
- **DocumentLoaded:**`DocumentLoadedEvent`

---

## Code Examples

### C# Example

```csharp
using Syncfusion.Windows.Forms.PdfViewer;

public void InitializePdfViewer()
{
    PdfViewerControl viewer = new PdfViewerControl();
    viewer.Dock = DockStyle.Fill;
    this.Controls.Add(viewer);

    // Load a PDF document
    viewer.LoadPdfDocument("path/to/pdf/document.pdf");
}
```

### VB.NET Example

```vb
Imports Syncfusion.Windows.Forms.PdfViewer

Public Sub InitializePdfViewer()
    Dim viewer As New PdfViewerControl()
    viewer.Dock = DockStyle.Fill
    Me.Controls.Add(viewer)

    ' Load a PDF document
    viewer.LoadPdfDocument("path/to/pdf/document.pdf")
End Sub
```

---

## Page-level Navigation/TOC (if applicable)

- [**Figure 5**] PDF Viewer control in Toolbox
- Procedure to Add PDF Viewer Control

## Cross References

- **Related Controls:** ButtonAdv, ColorPickerButton, CurrencyTextBox
- **Further Assistance:** Syncfusion Windows Forms Documentation

<!-- tags: [syncfusion, windows forms, pdf viewer, control, toolbox, properties, api] keywords: [pdf, viewer, drag, form, properties grid, customization] -->
```