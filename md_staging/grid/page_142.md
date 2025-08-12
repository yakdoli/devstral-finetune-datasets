<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_142.jpeg
document_name: grid
page_number: 142
page_id: grid#page_142
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:54:25Z
fidelity: lossless
-->

## 4.1.3.2 Cell Types

Each cell may contain a specialized control such as a Text Box, Check Box or Combo Box, and this attribute of the cell is referred to as its Cell Type. Following table lists all the default cell types.

| Feature         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| Static Cell     | Cannot be edited.                                                          |
| Custom Cell     | Allows custom integration.                                                 |
| Formula Cell    | Allows entries of algebraic formulas.                                      |
| Currency Cell   | Display currency type formats.                                             |
| NumericUpDown   | Allows to increase/decrease the numeric value.                             |
| ComboBox        | Implements a standard combo box interface.                                 |
| MaskedEdit      | Allows users to input masks to control validation.                         |
| RichText Cell   | Allows users to display and edit Rich Text.                                |
| WebBrowser Cell | Display a web browser.                                                     |
| ColorPiker       | Allows the user to interactively select a color.                           |
| Grid Drop-Down  | Allows drop-down grids in any mode.                                        |
| HeaderText      | Host a Header cell type.                                                   |
| CheckBox        | Implements a check box.                                                    |
| PushButton      | Implements a push button control.                                          |
| MonthCalendar   | Display a drop-down month calendar.                                        |
| Password Cell   | Accepts entries without displaying text.                                   |
| ProgressBar Cell| Display Progress Bars.                                                     |
| Slider Cell     | Display Slider Controls.                                                   |
| XHTMML Cell     | Display XHTML formatted text.                                              |

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: GridCellModel

### Members
#### Properties:
- **StaticCell**: Indicates whether the cell is static and cannot be edited.
- **CustomCell**: Allows customization of cell behavior and integration.
- **FormulaCell**: Indicates whether the cell accepts algebraic formulas.
- **CurrencyCell**: Indicates whether the cell displays currency type formats.
- **NumericUpDownControl**: Indicates whether the cell represents a numeric up-down control.
- **ComboBoxControl**: Indicates whether the cell implements a standard combobox interface.
- **MaskedEditControl**: Indicates whether the cell allows input masks for validation.
- **RichTextControl**: Indicates whether the cell allows rich text display and editing.
- **WebBrowserControl**: Indicates whether the cell displays a web browser.
- **ColorPickerControl**: Indicates whether the cell allows color selection.
- **GridDropDownControl**: Indicates whether the cell allows dropdown grids.
- **HeaderCellType**: Indicates the header cell type hosted by the cell.
- **CheckBoxControl**: Indicates whether the cell implements a checkbox.
- **PushButtonControl**: Indicates whether the cell implements a push button.
- **MonthCalendarControl**: Indicates whether the cell displays a dropdown month calendar.
- **PasswordCellControl**: Indicates whether the cell accepts entries without displaying text.
- **ProgressBarCellControl**: Indicates whether the cell displays progress bars.
- **SliderCellControl**: Indicates whether the cell displays slider controls.
- **XHTMMLCellControl**: Indicates whether the cell displays XHTML formatted text.

---

<!-- tags: [Syncfusion, Winforms, Grid, Cell Types, Cell Model, User Guide, Version 11.4.0.26] keywords: [Static Cell, Custom Cell, Formula Cell, Currency Cell, NumericUpDown, ComboBox, MaskedEdit, RichText, WebBrowser, ColorPiker, Grid Drop-Down, HeaderText, CheckBox, PushButton, MonthCalendar, Password Cell, ProgressBar Cell, Slider Cell, XHTMML Cell] -->