```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_264.jpeg
document_name: tools
page_number: 264
page_id: tools#page_264
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:02:07Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Table of Methods

| **Method**         | **Description**                                                                                                                                                                                                 |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IsFloating          | Gets the value indicating whether the docked control is floating or not. <br> *Ctrl* - Indicates the control for which dock / floating state is been queried. |

### C#

```csharp
private void button1_Click(object sender, EventArgs e)
{
    this.dockingManager1.IsFloating(this.panel1);
    Console.Write("Dock state : " + this.dockingManager1.IsFloating(this.panel1));
}
```

### VB.NET

```vbnet
Private Sub dockingManager1_NewDockStateEndLoad(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.dockingManager1.IsFloating(Me.panel1)
    Console.Write("Dock state : " + Me.dockingManager1.IsFloating(Me.panel1))
End Sub
```

## 3.4.4.6.2 How to float a single control even if it is tabbed to many controls?

This is discussed in the *Floating* topic.

## 3.4.4.6.3 How to get individual floating controls properties?

### To get the x,y coordinates if it is floating

1. Add a list view and a docking manager to your form.
2. Enable the listview as a dock control.

#### C#

```csharp
this.dockingManager1.SetEnableDocking(this.listView1, true);
```

#### VB.NET

```vbnet
Me.dockingManager1.SetEnableDocking(Me.listView1, True)
```

## API Reference

### IsFloating

- **Description**: Gets the value indicating whether the docked control is floating or not.
- **Parameter**: *Ctrl* - Indicates the control for which dock / floating state is been queried.

### SetEnableDocking

- **Parameters**:
  - `control`: The control to enable or disable docking for.
  - `enable`: A boolean indicating whether to enable or disable docking.

### Methods

- **IsFloating**: Returns a boolean indicating whether the docked control is floating.

## Code Examples

### C#

```csharp
this.dockingManager1.IsFloating(this.panel1);
```

### VB.NET

```vbnet
Me.dockingManager1.IsFloating(Me.panel1)
```

### Enabling Docking for a Control

#### C#

```csharp
this.dockingManager1.SetEnableDocking(this.listView1, true);
```

#### VB.NET

```vbnet
Me.dockingManager1.SetEnableDocking(Me.listView1, True)
```

<!-- tags: [product, module, control, api, version?] keywords: [Windows Forms, IsFloating, SetEnableDocking, Docking, Floating] -->
```