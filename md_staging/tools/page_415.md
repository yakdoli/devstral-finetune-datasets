```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_415.jpeg
document_name: tools
page_number: 415
page_id: tools#page_415
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:11:54Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Setting 3D Border Styles

### Setting a SunkenInner 3D Border Style

```vb
' Setting 3D border style
Me.monthCalendarAdv1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
' Setting "SunkenInner" 3D border style
Me.monthCalendarAdv1.Border3DStyle = System.Windows.Forms.Border3DStyle.SunkenInner
```

![Figure: Border3DStyle = "SunkenInner"](image.png)

**Figure 213: Border3DStyle = "SunkenInner"**

### Note: MonthCalendarAdv ThemedBorder Property

**Note:** The `MonthCalendarAdv.ThemedBorder` property should be set to `false` to make the 3D border setting effective. Refer to **Visual Settings**.  
[Visual Settings.](#visual-settings)

## Setting Border Sides and Color

### C#

```csharp
// Setting border to "All" sides
this.monthCalendarAdv1.BorderSides = System.Windows.Forms.Border3DSide.All;
// Setting color for 2D border
this.monthCalendarAdv1.BorderColor = System.Drawing.Color.DodgerBlue;
```

### VB.NET

```vb
' Setting border to "All" sides
Me.monthCalendarAdv1.BorderSides = System.Windows.Forms.Border3DSide.All
' Setting color for 2D border
this.monthCalendarAdv1.BorderColor = System.Drawing.Color.DodgerBlue
```

## Cross References

See also: `Visual Settings` for more information.

<!-- tags: [syncfusion, winforms, border styles, visual settings, monthcalendaradv] keywords: [border3dstyle, sunkeninner, themedborder, fixed3d, bordercolor, dodgerblue] -->
```