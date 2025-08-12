```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_919.jpeg
document_name: tools
page_number: 919
page_id: tools#page_919
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:43:31Z
fidelity: lossless
--> 

## Essential Tools for Windows Forms

### FontListBox Implementation

Here is how you can implement the FontListBox control in C# and VB.NET:

#### C#
```csharp
this.fontListBox1 = new Syncfusion.Windows.Forms.Tools.FontListBox();
this.fontListBox1.Size = new System.Drawing.Size(152, 94);

this.Controls.Add(this.fontListBox1);
```

#### VB.NET
```vb.net
Private fontListBox1 As Syncfusion.Windows.Forms.Tools.FontListBox
Me.fontListBox1 = New Syncfusion.Windows.Forms.Tools.FontListBox()
Me.fontListBox1.Size = New System.Drawing.Size(152, 21)

Me.Controls.Add(Me.fontListBox1)
```

### Figure 585: FontListBox Control
![FontListBox Control](image.png)

### Concepts and Features

This section will discuss the concepts and features of the FontListBox control in the below topics.

#### Selection Mode

At run time, the items in the FontListBox can be selected, based on the selection mode specified in SelectionMode property. Selection can be made using mouse as well as using keyboard.

The options are:
- one,
- MultiSimple,
- MultiExtended.

#### C#
```csharp
```

---

**Note:** The code examples above demonstrate the setup and configuration of the FontListBox control in C# and VB.NET, and the text provides a brief overview of the selection modes available for the control.

## API Reference

For more details about the properties, methods, and events of the FontListBox control, refer to the API documentation provided by Syncfusion.

## Code Examples

### C#
```csharp
// Implementation of FontListBox in C#
```

### VB.NET
```vb.net
' Implementation of FontListBox in VB.NET
```

## Cross References

For more information on related controls and features, refer to the documentation on essential tools in Windows Forms.

### Summary

This page discusses the FontListBox control in Syncfusion WinForms, including its implementation, selection modes, and related resources.
```