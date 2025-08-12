```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_072.jpeg
document_name: diagram
page_number: 072
page_id: diagram#page_072
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:11:21Z
fidelity: lossless
-->

## Content

### Overview
- Explains the functionality of the Tool item for managing text nodes and rich text objects in a diagram.
- Describes how mouse events are used to draw bounding rectangles for inserting and editing text and rich text nodes.
- Details the activation and usage of the RichTextTool to interact with rich text objects on a diagram.

### Text Node Editing and Insertion

- **existing text nodes.**
  - This tool manages the insertion of new text nodes into a diagram and the editing of existing ones.
  
- **Interaction Management**
  - Activating this tool causes it to track mouse-down, mouse-move, and mouse-up events, drawing a tracking rectangle.
  - The rectangle drawn is used as the bounds of a new text node, which is inserted into the diagram using an `InsertNodesCmd`.  

- **Editing with Double-Clicks**
  - This tool listens to double-click events. If the user double-clicks a text node, a text editor is opened, allowing the user to edit the text.

---

### RichTextTool

- **Interactive tool for inserting and editing rich text objects.**
  - This tool manages the insertion of new rich text nodes into a diagram and the editing of existing rich text nodes.
  
- **Interaction Management**
  - Activating this tool causes it to track mouse-down, mouse-move, and mouse-up events, drawing a tracking rectangle.
  - The rectangle drawn is used as the bounds of a new rich text node, which is inserted into the diagram using an `InsertNodesCmd` command.

- **Editing Capabilities**
  - This tool also listens to double-click events to enable editing of rich text objects in a similar manner to the standard text node tool.

### Sample Code
```csharp
diagram1.Controller.ActivateTool("RichTextTool");
```

---

## Code Examples
The following example demonstrates how to activate the RichTextTool to insert and edit rich text objects in a diagram.

## Cross References
- See also: [Document-Level Commands] for additional details on the `InsertNodesCmd`.

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Diagram.Controls
- **Class**: DiagramController

### Methods
- **ActivateTool(String toolName)**
  - Activates a specific tool by name.
  - **Parameters**
    - `toolName`: String value representing the name of the tool to activate (e.g., "RichTextTool").
  - **Returns**
    - `void`
  - **Description**
    - This method is used to activate a specific tool within the diagram, allowing the user to perform specific actions such as inserting or editing rich text objects.

---

<!-- tags: [Syncfusion, Windows Forms, Diagram, TextNode, RichTextTool] keywords: [diagram, text node, rich text, insertion, editing, mouse events, tracking rectangle, activation, double-click events, tool, controller] -->
```