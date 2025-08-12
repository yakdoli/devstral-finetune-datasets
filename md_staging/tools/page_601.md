```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_601.jpeg
document_name: tools
page_number: 601
page_id: tools#page_601
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:22:22Z
fidelity: lossless
--> 

## Essential Tools for Windows Forms

### Overview
- This page explains how to place a `ComboBoxBase` within a `PopupControlContainer` in Windows Forms.
- Focus is maintained on ensuring the derived `PopupControlContainer` does not lose focus and close prematurely.

---

### Content

#### Figure 371: ComboBoxBase with selected options at Run Time
![Figure 371: ComboBoxBase with selected options at Run Time](image.png)

##### 3.5.5.3.4.2 DropDown Event
In order to place `ComboBoxBase` within a `PopupControlContainer`, derive from our `PopupControlContainer`, override the `OnPopup` method, and set the focus to the derived control. This ensures that the derived `PopupControlContainer` does not lose focus and close prematurely.

---

##### Code Examples

###### C#
```csharp
// Derive from PopupControlContainer.
public class CustomPopupControlContainer : Syncfusion.Windows.Forms.PopupControlContainer
{
    public CustomPopupControlContainer()
    {
    }

    public CustomPopupControlContainer(IContainer container) : this()
    {
        container.Add(this);
    }

    protected override void OnPopup(EventArgs args)
    {
        // Sets focus to the derived control.
        base.OnPopup(args);
        this.Focus();
    }
}
```

###### VB.NET
```vb
' Derive from PopupControlContainer.
Public Class CustomPopupControlContainer
    Inherits Syncfusion.Windows.Forms.PopupControlContainer

    Public Sub New()
    End Sub

    Public Sub New(container As IContainer)
        container.Add(Me)
    End Sub

    Protected Overrides Sub OnPopup(args As EventArgs)
        ' Sets focus to the derived control.
        MyBase.OnPopup(args)
        Me.Focus()
    End Sub
End Class
```

---

## API Reference

### Methods
- `OnPopup(EventArgs args)`:
  - Overrides the base `OnPopup` method to maintain focus on the derived control.
  - **Parameters**:
    - `args`: Event arguments of the popup event.
  - **Returns**: `void`

---

## Code Examples (Continued)

### C# (Derived from the provided text)
#### Sample Usage
```csharp
using System;
using System.Windows.Forms;
using Syncfusion.Windows.Forms;

public class Form1 : Form
{
    private CustomPopupControlContainer popupControl;

    public Form1()
    {
        InitializeComponent();
        SetupUI();
    }

    private void InitializeComponent()
    {
        this.comboBoxBase = new Syncfusion.Windows.Forms.Tools.ComboBoxBase();
        this.SuspendLayout();
        // 
        // comboBoxBase
        // 
        this.comboBoxBase.DrawnText = "Three";
        this.comboBoxBase.DrawnText = "Four";
        this.comboBoxBase.DrawnText = "Five";
        this.Controls.Add(this.comboBoxBase);
        this.ResumeLayout(false);
    }

    private void SetupUI()
    {
        popupControl = new CustomPopupControlContainer();
        popupControl.Controls.Add(comboBoxBase);
        Controls.Add(popupControl);
    }
}
```

### VB.NET (Derived from the provided text)
#### Sample Usage
```vb
Imports System.Windows.Forms
Imports Syncfusion.Windows.Forms

Public Class Form1
    Inherits Form

    Private popupControl As CustomPopupControlContainer

    Public Sub New()
        InitializeComponent()
        SetupUI()
    End Sub

    Private Sub InitializeComponent()
        Me.comboBoxBase = New Syncfusion.Windows.Forms.Tools.ComboBoxBase()
        Me.SuspendLayout()
        ' 
        ' comboBoxBase
        ' 
        Me.comboBoxBase.DrawnText = "Three"
        Me.comboBoxBase.DrawnText = "Four"
        Me.comboBoxBase.DrawnText = "Five"
        Me.Controls.Add(Me.comboBoxBase)
        Me.ResumeLayout(False)
    End Sub

    Private Sub SetupUI()
        popupControl = New CustomPopupControlContainer()
        popupControl.Controls.Add(comboBoxBase)
        Controls.Add(popupControl)
    End Sub
End Class
```

---

## Page-level Navigation/TOC
- [3.5.5.3.4.2 DropDown Event](#3.5.5.3.4.2-dropdown-event)

---

<!-- tags: [ComboBoxBase, PopupControlContainer, WinForms, Event Handling, Focus Management] keywords: [ComboBoxBase, DropDownEvent, OnPopup, Focus, Windows Forms, C#, VB.NET] -->
```