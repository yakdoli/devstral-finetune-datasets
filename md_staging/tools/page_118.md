```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_118.jpeg
document_name: tools
page_number: 118
page_id: tools#page_118
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:33:26Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## 3.3.4.1 Why is it not possible to add a CommandBarController to a form containing XP Menus and ToolBars?

The CommandBars framework should be used only with the standard .NET Menus / ToolBars and not with the Essential Tools XP Menus. This is because the XP Menus designer infrastructure will freeze the .Net environment.

But it is possible to add a CommandBar to a form containing XP Menus through code as shown in the sample screen shot.

![CommandBar added to XP Menus and ToolBars](https://example.com/figure40.png)
*Figure 40: CommandBar added to XP Menus and ToolBars*

## 3.4 Docking Package

The Docking Package comprises of the Essential Tools docking windows architecture that allows users to add Visual Studio .NET type dockable controls to Windows Forms applications. Any control can be set as a docking window and docking layouts can be hosted within Forms, UserControls or any derivative of the ContainerControl type. The framework supports the complete range of docking behaviors such as docking/floating, nested levels, tabbed groups, state transitions, autohide, MDIChild transitions, non-dockable/non-floatable options, a unique fill mode and full state persistence. An advanced designer allows users to harness full WYSIWYG configuration of the dock layout.

## API Reference (if applicable)

### Essential Tools Docking Package
- **Class**: DockingManager
  - Properties:
    - DockPanel
    - DockPane
    - PaneCollection
    - LayoutType
    - LayoutOptions
  - Methods:
    - SaveLayout
    - LoadLayout
    - ResetLayout
    - UpdateLayout
    - GetDockPanel
    - GetDockPane
  - Events:
    - LayoutChanged
    - DockPanelCreated
    - DockPanelDestroyed

## Code Examples

```csharp
// Example demonstrating the use of the DockingManager in WinForms
using Syncfusion.Windows.Forms.Docking;

public partial class MainForm : Form
{
    private DockingManager dockingManager;

    public MainForm()
    {
        InitializeComponent();
        dockingManager = new DockingManager(this);

        // Configure docking options
        dockingManager.DockPanel.DefaultDockStyle = DockStyle.Left;
        dockingManager.DockPanel.EnableDocking = true;

        // Add controls to the docking manager
        dockingManager.DockPanel.DockPanel.AddDockedControl(ControlPanel1);
        dockingManager.DockPanel.DockPanel.AddDockedControl(ControlPanel2);

        // Load the saved layout
        dockingManager.LoadLayout("Settings.dockingLayout");
    }

    private void Form1_Load(object sender, EventArgs e)
    {
        // Additional setup for the form can be done here
    }
}
```

## RAG Annotations

<!-- tags: [docking package, commandbar, xp menus, toolbars, windows forms, essential tools, syncfusion] keywords: [commandbarcontroller, .net menus, toolbars, xp menus designer, dockable controls, docking windows architecture, visual studio, state transitions, autohide, full state persistence, WYSIWYG, UI/UX] -->
```