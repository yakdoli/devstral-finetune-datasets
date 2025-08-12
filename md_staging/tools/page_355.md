```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_355.jpeg
document_name: tools
page_number: 355
page_id: tools#page_355
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:08:33Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Introduces the ButtonEdit control as a composite control that combines buttons with a Text Box.
- Discusses customization and usage scenarios for ButtonEdit, including themes, visual styles, event handling, and databinding.
- Guides users on creating ButtonEdit controls through the designer and programmatically.

## Content

### 3.5.2.2.1 Features
**ButtonEdit is a composite control that combines buttons with a Text Box. The Button Edit control can be used for a variety of purposes that require a Text Box placed alongside one or more buttons. It has following features:**

- **Customization:** It can be customized to create many commonly used interfaces such as a file / folder browser or a drop-down text control.
- **Button Management:** Buttons can be added /removed through design verbs and also accessed through Buttons property collection editor.
- **Themes and Styles:** ButtonEdit Supports Themes (Blue, Oliver and Silver) and visual styles. See **Style Settings.**
- **Calendar Popup:** The ButtonEdit can be used to display the CalendarPopup. See **Click Event** topic.
- **Task Assignment:** You can add and assign tasks to each ButtonEditChildButton of ButtonEdit.
- **Custom Text Box Types:** The internal Textbox for ButtonEdit can be modified to any custom TextBox, such as CurrencyTextBox, Integer TextBox, PercentTextBox, and so on.
- **Image Overlay:** Images can be drawn over the buttons in ButtonEdit.
- **DataBinding Support:** Supports Databinding. See **Click Event** topic.

#### See Also
- **Concepts and Features**

### 3.5.2.2.2 Creating ButtonEdit
This section will help you to get started with the ButtonEdit control. The below topics will guide you to create ButtonEdit control through designer and programmatically.

#### 3.5.2.2.2.1 Through Designer
The ButtonEdit control can be used in situations where a set of buttons are needed alongside an edit control, such as in a browser for files dialog. This tutorial shows how to use the ButtonEdit control, set the Button properties and handle the events.

1. Create a new Windows Forms application and open the main form in the designer. Drag and drop ButtonEdit control from the toolbox to the form.

```


<!-- tags: [winforms, buttonedit, composite control, design, customization, databinding, themes, style settings, calendar popup, task assignment, custom text box, image overlay] keywords: [buttonedit, text box, customization, buttons, themes, visual styles, databinding, click event, task assignment, calendar popup, custom text box, image overlay] -->
```