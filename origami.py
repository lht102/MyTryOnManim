#! /usr/bin/env python3
from manimlib.imports import *
import math

sq_len = 3
sq_bottemLeft = np.array((-sq_len / 2, -sq_len / 2 + 1, 0))
ptA = sq_bottemLeft
ptB = sq_bottemLeft + RIGHT * sq_len
ptC = sq_bottemLeft + UP * sq_len
ptD = sq_bottemLeft + UP * sq_len + RIGHT * sq_len
ptM = (ptA + ptB) / 2
ptN = (ptC + ptD) / 2
ptT = ptM + UP * (sq_len / 2) * math.tan(math.pi / 3)
ptP = ptA + UP * sq_len * math.tan(math.pi / 6)
ptQ = ptB + UP * sq_len * math.tan(math.pi / 6)
leny = math.tan(PI / 12) * sq_len
lenx = sq_len / math.cos(PI / 12)
ptR = ptC + RIGHT * leny
ptS = ptB + UP * leny
ptMn = ptA + RIGHT * lenx / 2 * math.cos(PI / 12) + UP * lenx / 2 * math.sin(PI / 12)

class FoldingEquilateralTriangle(Scene):
    def construct(self):
        lineCD = Line(ptC, ptD, color=BLUE)
        lineBA = Line(ptB, ptA, color=BLUE)
        lineCP = Line(ptC, ptP, color=BLUE)
        linePA = Line(ptP, ptA, color=BLUE)
        lineDQ = Line(ptD, ptQ, color=BLUE)
        lineQB = Line(ptQ, ptB, color=BLUE)
        dotA = Dot(ptA)
        labelA = TextMobject("A")
        labelA.next_to(dotA, DOWN)
        dotB = Dot(ptB)
        labelB = TextMobject("B")
        labelB.next_to(dotB, DOWN)
        dotC = Dot(ptC)
        labelC = TextMobject("C")
        labelC.next_to(dotC, UP)
        dotD = Dot(ptD)
        labelD = TextMobject("D")
        labelD.next_to(dotD, UP)
        self.add(
            lineCD, lineBA, 
            lineCP, linePA,
            lineDQ, lineQB,
            dotA, dotB, dotC, dotD,
            labelA, labelB
        )
        braceWidth = Brace(lineCD, UP)
        braceWidthText = braceWidth.get_text("1")
        braceHeight = Brace(Line(ptD, ptB), RIGHT)
        braceHeightText = braceHeight.get_text("1")
        self.play(
            GrowFromCenter(braceWidth),
            FadeIn(braceWidthText),
            GrowFromCenter(braceHeight),
            FadeIn(braceHeightText)
        )
        self.wait(2)
        self.play(
            FadeOut(braceWidth),
            FadeOut(braceWidthText),
            FadeOut(braceHeight),
            FadeOut(braceHeightText)
        )
        dLineMid = DashedLine(ptN, ptM)
        self.play(ShowCreation(dLineMid))
        dotM = Dot(ptM)
        labelM = TextMobject("M")
        labelM.next_to(dotM, DOWN)
        self.play(
            ShowCreation(dotM),
            Write(labelM)
        )
        dotT = Dot(ptT)
        labelT = TextMobject("T")
        labelT.next_to(dotT)
        dotP = Dot(ptP)
        labelP = TextMobject("P")
        labelP.next_to(dotP)
        linePT = Line(ptP, ptT, color=BLUE)
        lineBT = Line(ptB, ptT, color=BLUE)
        dLinePB = DashedLine(ptP, ptB, color=BLUE)
        self.play(
            ShowCreation(dLinePB)
        )
        self.play(
            Transform(lineBA, lineBT),
            Transform(linePA, linePT),
            Transform(dotA.copy(), dotT),
            Write(labelT)
        )
        self.wait()
        self.play(
            Transform(dLinePB, Line(ptP, ptB, color=BLUE))
        )
        triangle = Polygon(ptT, ptB, ptM, color=RED)
        self.play(
            ShowCreation(triangle)
        )
        angleTMB = [Line(ptM + UP * .3, ptM + UP * .3 + RIGHT * .3), Line(ptM + UP * .3 + RIGHT * .3, ptM + RIGHT * .3)]
        self.play(ShowCreation(angleTMB[0]))
        self.play(ShowCreation(angleTMB[1]))
        braceBM = Brace(Line(ptB, ptM), DOWN)
        braceBMText = braceBM.get_text("0.5")
        braceBT = Brace(lineBT, UP / 2 + RIGHT * math.sqrt(3) / 2)
        braceBTText = braceBT.get_text("1")
        self.play(
            GrowFromCenter(braceBM),
            FadeIn(braceBMText),
            GrowFromCenter(braceBT),
            FadeIn(braceBTText),
            FadeOut(labelM),
            FadeOut(labelB)
        )
        self.wait(2)
        eqText = TextMobject("BM\\textsuperscript{2} + BT\\textsuperscript{2} = MT\\textsuperscript{2}")
        eqText.move_to(ptM + DOWN * 1.5)
        self.play(
            ShowCreation(eqText),
            FadeOut(braceBM),
            FadeOut(braceBMText),
            FadeOut(braceBT),
            FadeOut(braceBTText),
            FadeIn(labelM),
            FadeIn(labelB)
        )
        self.wait(2)
        lineMT = Line(ptM, ptT, color=RED)
        lineMTmoved = lineMT.copy()
        lineMTmoved.move_to(lineMT.get_center() + LEFT * (sq_len / 2 + .5))
        braceMT = Brace(lineMTmoved, LEFT)
        braceMTText = braceMT.get_tex("\\frac{\\sqrt{3}}{2}")
        self.play(Transform(lineMT, lineMTmoved))
        self.wait()
        self.play(
            GrowFromCenter(braceMT),
            FadeIn(braceMTText)
        )
        self.wait()
        angleTBM = Arc(arc_center=ptB, start_angle=lineBT.get_angle(), angle= PI / 3, radius=.5, color=GREEN)
        angleBTM = Arc(arc_center=ptT, start_angle=Line(ptT, ptM).get_angle(), angle= PI / 6, radius=.5, color=YELLOW)
        self.play(
            ShowCreation(angleTBM),
            ShowCreation(angleBTM)
        )
        self.wait()
        eqCalAngleText = TextMobject("$\\cos$($\\angle$MTB)", " = ", "$\\frac{\\text{TM}}{\\text{TB}}$\\\\", "$\\cos$($\\angle$MBT)", " = ", "$\\frac{\\text{BM}}{\\text{BT}}$")
        eqCalAngleText.move_to(eqText.get_center())
        eqCalAngleText[0].set_color(YELLOW)
        eqCalAngleText[3].set_color(GREEN)
        self.play(Transform(eqText, eqCalAngleText))
        self.wait()
        eqAngleText = TextMobject("$\\angle$MTB", " = ", "$30^\\circ$\\\\", "$\\angle$MTB", " = ", "$60^\\circ$")
        eqAngleText[0].set_color(YELLOW)
        eqAngleText[3].set_color(GREEN)
        eqAngleText.move_to(eqText.get_center())
        self.play(Transform(eqText, eqAngleText))
        self.wait()
        lineBAo = Line(ptB, ptA, color=BLUE)
        linePAo = Line(ptP, ptA, color=BLUE)
        self.play(
            FadeOut(dLinePB),
            FadeOut(triangle),
            FadeOut(angleTBM),
            FadeOut(angleBTM),
            FadeOut(braceMT),
            FadeOut(braceMTText),
            FadeOut(lineMT),
            FadeOut(eqText),
            Transform(lineBA, lineBAo),
            Transform(linePA, linePAo),
        )
        self.wait()
        lineTB = DashedLine(ptT, ptB, color=BLUE)
        lineTA = DashedLine(ptT, ptA, color=BLUE)
        angleATB = Arc(arc_center=ptT, start_angle=Line(ptT, ptA).get_angle(), angle= PI / 3, radius=.5)
        angleTBA = Arc(arc_center=ptB, start_angle=lineBT.get_angle(), angle= PI / 3, radius=.5)
        angleTAB = Arc(arc_center=ptA, start_angle=Line(ptA, ptB).get_angle(), angle= PI / 3, radius=.5)
        self.play(
            ShowCreation(lineTB),
            ShowCreation(lineTA),
            ShowCreation(angleATB),
            ShowCreation(angleTBA),
            ShowCreation(angleTAB),
        )
        triangleText = TextMobject("$\\angle$ATB", " = ", "$\\angle$TBA", " = ", "$\\angle$TAB", " = ", "$60^\\circ$")
        triangleText.move_to(eqText.get_center())
        self.play(ShowCreation(triangleText))
        self.wait()

