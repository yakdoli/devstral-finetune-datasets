```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_468.jpeg
document_name: chart
page_number: 468
page_id: chart#page_468
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:43:50Z
fidelity: lossless
--> 

## Toolbar Properties in Windows Forms

### Overview
- The ToolBar Properties dialog box provides various options to customize the appearance and behavior of the toolbar in Windows Forms.
- Key properties include alignment, background color, button colors, and size, among others.
- These settings allow for flexible configuration of the toolbar to meet specific design and functionality requirements.

### Content

#### Toolbar Properties Description

The ToolBar Properties Dialog Box displayed in the image allowsModification of the properties specific to the toolbar in Windows Forms. Here is a detailed description of the properties listed:

| Chart ToolBar Property         | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| Alignment                    | Indicates the alignment of the toolbar. Default value is **Center**.         |
| Autosize                     | Indicates if the toolbar can be resized automatically. Default value is **true**. |
| BackColor                    | Indicates the background color of the toolbar.                               |
| Border                       | Specifies the border style.                                                  |
| Buttons                      | List of buttons that you can add or delete as needed.                      |
| ButtonBackColor              | Gets or sets the background color of the toolbar button.                    |
| ButtonFlatStyle              | Gets or sets the flat style appearance for the toolbar button control. Default value is **FlatStyle.Flat**. |
| ButtonForeColor              | Gets or sets the foreground color of the toolbar button.                    |
| ButtonSize                   | Indicates the size of the toolbar buttons.                                    |

#### Figure: ToolBar Properties Dialog Box

![ToolBar Properties Dialog Box](#<FIGURE reference>)  
*Figure 299: ToolBar Properties Dialog Box*

Below are the toolbar properties and their descriptions:

- **Alignment**: Indicates the alignment of the toolbar. The default value is **Center**.
- **Autosize**: Indicates if the toolbar can be resized automatically. The default value is **true**.
- **BackColor**: Indicates the background color of the toolbar.
- **Border**: Specifies the border style for the toolbar.
- **Buttons**: A list of buttons that you can add or remove as required.
- **ButtonBackColor**: Gets or sets the background color of the toolbar button.
- **ButtonFlatStyle**: Gets or sets the flat style appearance for the toolbar button control. The default value is **FlatStyle.Flat**.
- **ButtonForeColor**: Gets or sets the foreground color of the toolbar button.
- **ButtonSize**: Indicates the size of the toolbar buttons.

### API Reference

The ToolBar properties in Windows Forms can be modified programmatically using the `Syncfusion.Windows.Forms` namespace. Below are the key properties that can be configured:

1. **Alignment**:
   - **Property**: `ToolBar.Align`
   - **Type**: `ToolBarAlign`
   - **Possible Values**: `Center`, `Left`, `Right`
   - **Default**: `Center`

2. **AutoSize**:
   - **Property**: `ToolBar.AutoSize`
   - **Type**: `bool`
   - **Default**: `true`

3. **BackColor**:
   - **Property**: `ToolBar.BackColor`
   - **Type**: `Color`
   - **Default**: System default

4. **Border**:
   - **Property**: `ToolBar.BorderStyle`
   - **Type**: `Border3DStyle`
   - **Possible Values**: `Raised`, `Sunken`, `Flat`
   - **Default**: Depends on system or style settings

5. **Buttons**:
   - **Property**: `ToolBar.Buttons`
   - **Type**: Collection of `ToolBarButton`
   - **Default**: Collection of predefined buttons

6. **ButtonBackColor**:
   - **Property**: `ToolBarButton.BackColor`
   - **Type**: `Color`
   - **Default**: System default

7. **ButtonFlatStyle**:
   - **Property**: `ToolBarButton.FlatStyle`
   - **Type**: `FlatStyle`
   - **Possible Values**: `Popup`, `Flat`, `Standard`
   - **Default**: `Flat`

8. **ButtonForeColor**:
   - **Property**: `ToolBarButton.ForeColor`
   - **Type**: `Color`
   - **Default**: System default

9. **ButtonSize**:
   - **Property**: `ToolBar.ButtonSize`
   - **Type**: `Size`
   - **Default**: Depends on theme or settings

### Code Examples

Here is an example in C# that demonstrates how to configure the ToolBar properties programmatically:

```csharp
// Create a ToolBar instance
Syncfusion.Windows.Forms.Tools.SuperToolTip tip = new Syncfusion.Windows.Forms.Tools.SuperToolTip();

// Create a ToolBarButton instance
Syncfusion.Windows.Forms.ToolBarButton button = new Syncfusion.Windows.Forms.ToolBarButton();
button.Text = "New Button";
button.BackColor = System.Drawing.Color.FromArgb(196, 196, 196);

// Add the button to the ToolBar
syncfusionToolbar.Buttons.Add(button);

// Set other properties
syncfusionToolbar.Alignment = Syncfusion.Windows.Forms.Tools.ToolBarAlign.Center;
syncfusionToolbar.AutoSize = true;
syncfusionToolbar.BackColor = System.Drawing.Color.DarkGray;
syncfusionToolbar.ButtonSize = new System.Drawing.Size(28, 28);
syncfusionToolbar.BorderStyle = System.Windows.Forms.Border3DStyle''.';
syncfusionToolbar.Direction = System.Windows.Forms.ToolBarDirection.Horizontal;

// Bind the ToolBar to a SuperToolTip
tip.SetToolTip(button, "This is a tooltip for the new button.");
```

### Cross References
For more information on configuring and using Syncfusion ToolBars, refer to:
- [Syncfusion Documentation: ToolBar](#<Doc reference>)
- [Windows Forms Controls: ToolBar](#<Doc reference>)

#### Notes
- The ToolBar properties must be configured before rendering to see changes.
- Ensure that the AutoSize property is appropriately set to allow dynamic resizing.

<!-- tags: [ToolBars, Buttons, Windows Forms, Syncfusion, properties, customization, controls] keywords: [alignment, autosize, backcolor, border, buttons, buttonbackcolor, buttonflatstyle, buttonforecolor, buttonsize] -->
```
