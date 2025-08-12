```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_081.jpeg
document_name: DocIo
page_number: 081
page_id: DocIo#page_081
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:33:31Z
fidelity: lossless
-->

## Essential DocIO

![Selecting Text Watermark in Printed Watermark Dialog Box](https://via.placeholder.com/100x100 "Figure 30: Selecting Text Watermark in Printed Watermark Dialog Box")

### Overview
- The text property defines the text of the Text Watermark.
- The FontName property defines the name of the text font.
- The Size property defines the font size.
- The Color property defines the color of the text.
- The SemiTransparent property determines whether the text watermark is semi-transparent.
- The Layout property defines the layout for the watermark.

### Details

#### Text Watermark Properties
- **Text**: Defines the text of the Text Watermark.
- **FontName**: Defines the name of the text font. Default value is `Times New Roman`.
- **Size**: Defines the font size. Default value is `36`.
- **Color**: Defines the color of the text. Default value is `Color.Gray`.
- **SemiTransparent**: Defines whether the text watermark is semi-transparent. Default value is `True`.

#### Layout Property
The Layout property defines the layout of the watermark:
- **Diagonal**: Diagonal watermark layout.
- **Horizontal**: Horizontal watermark layout.
- The default layout is `Diagonal`.

#### Class Hierarchy
The class hierarchy for the watermark functionality is as follows:
```
ParagraphItem
  |
  Watermark
    |
    TextWatermark
```

### Page-level Navigation/TOC
- **Class Hierarchy**: Details the structure of the watermark classes.

### RAG Annotations
<!-- tags: [DocIO, Watermark, TextWatermark, ClassHierarchy, WinForms, Syncfusion] keywords: [Text, FontName, Size, Color, SemiTransparent, Layout, ParagraphItem, Watermark, TextWatermark] -->
```