class MaximalEquilateralTriangle(Scene):
    def construct(self):
        lineAC = Line(ptA, ptC, color=BLUE)
        lineCD = Line(ptC, ptD, color=BLUE)
        lineDB = Line(ptD, ptB, color=BLUE)
        lineBA = Line(ptB, ptA, color=BLUE)
        lineAT = Line(ptA, ptT, color=RED)
        lineAB = Line(ptA, ptB, color=RED)
        lineTB = Line(ptT, ptB, color=RED)
        lineMT = DashedLine(ptM, ptT)
        lineATc = lineAT.copy();
        lineABc = lineAB.copy();
        lineTBc = lineTB.copy();
        lineMTc = lineMT.copy();
        dotA = Dot(ptA)
        labelA = TextMobject("A")
        labelA.next_to(ptA, DOWN)
        dotB = Dot(ptB)
        labelB = TextMobject("B")
        labelB.next_to(ptB, DOWN)
        dotM = Dot(ptM)
        labelM = TextMobject("M")
        labelM.next_to(ptM, DOWN)
        dotT = Dot(ptT)
        labelT = TextMobject("T")
        labelT.next_to(ptT, RIGHT)
        dotMn = Dot(ptMn)
        labelMn = TexMobject("\\text{M$^\\prime$}")
        labelMn.next_to(ptMn, LEFT + UP * .5)
        dotR = Dot(ptR)
        labelR = TexMobject("\\text{T$^\\prime$}")
        labelR.next_to(ptR, UP)
        dotS = Dot(ptS)
        labelS = TexMobject("\\text{B$^\\prime$}")
        labelS.next_to(ptS, RIGHT)
        angleA = Arc(arc_center=ptA, start_angle=lineAT.get_angle(), angle= PI / 6, radius=1, color=YELLOW)
        labelAngleA = TextMobject("$\\alpha$")
        labelAngleA.next_to(angleA, UP)
        self.add(
            lineAC, lineCD, lineDB, lineBA,
        )
        self.play(
            ShowCreation(lineMT),
            ShowCreation(lineAT),
            ShowCreation(lineAB),
            ShowCreation(lineTB),
            ShowCreation(labelA),
            ShowCreation(labelB),
            ShowCreation(labelT),
            ShowCreation(labelM),
            ShowCreation(dotA),
            ShowCreation(dotB),
            ShowCreation(dotT),
            ShowCreation(dotM),
            ShowCreation(angleA),
            ShowCreation(labelAngleA),
        )
        self.wait()
        angleAn = Arc(arc_center=ptA, start_angle=Line(ptA, ptR).get_angle(), angle= PI / 12, radius=1, color=YELLOW)
        theta = Arc(arc_center=ptA, start_angle=lineAB.get_angle(), angle= PI / 12, radius=1, color=YELLOW)
        labelTheta = TextMobject("$\\theta$")
        labelTheta.next_to(theta, RIGHT)
        dotAc = dotA.copy()
        self.play(
            Transform(lineATc, Line(ptA, ptR, color=GREEN)),
            Transform(lineABc, Line(ptA, ptS, color=GREEN)),
            Transform(lineTBc, Line(ptR, ptS, color=GREEN)),
            Transform(lineMTc, DashedLine(ptMn, ptR)),
            ShowCreation(theta),
            Transform(angleA, angleAn),
            ApplyMethod(labelAngleA.move_to, angleAn.get_center() + UP * .5 + RIGHT * .05),
            ShowCreation(dotAc),
            FadeIn(labelTheta)
        )
        ptText = ptM + DOWN * 1.5
        eqText = TexMobject("\\frac{\\text{M$^\\prime$T$^\\prime$}}{\\text{MT}} = \\frac{\\text{AB$^\\prime$}}{\\text{AB}}")
        eqText.move_to(ptText)
        eqText2 = TexMobject("\\text{height = M$^\\prime$T$^\\prime$} = \\frac{\\sqrt{3}}{2}AB^\\prime")
        eqText2.move_to(ptText)
        areaText = TexMobject("Area = \\frac{\\sqrt{3}}{4}{(", "AB^\\prime", ")}^2")
        areaText.move_to(ptText)
        areaText2 = TexMobject("Area = \\frac{\\sqrt{3}}{4}\\sec^2\\theta \\\\")
        areaText2.move_to(ptText)
        thetaText = TexMobject("0^\\circ \\leq \\theta \\leq 15^\\circ (\\text{By symmetry})")
        thetaText.move_to(areaText2.get_center() + DOWN)
        cosText = TexMobject("cos\\theta \\text{ is a decreasing function when }")
        cosText.move_to(ptText)
        cosTextSub = TexMobject("0^\\circ \\leq \\theta \\leq 15^\\circ")
        cosTextSub.move_to(cosText.get_center() + DOWN)
        secText = TexMobject("\\therefore sec\\theta \\text{ is increasing}")
        secText.move_to(ptText)
        maxAreaText = TexMobject("\\text{Obtain maximum area when } \\theta = 15^\\circ")
        maxAreaText.move_to(secText.get_center() + DOWN)
        self.play(
            ShowCreation(labelMn),
            ShowCreation(labelR),
            ShowCreation(labelS),
            ShowCreation(dotR),
            ShowCreation(dotS),
            ShowCreation(dotMn),
        )
        self.wait()
        self.play(ShowCreation(eqText))
        self.wait()
        self.play(Transform(eqText, eqText2))
        self.wait()
        self.play(Transform(eqText, areaText))
        self.wait()
        self.play(Transform(eqText, areaText2))
        self.wait()
        self.play(ShowCreation(thetaText))
        self.wait()
        self.play(
            Transform(thetaText, cosTextSub),
            Transform(eqText, cosText)
        )
        self.wait()
        self.play(
            Transform(thetaText, maxAreaText),
            Transform(eqText, secText)
        )
        self.wait()

