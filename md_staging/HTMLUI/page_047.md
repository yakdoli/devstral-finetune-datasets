```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_047.jpeg
document_name: HTMLUI
page_number: 047
page_id: HTMLUI#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:05:09Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## 4.3 Control Events

### Overview

- HTMLUI control provides a rich set of events to assist application developers in tracking the execution process.
- Events are programmed based on the Event arguments, which contain data related to the respective event.

### Content

**HTMLUI Control Events**

The events executed by the **HTMLUI control** are as follows:

- **LinkClicked Event**
- **LoadStarted Event**
- **LoadFinished Event**
- **LoadError Event**
- **PreRenderDocument Event**
- **ShowTitleChanged Event**
- **TitleChanged Event**

#### LinkClicked Event

- **Description**:
  This event is triggered after a hyperlink is clicked and before the hyperlink attempts to load a new resource.
- **Event Properties**:
  - **Cancel**: A boolean value indicating whether the default processing of resource loading should be canceled.
  - **Path**: Specifies the location of the resource being loaded.

##### Code Example: C#

```csharp
// Event that is to be raised after the hyperlink was clicked and before the hyperlink tries to load
// a new resource.
this.htmluiControl1.LinkClicked += new
Syncfusion.Windows.Forms.HTMLUI.LinkForwardEventHandler(this.htmluiControl1_LinkClicked);

private void htmluiControl1_LinkClicked(object sender,
Syncfusion.Windows.Forms.HTMLUI.LinkForwardEventArgs e)
{
    e.Cancel = true;
    Form2 form2 = new Form2(GetFilesLocation() + e.Path);
    form2.Show();
}
```

##### Code Example: VB.NET

```vb
' Event that is to be raised after the hyperlink was clicked and before the hyperlink tries to load
' a new resource.
AddHandler htmluiControl1.LinkClicked, AddressOf htmluiControl1_LinkClicked

Private Sub htmluiControl1_LinkClicked(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.HTMLUI.LinkForwardEventArgs)
    e.Cancel = True
    Dim form2 As New Form2(GetFilesLocation() + e.Path)
    form2.Show()
End Sub
```

---

### API Reference

- **Namespace**: `Syncfusion.Windows.Forms.HTMLUI`
- **Event**: `LinkClicked`
- **Parameters**:
  - `sender`: The object that triggered the event.
  - `e`: An instance of `LinkForwardEventArgs` containing event-specific data.
- **Event Arguments Properties**:
  - **Cancel**: Boolean
  - **Path**: String

### Code Examples

#### C#

```csharp
this.htmluiControl1.LinkClicked += new
Syncfusion.Windows.Forms.HTMLUI.LinkForwardEventHandler(this.htmluiControl1_LinkClicked);

private void htmluiControl1_LinkClicked(object sender,
Syncfusion.Windows.Forms.HTMLUI.LinkForwardEventArgs e)
{
    e.Cancel = true;
    Form2 form2 = new Form2(GetFilesLocation() + e.Path);
    form2.Show();
}
```

#### VB.NET

```vb
AddHandler htmluiControl1.LinkClicked, AddressOf htmluiControl1_LinkClicked

Private Sub htmluiControl1_LinkClicked(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.HTMLUI.LinkForwardEventArgs)
    e.Cancel = True
    Dim form2 As New Form2(GetFilesLocation() + e.Path)
    form2.Show()
End Sub
```

<!-- tags: [HTMLUI, Windows Forms, Control Events, LinkClicked Event, Load Events, ShowTitleChanged Event, TitleChanged Event] keywords: [HTMLUI control, hyperlink, control event, event arguments, LinkClicked, LoadStarted, LoadFinished, LoadError, PreRenderDocument, ShowTitleChanged, TitleChanged] -->
```