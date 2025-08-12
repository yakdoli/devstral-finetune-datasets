```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_417.jpeg
document_name: tools
page_number: 417
page_id: tools#page_417
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:11:09Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Shows background image settings for the MonthCalendarAdv control.
- Discusses theme customization features for the MonthCalendarAdv control.
- Explains how to control theme behavior using properties like ThemedBorder, ThemedEnabledGrid, and ThemedEnabledScrollButtons.

## Content

### BackgroundImage for MonthCalendarAdv

![BackgroundImage for MonthCalendarAdv](<Figure 215>)
**Figure 215: BackgroundImage for MonthCalendarAdv**

#### See Also
- **Border Styles, Visual Settings**
- **3.5.3.1.4.1.3 Visual Settings**

### Themes for MonthCalendarAdv

Some sections of the MonthCalendarAdv control are themed by default. The below table lists the properties which control the themed behavior of the border, grid, and scroll buttons.

| MonthCalendarAdv Properties             | Description                                                                 |
|------------------------------------------|-----------------------------------------------------------------------------|
| ThemedBorder                             | Specifies whether the border of the control is themed. By default it is true. |
| ThemedEnabledGrid                        | Specifies whether the grid holding the days is themed or not. By default it is false. |
| ThemedEnabledScrollButtons               | Specifies whether the scroll buttons are themed. It is set to true by default. |

### Example (C#)
```csharp
this.monthCalendarAdv1.ThemedBorder = true;
this.monthCalendarAdv1.ThemedEnabledGrid = true;
this.monthCalendarAdv1.ThemedEnabledScrollButtons = true;
```

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Class**: MonthCalendarAdv
  - **Properties**:
    - **ThemedBorder**: bool
    - **ThemedEnabledGrid**: bool
    - **ThemedEnabledScrollButtons**: bool

## Code Examples
```csharp
this.monthCalendarAdv1.ThemedBorder = true;
this.monthCalendarAdv1.ThemedEnabledGrid = true;
this.monthCalendarAdv1.ThemedEnabledScrollButtons = true;
```

<!-- tags: [syncfusion-sdk, winforms, monthcalendaradv, visualsettings, theming, controls, version 11.4.0.26] keywords: [backgroundimage, themedborder, themedenabledgrid, themedenabledscrollbuttons, theming, visual settings, monthcalendaradv, windows forms] -->
```