```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_803.jpeg
document_name: tools
page_number: 803
page_id: tools#page_803
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:36:50Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Code Example

[C#]

```csharp
using Syncfusion.Windows.Forms.Tools;
```

[VB.NET]

```vb
Imports Syncfusion.Windows.Forms.Tools
```

#### Step 2: Create an instance of the CurrencyTextBox. Add that instance to the Form.

[C#]

```csharp
private Syncfusion.Windows.Forms.Tools.CurrencyTextBox currencyTextBox1;
this.currencyTextBox2 = new Syncfusion.Windows.Forms.Tools.CurrencyTextBox();
this.Controls.Add(this.currencyTextBox1);
```

[VB.NET]

```vb
Private currencyTextBox1 As Syncfusion.Windows.Forms.Tools.CurrencyTextBox
Me.Controls.Add(Me.currencyTextBox1)
```

#### Concepts and Features

3.5.8.6.3 **Concepts and Features**

The following topics will help you become more familiar in using the CurrencyTextBox control.

The following Editors controls (DoubleTextBox, IntegerTextBox, PercentTextBox, and CurrencyTextBox) have been revamped. Click **here** to see the details of revamping.

#### Text Field

3.5.8.6.4 **Text Field**

The text field of a CurrencyTextBox control can be customized using the properties available. The below image illustrates the various sections of the control.

## API Reference

### Code Example

#### C#

```csharp
private Syncfusion.Windows.Forms.Tools.CurrencyTextBox currencyTextBox1;
this.currencyTextBox2 = new Syncfusion.Windows.Forms.Tools.CurrencyTextBox();
this.Controls.Add(this.currencyTextBox1);
```

#### VB.NET

```vb
Private currencyTextBox1 As Syncfusion.Windows.Forms.Tools.CurrencyTextBox
Me.Controls.Add(Me.currencyTextBox1)
```

### Getting Started

1. **Create an Instance**
   
   - Instantiate a CurrencyTextBox object and add it to the form.

---

### Example Usage

[C#]

```csharp
using Syncfusion.Windows.Forms.Tools;
using System;
using System.Windows.Forms;

namespace CurrencyTextBoxExample
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            CurrencyTextBox currencyTextBox = new CurrencyTextBox
            {
                Location = new System.Drawing.Point(50, 50),
                Size = new System.Drawing.Size(200, 30)
            };

            this.Controls.Add(currencyTextBox);
        }
    }
}
```

### Properties and Customization

- **CurrencySymbol**: Set or get the symbol to display next to the currency.
- **DecimalPlaces**: Set the number of decimal places to display.
- **GroupSeparator**: Enable or disable the use of a group separator (e.g., commas for thousands).

### Revision Summary

The CurrencyTextBox control has been revamped to include enhanced features for better usability and customization.

---

**Note:** For detailed information on the revamp features, refer to the linked resources.

---

<!-- tags: [syncfusion, windows forms, currencytextbox, control, user guide] keywords: [currencytextbox, form, code example, concepts, features, text field, revision, properties] -->
```