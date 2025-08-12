```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_212.jpeg
document_name: edit
page_number: 212
page_id: edit#page_212
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:11Z
fidelity: lossless
 -->

# Essential Edit for Windows Forms

## Code Example

```vbnet
Me.editControl1.UserMarginWidth = 100
// Sets the User Margin to the Left.
Me.editControl1.UserMarginPlacement = Syncfusion.Windows.Forms.Edit.Enums.MarginPlacement.Left
```

## Color Settings

The following properties can be used to set the background color, text color, and border color of the user margin in the Edit Control.

| Edit Control Property             | Description                                                                 |
|------------------------------------|----------------------------------------------------------------------------|
| UserMarginBackgroundColor         | Specifies BrushInfo object that is used when the user margin is being drawn. |
| UserMarginTextColor               | Specifies default color of user margin text.                              |
| UserMarginBorderColor             | Specifies color of the user margin border.                                |

## Color Property Configuration Examples

### C# Example

```csharp
this.editControl1.UserMarginBackgroundColor = new Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.BackwardDiagonal, System.Drawing.Color.Brown, System.Drawing.Color.MistyRose);
this.editControl1.UserMarginBorderColor = Color.IndianRed;
this.editControl1.UserMarginTextColor = Color.Green;
```

### VB.NET Example

```vbnet
Me.editControl1.UserMarginBackgroundColor = New Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.BackwardDiagonal, System.Drawing.Color.Brown, System.Drawing.Color.MistyRose)
Me.editControl1.UserMarginBorderColor = Color.IndianRed
Me.editControl1.UserMarginTextColor = Color.Green
```

## Summary

This section explains how to configure the placement and styling of the user margin within the Syncfusion Windows Forms Edit Control. Properties like `UserMarginWidth`, `UserMarginPlacement`, `UserMarginBackgroundColor`, `UserMarginTextColor`, and `UserMarginBorderColor` are crucial for customizing the appearance and behavior of the user margin.

## Page-level Navigation/TOC
- [Top](#top)
- [Color Settings](#color-settings)
- [Code Example](#code-example)
- [Color Property Configuration Examples](#color-property-configuration-examples)

<!-- tags: [Syncfusion Winforms, Edit Control, Margin Placement, Margin Color Settings] keywords: [marginwidth, usermarginplacement, marginbackgroundcolor, margintextcolor, marginbordercolor] -->
```