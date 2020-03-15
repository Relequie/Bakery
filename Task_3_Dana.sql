SELECT BakeryItem.ItemNumber, BakeryItem.Name, BakeryItem.Source, Bread.Subtype FROM Bread, BakeryItem
WHERE BakeryItem.ItemNumber = Bread.ItemNumber