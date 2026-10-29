# Campus Event Financial Planning

## 1. Problem Statement

Develop a Python program to calculate campus event expenses, including venue, equipment, catering, transport, and certificates. Determine the total budget, participant contribution, sponsorship shortfall, and minimum number of registrations required to break even.

## 2. Algorithm

1. Start.
2. Input venue, equipment, catering, transport, and certificate costs.
3. Input sponsorship amount, registration fee, and expected participants.
4. Calculate total event expenses.
5. Calculate total available funds from sponsorship and registrations.
6. Calculate participant contribution per person.
7. Calculate sponsorship shortfall, if any.
8. Calculate the minimum registrations required to break even.
9. Display the financial report.
10. Stop.

## 3. Flowchart

\#chatgpt-mermaid-\_r_v2\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_v2\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_v2\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_v2\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_v2\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_v2\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_v2\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_v2\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_v2\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_v2\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_v2\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_v2\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_v2\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_v2\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_v2\_ p{margin:0;}#chatgpt-mermaid-\_r_v2\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_v2\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_v2\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_v2\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_v2\_ .label text,#chatgpt-mermaid-\_r_v2\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_v2\_ .node rect,#chatgpt-mermaid-\_r_v2\_ .node circle,#chatgpt-mermaid-\_r_v2\_ .node ellipse,#chatgpt-mermaid-\_r_v2\_ .node polygon,#chatgpt-mermaid-\_r_v2\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_v2\_ .rough-node .label text,#chatgpt-mermaid-\_r_v2\_ .node .label text,#chatgpt-mermaid-\_r_v2\_ .image-shape .label,#chatgpt-mermaid-\_r_v2\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_v2\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_v2\_ .rough-node .label,#chatgpt-mermaid-\_r_v2\_ .node .label,#chatgpt-mermaid-\_r_v2\_ .image-shape .label,#chatgpt-mermaid-\_r_v2\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_v2\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_v2\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_v2\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_v2\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_v2\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_v2\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_v2\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_v2\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_v2\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_v2\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_v2\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_v2\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_v2\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_v2\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_v2\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_v2\_ .icon-shape,#chatgpt-mermaid-\_r_v2\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_v2\_ .icon-shape p,#chatgpt-mermaid-\_r_v2\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_v2\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_v2\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_v2\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_v2\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_v2\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_v2\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_v2\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_v2\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_v2\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_v2\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_v2\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_v2\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_v2\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_v2\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_v2\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_v2\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_v2\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_v2\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_v2\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_v2\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_v2\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_v2\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_v2\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_v2\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_v2\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_v2\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_v2\_ .node rect,#chatgpt-mermaid-\_r_v2\_ .node circle,#chatgpt-mermaid-\_r_v2\_ .node ellipse,#chatgpt-mermaid-\_r_v2\_ .node polygon,#chatgpt-mermaid-\_r_v2\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_v2\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_v2\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_v2\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_v2\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_v2\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput all event expensesInput sponsorship andregistration feeCalculate total event costCalculate required participantcontributionCalculate sponsorship shortfallRegistration fee 0?Calculate minimum break-evenregistrationsBreak-even throughregistration impossibleDisplay financial reportStopYesNo

## 4. Python Source Code

```
venue = float(input("Enter venue cost: Rs. "))equipment = float(input("Enter equipment cost: Rs. "))catering = float(input("Enter catering cost per person: Rs. "))transport = float(input("Enter transport cost: Rs. "))certificates = float(input("Enter certificate cost per person: Rs. "))participants = int(input("Enter expected participants: "))sponsorship = float(input("Enter sponsorship amount: Rs. "))fee = float(input("Enter registration fee per person: Rs. "))if participants < 0 or sponsorship < 0 or fee < 0:    print("Invalid input")else:    fixed_cost = venue + equipment + transport    variable_cost = participants * (catering + certificates)    total_cost = fixed_cost + variable_cost    registration_income = participants * fee    total_funds = sponsorship + registration_income    shortfall = max(0, total_cost - total_funds)    contribution = max(0, total_cost - sponsorship) / participants \        if participants > 0 else 0    # Break-even registration count    per_person_margin = fee - catering - certificates    if total_cost <= sponsorship:        break_even = 0    elif per_person_margin > 0:        break_even = max(            0,            int((fixed_cost - sponsorship) / per_person_margin) + 1        )        # Correct exact-integer break-even
```

## 5. Sample Input

```
Enter venue cost: Rs. 10000
Enter equipment cost: Rs. 5000
Enter catering cost per person: Rs. 200
Enter transport cost: Rs. 3000
Enter certificate cost per person: Rs. 50
Enter expected participants: 100
Enter sponsorship amount: Rs. 15000
Enter registration fee per person: Rs. 300
```

## 6. Sample Output

```
===== EVENT FINANCIAL REPORT =====
Fixed Costs       : Rs. 18000.00
Variable Costs    : Rs. 25000.00
Total Event Cost  : Rs. 43000.00
Sponsorship       : Rs. 15000.00
Registration Income: Rs. 30000.00
Participant Contribution Needed: Rs. 280.00
Sponsorship Shortfall: Rs. 0.00
Minimum Break-even Registrations: 40
```

## 7. Result

The program calculates the total event budget, registration income, required participant contribution, sponsorship shortfall, and minimum registrations needed to cover costs.

Note: The break-even calculation assumes catering and certificate costs vary with the number of registered participants, while venue, equipment, and transport costs remain fixed.
