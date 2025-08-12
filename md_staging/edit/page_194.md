```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_194.jpeg
document_name: edit
page_number: 194
page_id: edit#page_194
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:01Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Content

### Getting Details of Currently Loaded Stream

The name of the stream that is currently loaded in the Edit Control can be set by using the `FileOpened` property.

| Edit Control Property   | Description                                       |
|-------------------------|---------------------------------------------------|
| FileOpened             | Gets / sets the filestream that is used as an input. |

#### Code Examples

[C#]
```csharp
// Gets or sets the name of the stream that is currently loaded in the Edit Control.
this.editControl1.FileOpened = new FileStream("Temp.txt", FileMode.Create);
```

[VB.NET]
```vb.net
' Gets or sets the name of the stream that is currently loaded in the Edit Control.
Me.editControl1.FileOpened = New FileStream("Temp.txt", FileMode.Create)
```

#### See Also

- Creating, Loading and Saving a File
- Saving and Cancelling Changes

### 4.8.3 Saving And Cancelling Changes

This section demonstrates how changes made to the contents of the Edit Control can be saved or discarded.

#### SaveOnClose Property

This property specifies whether the default Save Changes prompt should be displayed on closing the Edit Control.

#### Code Example

[C#]
```csharp
// No specific code example provided.
```

---

## Cross References
- Creating, Loading and Saving a File
- Saving and Cancelling Changes

<!-- tags: [Syncfusion Winforms, Windows Forms, File Handling, Stream Operations, Save Features] keywords: [Edit Control, FileOpened, FileMode, Create, FileStream, SaveOnClose, Save Changes, C#, VB.NET, Windows Forms, Syncfusion, API Reference, Code Examples] -->
```