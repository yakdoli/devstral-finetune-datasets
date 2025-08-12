```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_654.jpeg
document_name: tools
page_number: 654
page_id: tools#page_654
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:26:41Z
fidelity: lossless
-->

## Overview

- Primitives can be added to `GradientPanelExt`'s border using the `GradientPanelExt PrimitiveCollection Editor`.
- The primitive alignment and position can be defined in the editor.
- The application can be built and run after setting up primitives.

## Content

### Working with GradientPanelExt Primitives

4. **Adding Primitives to GradientPanelExt Border**  
   Primitives can be added to `GradientPanelExt`'s border using the `GradientPanelExt PrimitiveCollection Editor`, which can be accessed using the `Primitives` property.

   ![GradientPanelExt PrimitiveCollection Editor](attachment:GradientPanelExt_PrimitiveCollection_Editor.png)

   **Figure 403: GradientPanelExt Primitive Collection Editor**

   The primitive alignment and position can be defined here.

   **Note:** The properties for the primitives can be set individually using the property grid as well.

5. **Setting Primitive Alignment and Position**  
   The primitive alignment and position can be defined here.

6. **Building and Running the Application**  
   Build and run the application.

## API Reference

- **`Primitives` Property**  
  - **Type:** `PrimitiveCollection`  
  - **Description:** Accesses the collection of primitives for the `GradientPanelExt` control.  
  - **Usage:**  
    ```csharp
    gradientPanelExt1.Primitives.Add(new GradientPanelExtPrimitive());
    ```

## Code Examples

### Example: Adding a Primitive to GradientPanelExt

```csharp
using Syncfusion.Windows.Forms.Tools;

// Initialize GradientPanelExt
GradientPanelExt gradientPanelExt1 = new GradientPanelExt();

// Access PrimitiveCollection
PrimitiveCollection primitives = gradientPanelExt1.Primitives;

// Add a new primitive
GradientPanelExtPrimitive primitive1 = new GradientPanelExtPrimitive();
primitive1.Name = "collapsePrimitive1";
primitive1.Position = 1;
primitive1.Size = new Size(20, 20);

// Add the primitive to the collection
primitives.Add(primitive1);

// Set other properties
gradientPanelExt1.BackColor = Color.White;
gradientPanelExt1.BorderColor = Color.Black;
gradientPanelExt1.CollapseImage = ...; // Optional: Set collapse image
gradientPanelExt1.ExpandImage = ...;   // Optional: Set expand image
```

## Page-level Navigation/TOC (if applicable)
- [Main Content](#content)
- [API Reference](#api-reference)
- [Code Examples](#code-examples)

## Cross References
- Refer to the `GradientPanelExt` documentation for more details on its properties and methods.
- See also: `PrimitiveCollection`, `GradientPanelExtPrimitive`.

<!-- tags: [SyncfusionWinforms, GradientPanelExt, Primitives, PrimitiveCollection] keywords: [GradientPanelExt, Primitives, PrimitiveCollection, Editor, Alignment, Position, Build, Run] -->
```