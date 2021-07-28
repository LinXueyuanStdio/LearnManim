from manimlib import *


class OpeningManimExample(Scene):
    def construct(self):
        intro_words = TexText("""
            Mobius Transformation ($z \\in \\mathds{C}$):\\\\
            $z \\rightarrow \\frac{a z+b}{c z+d}$
        """)
        intro_words.to_edge(UL)

        self.play(Write(intro_words))
        self.wait(2)

        # Complex map
        c_grid = ComplexPlane()
        moving_c_grid = c_grid.copy()
        moving_c_grid.prepare_for_nonlinear_transform()
        c_grid.set_stroke(BLUE_E, 1)
        c_grid.add_coordinate_labels(font_size=24)

        self.play(
            Write(c_grid, run_time=3),
            FadeIn(moving_c_grid),
        )
        # a = complex(-0.036618657410144806, - 0.5153947472572327)
        # b = complex(0.304897665977478, - 0.022737931460142136)
        # c = complex(-0.0695677250623703, - 0.46238890290260315)
        # d = complex(-0.2555081844329834, 0.19738952815532684)
        a = complex(0.06162194907665253, + 0.33362215757369995)
        b = complex(-0.20632705092430115, - 0.23111556470394135)
        c = complex(0.03713960573077202, - 0.36436328291893005)
        d = complex(-0.2518841624259949, + 0.07031621038913727)
        self.wait()
        self.play(
            moving_c_grid.animate.apply_complex_function(lambda z: (a * z + b) / (c * z + d)),
            run_time=6,
        )
        self.wait(2)
