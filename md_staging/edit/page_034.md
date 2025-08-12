```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_034.jpeg
document_name: edit
page_number: 034
page_id: edit#page_034
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:55:54Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Edit.Windows\\Samples\\2.0\\Advanced Editor Functions\\ActionGroupingDemo

## 4.2.2 New Line Styles

Edit Control allows you to specify a new line style, or get the currently used new line style in the text.

### SetNewLineStyle Method
The `SetNewLineStyle` method sets the current new line style in the Edit Control. `SetNewLineStyle` method accepts values from the `NewLineStyle` enumerator which has values like Windows, Mac, Unix and Control, which correspond to new line styles "`\\r\\n`", "`\\r`", "`\\n`" and "`\\n\\r`" respectively.

### GetNewLineStyle Method
Similarly, the `GetNewLineStyle` method returns a `NewLineStyle` enumerator value which indicates the currently used new line style in the Edit Control.

<div class="note">  
  <strong>Note:</strong> The default new line style value is set to 'Control'. This value can be changed according to the needs of the user using the `DefaultNewLineStyle` property.
</div>

### Code Examples

#### C#  

```csharp
// Change the current new line style in the Edit Control.
this.editControl1.SetNewLineStyle(Syncfusion.IO.NewLineStyle.Control);
this.editControl1.GetNewLineStyle();

// Specify the default new line style.
this.editControl1.DefaultNewLineStyle = Syncfusion.IO.NewLineStyle.Windows;
```

#### VB.NET  

```vb
' Change the current new line style in the Edit Control.
Me.editControl1.SetNewLineStyle(Syncfusion.IO.NewLineStyle.Control)
Me.editControl1.GetNewLineStyle()

' Specify the default new line style.
Me.editControl1.DefaultNewLineStyle = Syncfusion.IO.NewLineStyle.Windows
```

## 4.2.3 Clipboard Operations
<!-- tags: [product, module, control, api, version?] keywords: [edit control, new line style, clipboard operations, syncfusion windows forms, defaultnewlinestyle, setnewlinestyle, getnewlinestyle] -->
```