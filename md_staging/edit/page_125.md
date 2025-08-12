```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_125.jpeg
document_name: edit
page_number: 125
page_id: edit#page_125
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:01:48Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Transparent Selection

### Overview
- TransparentSelection property enables or disables the highlighting of selected text ranges.
- When TransparentSelection is set to True, the selected text range is highlighted with a dark background, allowing visibility of syntax highlighting within the selection.
- When TransparentSelection is set to False, the selected text range is highlighted with a semi-transparent background, allowing visibility of syntax highlighting within the selection.

### Content

#### Transparent Selection Enabled
When the TransparentSelection property is set to False, the selected text range is highlighted with a dark background, as shown in the following screenshot:

```html
<div>
    <pre>
        <span style="background: #d9d9e6;">26 </span><span style="color: #0000ff; font-weight: bold;">Region</span> <span style="color: #0000ff; font-style: italic;">"Exponent Region"</span>
        <br />
        <span style="background: #d9d9e6;">27 </span>
        <br />
        <span style="background: #d9d9e6;">28 </span><span style="color: #0000ff; font-weight: bold;">(defun</span> <span style="color: #0000ff; font-style: italic;">expon</span> <span style="color: #0000ff; font-style: italic;">(base power)</span>
        <br />
        <span style="background: #d9d9e6;">29 </span><span style="color: #0000ff; font-weight: bold;">(cond</span> <span style="color: #0000ff; font-style: italic;">((zerop power) 1)</span>
        <br />
        <span style="background: #d9d9e6;">30 </span><span style="color: #0000ff; font-weight: bold;">(evenp power)</span> <span style="color: #0000ff; font-style: italic;">(expon (* base base ) (truncate power 2)))</span>
        <br />
        <span style="background: #d9d9e6;">31 </span><span style="color: #0000ff; font-weight: bold;">(t</span> <span style="color: #0000ff; font-style: italic;">(* base (expon (* base base) (truncate power 2)))))))</span>
        <br />
        <span style="background: #d9d9e6;">32 </span>
        <br />
        <span style="background: #d9d9e6;">33 </span><span style="color: #0000ff; font-weight: bold;">#End Region</span>
    </pre>
</div>

<div align="center">
    <strong>Figure 41: Transparent Selection Enabled</strong>
</div>

Setting the TransparentSelection property to False will highlight the selected text range with a dark background (which will not let you view the syntax highlighting in the text within the selected region), as shown in the following screenshot:

```html
<div>
    <pre>
        <span style="background: #d9d9d9;">26 </span><span style="color: #0000ff; font-weight: bold;">Region</span> <span style="color: #0000ff; font-style: italic;">"Exponent Region"</span>
        <br />
        <span style="background: #d9d9d9;">27 </span>
        <br />
        <span style="background: #d9d9d9;">28 </span><span style="color: #0000ff; font-weight: bold;">(defun</span> <span style="color: #0000ff; font-style: italic;">expon</span> <span style="color: #0000ff; font-style: italic;">(base power)</span>
        <br />
        <span style="background: #d9d9d9;">29 </span><span style="color: #0000ff; font-weight: bold;">(cond</span> <span style="color: #0000ff; font-style: italic;">((zerop power) 1)</span>
        <br />
        <span style="background: #d9d9d9;">30 </span><span style="color: #0000ff; font-weight: bold;">(evenp power)</span> <span style="color: #0000ff; font-style: italic;">(expon (* base base ) (truncate power 2)))</span>
        <br />
        <span style="background: #d9d9d9;">31 </span><span style="color: #0000ff; font-style: italic;">(* base (expon (* base base) (truncate power 2)))))))</span>
        <br />
        <span style="background: #d9d9d9;">32 </span>
        <br />
        <span style="background: #d9d9d9;">33 </span><span style="color: #0000ff; font-weight: bold;">#End Region</span>
    </pre>
</div>

<div align="center">
    <strong>Figure 42: Transparent Selection Disabled</strong>
</div>

#### Cancelling / Resetting Selection

Text selection can be either cancelled or reset by using the below given methods.

| Edit Control Method       | Description                                      |
|---------------------------|--------------------------------------------------|
| SelectionCancel           | Removes selection and causes invalidation of the area that was selected. |
| ResetSelection            | Resets selection.                               |

## Code Example

```csharp
// Removes selection from text.
this.editControl1.SelectionCancel();
```

## API Reference
- **Namespace**: Syncfusion.Windows.Forms
- **Class**: EditControl
- **Methods**:
  - `SelectionCancel()`: Removes the selection and invalidates the selected area.
  - `ResetSelection()`: Resets the selection.

<!-- tags: [editcontrol, transparentselection, winforms, selectionmanagement] keywords: [selectioncancel, resetselection, transparentselectionproperty, textselection] -->
```
