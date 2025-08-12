```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_065.jpeg
document_name: QTP
page_number: 065
page_id: QTP#page_065
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:50Z
fidelity: lossless
-->

## 5 Known Issues

The following are the known issues in various platforms that are yet to be solved.

### 5.1 General

Documentation column is not supported in the Keyword View.

### 5.2 Essential Grid

Grid does not support drop-down controls such as Combo box, Grid List control, and so on.

### 5.3 Essential Tools

The following are the list of tools with their respective known issues:

#### Group Bar

When the Stacked Mode is set to true, the NavigationPanelButtonClick is not recorded.

#### GroupView

When the button view is set to false, the drag-and-drop, or re-ordering, of the GroupView item is not recorded. On clicking the re-ordered item, the index is recorded correctly.

#### DateTimePickerAdv

1. The events on the header panel that are inside the pop-up window cannot be replayed. The SetCurrentCell and ResizeRow events of the Syncfusion.QuickTestProfessional.Grid that are associated with the Calendar are triggered by the pop-up window. These events are recorded, but cannot be played back in the replay. While replaying, they should be manually removed.
   
2. Once the calendar events are handled, the replay works slower. This is because of the 'for each' loop in the replay, which enables you to trace all the controls that are inside the pop-up window and then show or hide them as you need.
```