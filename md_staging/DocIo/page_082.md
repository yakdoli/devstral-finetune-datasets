```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_082.jpeg
document_name: DocIo
page_number: 082
page_id: DocIo#page_082
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:32:31Z
fidelity: lossless
-->

# Public Properties

## Constructors

| Name | Description |
| --- | --- |
| TextWatermark.TextWatermark () | Initializes a new instance of the TextWatermark class. |
| TextWatermark.TextWatermark (string) | Initializes a new instance of the TextWatermark class. |
| TextWatermark.TextWatermark (string, string, int, WatermarkLayout) | Initializes a new instance of the TextWatermark class. |

## Public Properties

| Name | Description |
| --- | --- |
| Color | Gets or sets text watermark color. |
| EntityType | Gets the type of the entity. |
| FontName | Gets or sets watermark text's font name. |
| Layout | Gets or sets layout for Text watermark. |
| Semitransparent | Gets or sets semitransparent property for Text watermark. |
| Size | Gets or sets the text watermark size (in points). |
| Text | Gets or sets watermark text. |

The following example illustrates how to use the TextWatermark class.

### C#

```csharp
IWordDocument doc = new WordDocument();
doc.EnsureMinimal();
TextWatermark textWatermark = new TextWatermark();
doc.Watermark = textWatermark;
textWatermark.Size = 96;
textWatermark.Layout = WatermarkLayout.Horizontal;
```

<!-- tags: [Syncfusion Winforms, TextWatermark, document, class, SDK, version] keywords: [text watermark, layout, size, font, semitransparent, color] -->
```