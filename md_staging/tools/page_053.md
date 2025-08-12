```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_053.jpeg
document_name: tools
page_number: 053
page_id: tools#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:18:35Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to arrange items in an oval structure.
- Details the use of linear item arrangement.
- Describes the Perspective property for adjusting view size.
- Outlines the TransitionSpeed property for controlling rotation speed.

## Content

### 3.2.3.1.3 Oval
Items will be arranged in an oval structure.

#### Code Example
```csharp
this.carousel1.CarouselPath = CarouselPath.Oval;
```

```vb
Me.carousel1.CarouselPath = CarouselPath.Oval
```

### 3.2.3.1.4 Linear
Items will be arranged in a linear structure.

#### Code Example
```csharp
this.carousel1.CarouselPath = CarouselPath.Linear;
```

```vb
Me.carousel1.CarouselPath = CarouselPath.Linear
```

### 3.2.3.2 Perspective
The **Perspective** property is used to increase or decrease the size of the elliptical view of the control. It accepts float values, so the users can enlarge or shrink the elliptical view with respect to small values too.

#### Code Example
```csharp
this.carousel1.Perspective = 4f;
```

```vb
Me.carousel1.Perspective = 4f;
```

### 3.2.3.3 Transition Speed
The **TransitionSpeed** property enables the items in the control to be rotated at a user-defined speed.

## API Reference
- **CarouselPath**: Enumerates the options for arranging items in a carousel control.
  - **Oval**: Arranges items in an oval structure.
  - **Linear**: Arranges items in a linear structure.
- **Perspective**: Property to adjust the size of the elliptical view, accepting float values.
- **TransitionSpeed**: Property to control the rotation speed of items in the control.

## Code Examples
The following examples demonstrate how to configure the carousel control using the discussed properties.

### C# Example
```csharp
this.carousel1.CarouselPath = CarouselPath.Oval;
this.carousel1.Perspective = 4f;
this.carousel1.TransitionSpeed = 10;
```

### VB Example
```vb
Me.carousel1.CarouselPath = CarouselPath.Oval
Me.carousel1.Perspective = 4f;
Me.carousel1.TransitionSpeed = 10
```

### Note:
- The **TransitionSpeed** property accepts integer values to define the speed of rotation.
- Ensure that the carousel control is appropriately initialized before using these properties.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Carousel Control, CarouselPath, Perspective, TransitionSpeed] keywords: [item arrangement, oval structure, linear structure, elliptical view, rotation speed] -->
```