```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_359.jpeg
document_name: tools
page_number: 359
page_id: tools#page_359
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:08:49Z
fidelity: lossless
-->

### Essential Tools for Windows Forms

#### Code Example

```csharp
private Syncfusion.Windows.Forms.Tools.ButtonEdit buttonEdit1;
private System.Windows.Forms.TextBox textBox1;
private Syncfusion.Windows.Forms.Tools.ButtonEditChildButton buttonEditChildButton1;
private Syncfusion.Windows.Forms.Tools.ButtonEditChildButton buttonEditChildButton2;
private Syncfusion.Windows.Forms.Tools.ButtonEditChildButton buttonEditChildButton3;

this.buttonEdit1 = new Syncfusion.Windows.Forms.Tools.ButtonEdit();
this.textBox1 = new TextBox();
this.buttonEditChildButton1 = new Syncfusion.Windows.Forms.Tools.ButtonEditChildButton();
this.buttonEditChildButton2 = new Syncfusion.Windows.Forms.Tools.ButtonEditChildButton();
this.buttonEditChildButton3 = new Syncfusion.Windows.Forms.Tools.ButtonEditChildButton();
```

```vbnet
Private buttonEdit1 As Syncfusion.Windows.Forms.Tools.ButtonEdit
Private textBox1 As System.Windows.Forms.TextBox
Private buttonEditChildButton1 As Syncfusion.Windows.Forms.Tools.ButtonEditChildButton
Private buttonEditChildButton2 As Syncfusion.Windows.Forms.Tools.ButtonEditChildButton
Private buttonEditChildButton3 As Syncfusion.Windows.Forms.Tools.ButtonEditChildButton

Me.buttonEdit1 = New Syncfusion.Windows.Forms.Tools.ButtonEdit()
Me.textBox1 = New TextBox()
Me.buttonEditChildButton1 = New Syncfusion.Windows.Forms.Tools.ButtonEditChildButton()
Me.buttonEditChildButton2 = New Syncfusion.Windows.Forms.Tools.ButtonEditChildButton()
Me.buttonEditChildButton3 = New Syncfusion.Windows.Forms.Tools.ButtonEditChildButton()
```

#### Embedding TextBox

3. Embed the TextBox1 to the textBox of ButtonEdit.

```csharp
// Associating the TextBoxExt control.
this.buttonEdit1.TextBox = this.textBox1;
```

```vbnet
[VB.NET]
```

---

## Page-Level Navigation/TOC
- Overview
- Content
  - WinForms-specific conventions
- API Reference
- Code Examples
- Cross References
- RAG Annotations

## RAG Annotations
<!-- tags: [Syncfusion Winforms, ButtonEdit, TextBox, ButtonEditChildButton] keywords: [Embed TextBox, ButtonEdit Control, ChildButtons, Design-time, Runtime Features, Property Grid, Designer Steps] -->
```