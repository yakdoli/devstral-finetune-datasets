```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_733.jpeg
document_name: tools
page_number: 733
page_id: tools#page_733
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:30:13Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
if (this.NegativeSign == "-" && this.Text.StartsWith("-"))
{
    this.Clear();
}
return base.HandleSubtractKey();
}
```

## Overview
- This source code provides an example of handling a negative sign change in a custom DoubleTextBoxAdv control.
- It demonstrates overriding the behavior of the SubtractKey functionality so that the text is cleared when the NegativeSign is changed.

## Content

### Managing Negative Sign Changes in Custom DoubleTextBoxAdv

The provided code snippet in C# handles the behavior of the SubtractKey when the NegativeSign property is set to a specific value and the text starts with a negative sign. Here's a breakdown:

#### C# Implementation
```csharp
if (this.NegativeSign == "-" && this.Text.StartsWith("-"))
{
    this.Clear();
}
return base.HandleSubtractKey();
}
```

- **Check Conditions**: It checks if the `NegativeSign` is set to `"-"` and the `Text` starts with `"-"`.
- **Clear Action**: If both conditions are met, it clears the text using the `this.Clear()` method.
- **Base Implementation**: Finally, it delegates to the base `HandleSubtractKey()` method to allow further handling.

### VB.NET Implementation

Below is the equivalent implementation in VB.NET:

```vb
Public Class DoubleTextBoxAdv
    Inherits Syncfusion.Windows.Forms.Tools.DoubleTextBox

    Public Sub New()
        MyBase.New()
    End Sub

    Private m_deleteonnegative As Boolean = False

    Public Property DeleteOnNegative() As Boolean
        Get
            Return m_deleteonnegative
        End Get

        Set(ByVal value As Boolean)
            m_deleteonnegative = value
        End Set
    End Property

    ' Overrides the behavior of Subtract Key so that the text is cleared when the NegativeSign is changed.
    Protected Overrides Overrides Function HandleSubtractKey() As Syncfusion.Windows.Forms.Tools.NumberModifyState

        If m_deleteonnegative = True Then
            If Me.NegativeSign = "-" AndAlso Me.Text.StartsWith("-") Then
                Me.Clear()
            End If
        End If

        Return MyBase.HandleSubtractKey()
    End Function
End Class
```

- **Class Definition**: The `DoubleTextBoxAdv` class is derived from the `Syncfusion.Windows.Forms.Tools.DoubleTextBox` class.
- **Property**: The `DeleteOnNegative` Boolean property determines whether the text should be cleared when the negative sign changes.
- **Overriding HandleSubtractKey**: The `HandleSubtractKey` function is overridden to clear the text when the `DeleteOnNegative` property is `True` and the `NegativeSign` is `"-"` while the text starts with `"-"`.

## API Reference

### Properties
- **DeleteOnNegative**: A property of type `Boolean` that controls whether the text should be cleared when the negative sign changes.

### Methods
- **HandleSubtractKey**: An overridden method that handles the behavior of the SubtractKey in the control.

## Code Examples

### C# Example
The C# example demonstrates a concise approach to handling the SubtractKey event with a negative sign check.

```csharp
if (this.NegativeSign == "-" && this.Text.StartsWith("-"))
{
    this.Clear();
}
return base.HandleSubtractKey();
}
```

### VB.NET Example
The VB.NET example provides a more comprehensive approach, including properties and overriding functionalities:

```vb
Public Class DoubleTextBoxAdv
    Inherits Syncfusion.Windows.Forms.Tools.DoubleTextBox

    Public Sub New()
        MyBase.New()
    End Sub

    Private m_deleteonnegative As Boolean = False

    Public Property DeleteOnNegative() As Boolean
        Get
            Return m_deleteonnegative
        End Get

        Set(ByVal value As Boolean)
            m_deleteonnegative = value
        End Set
    End Property

    ' Overrides the behavior of Subtract Key so that the text is cleared when the NegativeSign is changed.
    Protected Overrides Overrides Function HandleSubtractKey() As Syncfusion.Windows.Forms.Tools.NumberModifyState

        If m_deleteonnegative = True Then
            If Me.NegativeSign = "-" AndAlso Me.Text.StartsWith("-") Then
                Me.Clear()
            End If
        End If

        Return MyBase.HandleSubtractKey()
    End Function
End Class
```

### Explanation
- **Inheritance**: The `DoubleTextBoxAdv` class inherits from `Syncfusion.Windows.Forms.Tools.DoubleTextBox`.
- **Property Handling**: The `DeleteOnNegative` property is used to toggle the behavior of clearing the text based on the negative sign change.
- **Override Logic**: The `HandleSubtractKey` function ensures that the text is cleared if the `DeleteOnNegative` property is `True` and the text starts with a negative sign.

## RAG Annotations

<!-- tags: [essential-tools, windows-forms, syncfusion-controls, double-textbox-adv, negative-sign, subtract-key, customize-text-box, vb-net, csharp, number-modify-state] keywords: [negativeSign, HandleSubtractKey, Clear, DeleteOnNegative, Text, m_deleteonnegative, NumberModifyState] -->
```