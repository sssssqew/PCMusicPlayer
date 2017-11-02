# general purpose 'tooltip' routines - currently unused in idlefork
# (although the 'calltips' extension is partly based on this code)
# may be useful for some purposes in (or almost in ;) the current project scope
# Ideas gleaned from PySol

from tkinter import *


class ToolTipBase:

    def __init__(self, button):
        self.button = button
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self._id1 = self.button.bind("<Enter>", self.enter)
        self._id2 = self.button.bind("<Leave>", self.leave)
        self._id3 = self.button.bind("<ButtonPress>", self.leave)

    def ch_bg_night(self):
        self.button.configure(fg="orange")

    def ch_bg_day(self):
        self.button.configure(fg="#383a39")

    def enter(self, event=None):
        self.schedule()
        self.ch_bg_night()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()
        self.ch_bg_day()

    def schedule(self):
        self.unschedule()
        self.id = self.button.after(1500, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.button.after_cancel(id)

    def showtip(self):
        if self.tipwindow:
            return
        # The tip window must be completely outside the button;
        # otherwise when the mouse enters the tip window we get
        # a leave event and it disappears, and then we get an enter
        # event and it reappears, and so on forever :-(
        x = self.button.winfo_rootx() + 300
        y = self.button.winfo_rooty() + self.button.winfo_height() - 200
        self.tipwindow = tw = Toplevel(self.button)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        self.showcontents()

    def showcontents(self, text="Your text here"):
        # Override this in derived class
        label = Label(self.tipwindow, text=text, justify=CENTER,
                      bg="black", relief=SOLID, borderwidth=0, anchor=CENTER, pady=30)
        label.pack()

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


class ToolTip(ToolTipBase):

    def __init__(self, button, text):
        ToolTipBase.__init__(self, button)
        self.text = text

    def showcontents(self):
        ToolTipBase.showcontents(self, self.text)


class ListboxToolTip(ToolTipBase):

    def __init__(self, button, items):
        ToolTipBase.__init__(self, button)
        self.items = items

    def showcontents(self):
        listbox = Listbox(self.tipwindow, bg="sky blue", fg="black", 
                                 font=("Helvetica", 13, "bold"),borderwidth=0, 
                                 highlightthickness=0, justify=CENTER)
        listbox.pack()
        for item in self.items:
            listbox.insert(END, item)