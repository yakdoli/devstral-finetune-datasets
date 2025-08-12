```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_344.jpeg
document_name: tools
page_number: 344
page_id: tools#page_344
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:06:51Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### ButtonControlAdv Visual Styles

The following code snippet demonstrates how to set the "OfficeXP" style for the ButtonAdv control using C#:

```csharp
this.buttonAdv1.UseVisualStyle = Syncfusion.Windows.Forms.UseStyle.True;
// Sample code for setting "OfficeXP" style for ButtonAdv
this.buttonAdv1.Appearance = Syncfusion.Windows.Forms.ButtonAppearance.OfficeXP;
```

The equivalent VB.NET code is as follows:

```vb
Me.buttonAdv1.UseVisualStyle = Syncfusion.Windows.Forms.UseStyle.True
' Sample code for setting "OfficeXP" style for ButtonAdv
Me.buttonAdv1.Appearance = Syncfusion.Windows.Forms.ButtonAppearance.OfficeXP
```

The available visual styles for the ButtonControlAdv are shown in the figure below.

![Visual Styles for ButtonAdv](https://i.imgur.com/imadeup.png)
*Figure 155: Visual Styles for ButtonAdv*

#### Note: While mouse hovering over the OfficeXP, Office2003 and WindowsXP at run time, the button will be painted with some standard colors. This is an inbuilt feature in the ButtonControlAdv.*

### Office Color Themes

The **ButtonControlAdv** supports all the three **OfficeColor Schemes** when **ButtonAdv.Appearance** is set to `Office2007`. Similarly, you can set `Blue` and `Black` color schemes also. The default value is `Blue`.

#### Setting the "Silver" Color Scheme

The following code snippet demonstrates how to set the "Silver" color scheme for the ButtonAdv control using C#:

```csharp
// Sample code for setting "Silver" color scheme for ButtonAdv
this.buttonAdv1.Office2007ColorScheme = Syncfusion.Windows.Forms.Office2007Theme.Silver;
```

The equivalent VB.NET code is as follows:

```vb
' Sample code for setting "Silver" color scheme for ButtonAdv
Me.buttonAdv1.Office2007ColorScheme = Syncfusion.Windows.Forms.Office2007Theme.Silver
```

This concludes the explanation of setting visual styles and color themes for the ButtonControlAdv in Syncfusion WinForms.

<!-- tags: [Syncfusion Winforms, ButtonControlAdv, Visual Styles, Office Color Themes] keywords: [ButtonAdv, OfficeXP, Office2007, OfficeColor Schemes, Silver, Blue, Black, UseVisualStyle, Appearance, Office2007Theme, Syncfusion.Windows.Forms] -->
```