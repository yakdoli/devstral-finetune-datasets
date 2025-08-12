```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_078.jpeg
document_name: DocIo
page_number: 078
page_id: DocIo#page_078
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:32:21Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Text Watermark
- The type of watermark is defined by using the Type property. This property returns the object of type, WatermarkType. It includes the following options.

### Watermark Types
- **NoWatermark**: document does not have watermark
- **PictureWatermark**: document has picture watermark
- **TextWatermark**: document has text watermark

You can create a Picture Watermark or Text Watermark, but you cannot create an object of the Watermark class.

Watermark is a paragraph item. It is found in the first paragraph of the header/footer subdocument. DocIO Watermark is accessible through the WordDocument.Watermark property.

## Class Hierarchy

- **ParagraphItem**
  - |  
    ⬛ *Watermark*

## Public Properties

| Name       | Description                              |
|------------|------------------------------------------|
| EntityType | Gets the type of the entity.            |
| Type       | Gets or sets the watermark type.        |

## Picture Watermark

The PictureWatermark class represents the picture watermark in the Word document.
```