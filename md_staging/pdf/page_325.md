```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_325.jpeg
document_name: pdf
page_number: 325
page_id: pdf#page_325
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:43:52Z
fidelity: lossless
-->

# Essential PDF

## Content

A tagged PDF can be converted from a Web page or HTML string by using the following code snippet:

### [C#]

```csharp
// Create a new PdfDocument.
PdfDocument document = new PdfDocument();
PdfLayoutResult result = null;

// Create a new instance of HtmlConverter class.
using (HtmlConverter html = new HtmlConverter())
{
    // Turn on or off various options.
    html.EnableJavaScript = true;
    html.EnableActiveXContents = true;

    // Convert to Tagged PDF.
    result = html.ConvertToTaggedPDF(document, url);
}

// Save and close the document.
document.Save(@"Sample.pdf");
document.Close(true);
```

### [VB.NET]

```vbnet
' Create a new PdfDocument.
Dim document As New PdfDocument()
Dim result As PdfLayoutResult = Nothing

' Create a new instance of HtmlConverter class.
Using html As New HtmlConverter()
    ' Turn on or off various options.
```

## API Reference (if applicable)

### ConvertToTaggedPDF Method

**Signature:**
```csharp
public PdfLayoutResult ConvertToTaggedPDF(PdfDocument document, String url, String baseURL)
```

**Parameters:**

| Name         | Type           | Description                              |
|--------------|----------------|------------------------------------------|
| `document`   | `PdfDocument`  | The PDF document to convert to.         |
| `url`        | `String`       | The URL or path of the HTML content.    |
| `baseURL`    | `String`       | The base URL or path for resolving URLs.|

**Returns:**
- `PdfLayoutResult`: The result of the conversion.

**Exceptions:**
- Thrown if any errors occur during the conversion process.

## Code Examples (multi-language supported)

### C# Example
```csharp
using Syncfusion.PDF.Parsing;
using System;

class Program
{
    static void Main()
    {
        string url = @"http://example.com";
        string baseAddress = @"https://example.com";
        string username = "exampleUser";
        string password = "examplePassword";

        // Create a new PdfDocument.
        PdfDocument document = new PdfDocument();

        // Create an HtmlConverter instance and convert to Tagged PDF.
        using (HtmlConverter html = new HtmlConverter())
        {
            html.EnableJavaScript = true;
            html.EnableActiveXContents = true;

            PdfLayoutResult result = html.ConvertToTaggedPDF(document, url, baseAddress);
        }

        // Save and close the document.
        document.Save(@"Sample.pdf");
        document.Close();
    }
}
```

### VB.NET Example
```vbnet
Imports Syncfusion.PDF.Parsing
Imports System

Module Module1
    Sub Main()
        Dim url As String = "http://example.com"
        Dim baseAddress As String = "https://example.com"
        Dim username As String = "exampleUser"
        Dim password As String = "examplePassword"

        ' Create a new PdfDocument.
        Dim document As New PdfDocument()

        ' Create an HtmlConverter instance and convert to Tagged PDF.
        Using html As New HtmlConverter()
            html.EnableJavaScript = True
            html.EnableActiveXContents = True

            Dim result As PdfLayoutResult = html.ConvertToTaggedPDF(document, url, baseAddress)
        End Using

        ' Save and close the document.
        document.Save("Sample.pdf")
        document.Close()
    End Sub
End Module
```

## Page-level Navigation/TOC (if applicable)
- [C#]
- [VB.NET]

## Cross References
See also:
- [Syncfusion PDF Documentation](#syncfusion-pdf-documentation)

<!-- tags: syncfusion, pdf, tagged pdf, html conversion, c#, vb.net, version: 11.4.0.26 -->
```