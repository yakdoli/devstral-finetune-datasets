```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_055.jpeg
document_name: tools
page_number: 055
page_id: tools#page_055
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:17:30Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to assign an image list to a control directly.
- Describes populating a control with images from an image list.
- Methods for fetching images through file paths or folder locations.
- Describes properties that control shadow, preview, highlight, and shade colors for images.
- Details touch interactions supported by the Carousel control, including pan, flick, pinch, and stretch.
- Introduces the CommandBars Package for creating and hosting ToolBars, ReBars, and StatusBars.

## Content

### 3.2.3.6 Properties

| Property             | Description                                                                                    | Data Type |
|----------------------|------------------------------------------------------------------------------------------------|-----------|
| ShowImageShadow      | Enables or disables shadows for the images.                                                   | bool      |
| ShowImagePreview     | Displays previews of the selected image at the center of the control.                        | bool      |
| Image Highlight Color| Apply the desired color for highlighting the selected image.                                   | Color     |
| Image ShadeColor     | Applies the desired color for shading the images at the back of the control.                  | Color     |

### 3.2.4 Touch Interactions

The Carousel control will respond to default touch interactions that substitute the standard mouse operations. Additionally, the pan, flick, pinch, and stretch operations are supported.

- Pan and flick: Initiates moving the items.
- Pinch and stretch: Will increase and decrease the perspective view of the items within the Carousel control.

---

### 3.3 CommandBars Package

The Essential Tools CommandBar implements a framework for creating and hosting ToolBars, ReBars, and StatusBars similar to those found in the Visual Studio .NET and Office XP user interfaces.

The three main classes of the CommandBar framework are CommandBarController, CommandBar, and ControlBar.

## API Reference

Not specified in this document section.

## Code Examples

Not specified in this document section.

## RAG Annotations

<!-- tags: [carousel, touch interactions, essential tools, windows forms, commandbars, toolbars, rebars, statusbars, image manipulation, property settings, version 11.4.0.26] keywords: [ShowImageShadow, ShowImagePreview, Image Highlight Color, Image ShadeColor, Pan, Flick, Pinch, Stretch] -->
```