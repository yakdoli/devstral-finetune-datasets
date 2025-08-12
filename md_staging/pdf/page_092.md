```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_092.jpeg
document_name: pdf
page_number: 092
page_id: pdf#page_092
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:29:06Z
fidelity: lossless
-->

## Overview

- Describes methods and properties related to setting layers, transparency, and transformations for graphics.
- Outlines the clientSize, color space, and layer properties for managing the graphics' layout.
- Explains the usage of matrix transformations and streaming for rendering and manipulating graphical contents.

## Content

### Methods

| Name              | Description                                     |
|-------------------|-------------------------------------------------|
| SetLayer         | Sets the layer for the graphics                |
| SetTransparency   | Sets transparency                              |
| SkewTransform     | Skews coordinate system axes                   |
| TranslateTransform | Translates coordinates by specified coordinates |

### Properties

| Name          | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| AutomaticFields | Gets the automatic fields                                                    |
| ClientSize        | Gets a SizeF structure that binds the region of the Graphics reduced by margins and page templates |
| ColorSpace       | Gets or sets the current color space                                      |
| Layer            | Gets the layer for the graphics, if exists                                |
| Matrix           | Gets the matrix reflecting current transformation                         |
| Page             | Gets the page for this graphics, if exists                                |
| Size             | Gets the size of the canvas                                                |
| StreamWriter     | Gets the stream writer                                                    |

### Units, Size and Co-ordinate System

The co-ordinate system is either Top or Left. Origin is translated depending on the margins and page templates. The measure units are points (1/72 inch). The **PdfUnitConverter** class enables to convert different measure units.

#### Size property of PdfGraphics
- Returns the size of the canvas.
- The **ClientSize** property returns a client area of the canvas, which might be smaller. Any output of the client area will not be visible.

### Graphics State and Co-ordinate System Manipulation

The **PdfGraphics** class allows manipulating with graphics state (save, restore) and coordinate system (rotate, translate, etc.).
- **Save and Restore** methods can be used for manipulating with graphics state.
- **TranslateTransform**, **RotateTransform**, etc., can be used for coordinate manipulations.
- Clip regions can be set using the **SetClip** method.

## API Reference (if applicable)
### Namespace, Class, Members

Refer to the methods and properties described above for specific details on functionality and usage.

## Code Examples (multi-language supported)
- No explicit code examples are provided in this section. Additional examples can be referenced in related documentation.

## Page-level Navigation/TOC (if applicable)
- None specified within the document body.

## Cross References
- See also: PdfGraphics, PdfUnitConverter, Syncfusion WinForms documentation.

<!-- tags: [pdfgraphics, pdflayer, pdflayout, coordinatetransformation, syncfusionwinforms, version11.4.0.26] keywords: [setlayer, settransparency, skewtransform, translatetransform, clientSize, colorSpace, layer, matrix, page, size, streamwriter, coordinatesystem, graphicsstate, save, restore] -->
```