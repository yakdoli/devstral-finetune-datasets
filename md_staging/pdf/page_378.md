```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_378.jpeg
document_name: pdf
page_number: 378
page_id: pdf#page_378
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:48:25Z
fidelity: lossless
-->

## Essential PDF

```vb.net
' Extract Image from PDF document pages
For Each lpage As PdfLoadedPage In loadedPages
	Dim img As Image() = lpage.ExtractImages()
	For Each img1 As Image In img
		img1.Save("Image" & Guid.NewGuid().ToString() & ".png", ImageFormat.Png)
	Next img1
Next lpage
```

### 5.4.3 How To Extract Text From an Existing PDF Document?

You can extract text from an existing PDF document page by page by using the `ExtractText` method of the `PdfLoadedPage` class. The following code example illustrates how to extract text from a document.

#### [C#]

```csharp
// Load an existing PDF
PdfLoadedDocument ldoc = new PdfLoadedDocument(txtUrl.Text);

// Loading Page collections
PdfLoadedPageCollection loadedPages = ldoc.Pages;
string pdftext = "";

// Extract text from PDF document pages
foreach (PdfLoadedPage lpage in loadedPages)
{
	pdftext += lpage.ExtractText();
}
```

#### [VB.NET]

```vb.net
' Load an existing PDF
Dim ldoc As PdfLoadedDocument = New PdfLoadedDocument(txtUrl.Text)

' Loading Page collections
Dim loadedPages As PdfLoadedPageCollection = ldoc.Pages
Dim pdftext As String = ""

' Extract text from PDF document pages
For Each lpage As PdfLoadedPage In loadedPages
	pdftext &= lpage.ExtractText()
Next
```
```