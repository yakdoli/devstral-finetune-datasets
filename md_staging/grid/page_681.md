```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_681.jpeg
document_name: grid
page_number: 681
page_id: grid#page_681
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:32:10Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Binding an Array of Custom Objects to the Grouping Grid

The following figure demonstrates how to bind an array of custom objects to the Grouping Grid:

<div align="center">
  <img src="binding_custom_objects.png" alt="Figure 272: Binding an Array of Custom Objects to the Grouping Grid" />
</div>

**Figure 272: Binding an Array of Custom Objects to the Grouping Grid**

**Note:** For more details, refer to the following browser sample:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Custom Collections\Array List Demo
```

### 4.3.4.2.3.2 IBindingList

#### Overview

This section demonstrates the implementation of IBindingList and how to bind this list to a Grid Grouping control. As IBindingList derives from IList, its implementation requires the implementation of all of the members of the IList, ICollection, and IEnumerable interfaces.

#### Benefits

The benefits of using IBindingList include the support for change notifications when the list is modified. It includes a `ListChanged` event, which will be fired upon any data changes. If the collection supports changes, it should also support firing a `ListChanged` event when the collection changes. To indicate that the collection should return `true` from the `SupportsChangeNotification` property. Hence, when items are added or removed from the collection, the grouping grid will be notified of these changes and will update itself automatically.

#### Implementation Procedure

Follow these steps to create your own collection that implements IBindingList and to bind this collection to a grouping grid.

<table>
  <thead>
    <tr>
      <th>CategoryID</th>
      <th>CategoryName</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Condiments</td>
      <td>Charlotte Cooper</td>
      <td>Bigfoot Breweries</td>
    </tr>
    <tr>
      <td>Confections</td>
      <td>Regina Murphy</td>
      <td>Grandma Kelly's Homestead</td>
    </tr>
    <tr>
      <td>Grains/Cereals</td>
      <td>Jean-Guy Lauzon</td>
      <td>Ma Maison</td>
    </tr>
    <tr>
      <td>Meat/Poultry</td>
      <td>Shelley Burke</td>
      <td>New Orleans Cajun Delights</td>
    </tr>
    <tr>
      <td>Produce</td>
      <td>Mayumi Ohno</td>
      <td>Mayumi's</td>
    </tr>
    <tr>
      <td>Seafood</td>
      <td>Robb Merchant</td>
      <td>New England Seafood Cannery</td>
    </tr>
  </tbody>
</table>

### Copyright Information

© 2013 Syncfusion. All rights reserved.

<!-- tags: [syncfusion, windows forms, grid, ibindinglist, grouping grid, demo, essential grid, windows forms] keywords: [ibindinglist, grouping grid, custom collections, samples, arraylist, change notification, list changed event, supports change notification, implementation procedure] -->
```