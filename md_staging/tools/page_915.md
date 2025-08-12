```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_915.jpeg
document_name: tools
page_number: 915
page_id: tools#page_915
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:43:13Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes properties and behaviors related to field validation in Windows Forms.
- Focuses on specifying actions when fields are null or validation fails.
- Highlights behavioral changes with MinMaxValidation and property constraints.

## Content

### Property Description
| Property         | Description                                  | field is null.                         |
|------------------|----------------------------------------------|----------------------------------------|
| **NullString**   | Specifies the string that will be set when the field is Null. | AllowNull must be true to set this string. If it is false, zero or MinValue, whichever is higher of these will be set. <br> It must be left blank if the field has to be empty. |
| **OnValidationFailed** | Specifies the action to be performed while validation fails. | SetNullString, <br> SeMinOrMax, <br> KeepFocus. <br> refer Notes column |

#### 3.5.8.11.3 Behavioral Changes

| Property                      | Description                                                                                          | Behavior                                                                      |
|-------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **MinMaxValidation.OnKeyPress** | Each and every key press is validated to make the value meet the constraints.                        | This is most useful when the MinValue is less than 10. <br> Refer Notes column |
| **MinMaxValidation.OnLostFocus** | Validation happens only when the control loses its focus.                                      | This allows the user to enter any value and it is validated when the focus is lost. <br> You can make use of OnValidationFailed property to gain control when validation fails. <br> Refer Notes column |
| **MinValue**                  | Cannot be greater than MaxValue.                                                                     | Exception will be thrown. <br> MaxValue has to be reset the accordingly.       |
| **MaxValue**                  | Cannot be lesser than MaxValue.                                                                      | Exception will be thrown.                                                     |

## API Reference
- **Properties**
  - AllowNull
  - MinValue
  - MaxValue
  - OnValidationFailed

## Code Examples

```csharp
// Sample code for validation in Windows Forms
public class CustomValidation
{
    public string NullString { get; set; }
    public bool AllowNull { get; set; }

    public void OnValidationFailedAction()
    {
        // Perform action when validation fails
        if (AllowNull)
        {
            SetNullString();
        }
        else
        {
            SetMinOrMax();
        }
    }

    private void SetNullString()
    {
        // Set the appropriate null string here
    }

    private void SetMinOrMax()
    {
        // Set MinValue or MaxValue as appropriate
    }

    public void ValidateField()
    {
        // Implementation for validation logic
    }
}
```

## Cross References
- Refer to the Notes column for additional details on specific behaviors.
- See also: validation logic, property constraints, and field handling in Windows Forms.

<!-- tags: [syncfusion-sdk, windows-forms, validation, property-validation, MinMaxValidation, tools#page_915] keywords: [NullString, OnValidationFailed, MinValue, MaxValue, MinMaxValidation] -->
```