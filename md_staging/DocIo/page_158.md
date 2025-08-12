```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_158.jpeg
document_name: DocIo
page_number: 158
page_id: DocIo#page_158
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:37:52Z
fidelity: lossless
-->

# Essential DocIO

```csharp
End If
Next
doc.Save("WebLink_modified.doc")
```

### Hyperlink for Images

The following code illustrates how to set hyperlinks for images.

#### [C#]

```csharp
IWParagraph para = doc.Sections[0].AddParagraph();
WPicture mImage = new WPicture(doc);
mImage.LoadImage(Image.FromFile(@"..\\..\\Nature.jpg"));

// Scaling Image.
mImage.HeightScale = 50f;
mImage.WidthScale = 50f;
IWField field = para.AppendField("Hyperlink", FieldType.FieldHyperlink);
Hyperlink hlink = new Hyperlink(field as WField);
hlink.Type = HyperlinkType.WebLink;
hlink.Uri = "http://www.syncfusion.com";
hlink.PictureToDisplay = mImage;
```

#### [VB.NET]

```vb
Dim para As IWParagraph = doc.Sections(0).AddParagraph()
Dim mImage As New WPicture(doc)
mImage.LoadImage(Image.FromFile("..\\..\\Nature.jpg"))

' Scaling Image.
mImage.HeightScale = 50F
mImage.WidthScale = 50F
Dim field As IWField = para.AppendField("Hyperlink", FieldType.FieldHyperlink)
Dim hlink As New Hyperlink(TryCast(field, WField))
hlink.Type = HyperlinkType.WebLink
hlink.Uri = "http://www.syncfusion.com"
hlink.PictureToDisplay = mImage
```

### 4.4.1.2.6 Document Variable

#### [[image omitted]]
<!-- tags: [DocIO, document manipulation, hyperlinks, images, document variables, Syncfusion SDK, C#, VB.NET] keywords: [essential, hyperlinks, images, document, manipulation, field, hyperlink type, scaling, web link, URI, picture, display, document variable, IWParagraph, WPicture, Hyperlink, FieldType ] -->
```