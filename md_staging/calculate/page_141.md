```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_141.jpeg
document_name: calculate
page_number: 141
page_id: calculate#page_141
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:36Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- The document describes the process of testing a string to see if it begins with an equal sign and how the `CalcSheet` and `CalcEngine` handle different scenarios for storing and recomputing cell values.
- It explains the usage of `DependentCells` and `FormulaInfoTable` collections in handling dependencies and recalculations in a spreadsheet application.
- It outlines how to manage error messages in the `CalcEngine`.

## Content

### Calculation Logic

1. **String Test**
   - The string is tested to see whether it begins with an equal sign.
   - If not, `CalcSheet` stores the entered string in its internal memory for later use.
   - A check is made to see if this cell is a key in the `DependentCells` collection.
   - If the cell is a key, all cells depending upon this cell are recomputed recursively.

2. **Formula Entry**
   - If the entered string does begin with an equal sign, the `CalcEngine` treats it as an entered formula.
   - The `CalcEngine` checks to see if the cell is a key in the `FormulaInfoTable`.

3. **Updating FormulaInfo**
   - If the cell is a key in the `FormulaInfoTable`, the corresponding `FormulaInfo` object is retrieved and updated.
   - This process includes:
     - Parsing the string.
     - Computing the string.
     - Saving the original formula, the parsed formula, and the computed value in the `FormulaInfo` object.

4. **New FormulaInfo Creation**
   - If the cell is not a key in the `FormulaInfoTable`, a new `FormulaInfo` object is created.
   - The new `FormulaInfo` object is populated from the entered string.
   - This process includes:
     - Parsing the string.
     - Computing the string.
     - Saving the original formula, the parsed formula, and the computed value in the `FormulaInfo` object.

5. **Dependency Management**
   - The `CalcEngine` handles scenarios where the newly entered string changes from an existing formula cell to a non-formula cell.
   - In this situation, the `CalcEngine` uses the `DependFormulaCells` collection to remove dependencies that are no longer needed.

6. **Conditional Dependent Tracking**
   - All dependent tracking is done conditionally depending upon the `CalcEngine.UseDependencies` property.
   - Formula calculations can be turned off using `CalcEngine.CalculatingSuspended`.

### Error Messages

#### Handling Error Messages in CalcEngine
- The error messages displayed by Essential Calculate are found in a string array within the `CalcEngine`.
- After creating a `CalcEngine` object, the text of these messages can be changed by modifying the array values.

#### Code Example

```csharp
[C#]
```

## Page-level Navigation/TOC (if applicable)
- This section provides a brief overview of the content on page 141 of the Essential Calculate user guide.
- It includes steps for handling strings, formulas, and dependencies in the `CalcEngine`.

---

```html
<!-- tags: [product, syncfusion, winforms, calculation, essential calculate, formulainfo, dependentcells] keywords: [calcengine, calculating suspended, error messages, formula calculation, cell dependent tracking] -->
``` 
```