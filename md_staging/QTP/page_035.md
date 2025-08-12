```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_035.jpeg
document_name: QTP
page_number: 035
page_id: QTP#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:31Z
fidelity: lossless
-->

## Editing a Test

### Overview
- Describes how to edit a test in QuickTest Professional, supporting two views: Keyword view and Expert view.
- Highlights the switching mechanism between views using the tab at the bottom left of the test screen.
- Focuses on managing testing processes using scripts in the Expert view.

### Content

#### Editing a Test

A test can be edited in either the Keyword view or in the Expert view. You can switch between these views by selecting the required tab at the bottom left of the QuickTest Professional test screen.

#### Editing in Expert View

This view is specially provided for the experts in VB script. In the Expert view, the VB scripts are generated while recording. You can also manually write scripts to the existing scripts in this view. So, this view can be used as a tool for managing the testing process in a more controlled manner. You can add scripts to trigger events manually.

**The following image shows adding a script line to the Expert View pane.**

![QuickTest Professional - Expert View Script Pane](https://example.com/path/to/image)

### Figure: QuickTest Professional - Expert View Script Pane

The screenshot displays the Expert View pane in QuickTest Professional, showing various script commands being entered. The script lines include actions such as setting cell data, current cells, clicking, and modifying radiobutton and checkbox states within a `gridControl1` object. The interface provides tools for recording, running, and stopping scripts, as well as managing resources and debugging options.

### Code Examples

```vb
SwfWindow("GridControl").SwfObject("gridControl1").SetCellData 13,2,"-739.00"
SwfWindow("GridControl").SwfObject("gridControl1").SetCurrentCell 16,2
SwfWindow("GridControl").SwfObject("gridControl1").SetCurrentCell 10,2
SwfWindow("GridControl").SwfObject("gridControl1").SetCellData 10,2,"rwftew"
SwfWindow("GridControl").SwfObject("gridControl1").Click
SwfWindow("GridControl").SwfObject("gridControl1").SetCurrentCell 4,1
SwfWindow("GridControl").SwfObject("gridControl1").SetCellCheckBox 4,1,"ON"
SwfWindow("GridControl").SwfObject("gridControl1").SetCurrentCell 4,2
SwfWindow("GridControl").SwfObject("gridControl1").SetCellCheckBox 4,2,"OFF"
```

### RAG Annotations
<!-- tags: [test-editing, expert-view, vb-script, syncfusion-qtp] keywords: [keyword view, expert view, script management, test process, manual triggers] -->
```