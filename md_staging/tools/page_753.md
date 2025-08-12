```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_753.jpeg
document_name: tools
page_number: 753
page_id: tools#page_753
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:31:37Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Details the behavior and properties of the `IntegerTextBox` control in Syncfusion Windows Forms.
- Focuses on the `NegativeInputPendingOnSelectAll` and `AllowLeadingZeros` properties.
- Includes examples in both C# and VB.NET for configuring these properties.

## Content

### NegativeInputPendingOnSelectAll

This property defines the behavior when the contents of the `IntegerTextBox` is fully selected and the negative key is pressed by the user.

| When set to 'False' | When set to 'True' |
| --- | --- |
| The current value is changed to the negative value immediately. | The current value is not changed at all. The next key stroke is taken to be a new value, and the entire contents of the `IntegerTextBox` is replaced by the negative value of the key stroke character entered. |

**C# Example:**
```csharp
this.integerTextBox1.DeleteSelectionOnNegative = true;
this.integerTextBox1.NegativeInputPendingOnSelectAll = true;
```

**VB.NET Example:**
```vb
Me.integerTextBox1.DeleteSelectionOnNegative = True
Me.integerTextBox1.NegativeInputPendingOnSelectAll = True
```

### AllowLeadingZeros

This property can be used to include zeros before the beginning value of the integer value of the control.

| IntegerTextBox Property | Description |
| --- | --- |
| AllowLeadingZeros | Indicates whether to allow inserts zero in the beginning value. The default value is set to 'False'. |

**C# Example:**
```
```

## API Reference
- **Namespace:** Syncfusion.Windows.Forms.Tools
- **Class:** IntegerTextBox
- **Properties:**
  - **NegativeInputPendingOnSelectAll:** Type: boolean
  - **AllowLeadingZeros:** Type: boolean

### Parameters
- **NegativeInputPendingOnSelectAll:** Determines the behavior when the negative key is pressed on a fully selected `IntegerTextBox`.
- **AllowLeadingZeros:** Determines whether leading zeros are allowed in the integer value.

## Code Examples

### C# Example
```csharp
this.integerTextBox1.DeleteSelectionOnNegative = true;
this.integerTextBox1.NegativeInputPendingOnSelectAll = true;
```

### VB.NET Example
```vb
Me.integerTextBox1.DeleteSelectionOnNegative = True
Me.integerTextBox1.NegativeInputPendingOnSelectAll = True
```

## RAG Annotations
<!-- tags: [Windows Forms, IntegerTextBox, Syncfusion] keywords: [NegativeInputPendingOnSelectAll, AllowLeadingZeros, DeleteSelection, LeadingZeros, IntegerTextBoxBehavior] -->
```