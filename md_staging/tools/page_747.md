```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_747.jpeg
document_name: tools
page_number: 747
page_id: tools#page_747
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:33:01Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Overview of various essential tools and functionalities for Windows Forms.
- Explanation of how formatted text and RightToLeft properties can be utilized for enhanced user experience.
- Demonstration of code examples in both C# and VB.NET for implementing these features.

## Content

### ClipMode Property

#### [VB.NET]
```vb
Me.integerTextBox1.ClipMode =
Syncfusion.Windows.Forms.Tools.CurrencyClipModes.IncludeFormatting
```

### Formatted Text

Formatted text can be displayed using the below given property.

| IntegerTextBox Property | Description |
|--------------------------|-------------|
| FormattedText           | Returns the formatted text with the formatting. |

#### [C#]
```csharp
this.integerTextBox1.FormattedText = "Hello";
```

#### [VB.NET]
```vb
Me.integerTextBox1.FormattedText = "Hello"
```

### RightToLeft

The text can be displayed from right to left for RTL languages using this property.

| IntegerTextBox Property | Description |
|--------------------------|-------------|
| RightToLeft             | Indicates whether the component should draw right-to-left for RTL languages. The default value is set to 'False'. |

#### Note:
The `RightToLeft` property will be automatically set to 'True' for RTL languages.

#### [C#]
```csharp
this.integerTextBox1.RightToLeft =
System.Windows.Forms.RightToLeft.Yes;
```

#### [VB.NET]
```vb
Me.integerTextBox1.RightToLeft = System.Windows.Forms.RightToLeft.Yes
```

## API Reference
- **Property**: `ClipMode`
  - Type: `CurrencyClipModes`
  - Description: Specifies the mode used to clip the text.
  - Values:
    - `IncludeFormatting`: Includes formatting in the clipping process.

- **Property**: `FormattedText`
  - Type: `string`
  - Description: Returns the text with formatting applied.

- **Property**: `RightToLeft`
  - Type: `RightToLeft`
  - Description: Determines the text layout direction.
  - Values:
    - `No`: Text is read from left to right.
    - `Yes`: Text is read from right to left.

## Code Examples

#### C#
```csharp
// Setting ClipMode
this.integerTextBox1.ClipMode = Syncfusion.Windows.Forms.Tools.CurrencyClipModes.IncludeFormatting;

// Setting FormattedText
this.integerTextBox1.FormattedText = "Hello";

// Setting RightToLeft
this.integerTextBox1.RightToLeft = System.Windows.Forms.RightToLeft.Yes;
```

#### VB.NET
```vb
' Setting ClipMode
Me.integerTextBox1.ClipMode = Syncfusion.Windows.Forms.Tools.CurrencyClipModes.IncludeFormatting

' Setting FormattedText
Me.integerTextBox1.FormattedText = "Hello"

' Setting RightToLeft
Me.integerTextBox1.RightToLeft = System.Windows.Forms.RightToLeft.Yes
```

## Cross References

- **See also**: [WinForms Text Formatting Guide](#winforms-text-formatting-guide)
- **See also**: [RTL Language Support in WinForms](#rtl-language-support-in-winforms)

<!-- tags: [Syncfusion, WinForms, Tools, Text Formatting, RightToLeft, FormattedText] keywords: [formatted text, rtl, clipmode, integer textbox, windows forms, winforms, properties] -->
```