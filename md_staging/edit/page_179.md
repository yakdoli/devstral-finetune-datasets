```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_179.jpeg
document_name: edit
page_number: 179
page_id: edit#page_179
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:04:45Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Demonstrates how to populate a **Context ToolTip** with additional information by handling the `UpdateContextToolTip` event in an Edit Control.
- Highlights the use of the **InitializeComponent** method and advises extending functionality within the constructor after this call.

## Content

### Context ToolTip Handling

The **Context ToolTip** can be populated with additional information on the corresponding lexem by handling the `UpdateContextToolTip` event of the Edit Control.

#### Code Example in C#

```csharp
[C#]

private void editControl_UpdateContextToolTip(object sender,
    Syncfusion.Windows.Forms.Edit.Dialogs.UpdateTooltipEventArgs e)
{
    if (e.Text == string.Empty)
    {
        Point pointVirtual = editControl1.PointToVirtualPosition(
            new Point(e.X, e.Y));

        if (pointVirtual.Y > 0)
        {
            // Get the current line
            ILexemLine line = editControl1.GetLine(
                pointVirtual.Y);

            if (line != null)
            {
```

### Figure: Context ToolTip
![Figure 59: Context ToolTip](Context_ToolTip_Demo.png)

### Explanation
The `UpdateContextToolTip` event allows developers to dynamically update the **Context ToolTip** based on the current state or position of the cursor within the Edit Control. The example provided demonstrates how to handle this event to show relevant information for a specific position in the text.

## API Reference

### Methods
- **InitializeComponent**: Automatically generated method by the **Windows Form Designer** to initialize components.
- **PointToVirtualPosition**: Converts screen coordinates to virtual coordinates within the Edit Control.
- **GetLine**: Retrieves the line at the specified virtual position.

## Code Examples

The provided C# example illustrates handling the `UpdateContextToolTip` event to determine and display appropriate lexem information.

## Cross References

See also:
- **Designer-generated code**
- **Edit Control events**
- **ToolTip customization**

### Footer Note
© 2013 Syncfusion. All rights reserved.
```