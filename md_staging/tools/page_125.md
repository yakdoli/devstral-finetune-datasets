```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_125.jpeg
document_name: tools
page_number: 125
page_id: tools#page_125
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:37:30Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Introduction to Windows Forms docking tools and their properties.
- Detailed exploration of the `dockingManager1` component with properties for customizing UI elements.
- Description of the process to set up the form's docking layout using drag-and-drop functionality.

## Content

### Properties of Docked Control

The `Properties` window for the `dockingManager1` component is shown in the screenshot below. The visible properties include various settings for themes, fonts, colors, and alignments related to the docking manager's appearance:

#### Appearance
- **AutoHideTabFont**: `Tahoma, 8.25pt`
- **AutoHideTabHeight**: `22`
- **BorderColor**: `ControlDark`
- **CaptionButtons**: `(Collection)`
- **DockLabelAlignment**: `Default`
- **DockTabAlignment**: `Bottom`
- **DockTabFont**: `Tahoma, 11world`
- **DockTabHeight**: `22`
- **HostFormClientBorder**: `True`
- **Office2007Theme**: `Blue`
- **PaintBorders**: `True`
- **RightToLeft**: `No`
- **ShowDockTabScrollButton**: `False`
- **SplitterWidth**: `4`
- **ThemesEnabled**: `False`

#### Appearance-Caption
- **ActiveCaptionBackground**: `Solid; Gainsboro`
- **ActiveCaptionFont**: `Arial, 8.25pt`
- **ActiveCaptionForeGround**: `Black`
- **EnableSuperToolTip**: `False`
- **InActiveCaptionBackground**: `Solid; Gainsboro`
- **InActiveCaptionFont**: `Trebuchet MS, 8.25pt`
- **InActiveCaptionForeGround**: `Black`
- **ShowCaptionImages**: `True`

Figure 45: Properties of Docked Control

### Setting Up the Docking Layout
6. The form's docking layout can be set up by dragging the dock-enabled controls and redocking or floating them at the desired locations by using the `DragProviderStyle` property.

## API Reference

- **Namespace**: `Syncfusion.Windows.Forms.Tools`
- **Class**: `DockingManager`
- **Properties**:
  - `AutoHideTabFont`: Font settings for the auto-hide tab.
  - `AutoHideTabHeight`: Height of the auto-hide tab.
  - `BorderColor`: Color of the border.
  - `CaptionButtons`: Collection of caption buttons.
  - `DockLabelAlignment`: Alignment of the dock label.
  - `DockTabAlignment`: Alignment of the dock tab.
  - `DockTabFont`: Font settings for the dock tab.
  - `DockTabHeight`: Height of the dock tab.
  - `HostFormClientBorder`: Indicates whether the host form client border is shown.
  - `Office2007Theme`: Specifies the Office 2007 theme color.
  - `PaintBorders`: Indicates whether borders are painted.
  - `RightToLeft`: Indicates the direction of text.
  - `ShowDockTabScrollButton`: Indicates whether the dock tab scroll button is shown.
  - `SplitterWidth`: Width of the splitter.
  - `ThemesEnabled`: Indicates whether themes are enabled.

  #### Appearance-Caption
  - `ActiveCaptionBackground`: Background color of the active caption.
  - `ActiveCaptionFont`: Font settings for the active caption.
  - `ActiveCaptionForeGround`: Foreground color of the active caption.
  - `EnableSuperToolTip`: Indicates whether super tool tips are enabled.
  - `InActiveCaptionBackground`: Background color of the inactive caption.
  - `InActiveCaptionFont`: Font settings for the inactive caption.
  - `InActiveCaptionForeGround`: Foreground color of the inactive caption.
  - `ShowCaptionImages`: Indicates whether caption images are shown.

## Code Examples

No code examples are provided in this section. For complete usage examples, refer to the related documentation or samples.

## Cross References
- See also: WinForms Docking Manager, Docking Layout, UI Customization.

<!-- tags: [Syncfusion, Windows Forms, Docking Manager, UI, Properties] keywords: [docking, controls, themes, fonts, borders, alignment, Office2007Theme, AutoHideTabFont] -->
```
