```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_214.jpeg
document_name: pdf
page_number: 214
page_id: pdf#page_214
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:38:02Z
fidelity: lossless
-->

## Essential PDF

```csharp
//Read the text from the text file
string path = "../../../../../Data/SampleText.txt";
StreamReader reader = new StreamReader(path, Encoding.ASCII);
string text = reader.ReadToEnd();
reader.Close();

//Set the formats for the text
PdfStringFormat format = new PdfStringFormat();
format.Alignment = PdfTextAlignment.Justify;
format.LineAlignment = PdfVerticalAlignment.Top;
format.ParagraphIndent = 15f;

//Create a text element
PdfTextElement element = new PdfTextElement(text, font);
element.Brush = new PdfSolidBrush(Color.Black);
element.StringFormat = format;
element.Font = new PdfStandardFont(PdfFontFamily.Helvetica, 12);

//Set the properties to paginate the text.
PdfLayoutFormat layoutFormat = new PdfLayoutFormat();
layoutFormat.Break = PdfLayoutBreakType.FitPage;
layoutFormat.Layout = PdfLayoutType.Paginate;

//Draw the text element with the properties and formats set.
PdfTextLayoutResult result = element.Draw(page, bounds, layoutFormat);

//Save the document.
doc.Save("Sample.pdf");
```

### VB.NET

```vb
'Create a new PDF document.
Dim doc As PdfDocument = New PdfDocument()

'Set compression level
doc.Compression = PdfCompressionLevel.None

'Add a page to the document.
Dim page As PdfPage = doc.Pages.Add()

'Read the text from the text file
Dim path As String = "../../../../../Data/SampleText.txt"
Dim reader As StreamReader = New StreamReader(path, Encoding.ASCII)
Dim text As String = reader.ReadToEnd()
reader.Close()
```
```


<!-- tags: [product, module, control, api, version?] keywords: [Essential PDF, text file, PdfStringFormat, PdfTextElement, PdfLayoutFormat, Foxit, boolean] -->
