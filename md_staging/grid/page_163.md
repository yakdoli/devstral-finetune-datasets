```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_163.jpeg
document_name: grid
page_number: 163
page_id: grid#page_163
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:59:17Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
style4.Text = "____-__-____";
maskedEditStyle4.UseLocaleDefault = false;
maskedEditStyle4.UseUserOverride = true;
```

## Overview
- The page describes how to configure masked edit styles for grid cells in a Windows Forms application.
- It includes examples in both C# and VB.NET for setting up masked edit boxes.

## Content

### Setting Up Masked Edit Styles

In the following examples, we configure grid cells to use masked edit boxes for specific data types such as social security numbers and dates.

#### Example in VB.NET

```vb
grd.Controls(2, 3).Text = "First Name"
Dim style1 As GridStyleInfo = grd.Controls(2, 4)
Dim maskedEditStyle1 As GridMaskEditInfo = style1.MaskEdit
grd.Controls(4, 3).Text = "Last Name"
grd.Controls(8, 3).Text = "Social Security"
Dim style4 As GridStyleInfo = grd.Controls(8, 4)
Dim maskedEditStyle4 As GridMaskEditInfo = style4.MaskEdit

' Masked Edit Box 1
style1.CellType = "MaskEdit"
maskedEditStyle1.AllowPrompt = False
maskedEditStyle1.ClipMode = Syncfusion.Windows.Forms.Tools.ClipModes.ExcludeLiterals
style1.CultureInfo = New System.Globalization.CultureInfo("en-US")
maskedEditStyle1.DateSeparator = "--"
maskedEditStyle1.Mask = ">C<CCCCCCCCCC"
style1.MaxLength = 13
style1.AutoSize = True
maskedEditStyle1.SpecialCultureValue = Syncfusion.Windows.Forms.Tools.SpecialCultureValues.None
maskedEditStyle1.UseLocaleDefault = False
maskedEditStyle1.UseUserOverride = True

' Masked Edit Box 4
style4.CellType = "MaskEdit"
maskedEditStyle4.AllowPrompt = False
maskedEditStyle4.ClipMode = Syncfusion.Windows.Forms.Tools.ClipModes.IncludeLiterals
style4.CultureInfo = New System.Globalization.CultureInfo("en-US")
maskedEditStyle4.DateSeparator = "--"
maskedEditStyle4.Mask = "999-99-9999"
style4.MaxLength = 11
maskedEditStyle4.SpecialCultureValue = Syncfusion.Windows.Forms.Tools.SpecialCultureValues.None
style4.Text = "____-__-____"
maskedEditStyle4.UseLocaleDefault = False
maskedEditStyle4.UseUserOverride = True
```

## Tags and Keywords
<!-- tags: [Syncfusion Winforms, MaskEdit, GridStyleInfo, GridMaskEditInfo, CellType, Mask, LocaleDefault, UserOverride] keywords: [masked edit, grid cell, clipboard modes, culture, Custom masks] -->
```