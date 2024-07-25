import tkinter as tk

class LirikAnimasi:
    def __init__(self, master):
        self.master = master
        self.master.title("Animasi Lirik Lagu")
        self.master.geometry("600x200")
        
        # Membuat kanvas dengan latar belakang hitam
        self.canvas = tk.Canvas(master, bg="black", width=600, height=200)
        self.canvas.pack()

        # Lirik lagu dalam daftar
        self.lirik = [
            "I have died everyday",
            "waiting for you",
            "Darling, don't be afraid",
            "I'll love you",
            "For a thousand more",
            "I'll love you",
            "For a thousand more",
        ]

        # Variabel untuk menyimpan objek teks dan indeks
        self.current_line_index = 0
        self.font_size = 36

        # Mulai animasi untuk baris pertama
        self.start_line_animation(self.current_line_index)

    def start_line_animation(self, index):
        if index < len(self.lirik):
            # Membuat objek teks dengan string kosong untuk mulai
            text_object = self.canvas.create_text(
                self.canvas.winfo_width() // 2, 100,  # Posisi di tengah kanvas
                text="",
                font=("Georgia", self.font_size),
                fill="red",
                anchor="w"  # Anchor di tengah
            )

            # Mulai animasi huruf satu per satu
            self.animate_line(text_object, self.lirik[index], 0)

    def animate_line(self, text_object, line_text, char_index):
        if char_index < len(line_text):
            # Menampilkan sebagian dari teks
            current_text = line_text[:char_index + 1]
            self.canvas.itemconfig(text_object, text=current_text)
            # Memposisikan ulang teks agar tetap di tengah
            text_width = self.canvas.bbox(text_object)[2] - self.canvas.bbox(text_object)[0]
            self.canvas.coords(text_object, (self.canvas.winfo_width() - text_width) // 2, 100)
            # Memanggil fungsi ini lagi setelah 60 milidetik
            self.master.after(100, self.animate_line, text_object, line_text, char_index + 1)
        else:
            # Menghapus teks setelah selesai menampilkan
            self.master.after(600, lambda: self.canvas.delete(text_object))
            # Setelah satu baris selesai, mulai animasi baris berikutnya
            self.master.after(1500, self.next_line)

    def next_line(self):
        self.current_line_index += 1
        self.start_line_animation(self.current_line_index)

if __name__ == "__main__":
    root = tk.Tk()
    app = LirikAnimasi(root)
    root.mainloop()
