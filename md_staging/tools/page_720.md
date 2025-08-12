```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_720.jpeg
document_name: tools
page_number: 720
page_id: tools#page_720
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:30:26Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Discusses the alignment and orientation properties of the spin button in a `DomainUpDownExt` control.
- Covers how to change the orientation and alignment of the spin button using specific properties.

## 3.5.8.2.3.2 SpinButton
This section will discuss the properties which control the alignment and orientation of the spin button in a `DomainUpDownExt` control.

### SpinButton in a DomainUpDownExt Control

<figure>
 <img src="image.png" alt="SpinButton in a DomainUpDownExt Control" />
 <figcaption>Figure 449: SpinButton in a DomainUpDownExt Control</figcaption>
</figure>

### Orientation

#### The spin button orientation can be changed to vertical or horizontal using the SpinOrientation property.

```csharp
// Spin button will be oriented horizontally.
this.domainUpDownExt1.SpinOrientation = Orientation.Horizontal;
// Spin button will be oriented vertically.
this.domainUpDownExt1.SpinOrientation = Orientation.Vertical;
```

```vb
' SpinButton will be oriented horizontally.
Me.domainUpDownExt1.SpinOrientation = Orientation.Horizontal
' SpinButton will be oriented vertically.
Me.domainUpDownExt1.SpinOrientation = Orientation.Vertical
```

<figure>
 <img src="image.png" alt="SpinButton Orientation = Horizontal and Vertical" />
 <figcaption>Figure 450: SpinButton Orientation = Horizontal and Vertical</figcaption>
</figure>

### Alignment

#### The spin button alignment can be set through the UpDownAlign property. By default it is set to right.

```csharp
// [C#]
```

## API Reference
- **Property**: `SpinOrientation`
  - Type: `Orientation`
  - Description: Controls the orientation of the spin button.
  - Possible values: `Horizontal`, `Vertical`
- **Property**: `UpDownAlign`
  - Type: `TextAlign`
  - Description: Controls the alignment of the spin button.
  - Default value: `Right`

## Code Examples
- **C#**: Demonstrates setting the orientation and alignment of the spin button.
- **VB.NET**: Demonstrates setting the orientation and alignment of the spin button.

## Page-level Navigation/TOC
- 3.5.8.2.3.2 SpinButton
  - Orientation
  - Alignment

<!-- tags: [spinbutton, domainupdownext, orientation, alignment, winforms] keywords: [SpinOrientation, UpDownAlign, horizontal, vertical, right] -->
```