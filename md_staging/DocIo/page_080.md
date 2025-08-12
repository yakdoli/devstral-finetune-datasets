```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_080.jpeg
document_name: DocIo
page_number: 080
page_id: DocIo#page_080
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:33:09Z
fidelity: lossless
-->

## Public Properties

| Name        | Description                                                     |
|-------------|-----------------------------------------------------------------|
| EntityType  | Gets the type of the entity.                                   |
| Picture     | Gets or sets picture for Picture watermark.                    |
| Scaling     | Gets or sets picture scaling in percents.                     |
| Washout     | Gets or sets Washout property for Picture watermark.          |

The following example illustrates how to use the PictureWatermark class.

### Example Usage

```csharp
IWordDocument doc = new WordDocument();
doc.EnsureMinimal();
PictureWatermark picWatermark = new PictureWatermark();
picWatermark.Scaling = 120f;
picWatermark.Washout = true;
doc.Watermark = picWatermark;
picWatermark.Picture = Image.FromFile(ImagesPath + "Water lilies.jpg");
```

```vb.net
Dim doc As IWordDocument = New WordDocument()
doc.EnsureMinimal()
Dim picWatermark As PictureWatermark = New PictureWatermark()
picWatermark.Scaling = 120f
picWatermark.Washout = True
doc.Watermark = picWatermark
picWatermark.Picture = Image.FromFile(ImagesPath & "Water lilies.jpg")
```

## Text Watermark

The TextWatermark class represents the text watermark in the Word document. The following screen shot illustrates the Text Watermark settings.

<!-- tags: [Basic class, PictureWatermark, TextWatermark, Setup, Property, Entity Type, Scaling, Washout] keywords: [RPC, property, Scaling, Washout, PictureWatermark, TextWatermark, Word document] -->
```