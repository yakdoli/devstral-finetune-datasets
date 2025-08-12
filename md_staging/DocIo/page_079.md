```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_079.jpeg
document_name: DocIo
page_number: 079
page_id: DocIo#page_079
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:32:52Z
fidelity: lossless
-->

# Printed Watermark

## Overview

- Explains how to select and configure picture watermarks using the "Printed Watermark" dialog box.
- Describes the properties controlling the appearance and behavior of watermarks, including picture selection, scaling, and washout effect.
- Includes details on class hierarchy, public constructors, and API usage for configuring picture watermarks.

## Content

### Printed Watermark Dialog Box

#### Figure: Selecting Picture Watermark in Printed Watermark Dialog Box

The "Printed Watermark" dialog box allows users to configure watermarks applied to documents. The dialog offers options for both picture watermarks and text watermarks.

**Properties Explained:**

- **Picture Property:** Defines the picture to be used as the watermark.
- **Scaling Property:** Defines the scaling of the watermark in percentage terms.
- **Washout Property:** Determines whether the washout effect is applied to the watermark. The default value is set to `True`.

### Class Hierarchy

The class hierarchy for watermarking is structured as follows:

```
ParagraphItem
    |
    Watermark
        |
        PictureWatermark
```

### Public Constructors

The following constructors are available for initializing instances of the `PictureWatermark` class:

| Name | Description |
| --- | --- |
| PictureWatermark.PictureWatermark() | Initializes a new instance of the PictureWatermark class. |
| PictureWatermark.PictureWatermark(Image, bool) | Initializes a new instance of the PictureWatermark class with specified image and washout settings. |

## Code Example

Here is a basic example of how to use the `PictureWatermark` class:

```csharp
using Syncfusion.DocIO;
using System.Drawing;

// Initialize a new instance of PictureWatermark
PictureWatermark watermark = new PictureWatermark();

// Set the picture to be used as the watermark
watermark.Picture = new Image(FilePath);

// Set the scaling
watermark.Scale = 50;

// Set the washout effect
watermark.Washout = true;

// Apply the watermark to the document
document.Watermark = watermark;
```

## API Reference

### PictureWatermark Class

#### Constructors

1. **PictureWatermark()**
   - Initializes a new instance of the PictureWatermark class.
   
2. **PictureWatermark(Image image, bool washout)**
   - Initializes a new instance of the PictureWatermark class with the specified image and washout effect settings.

#### Properties

- **Picture:** Gets or sets the image to be used as the watermark.
- **Scale:** Gets or sets the scaling of the watermark (range 0-100%).
- **Washout:** Gets or sets whether to apply the washout effect to the watermark.

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| image | Image | The image to be used as the watermark. |
| washout | bool | Determines whether the washout effect is applied. |

---

<!-- tags: [Syncfusion Winforms, DocIO, PictureWatermark, Watermark, Winforms API] keywords: [PictureWatermark, Watermark, Washout, Scaling, DocIO, Syncfusion, C#] -->
```