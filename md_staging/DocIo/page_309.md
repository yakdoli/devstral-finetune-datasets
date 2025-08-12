```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_309.jpeg
document_name: DocIo
page_number: 309
page_id: DocIo#page_309
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:48:49Z
fidelity: lossless
-->

# Essential DocIO

```csharp
if (sfd.ShowDialog() == true)
{
    using (Stream stream = sfd.OpenFile())
    {
        document.Save(stream, FormatType.Docx);
    }
}
```

3. Run the application. The .doc file is converted to .docx file.  
The same can be achieved using the VB.Net code as well.

```vb.net
[VB.NET]
Dim document As New WordDocument()
document.Open("SourceDocument.doc", FormatType.Doc)
Dim sfd As New SaveFileDialog()
If sfd.ShowDialog() = True Then
    Using stream As Stream = sfd.OpenFile()
        document.Save(stream, FormatType.Docx)
    End Using
End If
```

## Reading/Modifying .docx File

Once a file is saved into .docx format, Essential DocIO provides support for reading and modifying .docx files. Docx files can be read using the same API as that of .doc files; except for the format in which it is opened.

The control uses the following API to read the .docx format.

### C#

```csharp
WordDocument doc = new WordDocument("sample.docx", FormatType.Docx);
```

### VB.NET

```vb.net
Dim doc As New WordDocument("sample.docx", FormatType.Docx)
```

Run the file. You will be able to open and edit a .docx file.

## 4.10 Supported Elements

### Supported Elements in Silverlight

The list of various supported and non-supported elements of Essential DocIO in Silverlight platform is given in the following table.

---

```html
© 2013 Syncfusion. All rights reserved. 309 | Page
```
<!-- tags: [DocIo, Syncfusion Winforms, Silverlight, Supported Elements, WordDocument, format conversion, .docx, .doc, API, file operations, document processing, reading, modifying, supported elements] keywords: [DocIO, Syncfusion, Winforms, Silverlight, supported elements, WordDocument, .docx, .doc, format conversion, document API, read, modify, file operations] -->
```