```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_138.jpeg
document_name: tools
page_number: 138
page_id: tools#page_138
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:46:55Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section discusses the DragProviderStyle and Docking Package features in Syncfusion WinForms.
- Demonstrates properties such as DisallowFloating and EnableDoubleClickOnCaption.
- Covers Automated Hiding functionality in Docking Package.

## Content

### DragProviderStyle and DisallowFloating Property

#### Figure 55: DragProviderStyle="Standard" FloatingOnly = "True"

> A sample which demonstrates DisallowFloating property is available in the below sample installation path.

**..My Documents\Synfusion\EssentialStudio\[Version Number]\Windows\Tools.Windows\Samples\2.0\Docking Package\WindowFill**

### Floating State to Docking State and Vice Versa

Setting the **EnableDoubleClickOnCaption** property to true allows you to dock or float the control by just double-clicking on the captions of the docked control. By default, it is true.

#### See Also
- Nested Docking and Floating
- [How to make a docked control Floating Only?](#)
- [How to float a single control even if it is tabbed to many controls?](#)
- [How to find out whether a docked control is floating or not?](#)
- [How to get individual floating controls properties?](#)

### 3.4.3.1.4 AutoHiding

Docking manager provides an auto-hide facility to the docked control. When the auto-hide button (looks like a bell) is clicked, the docked controls will be hidden and will be placed along the side of the container control on which it was placed. When the mouse is moved over it, the auto-hidden control will be displayed, and the control will restore its appearance when the auto-hidden button is clicked again.

---

## API Reference

### Methods and Properties
- **EnableDoubleClickOnCaption**: Allows toggling the behavior of docking and floating controls using double-click on captions.
- **DisallowFloating**: Property to prevent a docked control from entering a floating state.
- **AutoHideButton**: A button with a bell icon used to temporarily hide docked controls.

---

## Code Examples

### Example: Enabling AutoHiding

```csharp
// Sample code to demonstrate enabling AutoHiding behavior
private void EnableAutoHiding()
{
    // Configure Docking Manager for auto-hide functionality
    DockingManager.EnableAutoHide = true;

    // Assign AutoHideButton for docked controls
    foreach (var control in DockManager.DockPanels)
    {
        control.AutoHideButton = new AutoHideButton();
    }
}
```

---

## Cross References

- **Related Topics**: Docking Advanced Features, DockState Transitions, Floating Control Management.
- **Documentation Links**:
  - [Syncfusion WinForms Docking Package Documentation](#)
  - [Docking and Floating Controls](#)

---

## Additional Notes

- **Figure Caption**: "Figure 55: DragProviderStyle="Standard" FloatingOnly = "True"" provides a visual representation of how the docked control behaves with specific settings.
- **See Also Section**: Provides links to related functionality and frequently asked questions regarding docking and floating controls.

<!-- tags: [winforms, docking, floating, autohide, disallowfloating, enabledoubleclickoncaption, Automated Dock Management, Version 11.4.0.26] keywords: [docking package, float only, auto hide, docked control, enable double click, disallow floating] -->
```