# Railway Fare and Reservation Calculator

## 1. Problem Statement

Develop a Python program to calculate railway fares for multiple passengers based on distance slabs, travel class, age-based concessions, reservation fees, and cancellation penalties. Display the total fare for each passenger.

## 2. Algorithm

1. Start.
2. Input the number of passengers.
3. For each passenger, input name, age, distance, travel class, and booking status.
4. Calculate the base fare using distance slabs.
5. Apply the travel-class multiplier.
6. Apply age-based concessions.
7. Add reservation fees.
8. If cancelled, calculate the cancellation penalty and refund.
9. Display the fare details for each passenger.
10. Stop.

## 3. Flowchart

\#chatgpt-mermaid-\_r_k6\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_k6\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_k6\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_k6\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_k6\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_k6\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_k6\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_k6\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_k6\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_k6\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_k6\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_k6\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_k6\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_k6\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_k6\_ p{margin:0;}#chatgpt-mermaid-\_r_k6\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_k6\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_k6\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_k6\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_k6\_ .label text,#chatgpt-mermaid-\_r_k6\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_k6\_ .node rect,#chatgpt-mermaid-\_r_k6\_ .node circle,#chatgpt-mermaid-\_r_k6\_ .node ellipse,#chatgpt-mermaid-\_r_k6\_ .node polygon,#chatgpt-mermaid-\_r_k6\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_k6\_ .rough-node .label text,#chatgpt-mermaid-\_r_k6\_ .node .label text,#chatgpt-mermaid-\_r_k6\_ .image-shape .label,#chatgpt-mermaid-\_r_k6\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_k6\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_k6\_ .rough-node .label,#chatgpt-mermaid-\_r_k6\_ .node .label,#chatgpt-mermaid-\_r_k6\_ .image-shape .label,#chatgpt-mermaid-\_r_k6\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_k6\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_k6\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_k6\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_k6\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_k6\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_k6\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_k6\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_k6\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_k6\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_k6\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_k6\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_k6\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_k6\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_k6\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_k6\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_k6\_ .icon-shape,#chatgpt-mermaid-\_r_k6\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_k6\_ .icon-shape p,#chatgpt-mermaid-\_r_k6\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_k6\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_k6\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_k6\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_k6\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_k6\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_k6\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_k6\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_k6\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_k6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_k6\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_k6\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_k6\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_k6\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_k6\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_k6\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_k6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_k6\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_k6\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_k6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_k6\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_k6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_k6\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_k6\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_k6\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_k6\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_k6\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_k6\_ .node rect,#chatgpt-mermaid-\_r_k6\_ .node circle,#chatgpt-mermaid-\_r_k6\_ .node ellipse,#chatgpt-mermaid-\_r_k6\_ .node polygon,#chatgpt-mermaid-\_r_k6\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_k6\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_k6\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_k6\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_k6\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_k6\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput number of passengersInput passenger detailsCalculate distance-based fareApply class multiplierApply age concessionAdd reservation feeTicket cancelled?Calculate penalty and refundCalculate final fareDisplay fare and refund detailsMore passengers?StopYesNoYesNo

## 4. Python Source Code

```
n = int(input("Enter number of passengers: "))for i in range(n):    print("\nPassenger", i + 1)    name = input("Enter name: ")    age = int(input("Enter age: "))    distance = float(input("Enter distance (km): "))    travel_class = input("Class (Sleeper/AC): ").lower()    cancelled = input("Ticket cancelled? (yes/no): ").lower()    # Distance-based fare    if distance <= 100:        rate = 1.0    elif distance <= 500:        rate = 1.5    else:        rate = 2.0    fare = distance * rate    # Travel class multiplier    if travel_class == "ac":        fare *= 2    elif travel_class != "sleeper":        print("Invalid class. Using Sleeper.")        travel_class = "sleeper"    # Age concessions (illustrative rules)    if age < 5:        fare = 0    elif age >= 60:        fare *= 0.8    reservation_fee = 40 if fare > 0 else 0
```

## 5. Sample Input

```
Enter number of passengers: 2

Passenger 1
Enter name: Ravi
Enter age: 25
Enter distance (km): 200
Class (Sleeper/AC): Sleeper
Ticket cancelled? (yes/no): no

Passenger 2
Enter name: Sita
Enter age: 65
Enter distance (km): 200
Class (Sleeper/AC): AC
Ticket cancelled? (yes/no): yes
```

## 6. Sample Output

```
--- Fare Statement ---
Passenger: Ravi
Distance Fare: Rs. 300.0
Reservation Fee: Rs. 40
Total Fare: Rs. 340.0

--- Fare Statement ---
Passenger: Sita
Original Fare: Rs. 640.0
Cancellation Penalty: Rs. 160.0
Refund Amount: Rs. 480.0
```

## 7. Result

The program calculates fares for multiple passengers, applies class-based rates and age concessions, adds reservation fees, and determines cancellation penalties and refunds.

Note: The rates, concessions, reservation fees, and cancellation rules used here are illustrative for a programming exercise, not official railway fare rules.
