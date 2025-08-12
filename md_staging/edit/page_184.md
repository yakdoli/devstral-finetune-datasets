```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_184.jpeg
document_name: edit
page_number: 184
page_id: edit#page_184
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:04:34Z
fidelity: lossless
--}

## Essential Edit for Windows Forms

### Setting Desired Cursor to the Edit Control

```csharp
// Set any desired cursor to the Edit Control.
this.editControl1.Cursor = System.Windows.Forms.Cursors.Hand;
```

```vb.net
' Set any desired cursor to the Edit Control.
Me.editControl1.Cursor = System.Windows.Forms.Cursors.Hand
```

### Showing / Hiding Cursor Caret

The ShowCaret and HideCaret methods are used to either show / hide the cursor caret.

```csharp
// Shows the cursor caret.
this.editControl1.ShowCaret();

// Hides the cursor caret.
this.editControl1.HideCaret();
```

```vb.net
' Shows the cursor caret.
Me.editControl1.ShowCaret()

' Hides the cursor caret.
Me.editControl1.HideCaret()
```

A sample demonstrating the Custom Cursor feature is available in the below sample installation path.

```
..\My Documents\Syncfusion\EssentialStudio\VersionNumber\Windows\Edit.Windows\Samples\2.0\Advanced Editor Functions\CustomCursorDemo
```

#### 4.6.6.2.4 IntelliMouse Scrolling

## API Reference

### ShowCaret Method

- **Namespace:** System.Windows.Forms
- **Class:** EditControl
- **Description:** Shows the cursor caret in the edit control.
- **Usage:**
  ```csharp
  editControl.ShowCaret();
  ```

### HideCaret Method

- **Namespace:** System.Windows.Forms
- **Class:** EditControl
- **Description:** Hides the cursor caret in the edit control.
- **Usage:**
  ```csharp
  editControl.HideCaret();
  ```

### Cursor Property

- **Namespace:** System.Windows.Forms
- **Class:** EditControl
- **Type:** System.Windows.Forms.Cursors
- **Description:** Sets the cursor that is displayed when the mouse pointer is over the edit control.
- **Usage:**
  ```csharp
  editControl.Cursor = System.Windows.Forms.Cursors.Hand;
  ```

### IntelliMouse Scrolling

- **Overview:** Describes how to enable IntelliMouse scrolling functionality in the edit control.
- **Steps:**
  1. Configure the edit control to support IntelliMouse scrolling.
  2. Handle mouse wheel events to implement scrolling behavior.

<!-- tags: [Syncfusion, WinForms, EditControl, Design, IntelliMouse, Cursors] keywords: [ShowCaret, HideCaret, Custom Cursor, IntelliMouse Scrolling, Windows Forms, Edit, Cursor, Mouse, Scrolling, Properties, Methods] -->
```