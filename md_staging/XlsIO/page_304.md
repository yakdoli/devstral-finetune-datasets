```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_304.jpeg
document_name: XlsIO
page_number: 304
page_id: XlsIO#page_304
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:09:55Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
the OLEObject field.
IOleObject ole1 = sheet.OleObjects.Add(@"..\..\Test.pptx", image, OleLinkType.Embed);

// Set the location
ole1.Location = sheet[5, 2];

// Set the size
ole1.Size = new Size(30, 30);
```

### [VB.NET]

```vb.net
Dim image As Image = Image.FromFile("..\..\image.png")

' Select the object to insert, image for the display icon and the type of the OLEObject field.
Dim ole1 As IOleObject = sheet.OleObjects.Add("..\..\Test.pptx", image, OleLinkType.Embed)

' Set the location
ole1.Location = sheet(5, 2)

' Set the size
ole1.Size = New Size(30, 30)
```

### Output Description
Run the code. The following output is generated.

![unclear] 

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

<!-- tags: [product, XlsIO, OLEObject, embedded objects, VB.NET, C#, Syncfusion Winforms, version: 11.4.0.26] keywords: [OLEObject, embedded objects, location, size, image, Test.pptx, OleLinkType.Embed] -->
```