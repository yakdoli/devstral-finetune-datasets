```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_099.jpeg
document_name: HTMLUI
page_number: 099
page_id: HTMLUI#page_099
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:08:22Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Demonstrates implementing custom functionality into HTML elements using HTMLUI.
- Shows how to create custom controls using HTMLUI elements in Windows Forms.

## Content

### Preparing Custom Controls with HTMLUI

#### Code Example: C#

```csharp
private void htmluiControl1_PreRenderDocument(object sender, 
Syncfusion.Windows.Forms.HTMLUI.PreRenderDocumentArgs e)
{
    Hashtable htmelements = new Hashtable();
    htmelements = e.Document.ElementsByUserID;

    // Here the base functionality of the 'this.checkBoxAdv1' is implemented to the 'checkBoxAdvElement1'.
    BaseElement CheckBoxAdvElement1 = htmelements["CheckBoxAdv"] as BaseElement;

    // Create a new Wrapper object.
    new CustomControlBase(CheckBoxAdvElement1, this.CheckBoxAdv1);
    BaseElement NumericUpDownElement = htmelements["NumericUpDown"] as BaseElement;
    new CustomControlBase(NumericUpDownElement, this.NumericUpDown1);
}
```

#### Code Example: VB.NET

```vb
Private Sub htmluiControl1_PreRenderDocument(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.HTMLUI.PreRenderDocumentArgs)
    Dim htmelements As Hashtable = New Hashtable()
    htmelements = e.Document.ElementsByUserID

    ' Here the base functionality of the 'this.checkBoxAdv1' is implemented to the 'checkBoxAdvElement1'.
    Dim CheckBoxAdvElement1 As BaseElement = CType(IIf(TypeOf htmelements("CheckBoxAdv") Is BaseElement, htmelements("CheckBoxAdv"), Nothing), BaseElement)

    ' Create a new Wrapper object.
    Dim oTempl As CustomControlBase = New CustomControlBase(CheckBoxAdvElement1, Me.CheckBoxAdv1)
    Dim NumericUpDownElement As BaseElement = CType(IIf(TypeOf htmelements("NumericUpDown") Is BaseElement, htmelements("NumericUpDown"), Nothing), BaseElement)
    Dim oTemp2 As CustomControlBase = New CustomControlBase(NumericUpDownElement, Me.NumericUpDown1)
End Sub
```

### Visual Representation

The following image illustrates three custom controls created using HTMLUI.

---

<!-- tags: [Syncfusion Winforms, HTMLUI, Custom Controls] keywords: [HTMLUI, Custom Controls, Windows Forms, PreRenderDocument, ElementsByUserID, BaseElement, CustomControlBase] -->
```