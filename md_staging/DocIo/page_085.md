```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_085.jpeg
document_name: DocIo
page_number: 085
page_id: DocIo#page_085
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:33:43Z
fidelity: lossless
-->

## Word Format Conversion

### Overview
- Detailed instructions for saving a document in Word 2007 and Word 2013 formats.
- Usage of `FormatType` enumerations to specify the desired Word format.
- Demonstration of creating and saving `.docx` files for Word 2013 format.

### Content

#### Saving in Word 2007 Format

```csharp
'Saves the document in Word 2007 format type.
doc.Save("Sample.docx", FormatType.Word2010)
```

#### Opening and Saving in Word 2013 Format

The following code illustrates how to open a Word 2013 format document and save it.

**[C#]**

```csharp
WordDocument doc = new WordDocument();
//Opens the Word 2013 format document.
document.Open(filename, FormatType.Automatic);
//Adding a new paragraph to the last section.
IWikiParagraph paragraph = document.LastSection.AddParagraph()
//Insert text into the paragraph.
paragraph.AppendText( "Creating Word 2013 format document!");
//Saves the document in Word 2013 format type.
doc.Save("Sample.docx", FormatType.Word2013);
```

**[VB.NET]**

```vb
Dim doc As New WordDocument()
'Opens the Word 2013 format document.
document.Open(filename, FormatType.Automatic);
'Adding a new paragraph to the last section.
Dim paragraph As IWikiParagraph = document.LastSection.AddParagraph()
'Insert text into the paragraph.
paragraph.AppendText("Creating Word 2013 format document!")
'Saves the document in Word 2013 format type.
doc.Save("Sample.docx", FormatType.Word2013)
```

#### Support for .doc Files in .docx Format

DoclO also has the ability to save .doc files into the .docx format (i.e., Microsoft Word 2007, Microsoft Word 2010, and Microsoft Word 2013 format files). All the elements supported by .doc are supported in .docx.

## API Reference

- **Namespace**: Syncfusion.DocIO
- **Class**: WordDocument
- **Methods**:
  - `Open(filename, FormatType)` - Opens a Word document with the specified file name and format type.
  - `LastSection` - Gets the last section of the document.
  - `AddParagraph()` - Adds a new paragraph to the section.
  - `AppendText(text)` - Appends the specified text to the paragraph.
  - `Save(filename, FormatType)` - Saves the document with the specified file name and format type.

### Code Examples

#### C# Example

```csharp
using Syncfusion.DocIO;

public void ConvertToWord2013() {
    WordDocument doc = new WordDocument();
    doc.Open("existingDocument.doc", FormatType.Automatic);
    
    IWikiParagraph paragraph = doc.LastSection.AddParagraph();
    paragraph.AppendText("This is a new paragraph added to a Word 2013 document.");
    
    doc.Save("convertedDocument.docx", FormatType.Word2013);
}
```

#### VB.NET Example

```vb
Imports Syncfusion.DocIO

Public Sub ConvertToWord2013()
    Dim doc As New WordDocument()
    doc.Open("existingDocument.doc", FormatType.Automatic)
    
    Dim paragraph As IWikiParagraph = doc.LastSection.AddParagraph()
    paragraph.AppendText("This is a new paragraph added to a Word 2013 document.")
    
    doc.Save("convertedDocument.docx", FormatType.Word2013)
End Sub
```

## Cross References

See also:
- [Syncfusion DocIO Overview](#docio-overview)

<!-- tags: [docio, word-format-conversion, csharp, vb.net, winforms, 11.4.0.26] keywords: [Microsoft Word, docx, word2007, word2010, word2013, FormatType, WordDocument] -->
```