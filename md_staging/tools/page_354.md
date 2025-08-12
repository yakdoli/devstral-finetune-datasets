```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_354.jpeg
document_name: tools
page_number: 354
page_id: tools#page_354
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:08:38Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

\[ \text{Figure 165: Button Pressed State Identified at Run time} \]

## 3.5.2.2 ButtonEdit

The ButtonEdit control embeds a text box control with a collection of button controls that can be customized to create many commonly used interfaces such as a file / folder browser or a drop-down text control. We can implement a file picker and folder browser using the ButtonEdit control. Drop-down popup controls can also be shown using the ButtonEdit control and the PopupContainerControl.

The edit control with a browse button extends a regular edit control by adding a button which can display an user-defined "browse" dialog. The ButtonEdit control provides an easy way to create controls with an edit control and any number of associated buttons.

\[ \text{Figure 166: ButtonEdit Control} \]

The ButtonEdit control derives from Syncfusion.Windows.Forms.ContainerControl and embeds one or more **ButtonEditChildButton** controls. The ButtonEditChildButton controls derive from Syncfusion.Windows.Forms.Button class and expose the functionality of buttons.

Using an edit control alongside one or more button controls is a very common requirement in graphical user interface programming. Some of the common examples are browse edit controls and drop-down controls.

```

<!-- tags: [syncfusion, winforms, buttonedit, buttoneditcontrol, containercontrol, filebrowser, folderbrowser, combobox-like control, dropdowncontrols, graphicaluserinterface] keywords: [buttonedit, filebrowser, folderbrowser, dropdowncontrols, browseeditcontrols, editcontrol, buttons, userinterfaceprogramming, graphicaluserinterface, interfaceprogramming] -->