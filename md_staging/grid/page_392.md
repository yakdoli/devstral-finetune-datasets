```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_392.jpeg
document_name: grid
page_number: 392
page_id: grid#page_392
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:14:23Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates customizing the appearance of specific rows and columns in the GridControl.
- Focuses on applying styles to row headers and adjusting background colors.
- Shows examples using C# and VB.NET for altering the "Row Header" base style.

## Content

### Customizing Row and Column Styles

#### Figure 142: Row 3 with Blue Text and Column 3 With Red Text. Note the Row Attribute Takes Precedence Over the Column Attribute in Cell 3,3 as the TGxt is Blue

![Row attributes taking precedence over column attributes](image of Figure 142)

The figure illustrates how a row's attribute (in this case, blue text for row 3) overrides a column's attribute (red text for column 3) in cell 3,3.

#### Code Example for Changing Base Style in C#

```csharp
// Change a base style, eg. Row Header.
gridControl1.BaseStylesMap["Row Header"].StyleInfo.BackColor = 
    Color.FromArgb(228, 255, 255);
```

#### Code Example for Changing Base Style in VB.NET

```vb
' Change a base style, eg. Row Header.
gridControl1.BaseStylesMap("Row Header").StyleInfo.BackColor = 
    Color.FromArgb(228, 255, 255)
```

#### Figure 143: Row Headers No Longer Shaded Gray, Now Light Blue

![Row headers changed to light blue](image of Figure 143)

This figure shows the updated appearance of the row headers after modifying their background color.

## Page-level Navigation/TOC
- **Figure 142**: Row 3 with Blue Text and Column 3 With Red Text
- **Figure 143**: Row Headers No Longer Shaded Gray, Now Light Blue
- **Code Examples**: Changing Base Styles in C# and VB.NET

<!-- tags: [WinForms, Syncfusion, GridControl, Custom Styles, Row Headers, Column Attributes, C#, VB.NET] keywords: [base style, row attribute, cell color, red, blue, light blue, background color, precedence, attribute] -->
```