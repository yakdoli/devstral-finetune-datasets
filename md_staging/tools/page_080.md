```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_080.jpeg
document_name: tools
page_number: 080
page_id: tools#page_080
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:19:32Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Setting BarItem Text

The following sample code can be used to set the text of a `barItem3` to "Syncfusion Sales".

```vbnet
Me.barItem3.Text = "Syncfusion Sales"
```

#### Property Window Demonstration

Here is an illustration of how to set the "PopupMenu" property in the Properties Window for the CommandBar Control.

#### Figure Reference

**Figure 26:** "PopupMenu" property in the Properties Window of CommandBar Control

![Properties Window of CommandBar Control](https://i.imgur.com/SampleImage1.png)

**Figure 27:** Popup Menu displayed from the DropDown Button of CommandBar Control

![Popup Menu displayed from CommandBar Control](https://i.imgur.com/SampleImage2.png)

### See Also

- [Popup Menu on Right Clicking the CommandBar](#)

---

### 3.3.3.4.2 Popup Menu on Right Clicking the CommandBar

#### Overview
- The purpose of this section is to demonstrate how to show the Popup Menu when right-clicking on the CommandBar.
- Detailed steps are provided to configure the CommandBar to display the Popup Menu on right-click.

#### Procedure

To show the Popup Menu on right-clicking on the CommandBar, follow these steps:

1. **Add CommandBar to the Form**:
   - Drag the CommandBarController onto the form.
   - Add a CommandBar to the form by right-clicking on CommandBarController.

2. **Configure Popup Menu**:
   - Add a PopupMenusManager along with the PopupMenu component.
   - This will introduce an extended property on the CommandBar properties window as "XPContextMenu on popupMenusManager".
   - Set the required Popup Menu from the dropdown list in the properties window.

#### Code Example

No specific code is required beyond configuring the properties as described above.

---

### Page-level Navigation/TOC (if applicable)

- **3.3.3.4.2 Popup Menu on Right Clicking the CommandBar**
  - Overview
  - Procedure

#### RAG Annotations

<!-- tags: [CommandBar, Syncfusion, Windows Forms, PopupMenu, PropertyWindow, RighClick, ExtendedProperty, CommandBarController] keywords: [CommandBar, right-click, popup menu, properties, dropdown, XPContextMenu, Syncfusion Winforms, Procedure, step-by-step] -->
```