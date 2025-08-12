```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en 
source_filename: page_201.jpeg
document_name: tools
page_number: 201
page_id: tools#page_201
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:29:00Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains nested docking and floating features in the Docking windows framework.
- Demonstrates full-featured support for nested docking and floating without requiring additional code.
- Includes practical examples and a visual representation.

## Content

### See Also
- How to avoid flickering while creating MDI child form?
- How to detect whether a particular control is in MDI mode or not?

#### 3.4.3.7.4 Nested Docking and Floating

Docking windows framework provides full-fledged support for nested docking and Floating at runtime without implementing a single piece of code.

![](https://i.imgur.com/empty_image.png)

*Figure 102: Nested Docking*

## API Reference

This section includes detailed API information relevant to the docking and floating features.

### Nested Docking

#### Methods
- `DockPanel.Dock`: Allows docking of panels within the main window.
- `Panel.AutoHide`: Controls the auto-hiding functionality of panels.
- `Panel.Float`: Permissions panels to float freely around the workspace.

#### Properties
- `DockState`: Indicates the current docking state of a panel.
- `VisiblePanels`: Provides a collection of currently visible panels.

## Code Examples

### Example 1: Basic Setup for Nested Docking

```csharp
using Syncfusion.Windows.Forms.Docking;
using System.Windows.Forms;

public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();
        InitializeDockingManager();
    }

    private void InitializeDockingManager()
    {
        DockPanel.DockPanel panel = new DockPanel.DockPanel();
        panel.Dock = DockStyle.Fill;
        panel.AutoHide = true;

        // Add panels to the dock panel here
    }
}
```

### Example 2: Configuring Auto-Hiding and Floating

```csharp
using Syncfusion.Windows.Forms.Docking;
using System.Windows.Forms;

public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();
        InitializeDockingManager();
    }

    private void InitializeDockingManager()
    {
        DockPanel.DockPanel panel = new DockPanel.DockPanel();
        panel.Dock = DockStyle.Fill;
        panel.AutoHide = true;

        // Configure auto-hiding for specific panels.
        foreach (var configPanel in panel.ConfigPanels)
        {
            configPanel.AutoHide = true;
            configPanel.Float();
        }
    }
}
```

## Cross References

- For more detailed information on MDI (Multiple Document Interface) functionality, refer to the "MDI" section in the documentation.
- Additional resources for UI Customization and Advanced Docking Features are included in the User Interface Customization and Advanced Docking Features chapters.

<!-- tags: [syncfusion, winforms, docking, floating, controls, ui, tools] keywords: [nested docking, floating, auto-hiding, runtime support, full-featured, dock panel, panels, user interface, documentation] -->
```