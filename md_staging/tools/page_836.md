```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_836.jpeg
document_name: tools
page_number: 836
page_id: tools#page_836
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:37:43Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the use of the MaskedEditBox control for formatted text input.
- Highlighted examples of common masks for social security numbers, telephone numbers, dates, times, and names.
- Code examples showing how to include the required namespace in C# and VB.NET.

## Content

### MaskedEditBox through Designer

![MaskedEditBox created Through Designer](https://image-source.com/image836.jpg)
*Figure 533: MaskedEditBox created Through Designer*

#### Examples of Some Common Masks

| Mask             | Usage                                                                 |
|------------------|-----------------------------------------------------------------------|
| `####-##-####`   | US Social security number mask (the `#` symbol allows numeric entry only in that position and the `-` symbol is literal); Example 222-22-2222. |
| `(###) ### ####` | US Telephone number mask; Example (919) 481 1974.                     |
| `#####/#####`    | Short date mask; Example 04/14/2005.                                 |
| `##:##`          | Short time mask; Example 12:24.                                      |
| `>!?<???????????`| First name or last name; The first letter is uppercase and the other letters are all lowercase; Example: Syncfusion.             |

### Through Code

The MaskedEditBox control can be used programmatically through code as detailed below.

1. Include the required namespace.

```csharp
using Syncfusion.Windows.Forms.Tools;
```

```vbnet
Imports Syncfusion.Windows.Forms.Tools
```

## API Reference

### Namespaces
- **Syncfusion.Windows.Forms.Tools**

## Code Examples

**C#:**

```csharp
using Syncfusion.Windows.Forms.Tools;

// Example usage of MaskedEditBox
MaskedEditBox maskEditBox = new MaskedEditBox();
maskEditBox.Mask = "####-##-####";
```

**VB.NET:**

```vbnet
Imports Syncfusion.Windows.Forms.Tools

' Example usage of MaskedEditBox
Dim maskEditBox As New MaskedEditBox()
maskEditBox.Mask = "####-##-####"
```

## Cross References
- Refer to documentation for understanding basic text input controls and their properties.

<!-- tags: [Windows Forms, MaskedEditBox, Designer, C#, VB.NET, Namespaces] keywords: [MaskedEditBox, text input, formatted input, US social security number, US telephone number, short date, short time, first name, last name, programmatically, namespace inclusion, Syncfusion.Windows.Forms.Tools] -->
```