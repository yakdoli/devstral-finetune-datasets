```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_630.jpeg
document_name: tools
page_number: 630
page_id: tools#page_630
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:25:10Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to hide popups using the `HidePopup` method in different modes.
- Focuses on handling changes in popups with `PopupCloseType` modes.
- Discusses using a custom `PopupControlContainer` to maintain focus with ComboBoxBase controls.

## Content

### Hiding popup with PopupCloseType mode

We can hide the popup using the `HidePopup` method in `PopupCloseType` mode.

To hide the popup with the changes applied to the popup, `PopupCloseType` should be set to **Done**. To cancel the changes, `PopupCloseType` should be set to **Canceled**. Setting `PopupCloseType` to **Deactivated** will deactivate the popup when the user clicks in a different application.

#### 3.5.6.1.3.3 Hosting ComboBoxBase Control

We can place the `ComboBoxBase` control within `PopupControlContainer` such that the `PopupControlContainer` does not close when the `ComboBoxBase`'s Popup is displayed.

You can do this by deriving from the `PopupControlContainer`, overriding the `OnPopup` method, and setting the focus to the derived control. This will ensure that the derived `PopupControlContainer` does not lose focus and close prematurely. The customized `PopupControlContainer` code should be like the code snippet shown below.

#### Code Example: CustomPopupControlContainer

**C#**
```csharp
public class CustomPopupControlContainer : Syncfusion.Windows.Forms.PopupControlContainer
{
    public CustomPopupControlContainer()
    {
    }

    public CustomPopupControlContainer(IContainer container) : this()
    {
        container.Add(this);
    }

    protected override void OnPopup(EventArgs args)
    {
        base.OnPopup(args);
        this.Focus();
    }
}
```

**VB.NET**
```vb
Public Class CustomPopupControlContainer
```

## API Reference

### CustomPopupControlContainer

- **Namespace**: Syncfusion.Windows.Forms
- **Properties**: `PopupCloseType`
- **Methods**: `OnPopup`, `HidePopup`
- **Events**: 

## Code Examples

The provided snippets demonstrate how to create a custom `PopupControlContainer` that maintains focus while a `ComboBoxBase` control is in use.

### CustomPopupControlContainer Class

- Inherits from `Syncfusion.Windows.Forms.PopupControlContainer`.
- Overrides the `OnPopup` method to focus on the container when the popup is displayed.

## Cross References

- For more details on `PopupControlContainer`, refer to the documentation on customizing popup behavior.
- Explore additional methods and properties related to handling popups in the API reference.

<!-- tags: [syncfusion, winforms, popupcontrolcontainer, comboboxbase, custompopupcontrol, onpopup, hidepopup] keywords: [popup, Pop up, custom popup] -->
```