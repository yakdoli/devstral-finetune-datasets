```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_744.jpeg
document_name: tools
page_number: 744
page_id: tools#page_744
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:31:56Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the Culture Settings of the IntegerTextBox control.
- Explains the properties `CurrentCultureRefresh`, `SpecialCultureValue`, and `UseUserOverride`.
- Provides code examples in C# and VB.NET.

## Content

### Properties Related to Culture Settings

| Property             | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| CurrentCulture,     | Not filled in the current record. The table shows the properties `CurrentCulture`, `UICulture`, and `InstalledCulture`. |
|                     |                                                                 |
|                     |                                                                 |
| UseUserOverride     | Specifies if the `NumberFormatInfo` used for formatting will use the User Overrides for the culture. The default value is set to 'True'. |

### Code Examples

#### C#

```csharp
this.integerTextBox1.Culture 
  = new System.Globalization.CultureInfo("ar-SA");
this.integerTextBox1.CurrentCultureRefresh = true;
this.integerTextBox1.SpecialCultureValue = 
  Syncfusion.Windows.Forms.Tools.SpecialCultureValues.None;
this.integerTextBox1.UseUserOverride = true;
```

#### VB.NET

```vb
Me.integerTextBox1.Culture = New System.Globalization.CultureInfo("ar-SA")
Me.integerTextBox1.CurrentCultureRefresh = True
Me.integerTextBox1.SpecialCultureValue = 
  Syncfusion.Windows.Forms.Tools.SpecialCultureValues.None
Me.integerTextBox1.UseUserOverride = True
```

### Figure: Culture Set for the PercentTextBox Control

![Culture Set for the PercentTextBox Control](images/figure_470.png)

**Figure 470:** Culture Set for the PercentTextBox Control

#### Note: The `RefreshCulture()` method can be used to refresh and reapply the culture-specific settings.

### Sample Installation Path

A Sample which demonstrates the Culture Settings of the IntegerTextBox control is available in the below sample installation path:

- ..My Documents\Syncfusion\EssentialStudio\<Version Number\>Windows\Tools.Windows\Samples\2.0\Editors Package\EditorControls

## Cross References
- See also: `CultureInfo`, `CultureInfoRefresh`, `SpecialCultureValues`, `UseUserOverride`.

<!-- tags: [syncfusion, tools, integer textbox control, culture settings, winforms, ar-SA, user override, special culture values] keywords: [culture, formatting, user override, culture refresh, special culture, sample installation, percentage textbox] -->
```