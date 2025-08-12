```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_593.jpeg
document_name: tools
page_number: 593
page_id: tools#page_593
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:21:51Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to use the `ComboBoxBase` control in Windows Forms.
- Explains the `ListBoxControl` property of `ComboBoxBase`.
- Provides steps to create and configure `ComboBoxBase` at runtime.

## Content

### Visual Studio Designer

#### Properties of `ComboBoxBase`
- The `ComboBoxBase` control is displayed in the Visual Studio Properties window.
- The `ListControl` property is set to `listBox1`, indicating that the control is bound to a list box.
- Other properties such as `ForeColor`, `GenerateMember`, and `IgnoreThemeBackground` are also shown.

**Figure 366: ListControl Property of ComboBoxBase**
![Figure 366: ListControl Property of ComboBoxBase](images/listControlProperty.png)

#### Runtime Display of `ComboBoxBase`
- The `ComboBoxBase` control is shown at runtime in a form.
- The dropdown list includes options like `ComboBoxDropDown`, `ComboBoxBase`, `ComboBoxAdv`, and `ComboBoxAutoComplete`.

**Figure 367: ComboBoxBase at Run Time**
![Figure 367: ComboBoxBase at Run Time](images/comboBoxBaseAtRuntime.png)

#### Creating `ComboBoxBase` Through Code

**1. Added Shared.Base to the reference folder through solution explorer and include the below namespace in the code.**

**[C#]**
```csharp
using Syncfusion.Windows.Forms.Tools;
```

**[VB.NET]**
```vb
Imports Syncfusion.Windows.Forms.Tools
```

## API Reference
- **Namespace**: `Syncfusion.Windows.Forms.Tools`
- **Class**: `ComboBoxBase`
- **Properties**: 
  - `ListControl`: Links the `ComboBoxBase` to a list control such as a list box.
  - `ForeColor`: Specifies the foreground color of the control.

## Code Examples

### C#
```csharp
using Syncfusion.Windows.Forms.Tools;

// Create a ComboBoxBase instance
var comboBoxBase = new ComboBoxBase();

// Set the ListControl property
comboBoxBase.ListControl = listBox1;
```

### VB.NET
```vb
Imports Syncfusion.Windows.Forms.Tools

' Create a ComboBoxBase instance
Dim comboBoxBase As New ComboBoxBase()

' Set the ListControl property
comboBoxBase.ListControl = listBox1
```

## Cross References
- See also: Related controls and properties in Syncfusion Windows Forms.

### Tags and Keywords
```html
<!-- tags: [WinForms, ComboBoxBase, ListControl, Windows Forms] keywords: [ComboBoxBase, ListControl, ListBoxControl, runtime, designers] -->
```
```