```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_049.jpeg
document_name: pdf
page_number: 049
page_id: pdf#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:26:44Z
fidelity: lossless
-->

# Essential PDF

```csharp
if (sfd.ShowDialog() == true)
{
    using (Stream stream = sfd.OpenFile())
    {
        // Save the PDF document in the user specific location
        pdfDoc.Save(stream2);
    }
}
```

### [VB.NET]
```vb
' Create instance for SaveFileDialog
Dim sfd As SaveFileDialog = New SaveFileDialog()
    "Text files (*.pdf)|*.pdf|All files (*.*)|*.*", FilterIndex = 1
    "pdf", Filter = "Text files (*.pdf)|*.pdf|All files (*.*)|*.*", FilterIndex
    DefaultExt = "pdf", Filter

If sfd.ShowDialog() = True Then
    Using stream As Stream = sfd.OpenFile()
        ' Save the PDF document in the user specific location
        pdfDoc.Save(stream2)
    End Using
End If
```

The created pdf document is saved to the disk using the above code.

### 5. Finally close the PDF Document using the following code, so that the objects are released.
```csharp
// Release the common resources.
pdfDoc.Close();

//(or)
// Releasing document stream. This releases entire document
PdfDoc.Close(true);
```

### [VB.NET]
```vb
' Release the common resources.
pdfDoc.Close()
```

## API Reference

* **Namespace**: [Syncfusion.Pdf](syncfusion-pdf-overview)
* **Class**: `PdfDocument`
* **Method**: `PdfDocument.Close()`
    - **Parameters**: None.
    - **Returns**: Void.
    - **Description**: Closes the PDF document and releases all associated resources. Optionally, forces the release of the full document content by passing `true` to the method.

## Code Examples

### C#
```csharp
// Example of closing a PDF document
pdfDoc.Close(true);
```

### VB.NET
```vb
' Example of closing a PDF document
pdfDoc.Close()
```

<!-- tags: pdf, document, save, close, release, Syncfusion.WinForms, 11.4.0.26 -->
```