```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_819.jpeg
document_name: tools
page_number: 819
page_id: tools#page_819
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:37:49Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Covers CurrencyTextBox properties and culture-related functionality.
- Explains how to use culturally aware formatting for currency input.
- Describes the Culture name formats and their display options.

## CurrencyTextBox Properties

| CurrencyTextBox Properties | Description |
|---------------------------|-------------|
| UseUserOverride           | Specifies if the NumberFormatInfo used for formatting will use the User overrides for the culture. |

### Code Examples

#### C#
```csharp
this.currencyTextBox1.UseUserOverride = false;
this.currencyTextBox1.Culture
    = new CultureInfo(CultureInfo.CurrentUICulture.LCID, this.currencyTextBox1.UseUserOverride);
```

#### VB.NET
```vb
Me.currencyTextBox1.UseUserOverride = False
Me.currencyTextBox1.Culture
    = New CultureInfo(CultureInfo.CurrentUICulture.LCID, Me.currencyTextBox1.UseUserOverride)
```

### Culture name

- The culture name can be displayed in different formats according to the specified culture value.
- Refer to the table below for detailed descriptions.

#### CurrencyTextBox.Culture Properties

| CurrencyTextBox.Culture Properties | Description |
|-------------------------------------|-------------|
| DisplayName                         | Gets the culture name in the format "<language full>(<country/region full>)" in the language of the localized version of the .NET framework. |
| EnglishName                         | Gets the culture name in the format "<language full>(<country/region full>)" in English. |
| NativeName                          | Gets the culture name in the format "<language full>(<country/region full>)" in the language that the culture is set to display. |
| ThreeLetterWindowsLanguageName      | Gets the three-letter code for the language as specified in the Windows API. |

### Illustration

The following figure illustrates this when the culture is 'en-US'.

---
### RAG Annotations
<!-- tags: CurrencyTextBox, CultureInfo, NumberFormatInfo, Culture, Windows Forms, Syncfusion Winforms, version: 11.4.0.26 -->
```