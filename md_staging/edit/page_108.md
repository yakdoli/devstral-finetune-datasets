```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_108.jpeg
document_name: edit
page_number: 108
page_id: edit#page_108
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:00:17Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Content

// To hide the outlining tooltip  
e.ShowMode = OutliningTooltipShowMode.Off;  
}  

**[VB.NET]**  

```vb
Private Sub editControl1_OutliningTooltipBeforePopup(sender As Object, e As Syncfusion.Windows.Forms.Edit.OutliningTooltipBeforePopupEventArgs) Handles editControl1.OutliningTooltipBeforePopup

    ' To display the outlining tooltip  
    e.ShowMode = OutliningTooltipShowMode.On

    ' To hide the outlining tooltip  
    e.ShowMode = OutliningTooltipShowMode.Off
End Sub
```

### See Also

- [Automatic Outlining](Automatic Outlining)

### 4.4.11.6 Wordwrap

Wordwrap allows users to view the entire contents of a line by wrapping text at the edge of the control (or text area) into one or more lines, that normally would have been outside the view in the Edit Control.

Edit Control allows advanced customization by using the Wordwrap functionality.

#### Type of Wordwrap

Wordwrap is enabled by setting the WordWrap property of the Edit Control to True. The two types of Wordwrap in Edit Control have been explained below.

| Edit Control Property | Description                                   |
|-----------------------|-----------------------------------------------|
| WordWrap              | Gets / sets state of the word wrapping mode. |
| WordWrapType          | Gets / sets type of word wrapping. The options provided are |

## API Reference

### WinForms-specific conventions

Refer to the WinForms-specific conventions in the guide for further details.

### Members

#### Properties

1. **WordWrap**
   - Gets / sets state of the word wrapping mode.

2. **WordWrapType**
   - Gets / sets type of word wrapping. The options provided are

### Code Examples

#### C#

```csharp
// Example usage of WordWrap property  
editControl1.WordWrap = true;
```

#### VB.NET

```vb
' Example usage of WordWrap property  
editControl1.WordWrap = True
```

## Cross References

- See also: Automatic Outlining

<!-- tags: [Syncfusion Winforms, Essential Edit, Wordwrap, Outlining Tooltip, Type of Wordwrap, Edit Control, Windows Forms] keywords: [WordWrap, OutliningTooltip, Edit Control Properties, Syncfusion Windows Forms, Advanced customization, Automatic Outlining] -->
```