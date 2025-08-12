```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_072.jpeg
document_name: calculate
page_number: 072
page_id: calculate#page_072
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:51Z
fidelity: lossless
-->

## Essential Calculate

### C# Code Example

```csharp
' 2) Populate your controls.
Me.textBoxA.Text = "12"
Me.textBoxB.Text = "3"
Me.textBoxC.Text = "= [A] + 2 * [B]"

' Must enter formula names before turning on calculations.
' 3) Assign formula object names.
calculator("A") = Me.textBoxA.Text
calculator("B") = Me.textBoxB.Text
calculator("C") = Me.textBoxC.Text
calculator("D") = Me.textBoxD.Text

' 4) Turn on auto calculations.
Me.calculator.AutoCalc = True

' 5) Subscribe to the event to set newly calculated values.
AddHandler Me.calculator.ValueSet, AddressOf calculator_ValueSet

' 6) Subscribe to some events to trigger the setting of values into CalcQuickBase.
AddHandler Me.textBoxA.Leave, AddressOf textBoxA_Leave
AddHandler Me.textBoxB.Leave, AddressOf textBoxB_Leave
AddHandler Me.textBoxC.Leave, AddressOf textBoxC_Leave
AddHandler Me.textBoxD.Leave, AddressOf textBoxD_Leave

' 7) Allow the CalcQuickBase sheet to create dependency lists necessary for auto calculations.
Me.calculator.RefreshAllCalculations()

' Form_Load
End Sub

' 8) Raised when a variable value is calculated.
Private Sub calculator_ValueSet(ByVal sender As Object, ByVal e As QuickValueSetEventArgs)
    Select Case e.Key
        Case "A"
            Me.textBoxA.Text = Me.calculator(e.Key).ToString()
        Case "B"
            Me.textBoxB.Text = Me.calculator(e.Key).ToString()
        Case "C"
            Me.textBoxC.Text = Me.calculator(e.Key).ToString()
        Case "D"
            Me.textBoxD.Text = Me.calculator(e.Key).ToString()
        Case Else
    End Select

    ' Calculator_ValueSet
End Sub
```

### Overview

- Populates controls with initial values and expressions.
- Assigns formula objects to respective text boxes.
- Enables automatic calculation and subscribes to appropriate events.
- Refreshes all calculations for dependency tracking.
- Updates text boxes with calculated values when changes occur.

### Code Explanation

The provided example demonstrates the setup and usage of the `CalcQuickBase` control in a Windows Forms application. Key steps include:

1. **Populating Controls**: Setting initial values and expressions for text boxes.
   ```csharp
   Me.textBoxA.Text = "12"
   Me.textBoxB.Text = "3"
   Me.textBoxC.Text = "= [A] + 2 * [B]"
   ```

2. **Assigning Formula Objects**: Linking text box values to formula variables.
   ```csharp
   calculator("A") = Me.textBoxA.Text
   calculator("B") = Me.textBoxB.Text
   calculator("C") = Me.textBoxC.Text
   calculator("D") = Me.textBoxD.Text
   ```

3. **Enabling Auto Calculations**: Activating automatic calculation mode.
   ```csharp
   Me.calculator.AutoCalc = True
   ```

4. **Subscribing to Events**: Handling new calculations and updating text boxes.
   ```csharp
   AddHandler Me.calculator.ValueSet, AddressOf calculator_ValueSet
   ```

5. **Dependency Tracking**: Refreshing all calculations for accurate dependency management.
   ```csharp
   Me.calculator.RefreshAllCalculations()
   ```

6. **Updating Controls**: Updating text boxes with calculated values when changes occur.
   ```csharp
   Private Sub calculator_ValueSet(ByVal sender As Object, ByVal e As QuickValueSetEventArgs)
       Select Case e.Key
           Case "A"
               Me.textBoxA.Text = Me.calculator(e.Key).ToString()
           Case "B"
               Me.textBoxB.Text = Me.calculator(e.Key).ToString()
           Case "C"
               Me.textBoxC.Text = Me.calculator(e.Key).ToString()
           Case "D"
               Me.textBoxD.Text = Me.calculator(e.Key).ToString()
           Case Else
       End Select
   ```

### API Reference

#### Properties

- **AutoCalc**: Enables or disables automatic calculation mode.
  - Type: Boolean
  - Description: Determines whether calculations are performed automatically on value changes.

#### Methods

- **RefreshAllCalculations()**: Triggers a refresh of all calculation dependencies.
  - Description: Ensures that all calculations are updated based on the latest values and formulas.

- **ValueSet**: Event raised when a variable value is calculated.
  - Parameters: `sender` - Object that raised the event, `e` - `QuickValueSetEventArgs` containing the variable key.
  - Description: Handler to update controls with the calculated value.

---

<!-- tags: [syncfusion, winforms, calculation, calcquickbase] keywords: [calculator, auto calculation, text box, formula, value set, refresh, dependency tracking] -->
```