```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_628.jpeg
document_name: tools
page_number: 628
page_id: tools#page_628
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:24:55Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### AutoScroll Behavior

[C#]

```csharp
this.popupControlContainer1.AutoScroll = true;
this.popupControlContainer1.AutoScrollMargin = new System.Drawing.Size(2, 2);
this.popupControlContainer1.AutoScrollMinSize = new System.Drawing.Size(3, 3);
```

[VB.NET]

```vb
Me.popupControlContainer1.AutoScroll = True
Me.popupControlContainer1.AutoScrollMargin = New System.Drawing.Size(2, 2)
Me.popupControlContainer1.AutoScrollMinSize = New System.Drawing.Size(3, 3)
```

#### 3.5.6.1.3.2 AutoClosing Behavior

When a `PopupControlContainer` control is associated as the popup for a control, by default, the pop-up will hide when the user clicks anywhere outside the pop-up besides the control (if any) that is specified in the "ParentControl" property. To control this default behavior, i.e., to display the popup even if there is any mouse action, set the **IgnoreMouseMessages** property to true.

### Example

The Popup of a textbox, on a button click should be closed only when the textbox is not empty. For this purpose, the popup should not be closed on any mouse action. So set the `IgnoreMouseMessages` property to true for this property.

[C#]

```csharp
this.popupControlContainer1.IgnoreMouseMessages = true;

private void button1_Click(object sender, EventArgs e)
{
    // Hides the PopupControlContainer under a button click.
    if (txtbox.Text != "")
    {
        this.popupControlContainer1.HidePopup(PopupCloseType.Done);
    }
}
```

[VB.NET]

```vb
Me.popupControlContainer1.IgnoreMouseMessages = True
```

## Page-level Navigation/TOC (if applicable)
<!-- tags: [syncfusion, winforms, popupcontrolcontainer, autoscroll, autoclose, ignoremousemessages] keywords: [popupcontrolcontainer, autoscroll, autoclosing behavior, ignoremousemessages] -->
```