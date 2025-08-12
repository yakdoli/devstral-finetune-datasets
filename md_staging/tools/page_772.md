```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_772.jpeg
document_name: tools
page_number: 772
page_id: tools#page_772
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10::33:40Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Default description of the tool and its functionality in Windows Forms.
- Focus on advanced features and implementation details of the PercentTextBox control.
- Discussion of culture settings and handling of numeric displays in Windows Forms.

## Content

### EnforceMinMaxDuringValidating

- **Property**: EnforceMinMaxDuringValidating
- **Description**: If the specified min and max values are not satisfied, the Validating event will handle and cancel when this property is set to 'True'.

#### Code Examples
##### C#
```csharp
this.percentTextBox1.MaxValue = 6;
this.percentTextBox1.MinValue = -6;
this.percentTextBox1.EnforceMinMaxDuringValidating = true;
```

##### VB.NET
```vb
Me.percentTextBox1.MaxValue = 6
Me.percentTextBox1.MinValue = -6
Me.percentTextBox1.EnforceMinMaxDuringValidating = True
```

### Methods Associated with Properties

| Methods                  | Description                                 |
|--------------------------|---------------------------------------------|
| ResetMaxValue            | Resets the MaxValue property to its default value. |
| ResetMinValue            | Resets the MinValue property to its default value. |

### 3.5.8.5.3.3 Culture Settings

This section discusses the Culture settings of the PercentTextBox control.

#### PercentTextBox Properties

| PercentTextBox Properties     | Description                                 |
|-------------------------------|---------------------------------------------|
| Culture                       | Gets / sets the culture for numeric display formatting. |
| CurrentCultureRefresh         | Indicates whether the Culture property should be refreshed upon culture change. |
| SpecialCultureValue           | Gets / sets the mode for the culture settings. |

## API Reference

### Properties

- **Culture**: Type - CultureInfo, Gets or sets the culture information for numeric display.
- **CurrentCultureRefresh**: Type - Boolean, Gets or sets whether to refresh the culturally dependent properties.
- **SpecialCultureValue**: Type - CultureMode, Gets or sets the specific culture mode.

## Code Examples

The examples illustrate how to configure and use the PercentTextBox control with culture settings.

### C#

```csharp
this.percentTextBox1.Culture = System.Globalization.CultureInfo.GetCultureInfo("en-US");
this.percentTextBox1.CurrentCultureRefresh = true;
this.percentTextBox1.SpecialCultureValue = System.Globalization.CultureMode.User;
```

### VB.NET

```vb
Me.percentTextBox1.Culture = System.Globalization.CultureInfo.GetCultureInfo("en-US")
Me.percentTextBox1.CurrentCultureRefresh = True
Me.percentTextBox1.SpecialCultureValue = System.Globalization.CultureMode.User
```

## Page-level Navigation/TOC (if applicable)

### Other Sections

- EnforceMinMaxDuringValidating
- Methods associated with the properties
- Culture Settings

## Cross References

- See also: numerical controls, textbox controls, and globalization and localization in Windows Forms.

## RAG Annotations

<!-- tags: [PercentTextBox, WinForms, CultureSettings, NumericControls, Globalization, Localization, EnforceMinMax, ValidatingEvent, C#, VB.NET] -->
```