```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_073.jpeg
document_name: calculate
page_number: 073
page_id: calculate#page_073
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:02Z
fidelity: lossless
-->

# Essential Calculate

```vb
' 9) Handles the changing of the text in the text box so the CalcQuickBase
' object can be updated as the text changes.
Private Sub textBoxA_Leave(ByVal sender As Object, ByVal e As EventArgs)
    If Me.textBoxA.Modified Then
        calculator("A") = Me.textBoxA.Text
        Me.textBoxA.Modified = False
    End If
End Sub
```

The following is an explanation of the numbered steps given in the preceding Form_Load.

1. **Instantiates the CalcQuickBase instance.**
2. **Sets some initial text into the first three text boxes. The first two values are just numerical entries but, the third value will be treated as a formula by the CalcQuickBase object as it begins with a "="**.
3. **This step registers the variable names A, B, C and D with the CalcQuickBase object, and sets the initial values of these variables to the contents of the text boxes.**
4. **Here the AutoCalc property is turned on so CalcQuickBase will start tracking any dependencies that it notes among the variables registered with it. Note that this step was done after the initial registering of the variables in step 3. So, any relations among the registered variables are unknown to the CalcQuickBase object. This shortcoming will be addressed in step 7 and the rationale for this order will be discussed there.**
5. **Subscribe to CalcQuickBase's ValueSet event so that the code can react to any automatic changing of the registered variables’ values and place them into the appropriate text box so your display will immediately reflect any change.**
6. **Subscribe to the text box events so that you can update the CalcQuickBase object when the text in a text box has changed.**
7. **This step forces the recalculation of all variables registered with the CalcQuickBase object. This has to be done after the AutoCalc property has been set to True, so that the dependencies between variables can be monitored. The reason to postpone setting AutoCalc until after the initial registration of the variables, is to avoid problems that might occur because of CalcQuickBase trying to set up dependency chains even before all the variables have been registered. Initializing the variables, turning on AutoCalc, and then calling RefreshAllCalculations, avoids this potential problem.**
8. **This is the event handler that moves a freshly computed variable into the text box that it is related to.**

<!-- tags: [syncfusion sdk, syncfusion winforms, calcquickbase, dependecy tracking, variable registration, auto calculation, event handling] keywords: [bla text text box, text_tBoxA Modified, CalcQuickBase object, AutoCalc property, ValueSet event, dependency tracking, RefreshAllCalculations] -->
```