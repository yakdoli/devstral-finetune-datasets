```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_284.jpeg
document_name: diagram
page_number: 284
page_id: diagram#page_284
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:24:31Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates configuring margins and page sizes for printing in Windows Forms.
- Includes C# and VB.NET code examples for setting dimensions and printing functionality.

## Content

### Setting Margins and Page Sizes

#### C#
```csharp
// The margins are of size 1 inch or 25 mm.
int verticalMargin = 260;
int horizontalMargin = 260;

// The following units are in millimeters, so convert them to pixels.
float pageHeight = Diagram.MeasureUnitsConverter.Convert((2970 - (verticalMargin * 2)) / 10, MeasureUnits.Millimeter, MeasureUnits.Pixel);

// float pageHeight = bounds.Height;
float pageWidth = Diagram.MeasureUnitsConverter.Convert((2100 - (horizontalMargin * 2)) / 10, MeasureUnits.Millimeter, MeasureUnits.Pixel);

// Set the model height to twice the page height.
diagram1.Model.DocumentSize.Height = (int)pageHeight / 2;

// Set the model width to page width
diagram1.Model.DocumentSize.Width = (int)pageWidth;
this.PrintPreview();
```

#### VB.NET
```vb
' The desired page size is 21 x 29.7 centimeters.
' The margins are of size 1 inch or 25 mm.
Dim verticalMargin As Integer = 260
Dim horizontalMargin As Integer = 260

' The following units are in millimeters, so convert them to pixels.
Dim pageHeight As Single = Diagram.MeasureUnitsConverter.Convert((2970 - (verticalMargin * 2)) / 10, MeasureUnits.Millimeter, MeasureUnits.Pixel)

' float pageHeight = bounds.Height;
Dim pageWidth As Single = Diagram.MeasureUnitsConverter.Convert((2100 - (horizontalMargin * 2)) / 10, MeasureUnits.Millimeter, MeasureUnits.Pixel)

' Set the model height to twice the page height.
diagram1.Model.Size = New SizeF(pageWidth, pageHeight / 2)
Me.PrintPreview()
```

### Sample Availability

A sample which demonstrates Printing is available in the below sample installation path:

```
..\My Documents\Syncfusion\EssentialStudioVersion
Number\Windows\Diagram.Windows\Samples\2.0\Getting Started\Printing
```

## API Reference

### Methods
- `Diagram.MeasureUnitsConverter.Convert(sourceValue, sourceUnits, destinationUnits)`: Converts a value from one unit of measure to another.

### Classes
- `MeasureUnits`: Contains enumeration values for different units of measure (e.g., Millimeter, Pixel).

### Events
- `PrintPreview()`: Triggered to display a preview of the print output.

## Cross References
- See also: Printing in Windows Forms controls, MeasureUnitsConverter in Diagram API.

<!-- tags: [diagram, printing, windows forms, margins, page size, measureunitsconverter, syncfusion, winforms, csharp, vb.net] keywords: [printing, margins, page size, measure units, pdf, essential studio] -->
```
