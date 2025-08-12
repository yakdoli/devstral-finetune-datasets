```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_059.jpeg
document_name: tools
page_number: 059
page_id: tools#page_059
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:17:44Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This page explains how to add or remove CommandBars in Windows Forms using design-time verbs.
- It covers the initial docking and customization options for CommandBars.
- Includes screenshots demonstrating the CommandBar Collection Editor and the process of adding CommandBars through the design-time verb.

## Content

### CommandBars in Windows Forms

The CommandBars can be added or removed using the `Add CommandBar` design time verb or smart tag found in the property grid.

#### Initial Docking and Customization
New CommandBars are initially docked to the top border of the form. They can then be dragged, redocked, or floated to desired locations.

#### CommandBar Collection Editor

Figure 10 illustrates the CommandBar Collection Editor, which allows the configuration of CommandBar properties such as Appearance, Background Color, and Text.

![](https://files.fm/thumb_viewer?dl=http%3A%2F%2Fmrayvpyy&_w=2048&_h=1024)
**Figure 10: CommandBar Collection Editor**

In the image:
- The left pane lists CommandBar members (`commandBar1` and `commandBar2`).
- The right pane displays properties for `commandBar1`, including Appearance, BackColor, BackgroundImage, and Text.

#### Adding CommandBar through Design-Time Verb

Figure 11 shows the process of adding a CommandBar using the `Add CommandBar` verb in the design-time view.

![](https://files.fm/thumb_viewer?dl=http%3A%2F%2Fnbuzf629&_w=2048&_h=1024)
**Figure 11: Adding CommandBar Through Designer Time Verb**

In the image:
- The smart tag for `commandBarController1` is expanded.
- The `Add CommandBar` option is highlighted as part of the design-time verb functionality.

### Summary
This section provides a comprehensive guide to manipulating CommandBars in Windows Forms via the CommandBar Collection Editor and the design-time verb feature. It covers the initial setup, customization, and dynamic adjustment of CommandBars within the form environment.

## API Reference

- **Namespace**: `Syncfusion.Windows.Forms.Tools`
- **Class**: `CommandBarController`
- **Properties**:
  - `CommandBars`: A collection for managing CommandBar instances.
  - `Name`: The name of the CommandBar instance.
  - `BackColor`: Properties to customize the appearance of CommandBars.

## Code Examples

### C#
```csharp
// Example: Adding a CommandBar using the designer
commandBarController1.CommandBars.Add(new CommandBar());
```

### Additional Notes
- **Designer Time**: Use the smart tag and the `Add CommandBar` verb for design-time manipulation.
- **Runtime**: Programmatically add CommandBars as needed.

<!-- tags: Windows Forms, CommandBars, Design-Time Verbs, CommandBar Collection Editor, Syncfusion Windows Forms Tools, CommandBarController, CommandBar Properties keywords: CommandBar, CommandBarController, Add CommandBar, Design-Time Verb, CommandBar Appearance, Windows Forms Customization -->
```