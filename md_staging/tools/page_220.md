```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_220.jpeg
document_name: tools
page_number: 220
page_id: tools#page_220
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:41:03Z
fidelity: lossless
--> 

# Essential Tools for Windows Forms

## Overview
- Explains the DockState event handling in Syncfusion Windows Forms.
- Focuses on the DockStateChanged Event, describing its behavior and data.
- Provides an example in C# for handling the DockStateChanged event.

---

### 3.4.3.8.5 Dock State

This section covers the following events:

#### 3.4.3.8.5.1 DockStateChanged Event

When the user changes the dock state of the control, DockStateChanged event will be raised immediately after this dock state change operation.

---

#### Event Data

The event handler receives an argument of type DockStateChangeEventArgs containing data related to this event. The following DockStateChangeEventArgs property provides information specific to this event.

| Member       | Description                                      |
|--------------|--------------------------------------------------|
| Control      | Gets the collection of controls undergoing the dock state transfer. |

---

#### C#

```csharp
//The DockStateChanged event occurs immediately after a dock operation.
private void dockingManager1_DockStateChanged(object sender, Syncfusion.Windows.Forms.Tools.DockStateChangeEventArgs arg)
{
    Console.WriteLine("DockStateChanged Event has occurred");
    Console.WriteLine("Total Number of controls in a group : " + arg.Controls.Length.ToString());
    //arg.Controls Gets the collection of controls undergoing the dockstate transfer.
    Control[] ctrls = arg.Controls;
    int i = 1;
    //Here display all the controls in arg.Controls group.
    foreach (Control ctrl in ctrls)
    {
        Console.WriteLine("Control" + i + " Name : " + ctrl.Name);
        i++;
    }
}
```

---

### Cross References
- See also: [Unclear] Details on Docking Manager and its operations.
```