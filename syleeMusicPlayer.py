#!/usr/bin/env python3
#-*-coding:utf-8-*-
# mp3 player

from tkinter import *
from PIL import Image, ImageTk
from mutagen.id3 import ID3, USLT, TRCK, TIT2, TPE1, TALB, TDRC, TCON, TENC, COMM, APIC, error
from mutagen import File
import vlc
import os
import random
import timeit
import time
import threading
import tooltips


class Song:
	'''
	get song info.
	'''

	def __init__(self, song_name):
		self.song_name = song_name

	def get_metadata(self):
		global art_name
		global info

		mp3 = File(self.song_name)
		art_name = os.path.splitext(self.song_name)[0] + ".jpg"

		meta = {}
		duration = mp3.info.length
		pTimeMin = str(int(duration // 60))
		pTimeSec = str(int(duration % 60))

		if int(pTimeMin) < 10:
			pTimeMin = "0" + pTimeMin

		if int(pTimeSec) < 10:
			pTimeSec = "0" + pTimeSec

		meta["재생시간"] = str(" : ".join([pTimeMin, pTimeSec]))
		meta["가사"] = str(mp3.tags.getall("USLT")[0])

		for key in mp3.tags:
			if key == "APIC:Cover" or key == "APIC:":
				artwork = mp3.tags[key].data
				if not os.path.isfile(art_name):
					with open(art_name, 'wb') as img:
					   img.write(artwork)
				else:
					print("앨범 아트가 이미 존재합니다.")
			if key == "TALB":
				meta["앨범"] = str(mp3.tags[key])					

			if key == "TIT2":
				meta["타이틀"] = str(mp3.tags[key])
				
			if key == "TPE1":
				meta["가수"] = str(mp3.tags[key])	

			if key == "TCON":
				meta["장르"] = str(mp3.tags[key])
			
			if key == "TDRC":
				date = str(mp3.tags[key])
				date = ".".join([date[:4] , date[4:6], date[6:8]])
				meta["발매일"] = date

		# concatenate song info 
		info = ""
		for key in sorted(meta.keys()):
			info += " : ".join([key, meta[key]])
			info += "\n------------------------------\n"

		return duration, len(meta["가사"])

class Play:
	'''
	control music playing
	'''

	def __init__(self):
		self.dir = 0

	def get_songs_list(self):
		songs_track = []
		cur_dir = os.getcwd()

		print("---------------- [track] ----------------")
		for file in os.listdir(cur_dir):
			for e in ext:
				if os.path.splitext(file)[1][1:] == e:
					songs_track.append(file)
					print(file)
					break		
		print("-----------------------------------------")

		# current directory -> play list
		play_list.delete(0, "end")
		for song in songs_track:
			play_list.insert("end", song)

	def load_track(self):  
		self.line = 0
		song_name = play_list.get(pos)
		song = Song(song_name)	
		self.duration, self.len_letters = song.get_metadata()
		self.p = vlc.MediaPlayer(song_name)

	def playing(self):
		time_per_letter = self.duration / self.len_letters
		# print("playing...")
	
		if self.p.is_playing():
			self.line += 0.1
			# print(str(self.line))
			# print("재생시간 : {}".format(self.duration))
			# print("글자수 : {}".format(self.len_letters))
			# print("글자당 시간간격 : {}".format(time_per_letter))
			song_info.see(str(round(self.line, 1)))
		threading.Timer(time_per_letter+0.1, self.playing).start()

	def play_music(self):
		self.p.play()
		p_btn.configure(text="Pause", command=self.pause_music)
		self.playing()

	def pause_music(self):
		self.p.pause()
		p_btn.configure(text="Play", command=self.play_music)
	
	def ch_img(self):
		global img_copy

		img_path = os.path.splitext(play_list.get(pos))[0] + ".jpg"
		img = Image.open(img_path).resize((width, height))
		photo = ImageTk.PhotoImage(img)
		img_copy = img.copy()

		album_cover.configure(image=photo)
		album_cover.image = photo

	def ch_focus(self):
		# enable focus
		play_list.selection_set(pos)
		play_list.activate(pos)
		play_list.focus()

	def ch_song(self):
		self.p.stop()
		self.load_track()
		self.ch_img()
		self.ch_focus()
		p_btn.configure(text="Play", command=self.play_music)
		song_info.delete('1.0', END)
		song_info.insert("1.0", info)
		song_info.tag_add("center", "1.0", "end")

	def prev_song(self):
		self.dir = -1
		self.ch_dir()
		
	def next_song(self):
		self.dir = 1
		self.ch_dir()

	def ch_dir(self):
		global pos
		play_list.selection_clear(pos)
		pos = (pos + self.dir) % play_list.size()
		self.ch_song()
		print(play_list.get(pos))
		# scroll up or down
		play_list.see(pos)
		

# callback for user events
def ch_bg_night(self):
	song_info.configure(fg="orange")

def ch_bg_day(self):
	song_info.configure(fg="#383a39")

def resize(e):
	img = img_copy.resize((e.width, e.width))
	photo = ImageTk.PhotoImage(img)
	album_cover.configure(image=photo)
	album_cover.image = photo

def show_list(e):
	time.sleep(0.1)
	song_info.pack_forget()
	play_list.pack(fill=BOTH, expand=True)
	
	# enable focus
	play_list.selection_clear(pos)
	play_list.selection_set(pos)
	play_list.activate(pos)
	play_list.focus()

	print("double clicked !!")
	# print(play_list.get(0, END))

def show_info(e):
	time.sleep(0.1)
	play_list.pack_forget()
	song_info.pack()
	print("show info")
	

def click_song(e):
	global pos
	play_list.selection_clear(pos)
	if play_list.curselection():
		pos = play_list.curselection()[0]
	play.ch_song()
	print(play_list.get(pos))

def remove_song(e):
	global pos
	del_idx = play_list.nearest(e.y)
	play_list.delete(del_idx)
	if pos > del_idx:
		pos = pos -1
	elif pos == del_idx:
		play.ch_song()

def scrolldown_list(e):
	time.sleep(0.2)
	play.next_song()	

	


# set album size
width = 500
height = 500

ext = ['mp3']
art_name = "" 
info = ""

# create GUI to control songs
window = Tk()
window.title("Sylee Music Player")
window.geometry("500x800")
# window.resizable(0, 0) # do not resize
window.minsize(300,700) 
window.maxsize(700,900)

# create playing control instance
play = Play()

play_list = Listbox(window, bg="black", fg="#383a39", font=("Helvetica", 12, "bold"), borderwidth=0, highlightthickness=0
										, justify=CENTER)
play_list.bind('<Double-Button-1>', click_song)
play_list.bind("<B1-Motion>", show_info)
play_list.bind("<B3-Motion>", scrolldown_list)
play_list.bind("<Double-Button-3>", remove_song)

play.get_songs_list()

pos = random.randint(0, play_list.size()-1)
play.load_track()

# add album cover to label
img = Image.open(art_name).resize((width, height))
photo = ImageTk.PhotoImage(img)
img_copy = img.copy()

album_cover = Label(window, image=photo)
album_cover.pack(fill=BOTH, expand=True)
album_cover.bind('<Configure>', resize)

# control buttons
btn_frame = Frame()
btn_frame.pack(fill="none", expand=True)

prev_btn = Button(btn_frame, text="Prev", fg="ivory2", bg="#383a39", font="Verdana 10 bold", command=play.prev_song)
prev_btn.pack(side=LEFT, padx=5, pady=5)

p_btn = Button(btn_frame, text="Play", fg="mint cream", bg="#383a39", font="Verdana 10 bold", command=play.play_music)
p_btn.pack(side=LEFT, padx=5, pady=5)

next_btn = Button(btn_frame, text="Next", fg="ivory2", bg="#383a39", font="Verdana 10 bold", command=play.next_song)
next_btn.pack(side=LEFT, padx=5, pady=5)

# display info.
song_info = Text(window, wrap=None, bg="black", fg="#383a39", font=("Helvetica", 12, "bold"), borderwidth=0, highlightthickness=0, pady=15)
song_info.tag_configure("center", justify='center')
song_info.insert("1.0", info)
song_info.tag_add("center", "1.0", "end")
song_info.pack()
song_info.bind('<Double-Button-1>', show_list)
song_info.bind("<Enter>", ch_bg_night)
song_info.bind("<Leave>", ch_bg_day)

# window.update()
# tip = tooltips.ListboxToolTip(song_info, ["* Double click *", "Show songs list"])

# process events
window.mainloop()