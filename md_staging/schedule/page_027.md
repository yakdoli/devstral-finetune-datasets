```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_027.jpeg
document_name: schedule
page_number: 027
page_id: schedule#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:09:07Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Overview
- Demonstrates how to integrate the `ScheduleControl` into a WinForms application.
- Explains the steps to configure and use the `ScheduleControl` on the design surface.
- Details the process of adding event handling for the `ScheduleControl`.

## Content

### ScheduleControl on the Design Surface
The following screenshot illustrates the `ScheduleControl` as it appears on the design surface in Visual Studio.

![The ScheduleControl on the Design Surface](insert_image_url)

**Figure 17: The ScheduleControl on the Design Surface**

### Adding a Form1_Load Handler

To implement functionality for the `ScheduleControl`, follow these steps:

1. Open the `Form1.cs` file in the code editor.
2. Locate the area of the form that is not covered by the `ScheduleControl`.
3. Double-click on this uncovered part of the form to add a `Form1_Load` event handler.

This action will automatically generate a code window displaying the `Form1_Load` method. The code should resemble the following snippet:

```csharp
private void Form1_Load(object sender, EventArgs e)
{
    // Your code here
}
```

### Explanation
- **Form1_Load**: This is a standard event triggered when the form is first loaded.
- **Code Window**: To start adding functionality for the `ScheduleControl`, such as setting default appearances or handling user interactions, you can add code within this method.

## API Reference

### Properties
- **Appearance**: Controls the visual style of the `ScheduleControl`.
  - **Default**: Provides default appearance settings for the control.
  - **Custom**: Allows customization of the appearance properties for specific needs.

## Code Examples

### C# Example
```csharp
private void Form1_Load(object sender, EventArgs e)
{
    scheduleControl1.Appearance = Syncfusion.Windows.Forms.ScheduleControl.Appearances.Custom;
    // Further customization can be added here
}
```

### VB.NET Example
```vb.net
Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
    scheduleControl1.Appearance = Syncfusion.Windows.Forms.ScheduleControl.Appearances.Custom
    ' Further customization can be added here
End Sub
```

## See also:
- Syncfusion.Windows.Forms.ScheduleControl
- Event handling in WinForms
- Customizing control properties in Visual Studio

<!-- tags: [WinForms, ScheduleControl, Form1_Load, DesignSurface, event handler, appearance] keywords: [design surface, appearance configuration, event handling, form load, visual studio, syncfusion windows forms, schedule control] -->
```