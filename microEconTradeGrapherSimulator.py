
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def laborMarketCalculator():
    """Gets inputs for current labor makret conditions and tells you the calc for current market metrics"""

    ChngQ = input("Enter Chng Quantity\n")
    #print(ChngQ)
    ChngP = input("Enter Chng Price\n")
    #print(ChngP)
    ChngL = input("Enter Chng Labor\n")

    P = input("Enter Price\n")
    P = int(P)
    #print(P)
    #print(type(P))

    Q = input("Enter Q\n")
    Q = int(Q)

    #ChngP = int(ChngP)
    ChngQ = int(ChngQ)
    ChngL = int(ChngL)

    print("ChngQ:", ChngQ, "ChngL:", ChngL)
    MPL: int = ChngQ/ChngL
    print("MPL:", MPL)
    VMPL: int = P * MPL
    print("VMPL:", VMPL)
    W: int = P * MPL
    print("MPL:",MPL,", VMPL:",VMPL,", W:",W)

def SupplyAndDemandGrapher():
    """Gets inputs for price slope and supply slope, then outputs both curves to a graph on GUI and marks the market equilibirum.
    need to do: also requests and labels axis and scales"""

    import random

    # Global Variables
    canvasXOffsetFromGraph = 100
    """Basically, I use this to set the starting points for many shapes, and
    this var  is specifying how far off from the left side of the canvas does the graph / shapes want to be drawn/
    Also, it can only shift things foward, NOT backwards: UNLESS you make it a NEGATIVE NUMBER"""
    graphLineWidth = 3
    graphHeight = 500 #Originally 500, if something stops working
    """Use this  in calculations of actual prices to adj for the fact that the price variable is based on the y pixel value,
    which increases as it goes down the graph. But the price needs to get lower as you go down the graph. 
    Thus this value is used in caculations to get the actual prices, correct the y value thing, 
    and easily change this value without typing a new number everywhere. If that makes any sense"""
    graphWidth = 500 #idk if need this, honestly should get rid of both and revert to OG, to much of a glithc liability and work, just not worth it.

    # For Graphic Interface
    import tkinter
    window_name = "Supply and demand grapher window"
    window = tkinter.Tk(className=window_name,useTk=True)
    window.geometry("700x700")  # W+H+Xpos+Ypos #OG:600*600
    window.title = ("window_name")

    #Generate canvas to plot on
    graphPlane = tkinter.Canvas(window,bg="white",width=600,height=600) #OG 500, 500

    #Acutal programs that write the stuff
    def generateSDGraph():
        print()
        print()
        print()
        print("-------------------New Graph--------------------")
        """generateSDGraph(): generates randomly the supply and demand prices, then calculates the slopes of the supply and demand curves from the prices,
        the y intercepts are preset.
        GLOBAL VARS: dCurveSlope, sCurveSlope, demandprice, supplyprice"""

        global demandprice
        demandprice = random.randint(0,225)
        print("DEMAND PRICE:",demandprice)
        global supplyprice
        supplyprice = random.randint(285,500)
        print("REAL demandprice",(graphHeight-demandprice),"REAL supplyprice",(graphHeight-supplyprice))

        # calc y intercepts for demand and supply curves
        global demandYInt
        demandYInt = graphHeight # demand (y intercept (quantity) #wut technically the x-int but whatever
        global supplyY2
        supplyY2 = 0  # supply Y2 value

        # create_line(x,y,x1,y1, **options) method START:END cords
        global demand_curve
        demand_curve = canvasXOffsetFromGraph, demandprice, 480+canvasXOffsetFromGraph, demandYInt

        global supply_curve
        supply_curve = canvasXOffsetFromGraph, supplyprice, 480+canvasXOffsetFromGraph, supplyY2
        print("d curve final",demand_curve,"S curve final",supply_curve)

        def canvasDraw():
            #lines N'stuff
            #canvas = 500*500
            #coords from top left corner down, so if thinking from normal grpah oreintation
            # to fix for Y VAL (normal y-500(canvas y bound) = alt y value to get to that same spot
            # to fix for X VAL, keep x val as normal, only range is inversed / different
            graphPlane.create_line(demand_curve,fill="blue", width=graphLineWidth) #demand curve
            graphPlane.create_line(supply_curve,fill="red", width=graphLineWidth) #supply curve

            #calc point intercept form and solution to find equilibrium
            #point slope form: y2-y1=m(x2-x1) --> solve for m (checked with symbolab: m= (y2-y1)/(x2-x1),
            #Preps equation by finding slope to solve sys of equations later
            global dCurveSlope
            dCurveSlope = (demandprice-graphHeight) / (canvasXOffsetFromGraph - (480+canvasXOffsetFromGraph)) #(y2-y)/(x2-x)
            global sCurveSlope
            sCurveSlope = supplyprice / (canvasXOffsetFromGraph - (480+canvasXOffsetFromGraph)) #(y2-y)/(x2-x)
            print("dCurveSlope:",dCurveSlope,"x","sCurveSlope:",sCurveSlope,"x")

            def testSlopeCalcFunc(): #TEST/DIAGNOSTIC FUNCTION
                #Creates parallel lines to check if code is generating correct slope
                demand_curve1 = 0, (demandprice - 20), 480, 480
                supply_curve2 = 0, (supplyprice + 20), 480, 20
                graphPlane.create_line(demand_curve1, fill="green", width=graphLineWidth)
                graphPlane.create_line(supply_curve2, fill="purple", width=graphLineWidth)
        canvasDraw()
        #print("Sucessfully ran function 'generateSDGraph()'")

    def generateEquilibrium():

        # the following is a rip-off / DIY version of the Cramer Rule
        eqStage1x = supplyprice - demandprice
        print("eqStage1x:", eqStage1x)
        eqStage2x = (-1 * dCurveSlope) / sCurveSlope
        print("eqStage2x:", eqStage2x)
        eqStage3x = eqStage1x / eqStage2x
        print("eqStage3x:", eqStage3x)

        print("dC,sC", dCurveSlope, sCurveSlope)  # precheck
        slopem1 = dCurveSlope * -1
        slopem2 = sCurveSlope * -1
        print("sl1 then sl2", slopem1, slopem2)  # post check for signs

        # Calc y coord
        ymcm1 = slopem2 * demandprice
        print("ycm1", ymcm1)
        ymcm2 = slopem1 * supplyprice
        print("ycm2", ymcm2)
        ymsm3: float = ymcm1 - ymcm2
        print("ycm3:", ymsm3)

        # Calc x coord
        xmcm1 = slopem2 * 1
        print("xcm1", xmcm1)
        xmcm2 = slopem1 * 1
        print("xcm2", xmcm2)
        xmsm3: float = xmcm1 - xmcm2
        print("xmsm3", xmsm3, "x val")

        # Calc Determinate
        mD = supplyprice - demandprice
        print("mD=", mD)

        global EquilCoordXalt
        EquilCoordXalt = (mD / xmsm3) + canvasXOffsetFromGraph #adding the offset is a quick fix, not sure why it broke in the first place tho

        global EquilCoordYalt
        EquilCoordYalt = (ymsm3 / xmsm3)

        print("alt cords(xy):",EquilCoordXalt,EquilCoordYalt)

        print()
        print()
        print()
        print("FINAL ANSWERSS!!!!")

        SS = int((((graphHeight-demandprice)-(graphHeight-supplyprice)) * EquilCoordXalt) / 2)
        carrierCostPercentage = SS / 12998000000
        print("The social surplus is ", SS, "$. Or about ", carrierCostPercentage," percent of the cost of one of our ten glorious $12.998 billion dollar Gerald R. Ford class aircraft carriers.", sep="")

        EquilCoordXalt = int(EquilCoordXalt)  # rounded for neatness
        EquilCoordYalt = int(EquilCoordYalt)
        print("The equilibrium quantity is: ",EquilCoordXalt, " units, and the equilibrium price is: $",(graphHeight-EquilCoordYalt), ".", sep="")
        return [EquilCoordXalt],[EquilCoordYalt]
        #print("Sucessfully ran function 'generateEquilibrium()'")

    def generateSurpluses():
        workAroundEquilCoordYalt = EquilCoordYalt
        workAroundEquilCoordXalt = EquilCoordXalt

        if globalEconTFBoolean == 1:
            def generateImportExport():

                global worldPrice
                global globalEconLineColor
                globalEconLineColor = "black"  # specifies the color of the import and export lines
                globalEconIEMax = 20  #It modifies how big the gap must be between the world price and the y intercept of one of the curves

                # quick calculate domestic equilibirum price, yes we do this later in the equilibirum function,
                # but to make things simple and contained in their own functions, well just also do it here for Import and Exports own use.
                # the following is a rip off / DIY version of Cramer's Rule
                slopem1 = dCurveSlope * -1
                slopem2 = sCurveSlope * -1

                # Calc y coord
                ymsm3: float = (slopem2 * demandprice) - (slopem1 * supplyprice)
                # Calc x coord
                xmsm3: float = (slopem2 * 1) - (slopem1 * 1)
                # Calc D
                #mD = supplyprice - demandprice

                global EquilCoordY
                EquilCoordY = int((ymsm3 / xmsm3))
                #print("EquilCoordX before = ", EquilCoordY)

                def generateImport():
                    global worldPrice
                    print("test here are values random: EquilCoordY,supplyprice,globalEconIEMax:", EquilCoordY,supplyprice,globalEconIEMax)
                    worldPrice = random.randint(EquilCoordY + 35, supplyprice - globalEconIEMax)  # Economy imports if world price is less than domestic equilibrium price, also future me: first range num  > 2nd range num
                    # Four is the number of pixel that the difference is noticiable in the GUI
                    graphPlane.create_text(255+canvasXOffsetFromGraph, 45, font="Times", text="Importing")
                    graphPlane.create_line(canvasXOffsetFromGraph, worldPrice, graphWidth+canvasXOffsetFromGraph, worldPrice, fill=globalEconLineColor, width=3)  # import line
                    return worldPrice

                def generateExport():
                    global worldPrice
                    print("test here are values random: EquilCoordY,supplyprice,globalEconIEMax:", EquilCoordY,supplyprice,globalEconIEMax)
                    worldPrice = random.randint(demandprice + globalEconIEMax, EquilCoordY - 20)  #Economy exports if world price is greater than domestic equilibrium price
                    graphPlane.create_text(255+canvasXOffsetFromGraph, 45, font="Times", text="Exporting")
                    graphPlane.create_line(canvasXOffsetFromGraph, worldPrice, graphWidth+canvasXOffsetFromGraph, worldPrice, fill=globalEconLineColor, width=3)  # export line
                    return worldPrice

                # Label for cetner graph to emphasize update
                graphPlane.create_text(250+canvasXOffsetFromGraph, 30, font="Times", text="WITH INTERNATIONAL TRADE")
                # Future Worldprice label?
                # graphPlane.create_text(480, 30, font="Times", text="World Price")

                # deciding import of export will appear
                global deciderVar  # will help decide wether to display a import or export
                deciderVar = random.randint(1, 2)
                if deciderVar == 1:
                    worldPrice = generateExport()
                if deciderVar == 2:
                    worldPrice = generateImport()
                #print("Sucessfully ran function 'generateImportExport()'")
                print(f"The world price is: ${graphHeight-worldPrice}.") #subtraction acounts for weird Y axis inversion
            generateImportExport()
        #print("WP test, oh god please", worldPrice) USE ONLY FOR IMPORT EXPORT TEST, otheriwse error as worldPrice is undefined

        def graphCSTriangle():
            if globalEconTFBoolean == 1:  # adjust CS and PS to account for global economy vs standard domestic calc
                EquilCoordYalt = worldPrice
                # easier just to change the val of var that it norm uses for stand equilibrium
                # to another intercept point I want (worldPrice and Supply)
                EquilCoordXalt = ((worldPrice/dCurveSlope)-(demandprice/dCurveSlope)+canvasXOffsetFromGraph) # y=mx+B?, solve for x, x = (y/m) - (b/m)
            else:
                EquilCoordYalt = workAroundEquilCoordYalt
                EquilCoordXalt = workAroundEquilCoordXalt
                print("graphCSTriangle ECON BEACON FALSE")
                
            chngP = (graphHeight-demandprice) - (graphHeight-EquilCoordYalt)
            #diagnostic thing print("chng P CS", chngP,"y cord",EquilCoordYalt,"x cord",EquilCoordYalt)
            CSValue = int(((EquilCoordXalt-100) * chngP) / 2)  # Area of CS TriangleA=(H*B)/2
            print(f"The consumer surplus is: ${CSValue}.") #idk what f does but it's important
            graphPlane.create_polygon(canvasXOffsetFromGraph, (demandprice + 2), canvasXOffsetFromGraph, (EquilCoordYalt), (EquilCoordXalt - 2), (EquilCoordYalt), fill="green")  # specifiy corners of the triangle: my order is: top, bottom left, bottom right
            
            print("EquilCoordXalt,EquilCoordYalt",EquilCoordXalt,EquilCoordYalt)
            
            #sets a variable equal to supply and world price intersect if global ecnomy, otherwise sets it to a value so it will be ignored by if statments
                
            #CS label out of bounds corrector
            if chngP < abs(55):
                print("TRUE chngP < abs(55)")
            if EquilCoordXalt < 220:
                print("TRUE EquilCoordXalt < 220:")
            if EquilCoordYalt < 202:
                print("TRUE EquilCoordYalt < 202")
            if globalEconTFBoolean == 1:
                supplyWorldInterceptforCSCorrector = ((worldPrice/sCurveSlope)-(supplyprice/sCurveSlope)+canvasXOffsetFromGraph)
            else:
                supplyWorldInterceptforCSCorrector = 200
                
            print("supplyWorldInterceptforCSCorrector",supplyWorldInterceptforCSCorrector)
  
            if chngP < abs(55) or EquilCoordXalt < 220 or EquilCoordYalt < 202 or (supplyWorldInterceptforCSCorrector < 189 and EquilCoordYalt > 80):
                print("TRIG1")
                correctiveCSLabelx1 = canvasXOffsetFromGraph - 50
                correctiveCSLabely1 = EquilCoordYalt - 23
                correctiveCSArrowx1 = canvasXOffsetFromGraph - 27
                correctiveCSArrowy1 = EquilCoordYalt - 20
                
                graphPlane.create_text(correctiveCSLabelx1, correctiveCSLabely1, font="Times 11",
                                        text="Consumer \n Surplus")  # Label for CS Triangle
                graphPlane.create_line(correctiveCSArrowx1, correctiveCSArrowy1, canvasXOffsetFromGraph + 14,
                                        EquilCoordYalt - 5, width=2, arrow=tkinter.LAST)
            else:
                print("ELSE1")
                if globalEconTFBoolean == 1:
                    print("BOOL1")
                    if EquilCoordYalt < 70:
                        print("TRIG2IF")
                        correctiveCSLabelx1 = canvasXOffsetFromGraph + 50
                        correctiveCSLabely1 = worldPrice + 23
                        correctiveCSArrowx1 = canvasXOffsetFromGraph + 40
                        correctiveCSArrowy1 = worldPrice + 20

                        graphPlane.create_text(correctiveCSLabelx1, correctiveCSLabely1, font="Times 11",
                                        text="Consumer \n Surplus")  # Label for CS Triangle
                        graphPlane.create_line(correctiveCSArrowx1, correctiveCSArrowy1, canvasXOffsetFromGraph + 10,
                                        EquilCoordYalt - 5, width=2, arrow=tkinter.LAST)
                
                    else:
                        graphPlane.create_text(53+canvasXOffsetFromGraph, (EquilCoordYalt - 10), font="Times",text="Consumer Surplus")
                        print("ELSE IN BOOL1") # Label for CS Triangle 
                else:
                    graphPlane.create_text(53+canvasXOffsetFromGraph, (EquilCoordYalt - 10), font="Times",text="Consumer Surplus")
                    print("ELSE3") # Label for CS Triangle
        
        graphCSTriangle()

        def graphPSTriangle(): #PRODUCER SURPLUS
            bottomLeftCSTriangleXCoordVal = canvasXOffsetFromGraph #formerly 0
            if globalEconTFBoolean == 1:  # adjust CS and PS to account for global economy vs standard domestic calc
                #print("sp, wp",supplyprice,worldPrice) #TEST
                #print("bottomLeftCSTriangleXCoordVal:",bottomLeftCSTriangleXCoordVal) #TEST
                #easier just to change the val of var that it norm uses for stand equilibrium
                #to another intercept point I want (worldPrice and Supply)
                EquilCoordXalt = ((worldPrice/sCurveSlope)-(supplyprice/sCurveSlope)+canvasXOffsetFromGraph) # x = -(y/m)+(b/m)?????
                EquilCoordYalt = worldPrice
                #print("IF shit executed! here is new val: X,Y",EquilCoordXalt,EquilCoordYalt)ca
            else:
                EquilCoordYalt = workAroundEquilCoordYalt
                EquilCoordXalt = workAroundEquilCoordXalt

            chngP = (graphHeight-EquilCoordYalt) - (graphHeight-supplyprice)
            print("Supply price:", supplyprice)
            #print("chng P PS",chngP)
            #print("EquilCoordXalt PS", EquilCoordXalt)
            PSValue = int(((EquilCoordXalt-100) * chngP) / 2)  # Area of CS TriangleA=(H*B)/2
            print(f"The producer surplus is: ${PSValue}.")
            # For making the three lines that graph the triangle
            graphPlane.create_polygon(0+canvasXOffsetFromGraph, (supplyprice), bottomLeftCSTriangleXCoordVal, (EquilCoordYalt), (EquilCoordXalt), (EquilCoordYalt), fill="purple")


            print("EquilCoordY",EquilCoordY)
            #PS label out of bounds corrector, plus corrects the arrow
            if chngP < abs(55) or EquilCoordXalt < 170:
                graphPlane.create_text(canvasXOffsetFromGraph-50, EquilCoordYalt+80, font="Times 11",
                                       text="Producer \n Surplus")  # Label for PS Triangle
                graphPlane.create_line((canvasXOffsetFromGraph-42), EquilCoordYalt+67, (8 + canvasXOffsetFromGraph), (EquilCoordYalt + 5), width=2, arrow=tkinter.LAST)
                print("trig first wire")
            else:
                if globalEconTFBoolean == 1:
                    print("EquilCoordY",EquilCoordY)
                    if EquilCoordY > (EquilCoordYalt + 5):
                        print("FIRST TRUE: EquilCoordY > (EquilCoordYalt + 5")
                    if EquilCoordY < (worldPrice+81):
                        print("SECOND TRUE: EquilCoordY < (worldPrice+81")
                        
                    if EquilCoordY > (EquilCoordYalt + 5) and EquilCoordY < (worldPrice+95): #Top limit, botom limit. Rmbr stuff is inversed
                        print("TRIGNEWIFS")
                        graphPlane.create_text(canvasXOffsetFromGraph-65, worldPrice+80, font="Times 11",text="Producer \n Surplus")  # Label for PS Triangle
                        graphPlane.create_line((canvasXOffsetFromGraph-60), worldPrice+67, (canvasXOffsetFromGraph-60), (EquilCoordYalt + 9), width=2) #line that goes up from label
                        graphPlane.create_line((canvasXOffsetFromGraph-60), EquilCoordYalt + 9, (14 + canvasXOffsetFromGraph), (EquilCoordYalt + 9), width=2, arrow=tkinter.LAST) #arrow that connects to horitzontal line and points to PS triangle area

                    else:
                        print("TRIG ELSE IN 2IF")
                        graphPlane.create_text(canvasXOffsetFromGraph-50, worldPrice+80, font="Times 11",
                                        text="Producer \n Surplus")  # Label for PS Triangle
                        graphPlane.create_line((canvasXOffsetFromGraph-42), worldPrice+67, (8 + canvasXOffsetFromGraph), (EquilCoordYalt + 5), width=2, arrow=tkinter.LAST)
                else: 
                    graphPlane.create_text(51+canvasXOffsetFromGraph, (EquilCoordYalt + 10), font="Times", text="Producer Surplus")
                    print("TRIG last else") # Label for PS Triangle
                    
        graphPSTriangle()

        #print("Sucessfully ran function 'generateSurpluses()'")

    def generateGraphAxis():
        """Generates the X and Y axis lines, plus the Quantity and Price labels"""

        if globalEconTFBoolean < 1:
            graphAxisLabelsTextSize = "times 20"
            graphAxisPriceLabelXVal = 40  # subtracts from 100 (canvasXOffsetFromGraph)
            graphAxisQuantityLabelText = "QUANTITY"
            graphAxisPriceLabelText = "PRICE"
            quantityLabelOverlapXValueCorrection =  0
            quantityLabelOverlapYValueCorrection =  0
        else:
            graphAxisQuantityLabelText = ("DOMESTIC \n"
                                          "QUANTITY")
            graphAxisPriceLabelText = ("DOMESTIC \n"
                                       "PRICE")
            graphAxisPriceLabelXVal = 46
            graphAxisLabelsTextSize = "times 15"
            
            quantityLabelOverlapXValueCorrection =  0
            quantityLabelOverlapYValueCorrection =  0

            #to prevent overlap of guidelines to imports and quantites with the Domestic Quantity / X axis label
            dx = ((worldPrice/dCurveSlope)-(demandprice/dCurveSlope)+canvasXOffsetFromGraph)
            if dx > 490:
                quantityLabelOverlapXValueCorrection =  50
                quantityLabelOverlapYValueCorrection =  50
                graphAxisLabelsTextSize = "times 12"
        
        # Quantity / X Axis
        graphPlane.create_line(canvasXOffsetFromGraph-1.5,0,canvasXOffsetFromGraph-1.5,graphHeight,width=3,fill="black")
        graphPlane.create_text(435+canvasXOffsetFromGraph+quantityLabelOverlapXValueCorrection,540+quantityLabelOverlapYValueCorrection,text=graphAxisQuantityLabelText, font=graphAxisLabelsTextSize)
        # #Price / Y Axis
        graphPlane.create_line(canvasXOffsetFromGraph-2.5,501,502+canvasXOffsetFromGraph,graphHeight,width=3,fill="black")
        graphPlane.create_text(canvasXOffsetFromGraph-graphAxisPriceLabelXVal,40,text=graphAxisPriceLabelText, font=graphAxisLabelsTextSize)

    def generateRetraceLine():
        """retraces lines such as WP & SD that tend to get overwritten"""
        graphPlane.create_line(demand_curve, fill="blue", width=graphLineWidth)  # demand curve
        graphPlane.create_line(supply_curve, fill="red", width=graphLineWidth)  # supply curve

        if globalEconTFBoolean == 1:  # all things that need to be redrawn if global MKT
            graphPlane.create_line(canvasXOffsetFromGraph, worldPrice, 500, worldPrice, fill=globalEconLineColor,
                                   width=3)  # Import or export line aka World Price

    def generateEquilibriumLabels():

        # EQUILIBRIUM DOT
        # printing the equilibrium dot here instead of in the generateEquilibrium() func
        # bc the surplus triangles would otherwise cover it up
        normalEquilibriumDotColor = "orange" #maybe later make a formal table of function to style dot colors depnding on how many there are

        def generateNormalEquilibriumGuideLines():

            ECLTC = 3 #Line Thicknes Compensation so it covers the intercept.

            # Y Line
            graphPlane.create_line(canvasXOffsetFromGraph, EquilCoordYalt, EquilCoordXalt - ECLTC, EquilCoordYalt,
                                   width=2, dash=(4, 1))
            # X line
            graphPlane.create_line(EquilCoordXalt, EquilCoordYalt, EquilCoordXalt, 500, width=2, dash=(4, 1))

        generateNormalEquilibriumGuideLines()

        # Normal Equilibirum dot, poiting lines, and text --------------------------

        # lines graph first, so the dot can be drawn on top
        ECLTC = 3 # Equilibrium Coordinate S&D Line Thicknes Compensation so it covers the intercept.
        # Equil Dot
        graphPlane.create_oval(EquilCoordXalt - ECLTC, EquilCoordYalt - ECLTC, EquilCoordXalt + ECLTC,
                               EquilCoordYalt + ECLTC,
                               fill=normalEquilibriumDotColor)

        # Quantity Label
        #worldPriceExspress = wPT + "$"
        graphPlane.create_text(EquilCoordXalt, 510, text="Eq", font="times 10")
        graphPlane.create_text(EquilCoordXalt, 520, text=int(EquilCoordXalt), font="times 10")

        # Label overlap trigger equation for world price and price
        if globalEconTFBoolean == 1:
            overlapWarningTrigger = abs(EquilCoordYalt-worldPrice)
            if (abs(overlapWarningTrigger) < 6):
                print("TRIGGERED OVERLAP WARNING PRICE LABELS")
                correctivePricey1 = 1
                correctiveyPricex1 = 3
                correctiveyPricey2 = 5
                correctiveyPricex2 = 6
                graphPlane.create_line(50, EquilCoordYalt, canvasXOffsetFromGraph, EquilCoordYalt, width=2, dash=(4, 1))
                graphPlane.create_line(50, EquilCoordYalt, 50, EquilCoordYalt-10 , width=2, dash=(4, 1))
            else:
                correctiveyPricey1 = 0
                correctiveyPricex1 = 0
                correctiveyPricey2 = 0
                correctiveyPricex2 = 0
        else:
            correctiveyPricey1 = 0
            correctiveyPricex1 = 0
            correctiveyPricey2 = 0
            correctiveyPricex2 = 0
                
        # Price Label
        graphPlane.create_text(canvasXOffsetFromGraph - 10 + correctiveyPricex1, EquilCoordYalt + correctiveyPricex1, text="Ep", font="times 10")
        EpExspress = str(graphHeight-EquilCoordYalt) + "$" #makes it so can display Equilibrium Price as string
        graphPlane.create_text(canvasXOffsetFromGraph - 30, EquilCoordYalt, text=EpExspress,
                               font="times 10")

        if globalEconTFBoolean == 0:
            # S&D Line Labels
            graphPlane.create_text(480 + canvasXOffsetFromGraph, 30, font="Times",
                                   text="Supply")  # Label for Supply Graph #x,y anchor='w',font,text
            graphPlane.create_text(480 + canvasXOffsetFromGraph, 470, font="Times",
                                   text="Demand")  # Label for Demand Graph

        if globalEconTFBoolean == 1:

            withTradeEquilibriumLabelsColor = "orange"
            #generateNormalEquilibriumGuideLines()

            #domestic demand with trade equilibrium point
            graphPlane.create_oval(((worldPrice/dCurveSlope)-(demandprice/dCurveSlope)+canvasXOffsetFromGraph) - ECLTC, worldPrice - ECLTC, ((worldPrice/dCurveSlope)-(demandprice/dCurveSlope)+canvasXOffsetFromGraph) + ECLTC,
                                   worldPrice + ECLTC, fill=withTradeEquilibriumLabelsColor)

            #domestic supply with trade equilibrium point
            graphPlane.create_oval(
                ((worldPrice/sCurveSlope)-(supplyprice/sCurveSlope)+canvasXOffsetFromGraph) - ECLTC,
                worldPrice - ECLTC,
                ((worldPrice/sCurveSlope)-(supplyprice/sCurveSlope)+canvasXOffsetFromGraph) + ECLTC,
                worldPrice + ECLTC, fill=withTradeEquilibriumLabelsColor)

            #supply guideline
            graphPlane.create_line(((worldPrice/sCurveSlope)-(supplyprice/sCurveSlope)+canvasXOffsetFromGraph), worldPrice+3, ((worldPrice/sCurveSlope)-(supplyprice/sCurveSlope)+canvasXOffsetFromGraph), 500,
                                   width=2, dash=(4, 1))
            #demand guideline
            graphPlane.create_line(((worldPrice/dCurveSlope)-(demandprice/dCurveSlope)+canvasXOffsetFromGraph), worldPrice+3, ((worldPrice/dCurveSlope)-(demandprice/dCurveSlope)+canvasXOffsetFromGraph), 500,
                                   width=2, dash=(4, 1))

            dx = ((worldPrice/dCurveSlope)-(demandprice/dCurveSlope)+canvasXOffsetFromGraph)
            sx = ((worldPrice/sCurveSlope)-(supplyprice/sCurveSlope)+canvasXOffsetFromGraph)
            cy = 540
            hx = ((dx+sx)/2)

            #Corrective variables to be used if labels are in danger of overlapping
            correctiveQ1y = 0
            correctiveQy2 = 0
            correctiveQy3 = 0
            correctiveQy4 = 0

            #print("dx-sx")
            #print(dx-sx)
            #print("sx-dx")
            #print(sx - dx)

            #overlap trigger equation
            if (abs(dx-sx) or abs(sx-dx) < 25):
                correctiveQy1 = 10
                correctiveQy2 = 20
                correctiveQy3 = 10 #NA
                correctiveQy4 = 10 # For dot lines
                correctiveQy5 = 10 # For dot lines
                graphPlane.create_line(dx, 502, dx, 504 + correctiveQy4, width= 2, dash=(4,1))
                # dashed line to point to Q1 if moved down for anti overlap reasons
                graphPlane.create_line(sx, 502, sx, 504 + correctiveQy5, width=2, dash=(4, 1))
                # dashed line to point to Q2 if moved down for anti overlap reasons

            #point labels
            graphPlane.create_text(dx, 510+correctiveQy1, text="Q1", font="times 10")
            graphPlane.create_text(sx, 510+correctiveQy2, text="Q2", font="times 10")

            #Quantity number labels for points
            graphPlane.create_text(dx, 521+correctiveQy1, text=int(dx), font="times 10")
            graphPlane.create_text(sx, 521+correctiveQy2, text=int(sx), font="times 10")

            #lines to create pointer to import / export
            graphPlane.create_line(dx, 526+correctiveQy1, dx, cy+correctiveQy2,
                                   width=2) #tbd tip1
            graphPlane.create_line(sx, 526+correctiveQy2, sx, cy+correctiveQy2,#EQUALIZE SO MEET HORIZONTAL EVENLY
                                   width=2) #tbd tip2
            graphPlane.create_line(dx, cy+correctiveQy2, sx, cy+correctiveQy2,
                                   width=2) #horizontal
            graphPlane.create_line(hx, cy+correctiveQy2, hx, cy+15+correctiveQy2,
                                   width=2,) # vert
            if sx > dx:
                global diffQ1Q2
                diffQ1Q2=abs(sx - dx)
                #print("IF:", diffQ1Q2)
            else:
                diffQ1Q2 = abs(dx - sx)
                #print("ELSE:",diffQ1Q2)

            diffQ1Q2 = int(diffQ1Q2)
            diffQ1Q2 = str(diffQ1Q2)

            if deciderVar == 1:
                numE = diffQ1Q2 + " Units"
                graphPlane.create_text(hx, cy+20+correctiveQy2, text="Exports", font="times 10")
                graphPlane.create_text(hx, cy+30+correctiveQy2, text=numE, font="times 10")

            else:
                numI = diffQ1Q2 + " units"
                graphPlane.create_text(hx, cy+20+correctiveQy2, text="Imports", font="times 10")
                graphPlane.create_text(hx, cy+30+correctiveQy2, text=numI, font="times 10")

            # S&D Line Labels
            graphPlane.create_text(475 + canvasXOffsetFromGraph, 50, font="Times 12",
                                   text="Domestic \nSupply")  # Label for Supply Graph #x,y anchor='w',font,text
            graphPlane.create_text(475 + canvasXOffsetFromGraph, 450, font="Times 12",
                                   text="Domestic \n Demand")  # Label for Demand Graph

            #World price labels
            graphPlane.create_text(canvasXOffsetFromGraph - 57, worldPrice, text="World Price:",
                                   font="times 10")  # Pw label
            wPT = worldPrice
            wPT = str(500-wPT)
            worldPriceExspress= wPT+"$"
            graphPlane.create_text(canvasXOffsetFromGraph - 16, worldPrice, text=worldPriceExspress,
                                   font="times 10")  # actual wp price display

        #if globalEconTFBoolean == 2:
            #pass

    # Commands / Functions for the buttons to call
    def sdButtonFunction():
        graphPlane.delete("all") #clears any previous drawings
        global globalEconTFBoolean
        globalEconTFBoolean = 0
        generateSDGraph()
        generateEquilibrium()
        generateSurpluses()
        generateRetraceLine()
        generateGraphAxis()
        generateEquilibriumLabels()
        # add buttons back in bc cleared earlier
        sdButton = tkinter.Button(window, text="Generate normal S&D market", fg="Black", width=40, height=25,
                                   command=sdButtonFunction)
        globalEconButton = tkinter.Button(window, text="Generate an import or export market", fg="Black", width=40,
                                          height=25, command=globalEconButtonFunction)

    def globalEconButtonFunction():
        graphPlane.delete("all") #clears any previous drawings
        generateSDGraph()
        global globalEconTFBoolean
        globalEconTFBoolean = 1
        generateEquilibrium()
        generateSurpluses()
        generateRetraceLine()
        generateGraphAxis()
        generateEquilibriumLabels()
        #add buttons back in bc cleared earlier
        sdButton = tkinter.Button(window, text="Generate normal S&D market", fg="Black", width=40, height=25,
                                   command=sdButtonFunction)
        globalEconButton = tkinter.Button(window, text="Generate an import or export market", fg="Black", width=40,
                                          height=25, command=globalEconButtonFunction)

    def globalTariffEconButtonFunction():
        graphPlane.delete("all")
        global globalEconTFBoolean
        globalEconTFBoolean = 1
        global globalTariffEconTFBoolean
        globalTariffEconTFBoolean = 1
        generateSDGraph()

        global globalTaxTFBoolean
        globalTaxTFBoolean = 1


    # starting buttons to generate graphs
    sdButton = tkinter.Button(window, text="Generate normal S&D market", fg="Black", width=40, height=25, command=sdButtonFunction)
    globalEconButton = tkinter.Button(window, text="Generate an import or export market", fg="Black", width=40, height=25, command=globalEconButtonFunction)
    globalTariffEconButton = tkinter.Button(window, text="Generate an import or export market", fg="Black", width=40, height=25, command=globalTariffEconButtonFunction)

    graphPlane.pack(side="top")
    sdButton.pack(side="left")
    globalEconButton.pack(side="right")
    globalTariffEconButton.pack(side="right")

    #run
    window.mainloop()

#for terminal
"""if __name__ == '__main__':
    print("Here are the aviailable functions to call: print hi, Labor Market Calculator, Supply And Demand Grapher")
    usersChoice=input("Enter the function you wish to execute: \n")
    print("Excellent choice, running the",usersChoice,"function now.")

    #IFs match userchoice to function to run
    if usersChoice == "print hi":
        print_hi(name=input("Enter your name:\n"))
    if usersChoice == "Labor Market Calculator":
        laborMarketCalculator()
    if usersChoice == "Supply And Demand Grapher":
        SupplyAndDemandGrapher()"""
        
SupplyAndDemandGrapher()

