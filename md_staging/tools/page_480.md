```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_480.jpeg
document_name: tools
page_number: 480
page_id: tools#page_480
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:15:19Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Border Styling in DateTimePickerAdv

#### C#

```csharp
// Sets 2D border
this.dateTimePickerAdv1.BorderStyle = 
    System.Windows.Forms.BorderStyle.FixedSingle;
// Sets 2D border style
this.dateTimePickerAdv1.BorderSingle = 
    System.Windows.Forms.ButtonBorderStyle.Dashed;
// Sets border for all the side of the control
this.dateTimePickerAdv1.BorderSides = 
    System.Windows.Forms.Border3DSide.All;
// Sets color for the 2D border
this.dateTimePickerAdv1.BorderColor = System.Drawing.Color.SteelBlue;

// Sets 3D border
this.dateTimePickerAdv1.BorderStyle = 
    System.Windows.Forms.BorderStyle.Fixed3D;
// Sets SunkenInner 3D border style
this.dateTimePickerAdv1.Border3DStyle = 
    System.Windows.Forms.Border3DStyle.SunkenInner;
```

#### VB.NET

```vb
'Sets 2D border
Me.dateTimePickerAdv1.BorderStyle = 
    System.Windows.Forms.BorderStyle.FixedSingle
'Sets 2D border style
Me.dateTimePickerAdv1.BorderSingle = 
    System.Windows.Forms.ButtonBorderStyle.Dashed
'Sets border for all the side of the control
Me.dateTimePickerAdv1.BorderSides = 
    System.Windows.Forms.Border3DSide.All
'Sets color for the 2D border
Me.dateTimePickerAdv1.BorderColor = System.Drawing.Color.SteelBlue

'Sets 3D border
Me.dateTimePickerAdv1.BorderStyle = 
    System.Windows.Forms.BorderStyle.Fixed3D
'Sets SunkenInner 3D border style
Me.dateTimePickerAdv1.Border3DStyle = 
    System.Windows.Forms.Border3DStyle.SunkenInner
```

### Border Styles Visualization

![Border Styles](https://example.com/sunken-inner-3d-dashed-2d)

The image shows two DateTimePickerAdv controls with different border styles:
- **Left**: A "SunkenInner" 3D border style.
- **Right**: A "Dashed" 2D border style.

## API Reference

### Border Styles Properties

- **`BorderStyle`**:
  - Type: `System.Windows.Forms.BorderStyle`
  - Description: Gets or sets the border style of the control.
  - Values:
    - `FixedSingle`
    - `Fixed3D`

- **`BorderSingle`**:
  - Type: `System.Windows.Forms.ButtonBorderStyle`
  - Description: Gets or sets the style of the border.
  - Values:
    - `Dashed`

- **`BorderSides`**:
  - Type: `System.Windows.Forms.Border3DSide`
  - Description: Gets or sets the sides of the 3D border.

- **`Border3DStyle`**:
  - Type: `System.Windows.Forms.Border3DStyle`
  - Description: Gets or sets the 3D style of the border.
  - Values:
    - `SunkenInner`

- **`BorderColor`**:
  - Type: `System.Drawing.Color`
  - Description: Gets or sets the color of the 2D border.

## Code Examples

### Example: Setting Border Styles Programmatically

#### C#

```csharp
// Create a DateTimePickerAdv instance
DateTimePickerAdv dateTimePicker = new DateTimePickerAdv();

// Set 2D border style
dateTimePicker.BorderStyle = BorderStyle.FixedSingle;
dateTimePicker.BorderColor = Color.SteelBlue;

// Set 3D border style
dateTimePicker.BorderStyle = BorderStyle.Fixed3D;
dateTimePicker.Border3DStyle = Border3DStyle.SunkenInner;
```

#### VB.NET

```vb
' Create a DateTimePickerAdv instance
Dim dateTimePicker As New DateTimePickerAdv()

' Set 2D border style
dateTimePicker.BorderStyle = BorderStyle.FixedSingle
dateTimePicker.BorderColor = Color.SteelBlue

' Set 3D border style
dateTimePicker.BorderStyle = BorderStyle.Fixed3D
dateTimePicker.Border3DStyle = Border3DStyle.SunkenInner
```

## Page-Level Navigation/TOC

- [Essential Tools for Windows Forms]
  - Overview
  - Border Styling in DateTimePickerAdv
  - Border Styles Visualization
  - API Reference
  - Code Examples

## Cross References

- See also:
  - [Border Style Overview](#border-style-overview)
  - [DateTimePickerAdv Control](#datetimepickeradv-control)

<!-- tags: [windows forms, datetimepickeradv, border styles, essential tools, winforms, syncfusion] keywords: [border, style, 2d, 3d, control, color, dashed, sunkeninner] -->
```