```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_242.jpeg
document_name: DocIo
page_number: 242
page_id: DocIo#page_242
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:43:34Z
fidelity: lossless
-->

# Essential DocIO

```csharp
//Inserting some XHTML
section.Body.InsertXHTML(HtmlString);
```

The `InsertXHTML` method has two overloads that specify the start paragraph item index and the end paragraph item index. The inserted XHTML adds several Word paragraphs, internally (with several possible paragraph items like lists and so on), and tables inside the Textbody of the Word document (Textbody is the container for paragraphs and tables in the Word object model).

It is also possible to check if the given XHTML string is valid or not by using the `WTextBody.IsValidXHTML` method. Refer to Appendix 1 and 2 for the list of supported tags and attributes.

Also, you can open the HTML file directly from the Word document constructor, and convert the HTML file into a Word document.

The following code illustrates opening an XHTML document and saving it as a Word document by using DocIO.

```csharp
WordDocument document = new WordDocument(String filename, FormatType formattype, XHTMLValidationType XHTMLValidationtype);
document.Save("sample.doc");
```

## Support for partial path of an image

Currently EssentialDocIO provides support for the partial path of an image only when directly loading the HTML file into the Word document using `document.Open()` method.

The following are the two overloaded methods.
- `Document.open(string fileName, FormatType formatType, XHTMLValidationType validationType, string baseUrl)`
- `Document.open(Stream stream, FormatType formatType, XHTMLValidationType validationType, string baseUrl)`

The following code illustrates loading the HTML file containing the partial path of an image.
```html

---
© 2013 Syncfusion. All rights reserved.  242 | Page
```
``` 

<!-- tags: [EssentialDocIO, Syncfusion, Winforms, DocIO, Word, HTML, XHTML, WTextBody, WordDocument, FormatType, XHTMLValidationType, document.Open(), partial path of an image] keywords: [XHTML, DocIO, Word document, HTML file, document conversion, partial path, image support, WordObjectModel, TextBody, List, Table, WTextBody, IsValidXHTML, Appendix 1, Appendix 2, document.Save(), document.Open(), Syncfusion.Winforms, WordDocument.open] -->
``` 
