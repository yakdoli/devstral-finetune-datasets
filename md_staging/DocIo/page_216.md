```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_216.jpeg
document_name: DocIo
page_number: 216
page_id: DocIo#page_216
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:42:01Z
fidelity: lossless
-->

# Essential DocIO

```vb
Dim section As IWSection = doc.AddSection()

Dim i As Integer = 0

Do While i < doc.Styles.Count
    Dim style = CType(doc.Styles(i), IWParagraphStyle)
    Dim paragraph As IWParagraph = section.AddParagraph()
    paragraph.ApplyStyle(style.Name)
    paragraph.AppendText("[ Style Applied ]: ")
    paragraph.AppendText(style.Name)
    i += 1
Loop
section.AddParagraph()
doc.Save("UserStyle.doc")
```

## Overview

- The following code illustrates how to apply built-in paragraph styles to the Word document.
- Demonstrates the process of applying paragraph formatting using the `WParagraphFormat` class.

## Content

### [C#]

```csharp
IWordDocument doc = new WordDocument();
doc.EnsureMinimal();

doc.LastParagraph.AppendText("Heading 1");
doc.LastParagraph.ApplyStyle(BuiltinStyle.Heading1);

doc.Save("BuiltinStyle.doc");
```

### [VB.NET]

```vb
Dim doc As IWordDocument = New WordDocument()

doc.EnsureMinimal()

doc.LastParagraph.AppendText("Heading 1")
doc.LastParagraph.ApplyStyle(BuiltinStyle.Heading1)

doc.Save("BuiltinStyle.doc")
```

### 4.4.2.4 Paragraph Formats

WP**aragraphFormat** class represents paragraph formatting in the Word document. To apply paragraph formatting in MS Word, open **Format** menu and click **Paragraph**.

## API Reference

### Namespace: Syncfusion.DocIO

#### Class: WParagraphFormat

This class provides properties and methods to manipulate paragraph formatting in Word documents.

#### Methods:
- `ApplyStyle(styleName As String)`
  - Applies the specified built-in or custom paragraph style to the paragraph.

## Code Examples

### C#

```csharp
using System;
using Syncfusion.DocIO;
using Syncfusion.DocIO.Dls;

class Program
{
    static void Main()
    {
        using (WordDocument doc = new WordDocument())
        {
            doc.EnsureMinimal();

            IParagraph para = doc.LastParagraph;
            para.AppendText("This is a formatted paragraph.");
            para.ApplyStyle(BuiltinStyle.Heading1);

            doc.Save("FormattedParagraph.doc");
        }
    }
}
```

### VB.NET

```vb
Imports System
Imports Syncfusion.DocIO
Imports Syncfusion.DocIO.Dls

Module Program
    Sub Main()
        Using doc As New WordDocument()
            doc.EnsureMinimal()

            Dim para As IParagraph = doc.LastParagraph
            para.AppendText("This is a formatted paragraph.")
            para.ApplyStyle(BuiltinStyle.Heading1)

            doc.Save("FormattedParagraph.doc")
        End Using
    End Sub
End Module
```

---

<!-- tags: [syncfusion, word, paragraph, format, style, document] keywords: [Syncfusion.DocIO, WParagraphFormat, built-in style, custom style, paragraph formatting, Word document, apply style, Microsoft Word, C#, VB.NET] -->
```