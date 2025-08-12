```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_083.jpeg
document_name: edit
page_number: 083
page_id: edit#page_083
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:58:38Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Content

### Configuring Line Number Options

#### C#

```csharp
// Specify the alignment of line numbers.
this.editControl.LineNumbersAlignment = Syncfusion.Windows.Forms.Edit.Enums.LineNumberAlignment.Right;

// Assign any color to the line numbers.
this.editControl.LineNumbersColor = Color.IndianRed;

// Assign any font to the line numbers.
this.editControl.LineNumbersFont = new Font("Verdana", 9);

// Enabling SelectOnLineNumberClick property to perform selection on clicking the line numbers.
this.editControl.SelectOnLineNumberClick = true;
```

#### VB.NET

```vb.net
' Specify the alignment of line numbers.
Me.editControl.LineNumbersAlignment = Syncfusion.Windows.Forms.Edit.Enums.LineNumberAlignment.Right

' Assign any color to the line numbers.
Me.editControl.LineNumbersColor = Color.IndianRed

' Assign any font to the line numbers.
Me.editControl.LineNumbersFont = new Font("Verdana", 9)

' Enabling SelectOnLineNumberClick property to perform selection on clicking the line numbers.
Me.editControl.SelectOnLineNumberClick = True
```

#### Figure: IndianRed Color Line Numbers with FontSize = "9", FontStyle = "Verdana"

![Figure: IndianRed Color Line Numbers with FontSize = "9", FontStyle = "Verdana"](https://i.imgur.com/6CyfcIH.jpg)

**Figure 22: IndianRed Color Line Numbers with FontSize = "9", FontStyle = "Verdana"**

### Highlighting Current Line at Run Time

You can highlight the current line where the mouse pointer is present by setting the `HighlightCurrentLine` property of the Edit Control to `True`. Set the color for the highlighted line by using the `CurrentLineHighlightColor` property.

## Page-level Navigation/TOC (if applicable)

- Configuring Line Number Options
  - C#
  - VB.NET
- Highlighting Current Line at Run Time

## Cross References

See also:
- [Figure: IndianRed Color Line Numbers with FontSize = "9", FontStyle = "Verdana"]

## RAG Annotations

### Tags:
- `essential edit`
- `windows forms`
- `line numbers`
- `alignment`
- `color`
- `font`
- `selection`
- `highlight current line`
- `currentlinehighlightcolor`
- `highlightcurrentline`

### Keywords:
- alignment
- color
- font
- selection
- current line
- highlight
- line numbers
- windows forms
```