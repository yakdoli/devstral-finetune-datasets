```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_252.jpeg
document_name: diagram
page_number: 252
page_id: diagram#page_252
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:21:57Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview

- Showcasing how to manage dynamic properties within diagrams.
- Highlighting the use of built-in UI dialog to add and remove properties.
- Illustrating the process of defining and managing additional information in a diagram.

## Content

### Dynamic Properties Management in Diagrams

The image depicts a **Properties** window used to manage additional information in a diagram, specifically aimed at demonstrating how properties can be added dynamically.

#### 1. **Built-in UI dialog to add additional information**

The left side of the image shows a Properties dialog box where developers can add, edit, or remove properties for an object. Key details include:

- **Designation:** Developer
- **ID:** 1234
- **Name:** Mark

This UI dialog provides a straightforward interface for users to modify these properties, enabling flexibility in customizing node or object behaviors.

#### 2. **Dynamic Property Definition**

The central part of the image shows a **Define Property** dialog, which allows the user to create new properties by specifying:

- **Name**: The name of the property.
- **Type**: The data type, set here to **String**.
- **Value**: The value associated with the property.

#### 3. **Property Details in the Diagram**

The right side of the image highlights aspects of the **BitmapNode9** object, showcasing its detailed properties:

- **Dialogue to Add/Remove Properties**: Indicated by an orange underline and arrow.
- **Dialogue to Add New Properties**: Highlighted through a separate dialog box.
- **Property to Add Additional Information**: Shown as an orange arrow pointing to the PropertyBag section.

### Features and Properties in Use

#### Node and Style Properties

- **Name:** BitmapNode9
- **FullScreen:** Model.BitmapNode9
- **GraphicsPath:** System.Drawing.Draw
- **Image:** 
  - **AllowMoveX:** True
  - **AllowMoveY:** True
- **Edit Style:** 
  - **EnableCentralPoint:** True
  - **Enable Connections:** False
  - **Enable Constraints:** False
  - **Enable Selection:** False
- **Line Hit Test:** 6
- **Line Style:** 
  - **Width:** 1, Color: [Trans]

#### Positioning and Scale

- **Pin Point Offset:** 50, 50
- **Pivot Point:** 70, 190
- **Node Scale:** 1 px = 1 px
- **Size:** 100, 100
- **Shadow Style:** (False, Color [A=128, #FFFFFF])

#### Visibility and Layering

- **Visible:** True
- **ZOrder:** 0

#### PropertyBag

- The PropertyBag section indicates the dynamic property data dictionary, providing flexibility to manage custom properties.

## API Reference

- **Namespace:** Syncfusion.Windows.Forms.Tools
- **Class:** Model.BitmapNode9
- **Properties:** 
  - **Name:** String
  - **Type:** String
  - **Value:** Object

## Code Examples

The image does not contain explicit code examples; however, a basic representation of adding properties dynamically might include:

```csharp
using Syncfusion.Windows.Forms.Tools;

// Create a dynamic property for an object
var propertyBag = node.PropertyBag;
propertyBag.Add("CustomProperty", "StringValue");
```

## Page-level Navigation/TOC

- **Section 1:** Dynamic Properties Management in Diagrams
  - Built-in UI dialog to add additional information
  - Property definition
  - Node and style properties
  - Positioning and scale
  - Visibility and layering

## Cross References

- **See also:**
  - PropertyBag API documentation
  - Diagram customization guide

<!-- tags: [diagram, windows forms, dynamic properties, properties, management, UI dialog] keywords: [syncfusion, windowsforms, bitmapnode9, property bag, dynamic property, property definition, visibility, z-order, node scale] -->
```