# import library
from guizero import App, Text, PushButton, Drawing, Box
  
def host(app):
  """
  function associated with host button.
  Turns host light blue and players lights black.
  Enables Player buttons
  Also changes the text value.

  """
  button2.enable()
  button3.enable()
  button4.enable()
  d1.oval(90, 90, 10, 10, color="blue", outline=True)
  d2.oval(90, 90, 10, 10, color="black", outline=True)
  d3.oval(90, 90, 10, 10, color="black", outline=True)
  d4.oval(90, 90, 10, 10, color="black", outline=True)
  text2.value = "Buzz in first to answer the question"
 
def player1(app):
  """
  function associated with player 1 button.
  Turns associated player light greenand other lights black.
  Disables player buttons and enable host button.
  Also changes the text value.

  """
  button2.disable()
  button3.disable()
  button4.disable()
  d1.oval(90, 90, 10, 10, color="black", outline=True)
  d2.oval(90, 90, 10, 10, color="green", outline=True)
  d3.oval(90, 90, 10, 10, color="black", outline=True)
  d4.oval(90, 90, 10, 10, color="black", outline=True)
  text2.value = "Player 1 buzzed in first.           "

def player2(app):
  """
  function associated with player 2 button.
  Turns associated player light green and other lights black.
  Disables player buttons and enable host button.
  Also changes the text value.

  """
  button2.disable()
  button3.disable()
  button4.disable()
  d1.oval(90, 90, 10, 10, color="black", outline=True)
  d2.oval(90, 90, 10, 10, color="black", outline=True)
  d3.oval(90, 90, 10, 10, color="green", outline=True)
  d4.oval(90, 90, 10, 10, color="black", outline=True)
  text2.value = "Player 2 buzzed in first.           "
 
  
def player3(app):
  """
  function associated with player 3 button.
  Turns associated player light green and other lights black.
  Disables player buttons and enable host button.
  Also changes the text value.

  """
  button2.disable()
  button3.disable()
  button4.disable()
  d1.oval(90, 90, 10, 10, color="black", outline=True)
  d2.oval(90, 90, 10, 10, color="black", outline=True)
  d3.oval(90, 90, 10, 10, color="black", outline=True)
  d4.oval(90, 90, 10, 10, color="green", outline=True)
  text2.value = "  Player 3 buzzed in first.           "

# Set up the app
app = App("Are You Smarter Than Mr. Sciallo?", bg = "yellow", width=450, height=600, layout="grid") #using grid layout .i.e rows and columns based
tbox = Box(app, border = 1, grid=[1,1,2,1], width = 450, height = 35) #text box

text1 = Text(app, "                              ",size = 20, grid=[1,0,2,1]) #space text added for y-axis margin to text box
text2 = Text(tbox, "Wait for the host to start the round",size = 20, grid=[1,1,2,1])
text3 = Text(app, "                             ",size = 20, grid=[1,2,2,1]) #space text added for y-axis margin to text box

d1 = Drawing(app, width=100, height=100, grid=[1,3]) 
d1.oval(90, 90, 10, 10, color="white", outline=True)#drawing circle shape using oval()
d2 = Drawing(app, width=100, height=100, grid=[1,4])
d2.oval(90, 90, 10, 10, color="white", outline=True)
d3 = Drawing(app, width=100, height=100, grid=[1,5])
d3.oval(90, 90, 10, 10, color="white", outline=True)
d4 = Drawing(app, width=100, height=100, grid=[1,6])
d4.oval(90, 90, 10, 10, color="white", outline=True)

button1 = PushButton(app, lambda: host(app), text="Host", grid=[2,3],padx = 25, pady = 5) #adding push button
button1.text_size = 22
button2 = PushButton(app, lambda: player1(app), text="Player 1", grid=[2,4],padx = 5, pady = 5)
button2.text_size = 22
button2.disable()
button3 = PushButton(app, lambda: player2(app), text="Player 2", grid=[2,5],padx = 5, pady = 5)
button3.text_size = 22
button3.disable()
button4 = PushButton(app, lambda: player3(app), text="Player 3", grid=[2,6],padx = 5, pady = 5)
button4.text_size = 22
button4.disable()

#Display the window
app.display()