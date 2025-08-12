```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_199.jpeg
document_name: tools
page_number: 199
page_id: tools#page_199
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:29:05Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Transition Between MDI Child and Docked Windows

The following figure illustrates the transformation of an MDI Child window into a Docked Window:

![Figure 100: MDI Child window transformed into Docked Window](https://docs.syncfusion.com/windowsforms/images/tools-windows-mdi-to-docked-window.png)

#### Note
You can set the docked control as an MDI Child in an easy method by using the "MDI Child" option in the **context menu**.

### Sample Installation Path

A sample demonstrating MDI child transition is available in the following sample installation path:

.. My Documents\Syncfusion\EssentialStudio\**Version Number**\Windows\Tools.Windows\Samples\2.0\Docking Package\MDIDemo

### Office 2007 Style for MDI Child Form

The MDI child forms can have Office 2007 look and feel, which can be enabled through the **Office2007MdiChildForm** property. Color schemes are also supported and can be specified using the **Office2007MdiColorScheme** property.

#### Example Code

```csharp
this.dockingManager1.Office2007MdiChildForm = true;
```

## API Reference

### Properties
- **Office2007MdiChildForm**: Enables the Office 2007 style for MDI child forms.
  - Type: Boolean
  - Description: Specifies whether the Office 2007 style is applied to MDI child form.
  - Default: `false`
  - Required: No

### Methods
- **SetOffice2007MdiChildForm**: Sets the Office 2007 style for MDI child forms.

### Events
- **Office2007MdiChildFormChanged**: Triggered when the Office 2007 style for MDI child forms is changed.

## Code Examples

### Enabling Office 2007 Style
```csharp
this.dockingManager1.Office2007MdiChildForm = true;
```

### Specifying Color Scheme
```csharp
this.dockingManager1.Office2007MdiColorScheme = Office2007ColorScheme.BlueOrange;
```

## Cross References

For more information on MDI child forms and docking, refer to the following:

- [Docking Package Documentation](https://docs.syncfusion.com/windowsforms/docking/)
- [MdiChildForm Documentation](https://docs.syncfusion.com/windowsforms/mdichildform/)

<!-- tags: [tools, windowsforms, docking, mdi, office 2007, api, version 11.4.0.26] keywords: [MDI Child, Docked Window, Office 2007 Style, Color Scheme, MDI Child Form] -->
```