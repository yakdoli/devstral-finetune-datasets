```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_818.jpeg
document_name: tools
page_number: 818
page_id: tools#page_818
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:36:42Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Focuses on globalization features in the CurrencyTextBox control.
- Highlights the use of `System.Globalization.CultureInfo` for locale-specific formatting.
- Describes how to set and refresh the culture for the CurrencyTextBox control.

## Content

### Globalization

The CurrencyTextBox class is globalization aware and uses `System.Globalization.CultureInfo` for locale-specific information. You can set the control's culture to any installed culture through its `culture` property.

#### CurrencyTextBox Properties

| CurrencyTextBox Properties             | Description                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------|
| **Culture**                             | It sets the culture that is used for formatting the numeric display.     |
| **CurrentCultureRefresh**               | Specifies whether the culture property is to be refreshed when the culture changes. |
| **SpecialCultureValue**                 | It sets the mode for the cultures. The options include:                   |
|                                         | - None,                                                                     |
|                                         | - CurrentCulture (default),                                                |
|                                         | - InstalledCulture,                                                        |
|                                         | - UICulture.                                                               |

#### Example

**Figure 521: CultureInfo="Arabic (Saudi Arabia)"**

![CultureInfo="Arabic (Saudi Arabia)"](example_image.png)

**C#:**

```csharp
this.currencyTextBox1.Culture = new System.Globalization.CultureInfo("ar-SA");
this.currencyTextBox1.CurrentCultureRefresh = true;
this.currencyTextBox1.SpecialCultureValue = Syncfusion.Windows.Forms.Tools.SpecialCultureValues.None;
```

**VB.NET:**

```vb
Me.currencyTextBox1.Culture = New System.Globalization.CultureInfo("ar-SA")
Me.currencyTextBox1.CurrentCultureRefresh = True
Me.currencyTextBox1.SpecialCultureValue = Syncfusion.Windows.Forms.Tools.SpecialCultureValues.None
```

### User Override for Culture

This section discusses how the user can manually specify the culture for the CurrencyTextBox control.

## API Reference

### Properties

- **Culture**  
  Sets the culture that is used for formatting the numeric display.  
  `Type: CultureInfo`

- **CurrentCultureRefresh**  
  Specifies whether the culture property is to be refreshed when the culture changes.  
  `Type: bool`

- **SpecialCultureValue**  
  Sets the mode for the cultures. Possible values are:  
  `Type: SpecialCultureValues`

## Code Examples

### C# Example

```csharp
this.currencyTextBox1.Culture = new System.Globalization.CultureInfo("ar-SA");
this.currencyTextBox1.CurrentCultureRefresh = true;
this.currencyTextBox1.SpecialCultureValue = Syncfusion.Windows.Forms.Tools.SpecialCultureValues.None;
```

### VB.NET Example

```vb
Me.currencyTextBox1.Culture = New System.Globalization.CultureInfo("ar-SA")
Me.currencyTextBox1.CurrentCultureRefresh = True
Me.currencyTextBox1.SpecialCultureValue = Syncfusion.Windows.Forms.Tools.SpecialCultureValues.None
```

<!-- tags: [Syncfusion, WinForms, CurrencyTextBox, CultureInfo, globalization] keywords: [CurrencyTextBox, CultureInfo, CurrentCultureRefresh, SpecialCultureValue] -->
``` 