class FoldingMaximalEquilateralTriangle(Scene):
    def construct(self):
        lenw = lenx * math.cos(PI / 12) * math.cos(PI / 6)
        ptK = ptA + UP * sq_len / 2 + RIGHT * lenw
        ptJ = ptA + UP * lenw + RIGHT * sq_len / 2
        ptW = ptD - RIGHT * leny
        ptH = (ptA + ptC) / 2
        ptI = (ptB + ptD) / 2
        lineMN = DashedLine(ptM, ptN)
        lineHI = DashedLine(ptH, ptI)
        lineAC = Line(ptA, ptC, color=BLUE)
        lineBD = Line(ptB, ptD, color=BLUE)
        lineAB = Line(ptA, ptB, color=BLUE)
        lineRW = Line(ptR, ptW, color=BLUE)
        lineWD = Line(ptW, ptD, color=BLUE)
        lineRC = Line(ptR, ptC, color=BLUE)
        lineDS = Line(ptD, ptS, color=BLUE)
        lineSB = Line(ptS, ptB, color=BLUE)
        self.add(
            lineAC,
            lineAB,
            lineRW,
            lineWD,
            lineRC,
            lineBD
        )
        lineAR = Line(ptA, ptR, color=BLUE)
        lineAJ = Line(ptA, ptJ, color=BLUE)
        lineRJ = Line(ptR, ptJ, color=BLUE)
        lineAS = Line(ptA, ptS, color=BLUE)
        lineAK = Line(ptA, ptK, color=BLUE)
        lineSK = Line(ptS, ptK, color=BLUE)
        lineWJ = Line(ptW, ptJ, color=BLUE)
        lineBJ = Line(ptB, ptJ, color=BLUE)
        lineBW = Line(ptB, ptW, color=BLUE)
        self.play(ShowCreation(lineMN))
        self.wait()
        lineACc = lineAC.copy()
        lineRCc = lineRC.copy() 
        lineWDc = lineWD.copy() 
        lineBDc = lineBD.copy() 
        lineSBc = lineSB.copy() 
        lineABc = lineAB.copy() 
        theta = Arc(arc_center=ptA, start_angle=lineAJ.get_angle(), angle= PI / 12, radius=1, color=YELLOW)
        labelTheta = TextMobject("$\\theta$")
        labelTheta.next_to(theta, UP * .5 + RIGHT * .1)
        self.play(
            Transform(lineAC, lineAJ),
            Transform(lineRC, lineRJ),
            FadeIn(lineAR),
            Transform(lineWD, lineWJ),
            Transform(lineBD, lineBJ),
            FadeIn(lineBW),
        )
        self.play(
            ShowCreation(theta),
            ShowCreation(labelTheta)
        )
        self.wait()
        self.play(
            Transform(lineBD, lineBDc),
            Transform(lineWD, lineWDc),
            FadeOut(lineBW)
        )
        self.add(lineSB, lineDS)
        self.remove(lineBD)
        self.wait()
        self.play(
            ShowCreation(lineHI)
        )
        self.play(
            Transform(lineAB, lineAK),
            Transform(lineSB, lineSK),
            FadeIn(lineAS),
        )
        self.play(ShowCreation(DashedLine(ptR, ptS)))
        self.wait()
        self.play(
            FadeOut(labelTheta),
            FadeOut(theta),
            Transform(lineAR, DashedLine(ptA, ptR)),
            Transform(lineAS, DashedLine(ptA, ptS)),
            Transform(lineAB, lineABc),
            Transform(lineSB, lineSBc),
            Transform(lineAC, lineACc),
            Transform(lineRC, lineRCc),
        )
        self.wait()

