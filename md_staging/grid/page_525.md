```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_525.jpeg
document_name: grid
page_number: 525
page_id: grid#page_525
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:21:59Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Essential Grid provides clipboard event handling and exceptional performance capabilities.
- It supports real-time updates with minimal CPU usage, focusing on high-frequency grid operations.

## Content

### Clipboard Events
**4.1.4.29.2 Clipboard Events**

Essential Grid exposes various events to manage the clipboard content while performing cut, paste, and copy operations. Following is the list of clipboard events:

- **ClipboardCanCopy**-This event is to be handled when the CanCopy method of grid is called.
- **ClipboardCanPaste**-This event is to be handled when the CanPaste method of grid is called.
- **ClipboardCanCut**-This event is to be handled when the CanCut method of grid is called.
- **ClipboardCopy**-This event is to be handled when the Copy method of grid is called.
- **ClipboardCut**-This event is to be handled when the Cut method of grid is called.
- **ClipboardPaste**-This event is to be handled when the Paste method of grid is called.
- **ClipboardPasted**-This event is to be handled after a paste operation.

### Performance
**4.1.4.30 Performance**

Essential Grid control has an extremely high performance standard. It can handle high frequency updates and work with large amounts of data without its performance being affected.

#### High Frequency Real Time Updates
**4.1.4.30.1 High Frequency Real Time Updates**

Essential Grid supports frequent updates that occur in random cells across the grid while keeping CPU usage to a minimum level.

##### Example:
```vb
Me.gridControl1.Model.CutPaste.Paste()
```

#### Example:

## API Reference (if applicable)
No specific API references are detailed in the current content.

## Code Examples (multi-language supported)
```vb
Me.gridControl1.Model.CutPaste.Paste()
```

## Page-level Navigation/TOC (if applicable)

- **Clipboard Events** (4.1.4.29.2)
- **High Frequency Real Time Updates** (4.1.4.30.1)
    - Example

## Cross References

- None explicitly mentioned on the page.

## RAG Annotations
<!-- tags: [essential-grid, clipboard-events, performance, real-time-updates, windows-forms, syncfusion, 11.4.0.26] keywords: [clipboardcanpaste, clipboardcancopy, clipboardpasted, paste, cutpaste, clipboardcanpaste, clipboardcanpaste, clipboardcancopy, clipboardcanpaste, clipboardcanpaste, clipboardcanpaste, clipboardcanpaste, clipboardcanpaste, clipboardcanpaste] -->
```