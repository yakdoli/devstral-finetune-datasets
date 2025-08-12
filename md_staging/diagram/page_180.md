```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_180.jpeg
document_name: diagram
page_number: 180
page_id: diagram#page_180
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:17:32Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

### Adjusting Vertical Ruler Text Style

By modifying the `VerticalRuler.TextStyle` properties in a Syncfusion Diagram control for Windows Forms, you can customize the appearance of the vertical ruler. Here are the properties and their settings:

```csharp
Me.diagram1.VerticalRuler.TextStyle.Bold = True
Me.diagram1.VerticalRuler.TextStyle.Italic = True
Me.diagram1.VerticalRuler.TextStyle.PointSize = 20
Me.diagram1.VerticalRuler.TextStyle.Strikout = True
Me.diagram1.VerticalRuler.TextStyle.Style = System.Drawing.FontStyle.Bold
Me.diagram1.VerticalRuler.TextStyle.Underline = True
Me.diagram1.VerticalRuler.TextStyle.Unit = MeasureUnits.Point
```

#### Sample Diagram

The resulting vertical ruler with these settings is shown in the following diagram:

![](https://i.imgur.com/vertical_ruler_sample.png)

**Figure 111: Vertical ruler Property Settings**

### Customizing Horizontal Ruler Properties

The same properties can be set separately for the horizontal ruler by using `HorizontalRuler` instead of `VerticalRuler`. Here's how to apply the same settings for the horizontal ruler:

```csharp
[C#]
```

## Adjusting Horizontal Ruler Text Style

To apply similar adjustments to the horizontal ruler, replace `VerticalRuler` with `HorizontalRuler` in the property settings as shown above.

#### Example: Setting Horizontal Ruler Properties

The following code snippet demonstrates how to customize the horizontal ruler's text style properties:

```csharp
Me.diagram1.HorizontalRuler.TextStyle.Bold = True
Me.diagram1.HorizontalRuler.TextStyle.Italic = True
Me.diagram1.HorizontalRuler.TextStyle.PointSize = 20
Me.diagram1.HorizontalRuler.TextStyle.Strikout = True
Me.diagram1.HorizontalRuler.TextStyle.Style = System.Drawing.FontStyle.Bold
Me.diagram1.HorizontalRuler.TextStyle.Underline = True
Me.diagram1.HorizontalRuler.TextStyle.Unit = MeasureUnits.Point
```

### Summary

By adjusting the `TextStyle` properties of both vertical and horizontal rulers in a Syncfusion Diagram control for Windows Forms, you can control the font, size, style, and other visual aspects of the ruler text. This allows for a customized and professional appearance tailored to your application's needs.

```html
<!-- tags: [diagram, windows forms, ruler, text style, vertical ruler, horizontal ruler, bold, italic, point size, underline, strikeout] keywords: [diagram, ruler properties, windows forms, vertical ruler, horizontal ruler, text styling, bold, italic, point size, underline, strikeout] -->
```