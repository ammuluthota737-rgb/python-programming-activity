# Retail Billing with Multiple Discount Rules

## 1. Problem Statement

Develop a Python program to process multiple products and quantities, calculate category-specific taxes, apply threshold discounts with maximum concession limits, and generate an itemized invoice showing the final bill.

## 2. Algorithm

1. Start.
2. Input the number of products.
3. Enter each product's name, category, price, and quantity.
4. Calculate the subtotal for each product.
5. Apply category-specific tax rates.
6. Calculate the total bill before discounts.
7. Apply threshold discounts and maximum concession limits.
8. Calculate the final payable amount.
9. Display the itemized invoice.
10. Stop.

## 3. Flowchart

\#chatgpt-mermaid-\_r_mi\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_mi\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_mi\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_mi\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_mi\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_mi\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_mi\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_mi\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_mi\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_mi\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_mi\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_mi\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_mi\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_mi\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_mi\_ p{margin:0;}#chatgpt-mermaid-\_r_mi\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_mi\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_mi\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_mi\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_mi\_ .label text,#chatgpt-mermaid-\_r_mi\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_mi\_ .node rect,#chatgpt-mermaid-\_r_mi\_ .node circle,#chatgpt-mermaid-\_r_mi\_ .node ellipse,#chatgpt-mermaid-\_r_mi\_ .node polygon,#chatgpt-mermaid-\_r_mi\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_mi\_ .rough-node .label text,#chatgpt-mermaid-\_r_mi\_ .node .label text,#chatgpt-mermaid-\_r_mi\_ .image-shape .label,#chatgpt-mermaid-\_r_mi\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_mi\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_mi\_ .rough-node .label,#chatgpt-mermaid-\_r_mi\_ .node .label,#chatgpt-mermaid-\_r_mi\_ .image-shape .label,#chatgpt-mermaid-\_r_mi\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_mi\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_mi\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_mi\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_mi\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_mi\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_mi\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_mi\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_mi\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_mi\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_mi\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_mi\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_mi\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_mi\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_mi\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_mi\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_mi\_ .icon-shape,#chatgpt-mermaid-\_r_mi\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_mi\_ .icon-shape p,#chatgpt-mermaid-\_r_mi\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_mi\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_mi\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_mi\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_mi\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_mi\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_mi\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_mi\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_mi\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_mi\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_mi\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_mi\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_mi\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_mi\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_mi\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_mi\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_mi\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_mi\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_mi\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_mi\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_mi\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_mi\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_mi\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_mi\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_mi\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_mi\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_mi\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_mi\_ .node rect,#chatgpt-mermaid-\_r_mi\_ .node circle,#chatgpt-mermaid-\_r_mi\_ .node ellipse,#chatgpt-mermaid-\_r_mi\_ .node polygon,#chatgpt-mermaid-\_r_mi\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_mi\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_mi\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_mi\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_mi\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_mi\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput number of productsInput product, category, priceand quantityCalculate item subtotalApply category-specific taxMore products?Calculate bill totalSubtotal = 5000?Calculate 10% discountNo threshold discountApply maximum concessionlimitCalculate final payable amountDisplay itemized invoiceStopYesNoYesNo

## 4. Python Source Code

```
n = int(input("Enter number of products: "))items = []subtotal = 0total_tax = 0for i in range(n):    print("\nProduct", i + 1)    name = input("Product name: ")    category = input("Category (food/clothing/electronics): ").lower()    price = float(input("Price: "))    quantity = int(input("Quantity: "))    amount = price * quantity    if category == "food":        tax_rate = 0.05    elif category == "clothing":        tax_rate = 0.05    elif category == "electronics":        tax_rate = 0.18    else:        tax_rate = 0.10    tax = amount * tax_rate    subtotal += amount    total_tax += tax    items.append((name, quantity, amount, tax))# Threshold discount with maximum concessionif subtotal >= 5000:    discount = min(subtotal * 0.10, 1000)elif subtotal >= 2000:    discount = min(subtotal * 0.05, 500)else:    discount = 0final_total = subtotal + total_tax - discountprint("\n========== ITEMIZED INVOICE ==========")print(f"{'Product':15}{'Qty':>5}{'Amount':>12}{'Tax':>10}")for name, qty, amount, tax in items:    print(f"{name:15}{qty:>5}{amount:>12.2f}{tax:>10.2f}")print("--------------------------------------")print(f"Subtotal       : Rs. {subtotal:.2f}")print(f"Total Tax      : Rs. {total_tax:.2f}")print(f"Discount       : Rs. {discount:.2f}")print(f"Final Bill     : Rs. {final_total:.2f}")
```

## 5. Sample Input

```
Enter number of products: 2

Product 1
Product name: Shirt
Category (food/clothing/electronics): clothing
Price: 1000
Quantity: 2

Product 2
Product name: Headphones
Category (food/clothing/electronics): electronics
Price: 2000
Quantity: 2
```

## 6. Sample Output

```
========== ITEMIZED INVOICE ==========
Product          Qty      Amount       Tax
Shirt              2     2000.00    100.00
Headphones         2     4000.00    720.00
--------------------------------------
Subtotal       : Rs. 6000.00
Total Tax      : Rs. 820.00
Discount       : Rs. 600.00
Final Bill     : Rs. 6220.00
```

## 7. Result

The program calculates product totals, applies category-specific taxes and threshold discounts, enforces the maximum concession limit, and generates an itemized invoice.

Note: Tax rates and discount rules are illustrative for this programming exercise. The discount is calculated on the pre-tax subtotal, and taxes are added afterward.
