```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_418.jpeg
document_name: tools
page_number: 418
page_id: tools#page_418
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:12:40Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the use of `MonthCalendarAdv` control in Visual Basic.NET.
- Explains theming options for the calendar control.
- Provides an overview of styles supported by `MonthCalendarAdv`.

## Content

### Visual Basic Code Example
```vb
Me.monthCalendarAdv1.ThemedBorder = True
Me.monthCalendarAdv1.ThemedEnabledGrid = True
Me.monthCalendarAdv1.ThemedEnabledScrollButtons = True
```

### Visual Representation
Two versions of the `MonthCalendarAdv` are shown in Figure 216:
- **Themes Disabled**: Displays a default calendar layout without themes applied.
- **Themes Enabled**: Displays an enhanced calendar layout with themes applied.

**Figure 216: MonthCalendarAdv With and without Themes**

### Themes Enabled and Disabled Comparison
- **Themes Disabled** shows a basic grid layout with a grey border and typical styling.
- **Themes Enabled** shows a more visually appealing calendar with a darker header, themed grid, and buttons.

### Styles
`MonthCalendarAdv` supports the following styles, which can be set through the `Style` property:

#### Supported Styles
- **Style**
  - Default
  - OfficeXP
  - Office2003
  - VS2005
  - Office2007
- The default value is `Default`.

## API Reference
### MonthCalendarAdv Property Table

| MonthCalendarAdv Property | Description |
|----------------------------|-------------|
| Style                      | Gets or Sets the visual style of the MonthCalendarAdv. The options are <br> <br> Default <br> OfficeXP <br> Office2003 <br> VS2005 <br> Office2007 <br> <br> The default value is 'Default'. |

### Notes
- Themes can be enabled or disabled for various elements of the calendar, such as borders, the grid, and scroll buttons.
- The `Style` property allows developers to customize the visual appearance of the calendar to match different themes or user preferences.

<!-- tags: [WinForms, MonthCalendarAdv, themes, styles, control, visual settings] keywords: [MonthCalendarAdv, VB.NET, theming, themed border, themed grid, themed scroll buttons, Office themes] -->
```