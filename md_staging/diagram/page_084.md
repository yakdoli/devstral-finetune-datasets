```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_084.jpeg
document_name: diagram
page_number: 084
page_id: diagram#page_084
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:12:04Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- This page explains the process of saving and modifying symbols in the Symbol Palette.
- It includes instructions for saving palettes and updating symbol properties.

## Content

### Save SymbolPalette Dialog

#### Figure 52: Save SymbolPalette Dialog

![Save SymbolPalette Dialog](https://example.com/save_symbolpalette_dialog.png)

**Description:**
The Save SymbolPalette Dialog allows you to save custom symbols to a specific location and modify their properties.

#### Instructions

1. **Saving the Palette**:
   - **Step 1**: Give a relevant file name for the palette and click **Save**. As the palette is saved, the new symbol is automatically loaded into the symbol palette.

2. **Modifying Custom Symbols**:
   - **Step 1**: You can modify the custom symbols by using the **Properties** window.
   - **Step 2**: Click the **New Symbol1** in the **Symbol Palettes** to view the properties.
   - **Step 3**: Change the name of the symbol by using the **Name** property.

---

## API Reference

### Namespace: Syncfusion.Windows.Forms.Diagram

#### Classes:
- **SymbolPalette**
  - **Properties**
    - `SymbolName`: Gets or sets the name of the symbol.
    - `SymbolImage`: Gets or sets the image associated with the symbol.

#### Methods:
- **SavePalette()**
  - Saves the current symbol palette to a specified location.
  
- **LoadPalette(string filePath)**
  - Loads a symbol palette from the specified file path.

---

## Code Examples

### C#

```csharp
// Saves the symbol palette with the name "NewSymbol"
palette.SavePalette("NewSymbol");

// Modifies the symbol name using the Properties window
propertiesDialog.ShowDialog();
```

### VB.NET

```vb.net
' Saves the symbol palette with the name "NewSymbol"
palette.SavePalette("NewSymbol")

' Modifies the symbol name using the Properties window
propertiesDialog.ShowDialog()
```

---

## Page-level Navigation/TOC

- **Main Title**: Essential Diagram for Windows Forms
- **Section 1**: Save SymbolPalette Dialog
  - Figure 52: Save SymbolPalette Dialog
  - Instructions for saving and modifying symbols

## Cross References

- Refer to the "Working with Symbol Palettes" section for more details on creating and managing custom symbols.

---

<!-- tags: [windows-forms, essential-diagram, symbol-palette, save-palette, modify-symbols, properties-window] keywords: [save, modify, custom symbols, properties, diagram, windows forms] -->
```