```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_176.jpeg
document_name: DocIo
page_number: 176
page_id: DocIo#page_176
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:39:06Z
fidelity: lossless
-->

## Overview
- The page discusses the `WPicture` class, which is part of the class hierarchy for handling picture objects in a Word document.
- It provides details about public constructors, properties, and their functionalities related to managing the appearance and positioning of images within documents.

## Content

### Class Hierarchy
- `ParagraphItem`
  - `WPicture`

### Public Constructor

| Name                             | Description                                 |
|-----------------------------------|---------------------------------------------|
| `WPicture.WPicture (IWordDocument)` | Gets the type of the entity.               |

### Public Properties

| Name              | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `EntityType`      | Gets the type of the entity.                                                   |
| `Height`          | Gets or sets picture height.                                              |
| `HeightScale`     | Gets or sets picture height scale factor in percent.                       |
| `HorizontalAlignment` | Gets or sets picture horizontal alignment.                              |
| `HorizontalOrigin`  | Gets sets horizontal origin of the picture.                              |
| `HorizontalPosition` | Gets sets absolute vertical position of the picture.                    |
| `Image`           | Gets internal System.Drawing.Image object.                                 |
| `ImageBytes`      | Gets image byte array.                                                     |
| `IsBelowText`     | Gets or sets whether picture is below image.                               |
| `Size`            | Gets or sets size of the picture object.                                   |
| `TextWrappingStyle` | Gets or sets text wrapping style of the picture.                         |
| `TextWrappingType`  | Gets or sets text wrapping type of the picture.                          |
| `VerticalAlignment` | Gets or sets picture vertical alignment.                                 |
| `VerticalOrigin`   | Gets or sets absolute horizontal position of the picture.                 |

<!-- tags: [syncfusion, winforms, docio, wpicture, word document, image, alignment, size, scaling] -->
```