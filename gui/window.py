from tkinter import *
from tkinter import messagebox

from attacker import Attacker
from config import DEFAULT_THREADS_COUNT, DEFAULT_SITE_URL


class MainWindow:
    def __init__(self):
        self.attacker = Attacker()

        self.window = Tk()
        self.window.title("DDOSer")

        Label(self.window, text="Потоків: ", font=18).grid(row=0, column=0, sticky=W, pady=10, padx=10)
        self.th = Entry(self.window)
        self.th.insert(END, DEFAULT_THREADS_COUNT)
        self.th.grid(row=0, column=1, sticky=W + E, padx=10)

        self.chk_state = BooleanVar()
        self.chk_state.set(True)
        Checkbutton(
            self.window, text='Логування', varia=self.chk_state, font=18, state='disable'
        ).grid(row=0, column=2, sticky=W, pady=10, padx=10)
        Label(self.window, text="Сайти: ", font=18).grid(row=1, column=0, pady=10, padx=10)
        self.urls = Text(self.window, width=55, height=20)
        self.urls.insert(END, '\n'.join(DEFAULT_SITE_URL))
        self.urls.grid(row=1, column=1, columnspan=2, padx=10, pady=20)

        self.state = Label(self.window, text="Stopped", font=18, fg='#c1121f')
        self.state.grid(row=2, column=0, pady=10, padx=10)
        self.stop_btn = Button(
            self.window,
            text="Stop", command=self.stop, width=25, padx=10, pady=10,
            background='#c1121f', cursor='hand2',
            activebackground='#c1121f', disabledforeground='grey', state='disable'
        )
        self.stop_btn.grid(column=1, row=2)
        self.start_btn = Button(
            self.window,
            text="Start", command=self.start, width=25, padx=10, pady=10,
            background='#008000',
            cursor='hand2', activebackground='#008000', disabledforeground='grey'
        )
        self.start_btn.grid(column=2, row=2)

    def run(self):
        self.window.mainloop()

    def parse_site_urls(self):
        site_urls = []
        for url in self.urls.get('1.0', END).split('\n'):
            if url.startswith('http'):
                site_urls.append(url)
        return site_urls

    def start(self):
        site_urls = self.parse_site_urls()
        threads_count = self.th.get()
        if not threads_count.isdigit():
            self.th.focus_set()
            messagebox.showerror(title='Помилка', message='Ви не вписали кількість потоків.')
            return
        if len(site_urls) == 0:
            self.urls.focus_set()
            messagebox.showerror(title='Помилка', message='Ви не вписали посилання на сайти для атаки.')
            return

        self.state['text'] = 'Running'
        self.state['fg'] = '#008000'
        self.stop_btn['state'] = 'active'
        self.start_btn['state'] = 'disable'
        self.window.update()
        self.attacker.sites_for_attack = self.parse_site_urls()
        self.attacker.start_workers(int(threads_count))

    def stop(self):
        self.start_btn['state'] = 'active'
        self.stop_btn['state'] = 'disable'
        self.state['text'] = 'Stopping'
        self.state['fg'] = '#ffbd00'
        self.window.update()

        self.attacker.stop_workers()

        self.state['text'] = 'Stopped'
        self.state['fg'] = '#c1121f'
        self.state.update()



