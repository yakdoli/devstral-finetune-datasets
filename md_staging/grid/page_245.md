```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_245.jpeg
document_name: grid
page_number: 245
page_id: grid#page_245
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:05:18Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

The supported operands include those listed in the following table. An operand by itself is also a well-formed algebraic expression that can serve as an entire formula in a cell.

| Operand                        | Example                         |
|--------------------------------|---------------------------------|
| number                         | 532.1, -10.2, or 18.          |
| cell reference                  | A12, BB1010, or Q18.          |
| library formula with valid arguments | Abs(E14), Cos(-3.14), or Sum(A1:A14). |
| any well formed algebraic expression | E1+E2, Cos(2)<A4, or Abs(A1-A5).   |

Within a formula cell, a case is ignored. So, a1 is the same as A1, and Cos(3) is the same as COS(3).

## 4.1.4.6.4 Inside Essential Grid's Formula Support

The Formula Cell control is implemented with four classes: GridFormulaCellModel, GridFormulaCellRenderer, GridFormulaEngine, and GridFormulaTag. The GridFormulaCellRenderer class handles a couple of activation issues which are specific to displaying formulas when a formula cell gets activated. The GridFormulaCellModel class does some significant work in its GetFormattedText method override where calculations and formula parsing are initiated dynamically as required.

The GridFormulaEngine class does the actual parsing and calculation that is required to evaluate a formula in a cell. This class also maintains the Formula Library. The programmer can gain access to an engine object by using the GridFormulaCellModel.Engine property. It is this property that will let you add functions to (or remove functions from) the Formula Library. The use of the class is discussed in the next section.

Finally, the GridFormulaTag class is used in conjunction with the GridStyleInfo class that has a property of this type. The GridFormulaTag tracks the computed value of the cell in its Text property.

## 4.1.4.6.5 Adding Formulas to the Formula Library

Here are the steps that are required to add a function to the Function Library.
```