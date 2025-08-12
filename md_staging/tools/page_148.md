<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_148.jpeg
document_name: tools
page_number: 148
page_id: tools#page_148
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:52:26Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Note

The Maximize button will be visible only if any other control is docked to the bottom of the former control.

#### Overview
- Control visibility handling in docked controls.

### Close Button

The visibility of the Close button can be controlled using the **CloseEnabled** property.

### AutoHide Button

Setting the **AutoHideEnabled** property shows or hides the auto hide button in the docked control. Clicking this button will autohide the docked controls.

#### Note

Docking Manager allows you to customize the above default buttons and also add custom caption buttons. See **Custom Caption Buttons** for more details.

### See Also

- **Context Menu, AutoHiding**
- **3.4.3.2.3 Custom Caption Buttons**

#### Custom Caption Buttons

Custom Caption Collection Editor, which can be accessed using **DockingManager.CaptionButtons** property, lets you customize the default buttons and also lets you add custom caption buttons.

---

**Figure 64: Docked Control with Custom Caption Buttons**

### Adding and customizing caption Buttons

---

```markdown
Figure: Docked Control with Custom Caption Buttons
```

---

## API Reference

### Properties
- **CloseEnabled**
- **AutoHideEnabled**
- **DockingManager.CaptionButtons**

## Code Examples

### Example: Customizing Caption Buttons

```csharp
// Example code for customizing caption buttons
using Syncfusion.Windows.Forms;

// Accessing the custom caption buttons editor
DockingManager.DockingWindow[0].CaptionButtons.Add(new DockingCaptionButton() {
    Text = "Custom Button",
    Click += delegate {
        MessageBox.Show("Custom Button Clicked!");
    }
});
```

### See also:
- **Custom Caption Buttons**
- **DockingManager.Properties**

---

<!-- tags: [Syncfusion Winforms, Custom Caption Buttons, Docking Manager, AutoHideEnabled, CloseEnabled] keywords: [Customization, Docked Controls, Auto Hide, Maximize Button, Windows Forms] -->