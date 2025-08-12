```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_520.jpeg
document_name: tools
page_number: 520
page_id: tools#page_520
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:18:17Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Setting User Colors and Custom Colors

The following code example demonstrates how to set user-defined and custom colors for a `ColorUIControl` in a Windows Forms application. It also shows how to resize the color cells using properties provided by the control.

#### C#

```csharp
{
    this.colorUIControl1.UserColors[ i ] = Color.FromArgb( 0, 0, i * 5 );
}

for ( int i = 0; i < this.colorUIControl1.UserCustomColors.Count; i ++ )
{
    this.colorUIControl1.UserCustomColors[ i ] = Color.FromArgb( i * 15, 0, 0 );
}

this.colorUIControl1.SelectedColorGroup = 
    Syncfusion.Windows.Forms.ColorUISelectedGroup.UserColors;

// Resize of ColorCells can be done using property UserColorsStretchOnResize.
this.colorUIControl1.UserColorsStretchOnResize = true;
```

#### VB.NET

```vb
[VB.NET]

Dim i As Integer
For i = 0 To Me.colorUIControl1.UserColors.Count - 1 Step i + 1
    Me.colorUIControl1.UserColors(i) = Color.FromArgb(0, 0, i * 5)
Next

Dim i As Integer
For i = 0 To Me.colorUIControl1.UserCustomColors.Count - 1 Step i + 1
    Me.colorUIControl1.UserCustomColors(i) = Color.FromArgb(i * 15, 0, 0)
Next

Me.colorUIControl1.SelectedColorGroup = 
    Syncfusion.Windows.Forms.ColorUISelectedGroup.UserColors

' Resize of ColorCells can be done using property UserColorsStretchOnResize.
Me.colorUIControl1.UserColorsStretchOnResize = True
```

#### Note: UserGroups should be selected in `ColorGroups` property to effect the above settings.

<!-- tags: [product, module, control, api, version?] keywords: [C#, VB.NET, Color, winforms, essential tools, custom colors, user colors, resize] -->
```