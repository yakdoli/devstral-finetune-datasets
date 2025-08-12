```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_286.jpeg
document_name: tools
page_number: 286
page_id: tools#page_286
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:04:41Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Guide to adding and associating AutoComplete controls to a TextBox programmatically.
- Lists: autocomplete items through designer, explained in the AutoComplete control topic.
- Step-by-step instructions for including namespaces, creating control instances, and associating AutoComplete.

## Content

### Figure: AutoCompletion of text in the TextBox
**Figure 119: AutoCompletion of text in the TextBox**

#### Note
We can also add a list of autocomplete items through designer, which can be used as a source for AutoComplete control. SeeSee **Source for AutoComplete Control** topic for details.

#### See also
- [Concepts and Features](Concepts and Features)
- [3.5.1.1.2.2 Through Code](3.5.1.1.2.2 Through Code)

This section will guide you to programmatically add and associate an AutoComplete control to a textbox.

#### Steps to Associate AutoComplete with a TextBox

1. **Include the required namespace.**

   ```csharp
   using Syncfusion.Windows.Forms.Tools;
   ```
   
   ```vb.net
   Imports Syncfusion.Windows.Forms.Tools
   ```

2. **Create instances of AutoComplete and TextBox controls.**

   ```csharp
   private Syncfusion.Windows.Forms.Tools.AutoComplete autoComplete1;
   private System.Windows.Forms.TextBox textBox1;

   this.textBox1 = new TextBox();
   this.autoComplete1 = new AutoComplete();
   ```

   ```vb.net
   Private autoComplete1 As Syncfusion.Windows.Forms.Tools.AutoComplete
   Private textBox1 As System.Windows.Forms.TextBox

   Me.textBox1 = New TextBox()
   Me.autoComplete1 = New AutoComplete()
   ```

3. **Associate AutoComplete with TextBox using SetAutoComplete() method.**

---

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Class**: AutoComplete
- **Method**: SetAutoComplete()
  - **Purpose**: Associates the AutoComplete control with a TextBox.
  - **Parameters**: 
    - **TextBox**: The TextBox control to which the AutoComplete is to be applied.
  - **Returns**: None
  - **Usage**: 
    ```csharp
    this.autoComplete1.SetAutoComplete(this.textBox1);
    ```

---

## Code Examples

### C# Example
```csharp
using Syncfusion.Windows.Forms.Tools;

private Syncfusion.Windows.Forms.Tools.AutoComplete autoComplete1;
private System.Windows.Forms.TextBox textBox1;

this.textBox1 = new TextBox();
this.autoComplete1 = new AutoComplete();

this.autoComplete1.SetAutoComplete(this.textBox1);
```

### VB.NET Example
```vb.net
Imports Syncfusion.Windows.Forms.Tools

Private autoComplete1 As Syncfusion.Windows.Forms.Tools.AutoComplete
Private textBox1 As System.Windows.Forms.TextBox

Me.textBox1 = New TextBox()
Me.autoComplete1 = New AutoComplete()

Me.autoComplete1.SetAutoComplete(Me.textBox1)
```

## Page-level Navigation/TOC
- Figures and topics for AutoCompletion in TextBox.
- References to related topics: Source for AutoComplete Control and Through Code.

---

<!-- tags: [Syncfusion, WinForms, AutoComplete, TextBox, Namespace, Control, Design-Time] keywords: [AutoComplete control, TextBox association, Programmatic control, Design-Time features, AutoComplete topics, Namespace inclusion, WinForms] -->
```