```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_807.jpeg
document_name: grid
page_number: 807
page_id: grid#page_807
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:41:39Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
{
    USStatesCollection states = new USStatesCollection();
    states.Add(new USState("AL", "Alabama"));
    states.Add(new USState("AK", "Alaska"));
    states.Add(new USState("CA", "California"));
    states.Add(new USState("FL", "Florida"));
    states.Add(new USState("GA", "Georgia"));
    states.Add(new USState("IN", "Indiana"));
    states.Add(new USState("MS", "Mississippi"));
    states.Add(new USState("NJ", "New Jersey"));
    states.Add(new USState("NM", "New Mexico"));
    states.Add(new USState("NY", "New York"));
    states.Add(new USState("TX", "Texas"));
    states.Add(new USState("WA", "Washington"));
    states.Add(new USState("PE", "Prince Edward Island"));
    states.Add(new USState("YT", "Yukon Territories"));
    return states;
}

public override bool IsReadOnly
{
    get
    {
        return true;
    }
}

public override bool IsFixedSize
{
    get
    {
        return true;
    }
}

// US State Class.
[Serializable]
public class USState
{
    private string _code;
    private string _name;

    public USState()
    {
```

## API Reference

### USStatesCollection

- **Add**: Adds a new USState to the collection.
  - **Parameters**:
    - `USState`: The USState object to add.
  - **Returns**: None.
  - **Description**: Adds a new USState to the collection.

### USState

- **Properties**:
  - `_code`: A private string representing the state code.
  - `_name`: A private string representing the state name.

## Code Examples

### Creating a US State Collection

```csharp
USStatesCollection states = new USStatesCollection();
states.Add(new USState("AL", "Alabama"));
states.Add(new USState("AK", "Alaska"));
// Add more states as needed
```

### Accessing State Details

```csharp
foreach (var state in states)
{
    Console.WriteLine($"State Code: {state._code}, State Name: {state._name}");
}
```

## Page-level Navigation/TOC

- [ ] USStatesCollection Methods and Properties
- [ ] USState Class Details
- [ ] Creating and Managing a State Collection

## RAG Annotations

<!-- tags: [Syncfusion, Windows Forms, Grid, USStatesCollection, USState] keywords: [state collection, US state, code, name, add, readonly, fixed size] -->
```