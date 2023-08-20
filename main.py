from manim import *

class Introduction(Scene):
    def construct(self):
        circ = Circle()
        self.add(circ)
        self.wait(3)

class AddAndRemoveMethods(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.wait(4)
        self.remove(square)
        self.wait(2)

class Background(Scene):
    def construct(self):
        self.camera.background_color = DARK_GREY

        config.background_color = GREEN
        line1 = Line()
        self.add(line1)
        self.wait(3)

        line2=Line(DOWN, UP)
        self.add(line2)
        self.wait(3)

        self.remove(line1, line2)
        self.wait(3)

class FadeAnimation(Scene):
    def construct(self):
        circ = Circle(radius=2)
        self.play(FadeIn(circ))
        self.wait()
        self.play(FadeOut(circ))

        square = Square(side_length=3)
        self.play(FadeIn(square))
        self.wait()
        self.play(FadeOut(square))

        line = Line(LEFT, RIGHT+UP+UP)
        self.play(FadeIn(line))
        self.wait()
        self.play(FadeOut(line))

class PolygonalShapes(Scene):
    def construct(self):
        rect = Rectangle(height=2, width=3)
        self.play(FadeIn(rect))
        self.wait()
        self.play(FadeOut(rect))
        self.wait()
        regular_polygon = RegularPolygon(n=8, radius=1.5)
        self.play(FadeIn(rect), FadeIn(regular_polygon))
        self.wait()

        triangle = Triangle(radius=2)
        self.play(FadeIn(triangle), FadeOut(rect), FadeOut(regular_polygon))

        polugon = Polygon(DOWN+2*LEFT,UP+LEFT, ORIGIN,
                          UP+RIGHT, DOWN+2*RIGHT)
        self.play(FadeIn(polugon), FadeOut(triangle))

class ArcShapes(Scene):

    def p(self, param, obj):
        if param=='o':
            self.play(FadeOut(obj))
        else:
            self.play(FadeIn(obj))

    def construct(self):
        arc=Arc(radius=3, start_angle=PI/4, angle=PI/6)
        self.play(FadeIn(arc))


        dot = Dot(radius=0.5)
        self.play(FadeIn(dot))
        self.wait()

        self.play(FadeOut(dot), FadeOut(arc))
        self.wait(0.4)

        ellipse = Ellipse(height=2, width=4)
        self.play(FadeIn(ellipse))
        self.wait(0.5)
        rect = Rectangle(height=2, width=4)
        self.play(FadeIn(rect))
        self.wait()

        self.play(FadeOut(ellipse), FadeOut(rect))

        annulus = Annulus(outer_radius=1,
                          inner_radius=0.8)
        self.play(FadeIn(annulus))

        sector = Sector(outer_radius=0.8, angle=PI/6)
        self.p('i', sector)

class ArrowShapes(Scene):
    def p(self, obj):
        self.play(FadeIn(obj))
        self.wait(0.5)
        self.play(FadeOut(obj))

    def construct(self):
        arrow = Arrow(LEFT, 3*RIGHT, tip_length=0.2)
        self.p(arrow)

        d_arrow = DoubleArrow(2*LEFT, 2*RIGHT, tip_length=0.4)
        self.p(d_arrow)

        curv_arrow = CurvedArrow(3*LEFT, 3*RIGHT, radius=10)
        self.p(curv_arrow)

class DecorativeShapes(Scene):
    def p(self, obj):
        self.play(FadeIn(obj))
        self.wait(0.5)
        self.play(FadeOut(obj))

    def construct(self):
        dashed_line1= DashedLine(ORIGIN,3*UP)
        self.play(FadeIn(dashed_line1))

        dl2 = DashedLine(2*LEFT, 2*RIGHT, dash_length=0.2)
        self.play(FadeIn(dl2))

        right_angle = RightAngle(dashed_line1, dl2)
        self.play(FadeIn(right_angle))

        self.play(FadeOut(dashed_line1), FadeOut(right_angle))

        line = Line(ORIGIN, 2*UP+1.5*RIGHT)
        angle = Angle(dl2, line, radius=1)

        self.play(FadeIn(line), FadeIn(angle))

        self.wait(0.5)
        self.play(FadeOut(line), FadeOut(angle))

        rounded_rect = RoundedRectangle(corner_radius=0.1,)
        self.p(rounded_rect)

        star = Star(n=7)
        self.p(star)

        circ = DashedVMobject(Circle(radius=2), num_dashes=3)
        self.p(circ)


class BezierAndRoundedAngle(Scene):
    def p(self, *obj):
        for i in obj:
            self.play(FadeIn(i))
        self.wait(0.5)
        for i in obj:
            self.play(FadeOut(i))

    def construct(self):
        spline1 = CubicBezier(
            3*LEFT,
            4*UP,
            3*RIGHT+2*DOWN,
            4*RIGHT+5*UP
        )
        spline2 = CubicBezier(
            3*LEFT,
            4*UP,
            3*RIGHT+2*DOWN,
            4*RIGHT+3*UP
        )
        self.p(spline1, spline2)

        star = Star(n=12).round_corners(radius=0.05)
        trian = Triangle(radius=2)
        trian.round_corners(radius=0.5)

        self.p(star,trian)

class AnimationsAttr(Scene):
    def construct(self):
        circ = Circle()
        line = Line()
        dot = Dot()
        self.play(FadeIn(dot), run_time=1)
        self.play(FadeIn(circ, shift=UP), run_time=2)
        self.play(FadeIn(line, shift=RIGHT), run_time=3)

        self.play(FadeOut(line,circ,dot, shift=LEFT), run_time=5)

class Test(Scene):
    def construct(self):
        line1 = Line(LEFT, ORIGIN)
        line2 = Line(2*UP, 3*DOWN)
        self.play(FadeIn(line1, line2))

class CreationUncreationGrow(Scene):
    def construct(self):
        arrow = Arrow()
        circ = Circle(1.5)
        sq = Square(3)
        pol = Polygon(2*UP, ORIGIN, 2*RIGHT)

        self.play(Create(arrow), run_time=5)
        self.wait()
        self.play(Uncreate(arrow), run_time=5)
        self.play(Create(circ), run_time=2)
        self.wait()
        self.play(Uncreate(circ), run_time=3)

        self.play(GrowFromCenter(sq))
        self.play(GrowFromCenter(pol))
        self.wait()


class HomeWork(Scene):
    def construct(self):
        dot=Dot()
        circs=[]
        self.play(FadeIn(dot))
        for i in range(3):
            circs.append(Circle(i+0.5))
            self.play(GrowFromCenter(circs[i]))
        self.wait()
        # self.play(FadeOut(dot, circs[0], circs[1],circs[2]))
        self.play(FadeOut(dot, *circs))
        poly8=RegularPolygon(n=8,radius=2.5)
        self.play(GrowFromCenter(poly8), run_time=0.5)

        poly4=Square(side_length=12.5**0.5)
        self.play(GrowFromCenter(poly4), run_time=0.5)
        circ=Circle((12.5**0.5)/2)
        self.play(Create(circ), run_time=1)
        poly3=Triangle(radius=(12.5**0.5)/2)
        self.play(GrowFromCenter(poly3), run_time=0.5)
        self.wait(3)
        self.play(FadeOut(poly8, poly4, poly3, circ))
        self.wait()

        poly3 = Polygon(2*(LEFT+UP), 2*(LEFT+DOWN), 2*(RIGHT+DOWN))
        self.play(FadeIn(poly3, shift=UP))
        self.wait()
        circ=Circle(2*2**0.5)
        self.play(Create(circ), run_tume=3)


        ang = RightAngle(Line(2*(LEFT+UP),2*(LEFT+DOWN)), Line(2*(LEFT+DOWN),2*(RIGHT+DOWN)), length=0.5, quadrant=(-1,1))
        self.play(GrowFromCenter(ang))
        self.wait(2)
        self.play(FadeOut(ang, circ, poly3))

        star=Star(n=6)
        self.play(GrowFromCenter(star))
        # circ=DashedVMobject(Circle(), num_dashes=3)
        # self.play(Create(circ), run_time=3)
        # self.wait()

        arc=Arc(start_angle=PI/6, angle=PI/3)
        self.play(Create(arc),run_time=2)
        arc2=Arc(start_angle=PI/2+PI/3, angle=PI/3)
        self.play(Create(arc2), run_time=2)
        arc3 = Arc(start_angle=3*PI / 2, angle=PI / 3)
        self.play(Create(arc3), run_time=2)
        self.wait()
        self.play(FadeOut(star, arc3,arc2,arc))
        self.wait()

        circ=Circle(1)
        self.play(Create(circ), run_time=2)

        arrx=Arrow(3*LEFT, 3*RIGHT)
        arry=Arrow(3*DOWN,3*UP)

        self.play(FadeIn(arrx, shift=RIGHT), run_time=0.5)
        self.play(FadeIn(arry, shift=UP), run_time=0.5)

        curv_Arr=CurvedArrow(2.5*RIGHT, 2.5*UP, radius=2.5)
        self.play(Create(curv_Arr))
        self.wait()
        self.play(FadeOut(arrx, arry, curv_Arr, circ))
        self.wait()

        l1=Line(2*LEFT, 2*RIGHT)
        l2=Line(2*LEFT+3*DOWN, 2*RIGHT+3*UP)
        self.play(Create(l1))
        self.play(Create(l2))
        ang=Angle(l1, l2)
        self.play(Create(ang))
        self.wait()
        self.play(FadeOut(l1, l2, ang))

        # tri=[Line(LEFT+2*UP, LEFT+DOWN), Line(LEFT+DOWN, 2*RIGHT+DOWN), Line(2*RIGHT+DOWN, LEFT+2*UP)]
        # for i in tri:
        #     self.play(Create(i))
        # self.wait()

        triang=Polygon(LEFT+2.5*UP, LEFT+DOWN, 2.5*RIGHT+DOWN)
        self.play(Create(triang), run_time=1.5)

        circ=Circle(1)
        self.play(GrowFromCenter(circ))

        dot=Dot()
        l1=Line(1.1*LEFT+0.4*UP, 0.9*LEFT+0.4*UP)
        l2=Line(1.1*DOWN+RIGHT, 0.9*DOWN+RIGHT)
        l3=Line(1.1*DOWN+1.1*RIGHT, 0.9*DOWN+1.1*RIGHT)

        self.play(GrowFromCenter(dot))
        self.play(FadeIn(l1, shift=LEFT))
        self.play(FadeIn(l2,l3,shift=UP))
        self.wait()
        self.play(FadeOut(triang,circ,dot,l1,l2,l3))
        self.wait()


        figure={
            'poly6': RegularPolygon(n=6),
            'dotline': DashedVMobject(Line(1.5*DOWN, 1.5*UP)),
            'd_arc_arr': CurvedDoubleArrow(0.5*RIGHT+1.1*UP,0.5*LEFT+1.1*UP, radius=1.25)
        }

        self.play(GrowFromCenter(figure['poly6']))
        self.play(Create(figure['dotline']))
        self.play(FadeIn(figure['d_arc_arr'], shift=DOWN))

        self.wait()
        self.play(FadeOut(*figure.values()))
        self.wait()


        figure = {
            'rect_dash': DashedVMobject(Rectangle(width=5, height=3).round_corners(radius=0.4)),
            'trian': Triangle(radius=1, start_angle=PI/6+PI/2).round_corners(0.1),
        }

        self.play(GrowFromCenter(figure['rect_dash']))
        self.play(GrowFromCenter(figure['trian']))
        self.wait()
        self.play(FadeOut(*figure.values()))
        self.wait()

        figure={
            'besie': CubicBezier(3*LEFT+3*DOWN, 5*UP+LEFT, 4*DOWN+RIGHT, 3*RIGHT+3*UP),
            'arrow': Arrow(3*LEFT+3*DOWN,  3*RIGHT+3*UP)
        }
        self.play(Create(figure['besie']))
        self.play(Create(figure['arrow']))

        self.wait()
        self.play(FadeOut(*figure.values()))
        self.wait()

        figure={
            'circ': Circle(1.5),
            'arc': Arc(radius=1, start_angle=PI+PI/3, angle=PI/3)
        }