```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_310.jpeg
document_name: tools
page_number: 310
page_id: tools#page_310
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:06:12Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### 3.5.1.1.3.6 Support to Set Maximum Limit for Suggestion List

The AutoComplete control displays a filtered suggestion list from a mapped data source in a drop-down as the user types text into the text box. This feature provides support to set the maximum number for the filtered suggestion.

#### Use Case Scenarios

When you want to narrow down the filtering and get more accurate data, you can use this feature.

#### Properties

**Table 12: Property Table**

| Property               | Description                                      | Type | Data Type | Reference links |
|------------------------|--------------------------------------------------|------|-----------|-----------------|
| MaxNumberofSuggestion | Set the maximum limit for the suggestion list. | NA   | Integer.  | NA              |

#### Sample Link

To view a sample:

1. Open Syncfusion Dashboard.
2. Click Windows Forms.
3. Click Run Samples.
4. Navigate to Tools Samples > Editors Package > AutoCompleteDemo.

#### Maximum Number of Suggestion

You can set the maximum number of suggestions to be displayed in the AutoComplete using the `MaxNumberofSuggestion` property. The following code illustrates this:

```csharp
this.autoCompletel.MaxNumberofSuggestion = 5;
```

```vb
Me.autoCompletel.MaxNumberofSuggestion = 5
```

<!-- tags: [autosuggest, windowsforms, syncfusion, tools, maximumlimit, csharp, vb] -->
```