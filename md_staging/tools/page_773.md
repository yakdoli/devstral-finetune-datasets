```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_773.jpeg
document_name: tools
page_number: 773
page_id: tools#page_773
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:32:53Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Describes specific options and properties for controlling culture settings in the PercentTextBox control.
- Focuses on language-specific configurations and inheritance rules for formatting.
- Demonstrates how to set the culture for the PercentTextBox control in C# and VB.NET.

## Content

### Culture Settings

| **Property** | **Description** |
|--------------|-----------------|
| It includes the below given options. | None, <br> CurrentCulture, <br> UICulture and <br> InstalledCulture. |
| UseUserOverride | Specifies if the NumberFormatInfo used for formatting will use the User Overrides for the culture. The default value is set to 'True'. |

#### Sample Code: Setting Culture in C#

```csharp
this.percentTextBox1.Culture = new System.Globalization.CultureInfo("ar-JO");
this.percentTextBox1.CurrentCultureRefresh = true;
this.percentTextBox1.SpecialCultureValue = Syncfusion.Windows.Forms.Tools.SpecialCultureValues.None;
this.percentTextBox1.UseUserOverride = true;
```

#### Sample Code: Setting Culture in VB.NET

```vb
Me.percentTextBox1.Culture = New System.Globalization.CultureInfo("ar-JO")
Me.percentTextBox1.CurrentCultureRefresh = True
Me.percentTextBox1.SpecialCultureValue = Syncfusion.Windows.Forms.Tools.SpecialCultureValues.None
Me.percentTextBox1.UseUserOverride = True
```

![Figure: Culture Set for the PercentTextBox Control](./Culture_Set_for_PercentTextBox.png)
*Figure 488: Culture Set for the PercentTextBox Control*

### RefreshCulture Method

> **Note:** The RefreshCulture() method can be used to refresh and reapply the culture specific settings.

A sample which demonstrates the Culture Settings of the PercentTextBox control is available in the below sample installation path.

## API Reference (if applicable)

### Properties

- **Culture:** System.Globalization.CultureInfo
- **CurrentCultureRefresh:** Boolean
- **SpecialCultureValue:** SpecialCultureValues
- **UseUserOverride:** Boolean

## Code Examples

### Setting the Culture for PercentTextBox

#### C# Example

```csharp
this.percentTextBox1.Culture = new System.Globalization.CultureInfo("ar-JO");
```

#### VB.NET Example

```vb
Me.percentTextBox1.Culture = New System.Globalization.CultureInfo("ar-JO")
```

### Refreshing Culture Settings

To refresh the culture settings, you can call the `RefreshCulture()` method:

#### C# Example

```csharp
this.percentTextBox1.RefreshCulture();
```

#### VB.NET Example

```vb
Me.percentTextBox1.RefreshCulture()
```

## Cross References

- See also: [Configuring Globalization and Localization Settings in Syncfusion WinForms](#)
- See also: [Syncfusion Windows Forms PercentTextBox Control Overview](#)

<!-- tags: [windows-forms, culture-settings, percenttextbox, globalization, localization, culture-refresh] keywords: [percenttextbox, culture, globalization, localization, user-override, specialculturevalue, refreshculture()] -->
```