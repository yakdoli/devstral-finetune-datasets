```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_162.jpeg
document_name: grid
page_number: 162
page_id: grid#page_162
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:58:08Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## 4.1.4.1.9 Masked Edit

The **MaskedEdit** cell type lets you to edit and display specially formatted text cells that conform to an edit mask that you specify. To make use of this cell type, set the **CellType** property to **MaskedEdit**. You can set additional properties like Mask, ClipMode, and so on, through the cell style's **GridMaskEditInfo** object. The various options will allow you to input masks to control the type of input that is valid within a cell. For example, you can use a MaskedEdit cell to facilitate the entry of a formatted Social Security number, a phone number, or a 3 character alpha-code.

## Code Example

The following code example illustrates how to set the cell type to MaskedEdit.

```csharp
// [C#]

gridControl[2, 3].Text = "First Name";
GridStyleInfo style1 = gridControl[2, 4];
GridMaskEditInfo maskedEditStyle1 = style1.MaskEdit;
gridControl[4, 3].Text = "Last Name";
gridControl[8, 3].Text = "Social Security";
GridStyleInfo style4 = gridControl[8, 4];
GridMaskEditInfo maskedEditStyle4 = style4.MaskEdit;

// Masked Edit Box 1
style1.CellType = "MaskEdit";
maskedEditStyle1.AllowPrompt = false;
maskedEditStyle1.ClipMode =
    Syncfusion.Windows.Forms.Tools.ClipModes.ExcludeLiterals;
style1.CultureInfo = new System.Globalization.CultureInfo("en-US");
maskedEditStyle1.DateSeparator = '-';
maskedEditStyle1.Mask = ">C<CCCCCCCCCC";
style1.MaxLength = 13;
style1.AutoSize = true;
maskedEditStyle1.SpecialCultureValue =
    Syncfusion.Windows.Forms.Tools.SpecialCultureValues.None;
maskedEditStyle1.UseLocaleDefault = false;
maskedEditStyle1.UseUserOverride = true;

// Masked Edit Box 4
style4.CellType = "MaskEdit";
maskedEditStyle4.AllowPrompt = false;
maskedEditStyle4.ClipMode =
    Syncfusion.Windows.Forms.Tools.ClipModes.IncludeLiterals;
style4.CultureInfo = new System.Globalization.CultureInfo("en-US");
maskedEditStyle4.DateSeparator = '-';
maskedEditStyle4.Mask = "999-99-9999";
style4.MaxLength = 11;
maskedEditStyle4.SpecialCultureValue =
    Syncfusion.Windows.Forms.Tools.SpecialCultureValues.None;
```

<!-- tags: [syncfusion winforms, grid, masked edit, cell type, mask, input validation, social security number, phone number, alpha-code, clip mode, special culture, user override] -->
```