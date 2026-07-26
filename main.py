#print("RUNNING CAPITAL GAME VERSION 1")

import customtkinter as ctk
import json
import random
import tkinter as tk
import winsound

# ===========================================
# Appearance
# ===========================================

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


# ===========================================
# Main Application
# ===========================================

class CapitalMaster(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("🌍 Capital Master")
        self.geometry("1200x750")
        self.minsize(1000,650)


        self.database={}
        self.load_database()

        self.selected_mode="International"
        self.selected_country="India"

        self.score=0
        self.question_number=0

        self.current_question=None
        self.correct_answer=None

        self.answer_locked=False
        self.current_info=None

        self.confetti_particles = []

        self.home_screen()



    # ===========================================
    # LOAD DATABASE
    # ===========================================
    def load_database(self):
        try:
            with open(
                "database.json",
                "r",
                encoding="utf-8"
            ) as file:

                self.database=json.load(file)
        except Exception as e:
            print(e)

            self.database={
                "international":[],
                "countries":{}
            }


    # ===========================================
    # CLEAR ALL WIDGETS
    # ===========================================
    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()



    # ===========================================
    # HOME SCREEN
    # ===========================================
    def home_screen(self):
        self.clear()

        frame=ctk.CTkFrame(
            self,
            corner_radius=15
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        title=ctk.CTkLabel(
            frame,
            text="🌍 CAPITAL MASTER",
            font=("Arial",40,"bold")
        )

        title.pack(pady=30)

        subtitle=ctk.CTkLabel(
            frame,
            text="Countries • States • Capitals",
            font=("Arial",20)
        )

        subtitle.pack()

        ctk.CTkLabel(
            frame,
            text="Select Mode",
            font=("Arial",24,"bold")
        ).pack(pady=30)

        buttons=ctk.CTkFrame(
            frame,
            fg_color="transparent"
        )

        buttons.pack()

        self.international_btn=ctk.CTkButton(
            buttons,
            text="🌍 International",
            width=250,
            height=60,
            font=("Arial",18),
            command=self.select_international
        )

        self.international_btn.grid(
            row=0,
            column=0,
            padx=20
        )

        self.country_btn=ctk.CTkButton(
            buttons,
            text="🏳 Country",
            width=250,
            height=60,
            font=("Arial",18),
            command=self.select_country
        )

        self.country_btn.grid(
            row=0,
            column=1,
            padx=20
        )

        self.country_frame=ctk.CTkFrame(
            frame,
            fg_color="transparent"
        )

        ctk.CTkLabel(
            self.country_frame,
            text="Choose Country",
            font=("Arial",18)
        ).pack()

        countries=list(
            self.database["countries"].keys()
        )

        self.country_option=ctk.CTkOptionMenu(
            self.country_frame,
            values=countries,
            width=250,
            height=45,
            font=("Arial",16),
            fg_color="#333333",
            button_color="#555555",
            button_hover_color="#777777",
            dropdown_fg_color="#222222",
            dropdown_hover_color="#00B4D8",
            text_color="white",
            dropdown_text_color="white",
            command=self.country_selected
        )

        # Set default country
        default_country = "India"

        if default_country in countries:
            self.country_option.set(default_country)
            self.selected_country = default_country
        else:
            self.country_option.set(countries[0])
            self.selected_country = countries[0]

        self.country_option.pack(
            pady=10
        )

        self.start_btn=ctk.CTkButton(
            frame,
            text="▶ START GAME",
            width=300,
            height=60,
            font=("Arial",22,"bold"),
            command=self.start_game
        )

        self.start_btn.pack(
            side="bottom",
            pady=50
        )

        self.select_international()



    # ===========================================
    # UPDATE DATABSE WITH INTERNATIONAL COUNTRIES
    # ===========================================
    def select_international(self):
        self.selected_mode="International"
        self.country_frame.pack_forget()
        self.update_mode_buttons()


    # ===========================================
    # UPDATE DATABASE WITH STATE FROM COUNTRY
    # ===========================================
    def select_country(self):
        self.selected_mode="Country"
        self.country_frame.pack(
            pady=20
        )
        self.update_mode_buttons()


    # ===========================================
    # HIGHLIGHT SELECTED COUNTRY
    # ===========================================
    def country_selected(self,value):
        self.selected_country=value
        self.country_option.configure(
            fg_color="#00B4D8",
            button_color="#0096C7",
            button_hover_color="#0077B6"
        )


    # ===========================================
    # START QUIZ
    # ===========================================
    def start_game(self):
        self.score=0
        self.question_number=0
        self.quiz_screen()
        self.generate_question()



    # ===========================================
    # QUIZ SCREEN
    # ===========================================
    def quiz_screen(self):
        self.clear()
        
        self.quiz_frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )
        self.quiz_frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )
        
        self.confetti_canvas = tk.Canvas(
            self.quiz_frame,
            bg=self.quiz_frame._apply_appearance_mode(
                self.quiz_frame.cget("fg_color")
            ),
            highlightthickness=0,
            bd=0
        )

        self.confetti_canvas.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )

        # Hide until needed
        self.confetti_canvas.place_forget()

        self.score_label=ctk.CTkLabel(
            self.quiz_frame,
            text="Score: 0",
            font=("Arial",22,"bold")
        )
        self.score_label.pack(
            pady=15
        )
        
        self.question_label=ctk.CTkLabel(
            self.quiz_frame,
            text="",
            font=("Arial",30,"bold"),
            wraplength=900
        )
        self.question_label.pack(
            pady=40
        )
        
        self.answer_frame=ctk.CTkFrame(
            self.quiz_frame,
            fg_color="transparent"
        )
        self.answer_frame.pack()
        self.answer_buttons=[]

        for i in range(4):
            btn=ctk.CTkButton(
                self.answer_frame,
                text="",
                width=350,
                height=60,
                font=("Arial",18),
                command=lambda x=i:self.check_answer(x),
                hover_color="#144870"
            )
            btn.grid(
                row=i//2,
                column=i%2,
                padx=20,
                pady=15
            )
            self.answer_buttons.append(btn)

        self.next_button=ctk.CTkButton(
            self.quiz_frame,
            text="Next Question ➜",
            width=250,
            height=50,
            command=self.generate_question
        )
        self.next_button.pack(
            pady=30
        )
        
        self.menu_button = ctk.CTkButton(
            self.quiz_frame,
            text="🏠 Main Menu",
            width=150,
            height=40,
            fg_color="#444444",
            hover_color="#666666",
            command=self.back_to_main_menu
        )

        self.menu_button.pack(
            pady=10
        )



    # ===========================================
    # QUESTION GENERATOR
    # ===========================================
    def generate_question(self):
        self.clear_confetti()
        self.answer_locked = False
        self.question_number += 1
        self.confetti_particles = []

        if self.selected_mode == "International":
            country_name = random.choice(
                list(self.database["countries"].keys())
            )

            country_data = self.database["countries"][country_name]

            question = (
                f"What is the capital of "
                f"{country_name}?"
            )

            correct = country_data["capital"]
            options = [
                data["capital"]
                for data in self.database["countries"].values()
            ]
        else:
            country_data = self.database["countries"][
                self.selected_country
            ]

            state_name = random.choice(
                list(country_data["states"].keys())
            )

            question = (
                f"What is the capital of "
                f"{state_name}?"
            )

            correct = country_data["states"][state_name]["capital"]

            options = [
                state["capital"]
                for state in country_data["states"].values()
            ]

        options = list(set(options))

        wrong_answers = [
            x for x in options
            if x != correct
        ]

        choices = random.sample(
            wrong_answers,
            min(3, len(wrong_answers))
        )

        choices.append(correct)
        random.shuffle(choices)
        self.correct_answer = correct
        self.question_label.configure(
            text=question
        )

        for i, button in enumerate(self.answer_buttons):
            button.configure(
                text=choices[i],
                fg_color="#1f6aa5",
                hover_color="#144870",
                text_color="white",
                state="normal"
            )
            button._state = "normal"



    # ===========================================
    # ANSWER CHECK
    # ===========================================
    def check_answer(self,index):
        if self.answer_locked:
            return

        self.answer_locked=True
        selected = self.answer_buttons[index].cget("text")

        # Orange flash first
        self.answer_buttons[index].configure(
            fg_color="#FFA500",
            hover_color="#FFA500",
            text_color="white"
        )

        self.after(
            50,
            lambda:self.show_result(index,selected)
        )


    # ===========================================
    # MODE BUTTON
    # ===========================================
    def update_mode_buttons(self):
        if self.selected_mode == "International":
            self.international_btn.configure(
                fg_color="#00B4D8",
                hover_color="#0096C7",
                text_color="white"
            )

            self.country_btn.configure(
                fg_color="#444444",
                hover_color="#555555",
                text_color="#BBBBBB"
            )
        else:
            self.country_btn.configure(
                fg_color="#00B4D8",
                hover_color="#0096C7",
                text_color="white"
            )

            self.international_btn.configure(
                fg_color="#444444",
                hover_color="#555555",
                text_color="#BBBBBB"
            )



    # ===========================================
    # SHOW RESULT
    # ===========================================
    def show_result(self,index,selected):
        #print("SHOW RESULT CALLED")
        
        if selected == self.correct_answer:
            self.score += 1
            self.answer_buttons[index].configure(
                fg_color="#28a745",
                hover_color="#28a745"
            )
            self.after(
                100,
                self.confetti
            )
            self.play_sound("correct")
        else:
            self.answer_buttons[index].configure(
                fg_color="#dc3545",
                hover_color="#dc3545"
            )

            self.play_sound("wrong")

            # highlight correct answer

            for button in self.answer_buttons:

                button.configure(
                    state="disabled",
                    hover_color=button.cget("fg_color")
                )

        self.score_label.configure(
            text=f"Score: {self.score}"
        )

        for button in self.answer_buttons:
            button.configure(
                state="disabled"
            )

        self.show_information()


    # ===========================================
    # PLAY SOUND
    # ===========================================
    def play_sound(self,type):
        try:
            if type=="correct":
                winsound.Beep(
                    900,
                    150
                )
            else:
                winsound.Beep(
                    300,
                    250
                )
        except:
            pass


    # ===========================================
    # SHOW CONFETTI
    # ===========================================
    def confetti(self):
        #print("CONFETTI START")

        self.quiz_frame.update_idletasks()

        width = self.quiz_frame.winfo_width()
        height = self.quiz_frame.winfo_height()

        #print("Frame:", width, height)

        canvas = self.confetti_canvas

        if not canvas.winfo_exists():
            return

        canvas.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )

        canvas.delete("all")
        
        self.confetti_canvas = canvas

        colors = [
            "#FF4D4D",
            "#FFD700",
            "#00FF7F",
            "#00BFFF",
            "#FF69B4",
            "#FFA500",
            "#9B59B6"
        ]

        shapes = [
            "circle",
            "square",
            "diamond"
        ]

        particles = []

        for i in range(160):
            # LEFT + RIGHT corner burst
            if i < 80:
                x = random.randint(0, 120)
                dx = random.uniform(2, 8)
            else:
                x = random.randint(width - 120, width)
                dx = random.uniform(-8, -2)


            y = random.randint(-100, 10)

            size = random.randint(6, 14)

            color = random.choice(colors)

            shape = random.choice(shapes)


            if shape == "circle":
                particle = canvas.create_oval(
                    x,
                    y,
                    x + size,
                    y + size,
                    fill=color,
                    outline=""
                )
            elif shape == "square":
                particle = canvas.create_rectangle(
                    x,
                    y,
                    x + size,
                    y + size,
                    fill=color,
                    outline=""
                )
            else:
                particle = canvas.create_polygon(
                    x,
                    y + size//2,
                    x + size//2,
                    y,
                    x + size,
                    y + size//2,
                    x + size//2,
                    y + size,
                    fill=color,
                    outline=""
                )

            particles.append(
                {
                    "id": particle,
                    "dx": dx,
                    "dy": random.uniform(1.5,3.5),
                    "gravity": random.uniform(0.08,0.18),
                    "shape": shape,
                    "angle": 0,
                    "x": x,
                    "y": y,
                    "size": size,
                    "color": color
                }
            )


        # ============================
        # animation
        # ============================
        def animate():
            if not canvas.winfo_exists():
                return

            alive = False

            for p in particles:
                try:
                    canvas.move(
                        p["id"],
                        p["dx"],
                        p["dy"]
                    )

                    p["dy"] += p["gravity"]

                    coords = canvas.coords(
                        p["id"]
                    )

                    if len(coords) >= 2:
                        y = coords[1]

                        if y < height + 50:
                            alive = True

                    # fake rotation effect
                    p["angle"] += 10

                    if int(p["angle"]) % 40 == 0:
                        current = canvas.itemcget(
                            p["id"],
                            "fill"
                        )

                        canvas.itemconfigure(
                            p["id"],
                            fill=current
                        )
                except tk.TclError:
                    continue

            if alive:
                self.after(
                    25,
                    animate
                )
            else:
                canvas.delete("all")
                canvas.place_forget()

        animate()



    # ===========================================
    # CLEAR CONFETTI
    # ===========================================
    def clear_confetti(self):
        self.confetti_particles = []

        if (hasattr(self, "confetti_canvas")
            and self.confetti_canvas
            and self.confetti_canvas.winfo_exists()
        ):
            self.confetti_canvas.delete("all")
            self.confetti_canvas.place_forget()

    # ===========================================
    # SHOW INFORMATION
    # ===========================================
    def show_information(self):
        pass
        # print(
            # "Information coming next..."
        # )


    # ===========================================
    # RETURN TO MAIN MENU
    # ===========================================
    def back_to_main_menu(self):
        #print("BACK TO MAIN MENU")

        # Stop any confetti animation
        self.clear_confetti()

        # Reset game variables
        self.score = 0
        self.question_number = 0
        self.answer_locked = False
        self.correct_answer = None

        # Rebuild the home screen
        self.home_screen()



# ===========================================
if __name__=="__main__":
    app=CapitalMaster()
    app.mainloop()
