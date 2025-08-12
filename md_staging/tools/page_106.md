```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_106.jpeg
document_name: tools
page_number: 106
page_id: tools#page_106
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:25:14Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

| CommandBarWrapping | This event occurs when the CommandBar is being wrapped. |
| --- | --- |

## Content

### CommandBarDropDownClicked Event

#### Overview

- The CommandBarDropDownClicked event is triggered when the dropdown button of a CommandBar is clicked.
- The event handler receives an argument of type `EventArgs` containing data related to this event.

---

### Code Examples

#### C#

```csharp
// Add a PopupMenu control and assign it to the PopupMenu property of the CommandBar.
this.commandBar1.PopupMenu = this.popupMenu1;
// Add a ParentBarItem to the PopupMenu.
this.popupMenu1.ParentBarItem = this.parentBarItem1;
// Add items to the ParentBarItem.
this.parentBarItem1.Items.AddRange(new Syncfusion.Windows.Forms.Tools.XPMenus.BarItem[] {
    this.barItem1,
    this.barItem2,
    this.barItem3}
);
this.barItem1.Text = "Windows Forms Samples";
this.barItem2.Text = "ASP.NET Samples";
this.barItem3.Text = "WPF Samples";

// Handle the CommandBarDropDownClicked event.
this.commandBar1.CommandBarDropDownClicked += new EventHandler(commandBar1_CommandBarDropDownClicked);

private void commandBar1_CommandBarDropDownClicked(object sender, EventArgs e)
{
    // The below line will be displayed in the output window at runtime.
    Console.WriteLine("CommandBarDropDownClicked event is raised ");
}
```

#### VB.NET

```vb
' Add a PopupMenu control and assign it to the PopupMenu property of the CommandBar.
Me.commandBar1.PopupMenu = Me.popupMenu1
' Add a ParentBarItem to the PopupMenu.
Me.popupMenu1.ParentBarItem = Me.parentBarItem1
```

---

## API Reference

### Events
- **CommandBarWrapping**
  - Description: Triggered when the CommandBar is being wrapped.
- **CommandBarDropDownClicked**
  - Description: Triggered when the dropdown button of a CommandBar is clicked.
  - Parameters:
    - `sender`: The object that raised the event.
    - `EventArgs`: Containing data related to the event.
  - Returns: None.

---

<!-- tags: [CommandBar, EventHandling, WinForms, C#, VB.NET] keywords: [CommandBarWrapping, CommandBarDropDownClicked, EventHandling] -->
```