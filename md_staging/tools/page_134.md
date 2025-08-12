```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_134.jpeg
document_name: tools
page_number: 134
page_id: tools#page_134
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:44:20Z
fidelity: lossless
--> 

## Essential Tools for Windows Forms

**Note:** In the Tabbed style, the control is docked as a tabbed window along with the dock target. This style is not applicable when the dock target is the host form / user control.

### Context Menu for Tabbed Controls

The tabbed control can display a context menu when the user right-clicks on the tabs. See [Context Menu](#).

### Aligning the Tabs

The alignment of the tabs can be specified using the DockTabAlignment property.

#### DockingManager Property Details

| DockingManager Property | Description |
|--------------------------|---------------------------------------------------------------------------------------|
| DockTabAlignment         | Property which sets the value indicating the alignment of the dock tabs. The different alignment options are,<br><br>Top,<br>Bottom,<br>Left and<br>Right. |

**Note:** This property can also be set easily using **Task Window**.

#### Code Examples

**[C#]**

```csharp
this.dockingManager.DockTabAlignment =
Syncfusion.Windows.Forms.Tools.DockTabAlignmentStyle.Right;
```

**[VB.NET]**

```vb
Me.dockingManager.DockTabAlignment =
Syncfusion.Windows.Forms.Tools.DockTabAlignmentStyle.Right
```
```