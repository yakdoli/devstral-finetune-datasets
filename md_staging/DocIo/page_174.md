```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_174.jpeg
document_name: DocIo
page_number: 174
page_id: DocIo#page_174
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:38:43Z
fidelity: lossless
-->

## Overview
- Discusses "read-only" ShapeObject and InlineShapeObject classes, highlighting restrictions and exceptions for picture and textbox shapes.
- Explains the EntityType property of the ShapeObject class and the representation of inline shape objects in the InlineShapeObject class.
- Introduces the WPicture class for representing pictures in a Word document and its positioning properties.

## Content

### ShapeObject and InlineShapeObject Classes
**Note:** ShapeObject and InlineShapeObject classes are *"read only"* classes. You cannot modify shapes. An exception to this is the picture and textbox shape. All shapes except pictures and textbox shapes are only preserved.

#### ShapeObject Class
The ShapeObject class has only one public property – `EntityType`. This property defines the type of the entity and returns the `EntityType.Shape` for this class.

#### InlineShapeObject Class
The InlineShapeObject represents all the inline shape objects (except inline textboxes and pictures). Inline shape objects are shape objects which have Inline with text layout.

#### Class Hierarchy
```plaintext
ParagraphItem
|
  ShapeObject
  |
    InlineShapeObject
```

### ShapeObject Public Property
**Name**: EntityType  
**Description**: Gets the type of the entity.

### 4.4.1.4.1 Picture
The WPicture class represents a picture in the Word document.

#### Positioning Properties
A picture is a shape. Positioning properties of the WPicture class are almost the same as the other shapes. A picture is positioned by using the `VerticalPosition` and `HorizontalPosition` properties. The measure unit is Point. Relative positioning is defined by using the `HorizontalAlignment` and `VerticalAlignment` properties.

#### HorizontalAlignment Property Variants
The `HorizontalAlignment` property returns the object of the ShapeHorizontalAlignment type. The following are the variants for the `HorizontalAlignment` property:
- None
- Left

### Conclusion
This section explains the structure and usage of shape objects in documents, focusing on the limitations and properties of ShapeObject and InlineShapeObject classes. It also introduces the WPicture class for image handling in Word documents, detailing the positioning properties and alignment options.

## API Reference
### Properties
#### ShapeObject
- **Name**: `EntityType`
- **Description**: Gets the type of the entity.

#### WPicture
- **Properties**
  - `VerticalPosition`: Defines the vertical position of the picture in points.
  - `HorizontalPosition`: Defines the horizontal position of the picture in points.
  - `HorizontalAlignment`: Determines the horizontal alignment of the picture.
  - `VerticalAlignment`: Determines the vertical alignment of the picture.

## Code Examples
```csharp
// Example: Accessing EntityType of a ShapeObject
ShapeObject shape = document.Paragraphs[0].ShapeObjects[0];
EntityType entityType = shape.EntityType;

// Example: Setting HorizontalAlignment for a WPicture
WPicture picture = document.Sections[0].Paragraphs[0].Pictures[0];
picture.HorizontalAlignment = ShapeHorizontalAlignment.Left;
```

<!-- tags: [Syncfusion, DocIo, ShapeObject, InlineShapeObject, WPicture, WinForms, Version: 11.4.0.26] keywords: [shape, inline shape, picture, Word document, positioning, horizontal alignment, vertical alignment] -->
```