class MaximalHexagon(Scene):
    def construct(self):
        sq_len = 2
        sq_bottemLeft = ORIGIN
        ptA = sq_bottemLeft
        ptB = sq_bottemLeft + RIGHT * sq_len
        ptC = sq_bottemLeft + UP * sq_len
        ptD = sq_bottemLeft + UP * sq_len + RIGHT * sq_len
        ptM = (ptA + ptB) / 2
        ptN = (ptC + ptD) / 2
        ptT = ptM + UP * (sq_len / 2) * math.tan(math.pi / 3)
        ptP = ptA + UP * sq_len * math.tan(math.pi / 6)
        ptQ = ptB + UP * sq_len * math.tan(math.pi / 6)
        leny = math.tan(PI / 12) * sq_len
        lenx = sq_len / math.cos(PI / 12)
        ptR = ptC + RIGHT * leny
        ptS = ptB + UP * leny
        ptMn = ptA + RIGHT * lenx / 2 * math.cos(PI / 12) + UP * lenx / 2 * math.sin(PI / 12)
        dotO = Dot(ORIGIN)
        lineAC = Line(ptA, ptC, color=BLUE)
        lineCD = Line(ptC, ptD, color=BLUE)
        lineDB = Line(ptD, ptB, color=BLUE)
        lineBA = Line(ptB, ptA, color=BLUE)
        lineAT = Line(ptA, ptT, color=RED)
        lineAB = Line(ptA, ptB, color=RED)
        lineTB = Line(ptT, ptB, color=RED)
        lineAR =  Line(ptA, ptR, color=GREEN)
        lineAS = Line(ptA, ptS, color=GREEN)
        lineRS = Line(ptR, ptS, color=GREEN)
        sqboxTopRight = VGroup(lineAC, lineCD, lineDB, lineBA)
        sqboxTopLeft = sqboxTopRight.copy().rotate_about_origin(PI / 2)
        sqboxBottomRight = sqboxTopRight.copy().rotate_about_origin(PI)
        sqboxBottomRight = sqboxTopRight.copy().rotate_about_origin(3 * PI / 2)
        sqTopRight = VGroup(lineAC, lineCD, lineDB, lineBA, lineAT, lineAB, lineTB, lineAR, lineAS, lineRS)
        sqTopLeft = sqTopRight.copy().rotate_about_origin(PI / 2)
        sqBottomLeft = sqTopRight.copy().rotate_about_origin(PI)
        sqBottomRight = sqTopRight.copy().rotate_about_origin(3 * PI / 2)
        triTopLeft1 = VGroup(
            DashedLine(ptA, ptR, color=YELLOW),
            DashedLine(ptA, ptS, color=YELLOW),
            DashedLine(ptR, ptS, color=YELLOW)
        )
        triTopLeft1.rotate_about_origin(60 * DEGREES)
        triTopLeft2 = triTopLeft1.copy().rotate_about_origin(60 * DEGREES)
        triBottomLeft1 = triTopLeft1.copy().rotate_about_origin(60 * DEGREES * 3)
        triBottomLeft2 = triTopLeft1.copy().rotate_about_origin(60 * DEGREES * 4)
        self.play(
            ShowCreation(dotO),
            ShowCreation(sqTopRight),
        )
        self.play(
            ShowCreation(sqTopLeft),
        )
        self.play(
            ShowCreation(sqBottomLeft),
        )
        self.play(
            ShowCreation(sqBottomRight),
            ShowCreation(Line(ORIGIN, ORIGIN + RIGHT * sq_len, color=RED)),
        )
        self.wait();
        self.play(
            ShowCreation(triTopLeft1),
        )
        self.play(
            ShowCreation(triTopLeft2),
        )
        self.wait()
        self.play(
            ShowCreation(triBottomLeft1),
        )
        self.play(
            ShowCreation(triBottomLeft2),
        )
        self.wait()
        self.play(
            FadeIn(sqboxTopLeft),
            FadeIn(sqboxBottomRight),
            FadeOut(sqTopLeft),
            FadeOut(sqBottomRight),
        )
        self.wait()
