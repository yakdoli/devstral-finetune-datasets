```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_543.jpeg
document_name: grid
page_number: 543
page_id: grid#page_543
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:23:25Z
fidelity: lossless
-->

## Customizing Columns using GridBoundColumn Collection Editor

### Overview
- Demonstrates how to customize grid columns by using the GridBoundColumn Collection Editor.
- Shows the process of adding and modifying BoundColumns in Windows Forms.
- Displays the output of a grid with predefined columns after customization.

### Procedure

#### Step 1: Customize GridBoundColumns
1. Open the GridBoundColumn Collection Editor.  
2. See the properties being set for gridBoundColumn1 shown in Figure 214:
   - **Name**: gridBoundColumn1
   - **GenerateMember**: True
   - **Modifiers**: Private
   - **HeaderText**: (empty)
   - **ReadOnly**: False

   **Figure 214: Customizing Columns by using the GridBoundColumn Collection Editor**

   ```plaintext
   GridBoundColumn Collection Editor
   ```

#### Step 2: Run the Application
3. Execute the application to see the updated grid.
4. Observe the output, as shown in Figure 215, where the GridBoundColumn setup reflects the editing made through the Designer.

   **Figure 215: GridBoundColumn created Through Designer**

   ```plaintext
   Form1
   +--------+-----------------------+-------------+
   | CustomerID | CompanyName          | ContactName |
   +--------+-----------------------+-------------+
   | ALFKI   | Alfreds Futterkiste   | Maria       |
   | ANATR   | Ana Trujillo Empar    | Ana Trujillo|
   | ANTON   | Antonio Moreno Ta      | Antonio More|
   | AROUT   | Around the Horn        | Thomas Hardy|
   | BERGS   | Berglunds snabbk       | Christina Bergl |
   | BLAUS   | Blauer See Delikat     | Hanna Moos  |
   | BLONP   | Blondessdsl père       | Frédérique Cit |
   | BOLID   | Bólido Comidas pr      | Martín Sommer |
   +--------+-----------------------+-------------+
   ```

### Summary
Grid Data Bound Grid is added to the windows application and bound to a local data source. This tutorial covers the process of designing and customizing grid columns using the GridBoundColumn Collection Editor.

### Cross References
For more details, see the Grid Data Bound Grid tutorial.

## API Reference
This section provides a reference to the GridBoundColumn class and its associated properties, methods, and events.

### Code Examples
Here is the basic structure for adding a GridBoundColumn to a GridControl:

```csharp
gridModel.BoundColumns.Add("CustomerID");
gridModel.BoundColumns.Add("CompanyName");
gridModel.BoundColumns.Add("ContactName");
```

This code snippet demonstrates how to programmatically add BoundColumns to the GridControl.

## RAG Annotations
<!-- tags: [syncfusion, windows-forms, gridcontrol, gridboundcolumn, designer, customization] keywords: [GridBoundColumn, Column Editor, Windows Forms, Data Binding, Customization, Designer] -->
```