from manim import *

class SinyalEvolusi(Scene):
    def construct(self):
        bar_width = 0.2
        bar_spacing = 0.1

        # Daftar generasi sinyal: label, subtitle, tinggi bar, warna
        sinyal_data = [
            ("G", "General Packet Radio Service (2G)", [0.5, 0.7, 0.9, 1.1], ORANGE),
            ("E", "Enhanced Data Rates for GSM Evolution (2.75G)", [0.5, 0.7, 0.9, 1.1], GOLD),
            ("H+", "High Speed Packet Access (3G)", [0.5, 0.7, 0.9, 1.1], YELLOW),
            ("LTE", "Long Term Evolution (4G)", [0.5, 0.7, 0.9, 1.1], GREEN),
            ("5G", "5th Generation New Radio (NR)", [0.5, 0.7, 0.9, 1.1], TEAL)
        ]

        # Inisialisasi bar sinyal
        bars = VGroup()
        for i in range(4):
            bar = Rectangle(width=bar_width, height=0.2, fill_color=WHITE, fill_opacity=0.8)
            bar.move_to(np.array([i * (bar_width + bar_spacing) -1, 0.1, 2]))
            bars.add(bar)

        self.play(*[GrowFromEdge(bar, edge=DOWN) for bar in bars], run_time=0.5)
        self.wait(0.3)

        # Teks awal (akan di-transform ke generasi berikutnya)
        main_text = Text("", font_size=48)
        subtitle = Text("", font_size=24)
        main_text.next_to(bars, RIGHT, buff=0.3)
        subtitle.to_edge(DOWN, buff=2.5)

        self.add(main_text, subtitle)

        for label, sub, heights, color in sinyal_data:
            # Animasi ubah tinggi dan warna bar
            bar_anims = []
            for bar, new_h in zip(bars, heights):
                new_bar = Rectangle(width=bar_width, height=new_h, fill_color=color, fill_opacity=0.8)
                new_bar.move_to(np.array([bar.get_center()[0], new_h / 2, 0]))
                bar_anims.append(Transform(bar, new_bar))

            self.play(*bar_anims, run_time=0.8)

            # Teks generasi sinyal
            new_main = Text(label, font_size=48 if label != "G" else 32)
            new_main.next_to(bars, RIGHT, buff=0.3)

            new_sub = Text(sub, font_size=24)
            new_sub.to_edge(DOWN, buff=2.5)

            self.play(
                Transform(main_text, new_main),
                Transform(subtitle, new_sub),
                run_time=0.8
            )

            # Efek kedipan bar
            self.play(bars.animate.set_fill(color, opacity=0.5), run_time=0.2)
            self.play(bars.animate.set_fill(color, opacity=0.8), run_time=0.2)

            self.wait(0.5)

        self.wait(1)
  