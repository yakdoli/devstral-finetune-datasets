```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_013.jpeg
document_name: edit
page_number: 013
page_id: edit#page_013
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:54:40Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Documentation on the Essential Edit control for Windows Forms.
- Navigation path: Dashboard -> Documentation -> Installed Documentation.

## Content
- This page provides an overview of the Essential Edit control, which is a specialized input textbox for Windows Forms applications.
- The Essential Edit control offers advanced editing features and customization options for various data entry scenarios.

### WinForms-specific conventions
- **Namespace**: Syncfusion.Windows.Forms
- **Control Name**: Essential Edit

### Navigation Path
- **Menu Path**:
  - Dashboard
  - Documentation
  - Installed Documentation

## Code Examples

### C# Example
```csharp
using Syncfusion.Windows.Forms;

public void ConfigureEssentialEdit()
{
    EssentialEdit editor = new EssentialEdit();
    editor.Dock = DockStyle.Fill;
    editor.Text = "Sample Text";

    // Custom settings
    editor.BorderStyle = BorderStyle.FixedSingle;
    editor.Enabled = true;

    // Add to form
    this.Controls.Add(editor);
}
```

### VB.NET Example
```vb
Imports Syncfusion.Windows.Forms

Public Sub ConfigureEssentialEdit()
    Dim editor As New EssentialEdit()
    editor.Dock = DockStyle.Fill
    editor.Text = "Sample Text"

    ' Custom settings
    editor.BorderStyle = BorderStyle.FixedSingle
    editor.Enabled = True

    ' Add to form
    Me.Controls.Add(editor)
End Sub
```

## API Reference

### Properties
- **Text**: The text content of the Essential Edit control.
- **Enabled**: Indicates whether the control is enabled or not.
- **BorderStyle**: Defines the border style of the control.
- **Dock**: Specifies the docking behavior of the control.

### Methods
- **Focus()**: Sets input focus to the control.
- **Clear()**: Clears all the text in the control.
- **SelectAll()**: Selects all the text in the control.

### Events
- **TextChanged**: Occurs when the text in the control changes.
- **KeyUp**: Occurs when a key is released while the control has focus.

## Cross References
- **See Also**: [API Reference for Essential Edit](#)
- [Essential Edit Customization and Features](#)

```html
<!-- tags: Syncfusion WinForms, Essential Edit, Control, Textbox, API, Version 11.4.0.26 -->
<!-- keywords: Windows Forms, Input, Text, Customization, C#, VB.NET, Visual Studio, Documentation -->
``` 
```