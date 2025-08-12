```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_238.jpeg
document_name: grid
page_number: 238
page_id: grid#page_238
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:03:23Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### WinForms-specific conventions

#### Figure 129: Multilevel Undo/Redo

![Multilevel Undo/Redo](https://i.imgur.com/figz23.png)

#### 4.1.4.5.7 Find Replace

The **Find Replace** feature enables you to search and replace the required element present in the Grid/Worksheet. You can implement the fastest Find and Replace functionality with Grid controls by using `GridFindReplaceDialogSink` and `GridFindReplaceEventArgs` classes. The `GridFindReplaceDialogSink` class provides the methods that are necessary to perform a Find and Replace operation. The `GridFindReplaceEventArgs` class provides information about the Find and Replace dialog box.

The value entered in the **Search For** field is highlighted in the worksheet after the search action is performed. You can switch over to each highlighted text by clicking the **Find Next** button. This functionality is available only when there is more than one search result.

### Search and Replace Options

<!-- tags: [Syncfusion Winforms, version 11.4.0.26, grid controls, find replace] keywords: [GridFindReplaceDialogSink, GridFindReplaceEventArgs, search, replace, worksheet] -->
```