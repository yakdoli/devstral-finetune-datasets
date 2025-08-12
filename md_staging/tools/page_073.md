```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_073.jpeg
document_name: tools
page_number: 073
page_id: tools#page_073
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:19:56Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- A demonstration of the Docked CommandBar in Windows Forms applications.

## Content

### Docked CommandBar Demonstration

#### Figure: CommandBar docked to the right border of the form on clicking the Right Button

A sample which demonstrates the Docked CommandBar is available in the below sample installation path.

```
..My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Tools.Windows\Samples\2.0\CommandBars Package\CommandBars
```

**See Also**

- [Floating CommandBar](Floating CommandBar)

### 3.3.3.2 Button Settings

The buttons settings of the CommandBar control are given below.

#### Close and DropDown Button

The close button of CommandBar gets displayed when it is in the float state, whereas the dropdown button gets displayed both in the dock and float state.

#### Table 8: Button Settings

| CommandBar Property           | Description                                                                                          |
|-------------------------------|------------------------------------------------------------------------------------------------------|
| HideCloseButton               | Determines whether the CommandBar will have a close button when floating.                          |
| HideDropDownButton            | Draws the CommandBar with / without the dropdown button.                                          |

**Note:** Popup Menu can be displayed from the dropdown button of the CommandBar. Refer Popup Menu topic.

### Code Examples

#### C#

```csharp
this.commandBar1.HideCloseButton = true;
this.commandBar1.HideDropDownButton = true;
```

#### VB.NET

```vb
Me.commandBar1.HideCloseButton = True
```

## API Reference

- **HideCloseButton**: Determines whether the CommandBar will have a close button when floating.
- **HideDropDownButton**: Draws the CommandBar with / without the dropdown button.

## See also

- Docked CommandBar
- Floating CommandBar
- Popup Menu

<!-- tags: [winforms, commandbar, docked, float state, dropdown button, close button, settings] keywords: [syncfusion, essential studio, windows forms, button settings, hideclosebutton, hidedropdownbutton, popup menu] -->
```