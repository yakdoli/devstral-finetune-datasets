<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_068.jpeg
document_name: calculate
page_number: 068
page_id: calculate#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:33Z
fidelity: lossless
-->

## Essential Calculate

The collection that `CalcQuickBase` maintains in order to hold information on variables, is a collection of `FormulaInfo` objects. The `FormulaInfo` class has the following public properties.

- **FormulaText:** String holding the formula as originally entered
- **ParsedFormula:** String holding the parsed version of the formula
- **FormulaValue:** String holding the last computed value for the formula

Indexing is an instance of the `CalcQuickBase` class, which sets the `FormulaText` property and gets the `FormulaValue` property for the `FormulaInfo` object that is associated with the variable name and used as the indexer. A `FormulaInfo` object is dynamically created if you use a variable name that is not in the `CalcQuickBase FormulaInfo` collection. To retrieve `FormulaText`, you must use the `CalcQuickBase.GetFormula` method and pass it in the variable name.

While using an indexer to get a value from a `CalcQuickBase` object, the `FormulaValue` property is returned. So, the question arises: as to exactly "when" this `FormulaValue` is computed from the `FormulaText` that has been set into this `FormulaInfo` object. When a new value for `FormulaValue` is computed, it is controlled by an internal member of `FormulaInfo`, the `calcID`. The `CalcQuickBase` object maintains a `calcID` value as well. Whenever the `FormulaInfo.FormulaValue` is requested, the `CalcQuickBase.calcID` is compared to the `FormulaInfo.calcID`, and if they do not match, the `FormulaInfo.FormulaValue` is recomputed and its `FormulaInfo.calcID` is set to match the `CalcQuickBase.calcID`. So, `FormulaValue` is only computed when the `calcID` value does not match the `CalcQuickBase.calcID` value. Also, you can force new computations by calling the `SetDirty` method on your `CalcQuickBase` instance.

The actual collection of `FormulaInfo` objects (and some related collections) are protected members of the `CalcQuickBase` class. In order to access the objects of these collections directly, you must derive the `CalcQuickBase` class of Essential Calculate. The `Calculate` class reference has more information on these protected collections.

You can access the underlying `Calculate.Engine` object through the public read-only `Engine` property of the `CalcQuickBase` class. You can then use this `Engine` property to add custom functions to the Function Library that is available for the `CalcQuickBase` object.

## 4.1.1.2 Automatic Calculations

Essential Calculate enables you to monitor value changes, and then automatically recomputes formulas that depend upon the changed values. There is an additional overhead associated with automatic calculations that enables you to determine "when" you want to use this feature.

### 4.1.1.2.1 Using Explicit Events

## Page-level Navigation/TOC (if applicable)
- [Unclear]

<!-- tags: [CalcQuickBase, FormulaInfo, VariableIndexing, AutomaticCalculations, ExplicitEvents] keywords: [Essential Calculate, FormulaValue, calcID, SetDirty, Calculate.Engine, CustomFunctions, ProtectedCollections, FunctionLibrary] -->